# my_project2/main.py
from my_package_timer import MyClass
from my_package_timer import LogManager
import logging
import time

# MyClass의 인스턴스를 생성합니다.
my_instance = MyClass("My Project2 - Time&Log", 5)  # 5초마다 현재 시간 출력

# greet 메서드를 호출하여 인사말을 출력합니다.
print(my_instance.greet())

# LogManager 인스턴스를 생성합니다.
# log_manager = LogManager(log_file='my_app.log', log_level=logging.DEBUG)
log_manager = LogManager(log_level=logging.DEBUG)
log_manager.debug('Logging --- Start')

# # 타이머를 시작합니다.
my_instance.start()

# # 15초 후 타이머를 중지합니다. (15초 동안 실행)
time.sleep(15)

my_instance.stop()

log_manager.debug('Logging --- End')