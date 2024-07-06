# my_project2/my_package_timer/log_manager.py
# 로그를 파일에 기록하는 모듈
import logging
import datetime
import os

class LogManager:
    def __init__(self, log_level=logging.INFO):
        self.logger = logging.getLogger('LogManager')
        self.logger.setLevel(log_level)

        # Ensure the log directory exists
        log_dir = 'log'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Generate log file name based on current date
        log_file = os.path.join(log_dir, f"app_{datetime.datetime.now().strftime('%Y-%m-%d')}.log")

        # Ensure no duplicate handlers are added
        if not self.logger.handlers:
            # Create a file handler
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(log_level)

            # Create a console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(log_level)

            # Create a formatter and set it for both handlers
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add handlers to the logger
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)