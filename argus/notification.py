import base64

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets


class NotificationIcon:
    Info, Success, Warning, Error, Close = range(5)
    Types = {
        Info: None,
        Success: None,
        Warning: None,
        Error: None,
        Close: None
    }

    @classmethod
    def init(cls):
        cls.Types[cls.Info] = QtGui.QPixmap(
            QtGui.QImage.fromData(base64.b64decode(
                'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAC5ElEQVRYR8VX0VHbQBB9e/bkN3QQU0FMBSEVYFcQ8xPBJLJ1FWAqOMcaxogfTAWQCiAVRKkgTgfmM4zRZu6QhGzL0p0nDPr17e7bt7tv14RX/uiV48MJgAon+8TiAMRtMFogaqUJxADPwRRzg67kl8+xbWJWANR40iPQSSFgtX/mGQkaDr56V3VAKgGos4s2JXwJoF3naMPvMS+SrpTHs032GwGkdF+DsFMVnJm/oyGGeHico0EjIjpYes+YMyVd6R/flfkpBWCCQ9zaZM2LZDfLMGXsZ5kdI/lYBmINgHHyyLd1mWdBbAFAM/GY7K2WYx1AeB4T6L1N9umbGxZ0qktATaEAdCps48D39oq/LwEw3U5CN92LfczJoewfT7MAywDCaEbAuxeLrh0zz4L+0e4aAJfGy+sP3IMxlH1vpMJoSMCJDXgWtJeJVc6ACs9HBBrYODCJAFdYvAmkPJxnNqMwYht7Bn+T/lGg3z4DGEd3RPhQ54DBvwAOVkeqagRXfTLjh+x7+8sALOtfHLuiYzWOAiLoKbD58mnIGbCmLxUepS6NQmYlUGE0JeCTTXT9JvA9E9sZgO5iIpoyc6/YzcqSwQzgGgBXB7oXpH9klpRSkxY1xW/b7Iu2zk34PILPnazCqEPAtTWA8iZ0HsOu9L0bw4DzCJeNocMGNDpQ3IKO+6NUiJ4ysZNiBv5I3zPnmJmG5oM+wbS+9+qkvGi7NAXGmeUy0ioofa+XA0jH0UaMKpdRWs/adcwMqfV/tenqpqHY/Znt+j2gJi00RUzA201dXaxh9iZdZloJS+9H1otrkbRrD5InFqpPskxEshJQ468CkSmJC+i1HigaaxCAuCljgoDhwPdOjf7rFVxxuJrMkXScjtKc1rOLNpJk6nii5XmYzbngzlZn+RIb40kPJPTBYXUt6VEDJ8Pi6bWpNFb/jFYY6YGpDeKdjBmTKdMcxDGEmP73v2a2Gr/NOycGtglQZ/MPzEqCMLGckJEAAAAASUVORK5CYII=')))
        cls.Types[cls.Success] = QtGui.QPixmap(
            QtGui.QImage.fromData(base64.b64decode(
                'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAACZUlEQVRYR8VXS3LTQBDtVsDbcAPMCbB3limkcAKSG4QFdnaYE2BOQLKzxSLJCeAGSUQheSnfwLmB2VJhXmpExpFHI2sk2RWv5FJPv9evP9NieuIfPzE+VSJw8qt3IMDvmahDoDYxt2UAACXMWIIowR5ffn8TJbaBWRE4CXvHAH9RgKXOgQUI48CfXZbZbiTw8Xe/w3d0zkydMkem91IZpyWOJu5sUXS+kEAqt3B+MNOLOuDqDEBLxxFHk7eza5MfIwEJDjhXTYD1s8zinYlEjsCD7FdNI9cJpEq0RFdPR47AMOzLCn69zegz6UgCP+pmfa8RSKudnPNdgCufTOLDxJtdPP7PoA1Cd8HEL5sSUCCD0B0x8bc1f8Bi6sevcgS2VXh6hMOwDz0gsUddNaxWKRjeuKfE/KlJ9Dq4UYH/o/Ns6scj+bgiMAjdayb26xLQwTfVEwg3gRcf6ARq578KuLo7VDc8psCQqwfjr4EfjYvkrAquFJ56UYpdSkAZSmNd1rrg0leOQFELgvA58OJTxVyRaAJORPOpF6UXnFUR5sDiXjs7UqsOMGMRlrWhTkJXpFL3mNrQZhA1lH3F0TiI5FurUQyMpn58VjhkSqQA4Tbw4nSVW6sBU5VXktXSeONlJH3s8jrOVr9RgVSFuNcWfzlh5n3LoKzMAPxxWuiULiQpiR2sZNnCyzIuWUr5Z1Ml0sgdHFZaShVDuR86/0huL3VXtDk/F4e11vKsTHLSCeKx7bYkW80hjLOrV1GhWH0ZrSlyh2MwdZhYfi8oZeYgLBmUiGd8sfVPM6syr2lUSYGaGBuP3QN6rVUwYV/egwAAAABJRU5ErkJggg==')))
        cls.Types[cls.Warning] = QtGui.QPixmap(
            QtGui.QImage.fromData(base64.b64decode(
                'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAACmElEQVRYR8VXTW7TUBD+xjYSXZFukOIsSE9AskNJJMoJmq4r7OYEwAkabhBOkB/Emt4gVIojdpgbpIumEitX6gKB7UHPkauXxLHfc4F6Z3l+vvnmm/fGhAd+6IHzQwvA9cfOITMfAdQAcx1EdVEAM/tEFADsWyaPn57MfdXClABcT1qnzHSWJiwMzrwgoF91vXGRbS6AH59ajd8hDYmoURQo67tgxoij42rv62KX/04Agu44xmciVMokT32YERgGjquvZ1+y4mQCWPUa0/sk3vQlwqssEFsAVrQbU4XKL/ai2+5PPK6waQ4AOsoDnDARh83NdmwBuJq0fQI9L6p+L7rd3+/5gbAToMPI+FbkIzRRc72mbLcGIFE7jGFRIPHddmZrvstJh1X8CHGv6sxHqe1GkPYCoGcqgcoCAPPCdr2DLQC6wqMoPEj7qdqCNKllxs30sLpjYDluDUDGG5XqhY2sal3w4PiD7c7fJnHShMtJR8zpy/8CALiwndnhBgD1/t+XAXkaZAaUVHwnHulg0W6BNEWlAQD8zna8gQB0Ne70iXCm2j55jCUAei1gxvuaO+uXAcDg7zXHSy640iKUAehOEDJFqDmGQkiPLO5Fv+KADXOqvCuIsrPGsIyQdHou22YeRMJgOdHTQTkAfGk7XrLKrWlAvOhcRgBfWiZ3RQti0zxXuUFXCXMuo0TRitfxugjbIxC5RYzI6s9kIGFh+KLOpiW22id5AUuI8IaisFG4kCQg/sFKJgtPLix3KWXGeRETRbQDuCFCV2spTYMm+2FEI1WBbYIRPTeiqFtqLZeDraaD+qrbkpgQAvfl1WsXU0p/RjIjYYhTkNFgcCVlRlRKoAAc+5aF0V//NVPoc2kTLQZKZ8lx/AMXBmMwuXUwOAAAAABJRU5ErkJggg==')))
        cls.Types[cls.Error] = QtGui.QPixmap(
            QtGui.QImage.fromData(base64.b64decode(
                'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAACrklEQVRYR82XW27aQBSG/4PtiNhIpStouoImKwjZAV1B07coWCpZQcgK6kh2lLeSFZSsIOwgdAdkBaUSEBQDpxpjU9vM+EJR03nDzJz/mzm3GcIrD3plfZQCeD47O1ho2jERNRmoE9AQG2BgBGBAwIiZe5Zh3JPjiG+5oxCAEF5q2iWITnMtRhOYu5XF4mr/9naYtSYXYGLbHQCXhYVTEwlom657rVqvBOB2uz71/a+ldq1SYe6ahnEhc4sSYGzbfQKOt915eh0D/ZrrnqS/SwEmrVYXRJ92Jb4OC+C65rrtuN0NgIltNwF837V4zN5Hy3V70e9NgFZrCKJ3CQDmJ9MwDsW36XzeB/AhA/CHqeuN2WxWX2paX2JraHneeynA+Pz8lCqVbxLjV5brimxAEJxqiEA8CjZVBvFy+bl2c9MV9hInoAw85qFpGEeRYQVEQjzMokcQHWxsiPne8jzh6j8AodGfyqNlHpiGcaKAkIk/gChwm2yYuv5W2FqfwLNtN5bAQ2bwySB83zENo50A8/1McaFRAU72XVek+mpk+D/JlIKI/xkee654uCbIhjVAqZIrgSgpLhiCwN4OAEj4vEB2yDybBCjsAol4ZD0nRdMQSRcUCsKUeNSw4o2mKMRGEOamoVx8FXDZKVosDYNMUHXAsBRnppo8RQcbpTgIGEkhykpFjnWxzGhPQYxt2yHgS/oIlKVYTJxImpG482nz+VG1Wh1N84pMCCGa0ULXHwmoJwCYnyzPW5fn/68dh7EgPbrMMl3gz7gro+n/7EoWD7w4a96l1NnJ1Yz5Lt6wCgFEk0r1CIkbiPnC9DxH5aHcd4FYGD5MOqVOg/muslh0/vphkm63k5eXZvA0I6qD+ZCI3jDzLxANiHn1NNvb6+30aVYgwLeeUsgFW1svsPA3Ncq4MHzVeO8AAAAASUVORK5CYII=')))
        cls.Types[cls.Close] = QtGui.QPixmap(
            QtGui.QImage.fromData(base64.b64decode(
                'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAeElEQVQ4T2NkoBAwUqifgboGzJy76AIjE3NCWmL0BWwumzV/qcH/f38XpCfHGcDkUVwAUsDw9+8GBmbmAHRDcMlheAGbQnwGYw0DZA1gp+JwFUgKZyDCDQGpwuIlrGGAHHAUGUCRFygKRIqjkeKERE6+oG5eIMcFAOqSchGwiKKAAAAAAElFTkSuQmCC')))

    @classmethod
    def icon(cls, ntype):
        return cls.Types.get(ntype)


