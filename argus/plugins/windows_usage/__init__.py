import os
import subprocess
from functools import partial

import psutil
from PySide6 import QtCore


def update_stats(label):
    cpu_usage = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    label.setText(f'CPU: {cpu_usage}% Memory: {memory_usage}%')


def register(label, main_window):
    timer = QtCore.QTimer(main_window)
    timer.timeout.connect(partial(update_stats, label))
    timer.start(1000)


def double_click_handler():
    subprocess.Popen(os.path.join(os.path.dirname(__file__), 'taskmgr.bat'))
