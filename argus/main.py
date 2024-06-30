import os
import sys
import importlib

from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore

from argus.plugin import PluginBase
from argus.widgets import StatusLabel


class SystemMonitor(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_tray()
        self.dragging = False

    def _import_modules_from_folder(self, folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith('.py'):
                module_name = filename[:-3]
            else:
                module_name = filename
            module = importlib.import_module(f'plugins.{module_name}')

            for class_name in dir(module):
                if class_name.startswith('_'):
                    continue

                if type(getattr(module, class_name)) != type:
                    continue

                if PluginBase not in getattr(module, class_name).__bases__:
                    continue

                class_module = getattr(module, class_name)
                label = StatusLabel()
                class_ins = class_module(label, self)
                label.double_clicked.connect(class_ins.double_click_handler)

                self.container_layout.addWidget(label)

    def init_ui(self):
        self.setWindowTitle('System Monitor')
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.Tool
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("background: rgba(0, 0, 0, 20); color: white;")
        self.resize(200, 10)

        self.container_layout = QtWidgets.QVBoxLayout()
        self.container_layout.setAlignment(QtCore.Qt.AlignTop)
        self.container_layout.setSpacing(0)

        container = QtWidgets.QWidget()
        container.setStyleSheet('border-radius: 10px')
        container.setLayout(self.container_layout)
        self.setCentralWidget(container)

        self._import_modules_from_folder('plugins')

    def init_tray(self):
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(QtGui.QIcon('icon.png'))

        show_action = QtWidgets.QAction('Show', self)
        quit_action = QtWidgets.QAction('Quit', self)
        show_action.triggered.connect(self.show)
        quit_action.triggered.connect(QtWidgets.QApplication.instance().quit)

        tray_menu = QtWidgets.QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = True
            self.drag_start_position = event.globalPos()
            self.window_start_position = self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if self.dragging:
            current_position = event.globalPos()
            delta = current_position - self.drag_start_position
            self.move(self.window_start_position + delta)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragging = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    monitor = SystemMonitor()
    monitor.show()
    sys.exit(app.exec_())
