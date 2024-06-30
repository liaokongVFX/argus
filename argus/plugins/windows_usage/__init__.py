import os
import subprocess

import psutil
from argus.plugin import PluginBase


class WindowsUserPlugin(PluginBase):
    def set_init_label(self):
        return 'CPU: 0% Memory: 0%'

    def start(self):
        cpu_usage = psutil.cpu_percent()
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent

        self.label.setText(f'CPU: {cpu_usage}% Memory: {memory_usage}%')

    def double_click_handler(self):
        if not self.label.is_checked:
            self.label.set_status()

        self.show_notification('打开任务管理器')

        subprocess.Popen(
            os.path.join(os.path.dirname(__file__), 'taskmgr.bat'))
