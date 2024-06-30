from PySide2 import QtCore
from argus.notification import NotificationWindow


class PluginBase(object):
    interval = 1000

    def __init__(self, label, main_window):
        self.label = label
        self.main_window = main_window

        self.label.setText(self.set_init_label())

        self.timer = QtCore.QTimer(main_window)
        self.timer.timeout.connect(lambda: self.start())
        self.timer.start(self.interval)

    def set_init_label(self):
        return ''

    def start(self):
        raise NotImplementedError

    def double_click_handler(self):
        pass

    @staticmethod
    def show_notification(message, notif_type='success', title='提示',
                          close_time=None, callback=None):
        return getattr(NotificationWindow, notif_type)(
            title, message, close_time=close_time, callback=callback
        )
