# main.py

from my_module import MyClass
from log_manager import LogManager
import logging

# MyClass의 인스턴스를 생성합니다.
my_instance = MyClass("My Project", 5)  # 5초마다 현재 시간 출력

# greet 메서드를 호출하여 인사말을 출력합니다.
print(my_instance.greet())

# # 타이머를 시작합니다.
my_instance.start()

# # 15초 후 타이머를 중지합니다. (15초 동안 실행)
import time
time.sleep(15)
my_instance.stop()

# LogManager 인스턴스를 생성합니다.
# log_manager = LogManager(log_file='my_app.log', log_level=logging.DEBUG)
log_manager = LogManager(log_level=logging.DEBUG)

# 로그 메시지를 기록합니다.
log_manager.debug('This is a debug message')
log_manager.info('This is an info message')
log_manager.warning('This is a warning message')
log_manager.error('This is an error message')
log_manager.critical('This is a critical message')