class NotificationItem(QtWidgets.QWidget):
    closed = QtCore.Signal(QtWidgets.QListWidgetItem)

    def __init__(self, title, message, item, *args, ntype=0,
                 close_time=None, callback=None, **kwargs):
        super(NotificationItem, self).__init__(*args, **kwargs)
        self.item = item
        self.callback = callback
        _layout = QtWidgets.QHBoxLayout(self, spacing=0)
        _layout.setContentsMargins(0, 0, 0, 0)
        self.bg_widget = QtWidgets.QWidget(self)  # 背景控件, 用于支持动画效果
        _layout.addWidget(self.bg_widget)

        _layout = QtWidgets.QGridLayout(self.bg_widget)
        _layout.setHorizontalSpacing(15)
        _layout.setVerticalSpacing(2)
        _layout.setContentsMargins(20, 10, 20, 10)

        # 标题左边图标
        _layout.addWidget(
            QtWidgets.QLabel(self, pixmap=NotificationIcon.icon(ntype)), 0, 0)

        # 标题
        self.label_title = QtWidgets.QLabel(title, self)
        font = self.label_title.font()
        font.setBold(True)
        font.setPixelSize(18)
        self.label_title.setFont(font)

        # 关闭按钮
        self.label_close = QtWidgets.QLabel(
            self, cursor=QtCore.Qt.PointingHandCursor,
            pixmap=NotificationIcon.icon(NotificationIcon.Close)
        )

        # 消息内容
        self.label_message = QtWidgets.QLabel(
            message, self,
            cursor=QtCore.Qt.PointingHandCursor,
            wordWrap=True,
            alignment=QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        font = self.label_message.font()
        font.setPixelSize(14)
        self.label_message.setFont(font)
        self.label_message.adjustSize()

        # 添加到布局
        _layout.addWidget(self.label_title, 0, 1)
        _layout.addItem(
            QtWidgets.QSpacerItem(
                40, 20, QtWidgets.QSizePolicy.Expanding,
                QtWidgets.QSizePolicy.Minimum
            ), 0, 2
        )
        _layout.addWidget(self.label_close, 0, 3)
        _layout.addWidget(self.label_message, 1, 1, 1, 2)

        # 边框阴影
        effect = QtWidgets.QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setColor(QtGui.QColor(0, 0, 0, 25))
        effect.setOffset(0, 2)
        self.setGraphicsEffect(effect)

        self.adjustSize()

        self._timer = None
        if close_time:
            self._timer = QtCore.QTimer(self, timeout=self.do_close)
            self._timer.setSingleShot(True)
            self._timer.start(close_time)

    def do_close(self):
        try:
            # 可能由于手动点击导致item已经被删除了
            self.closed.emit(self.item)
        except:
            pass

    def mousePressEvent(self, event):
        super(NotificationItem, self).mousePressEvent(event)
        w = self.childAt(event.pos())
        if not w:
            return
        if w == self.label_close:
            if self._timer:
                self._timer.stop()
            self.closed.emit(self.item)

        elif (w == self.label_message and
              self.callback and callable(self.callback)):
            if self._timer:
                self._timer.stop()
            self.closed.emit(self.item)
            self.callback()

    def paintEvent(self, event):
        super(NotificationItem, self).paintEvent(event)
        painter = QtGui.QPainter(self)
        path = QtGui.QPainterPath()
        path.addRoundedRect(QtCore.QRectF(self.rect()), 6, 6)
        painter.fillPath(path, QtCore.Qt.white)


class NotificationWindow(QtWidgets.QListWidget):
    _instance = None

    def __init__(self, *args, **kwargs):
        super(NotificationWindow, self).__init__(*args, **kwargs)
        self.setSpacing(8)
        self.setMinimumWidth(412)
        self.setMaximumWidth(412)
        QtWidgets.QApplication.instance().setQuitOnLastWindowClosed(True)
        self.setWindowFlags(self.windowFlags() |
                            QtCore.Qt.Tool |
                            QtCore.Qt.FramelessWindowHint |
                            QtCore.Qt.WindowStaysOnTopHint)
        self.setFrameShape(self.NoFrame)
        self.viewport().setAutoFillBackground(False)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        rect = QtWidgets.QApplication.instance().desktop().availableGeometry(self)
        self.setMinimumHeight(rect.height())
        self.setMaximumHeight(rect.height())
        self.move(rect.width() - self.minimumWidth() - 18, 0)

    def remove_item(self, item):
        w = self.itemWidget(item)
        self.removeItemWidget(item)
        self.takeItem(self.indexFromItem(item).row())
        w.close()
        w.deleteLater()
        del item

    @classmethod
    def _create_instance(cls):
        # 创建实例
        if not cls._instance:
            cls._instance = NotificationWindow()
            cls._instance.show()
            NotificationIcon.init()

    @classmethod
    def info(cls, title, message, close_time=None, callback=None):
        cls._create_instance()
        item = QtWidgets.QListWidgetItem(cls._instance)
        w = NotificationItem(title, message, item, cls._instance,
                             ntype=NotificationIcon.Info,
                             close_time=close_time, callback=callback)
        w.closed.connect(cls._instance.remove_item)
        item.setSizeHint(QtCore.QSize(cls._instance.width() -
                                      cls._instance.spacing(), w.height()))
        cls._instance.setItemWidget(item, w)

    @classmethod
    def success(cls, title, message, close_time=None, callback=None):
        cls._create_instance()
        item = QtWidgets.QListWidgetItem(cls._instance)
        w = NotificationItem(title, message, item, cls._instance,
                             ntype=NotificationIcon.Success,
                             close_time=close_time, callback=callback)
        w.closed.connect(cls._instance.remove_item)
        item.setSizeHint(QtCore.QSize(cls._instance.width() -
                                      cls._instance.spacing(), w.height()))
        cls._instance.setItemWidget(item, w)

    @classmethod
    def warning(cls, title, message, close_time=None, callback=None):
        cls._create_instance()
        item = QtWidgets.QListWidgetItem(cls._instance)
        w = NotificationItem(title, message, item, cls._instance,
                             ntype=NotificationIcon.Warning,
                             close_time=close_time, callback=callback)
        w.closed.connect(cls._instance.remove_item)
        item.setSizeHint(QtCore.QSize(cls._instance.width() -
                                      cls._instance.spacing(), w.height()))
        cls._instance.setItemWidget(item, w)

    @classmethod
    def error(cls, title, message, close_time=None, callback=None):
        cls._create_instance()
        item = QtWidgets.QListWidgetItem(cls._instance)
        w = NotificationItem(title, message, item,
                             ntype=NotificationIcon.Error,
                             close_time=close_time, callback=callback)
        w.closed.connect(cls._instance.remove_item)

        width = cls._instance.width() - cls._instance.spacing()
        item.setSizeHint(QtCore.QSize(width, w.height()))
        cls._instance.setItemWidget(item, w)


if __name__ == '__main__':
    import sys
    import cgitb

    cgitb.enable(format='text')

    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    layout = QtWidgets.QHBoxLayout(w)


    def callback():
        print('回调点击')


    layout.addWidget(QtWidgets.QPushButton(
        'Info', w, clicked=lambda: NotificationWindow.info('提示',
                                                           '这是一条会自动关闭的消息',
                                                           callback=callback)))
    layout.addWidget(QtWidgets.QPushButton(
        'Success', w, clicked=lambda: NotificationWindow.success('提示',
                                                                 '这是一条会自动关闭的消息',
                                                                 callback=callback)))
    layout.addWidget(QtWidgets.QPushButton(
        'Warning', w, clicked=lambda: NotificationWindow.warning(
            '提示',
            '这是提示文案这是提示文案这是提示文案这是提示文案。',
            callback=callback)))
    layout.addWidget(QtWidgets.QPushButton(
        'Error', w, clicked=lambda: NotificationWindow.error(
            '提示',
            '<html><head/><body><p><span style=" font-style:italic; color:teal;">这是提示文案这是提示文案这是提示文案这是提示文案这是提示文案这是提示文案这是提示文案这是提示文案</span></p></body></html>',
            callback=callback)))
    w.show()

    sys.exit(app.exec_())
