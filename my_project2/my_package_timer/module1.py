# my_project2/my_package_timer/my_module.py
# 현재시간을 일정간격으로 로그를 기록하는 모듈
from .module2 import LogManager
import logging
import datetime
import threading

class MyClass:
    def __init__(self, name, interval=1):
        self.name = name
        self.interval = interval
        self._timer = None
        self._is_running = False

    def greet(self):
        return f"Hello, {self.name}!"

    def _print_current_time(self):
        #print(f"현재 시간: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        log_manager = LogManager(log_level=logging.DEBUG)
        log_manager.info(f"현재 시간: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self._start_timer()

    def _start_timer(self):
        self._timer = threading.Timer(self.interval, self._print_current_time)
        self._timer.start()

    def start(self):
        self._is_running = True
        self._start_timer()

    def stop(self):
        self._timer.cancel()
        self._is_running = False
