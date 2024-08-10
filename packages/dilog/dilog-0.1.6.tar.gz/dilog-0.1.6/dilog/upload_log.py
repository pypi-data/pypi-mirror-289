import os
import zipfile
from datetime import datetime
import oss2

def get_ali_credentials():
    """
    获取阿里云 OSS 的凭据。凭据应设置为环境变量。
    """
    access_key_id = os.getenv('ALI_ACCESS_KEY_ID')
    access_key_secret = os.getenv('ALI_ACCESS_KEY_SECRET')
    endpoint = os.getenv('ALI_OSS_ENDPOINT')
    bucket_name = os.getenv('ALI_BUCKET_NAME')
    
    missing_vars = []
    if not access_key_id:
        missing_vars.append('ALI_ACCESS_KEY_ID')
    if not access_key_secret:
        missing_vars.append('ALI_ACCESS_KEY_SECRET')
    if not endpoint:
        missing_vars.append('ALI_OSS_ENDPOINT')
    if not bucket_name:
        missing_vars.append('ALI_BUCKET_NAME')
    
    if missing_vars:
        raise EnvironmentError(f"缺少必要的环境变量: {', '.join(missing_vars)}")
    
    return access_key_id, access_key_secret, endpoint, bucket_name

def compress_log_file(log_filepath, suffix):
    """
    压缩日志文件为 zip 格式。
    """
    zip_filename = log_filepath + f'-{suffix}.zip'
    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(log_filepath, os.path.basename(log_filepath))
        return zip_filename
    except Exception as e:
        print(f"压缩文件时出错: {e}")
        return None

def upload_to_oss(file_path):
    """
    将文件上传到阿里云 OSS。
    """
    access_key_id, access_key_secret, endpoint, bucket_name = get_ali_credentials()
    
    try:
        auth = oss2.Auth(access_key_id, access_key_secret)
        bucket = oss2.Bucket(auth, endpoint, bucket_name)
        file_name = os.path.basename(file_path)
        bucket.put_object_from_file(file_name, file_path)
        print(f"文件 {file_name} 已上传到 OSS。")
    except Exception as e:
        print(f"上传文件到 OSS 时出错: {e}")

def handle_error_feedback(suffix):
    """
    处理错误反馈，压缩日志文件并上传到阿里云 OSS。
    """
    log_dir = os.path.join(os.getcwd(), 'logs')
    log_filename = datetime.now().strftime('%Y-%m-%d.log')
    log_filepath = os.path.join(log_dir, log_filename)

    if not os.path.exists(log_filepath):
        print("今日未产生记录")
        return

    zip_filepath = compress_log_file(log_filepath, suffix)
    if zip_filepath:
        upload_to_oss(zip_filepath)
        try:
            os.remove(zip_filepath)  # 上传后删除压缩文件
            print("本地压缩文件已删除")
        except Exception as e:
            print(f"删除压缩文件时出错: {e}")

