import logging
import logging.config
import yaml
import os
from datetime import datetime
import threading

class LogHandler:
    _instance = None
    _lock = threading.Lock()

    @staticmethod
    def get_instance():
        if LogHandler._instance is None:
            with LogHandler._lock:
                if LogHandler._instance is None:
                    LogHandler()
        return LogHandler._instance

    def __init__(self):
        if LogHandler._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            LogHandler._instance = self
            self._setup_logger()

    def _setup_logger(self):
        log_dir = os.path.join(os.getcwd(), 'logs')
        os.makedirs(log_dir, exist_ok=True)
        log_filename = datetime.now().strftime('%Y-%m-%d.log')
        log_filepath = os.path.join(log_dir, log_filename)

        if not os.path.exists(log_filepath):
            open(log_filepath, 'w', encoding='utf-8').close()  # 创建一个UTF-8编码的空日志文件

        config_path = os.path.join(os.path.dirname(__file__), 'logging_config.yaml')
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Logging configuration file not found at {config_path}")

        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file.read())
            config['handlers']['file']['filename'] = log_filepath
            logging.config.dictConfig(config)

        self.logger = logging.getLogger('DIDI')

    def report(self, tag, content, level='INFO'):
        log_entry = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'tag': tag,
            'content': content
        }
        if level == 'DEBUG':
            self.logger.debug(log_entry)
        elif level == 'INFO':
            self.logger.info(log_entry)
        elif level == 'ERROR':
            self.logger.error(log_entry)
        elif level == 'SYSTEM':
            self.logger.critical(log_entry)

log_handler = LogHandler.get_instance()
