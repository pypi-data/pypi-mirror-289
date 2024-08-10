import os
import sys
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import mplfinance as mpf
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QCursor
from matplotlib.widgets import Cursor

import lyydata
import lyystkcode
import configparser
import lyydata
from ttkbootstrap import Style
import lyystkcode

os.chdir(r"D:\UserData\resource\data")
from lyylog2 import log
log("finish all import")

"""
lyy的炒股软件
"""
# pyinstaller --noconfirm -n LengStock  --distpath  "D:/Soft/_lyysoft"  --add-data "D:/Soft/Program/pythonx64/Lib/site-packages/py_mini_racer/mini_racer.dll;." -D -w -i D:\UserData\resource\com_icos\man.ico D:\UserData\Documents\BaiduSyncdisk\0LengsStock\lengstock_main.py
import lyycfg
cf = configparser.ConfigParser()

lengstock_cfg = lyycfg.create_empty_cfg()
lengstock_cfg.geometry_sub = "1024x768"




class InfoWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("行情信息")
        self.setGeometry(100, 200, 120, 120)
        
        # 设置窗口为透明
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool)

        # 创建标签
        self.label = QtWidgets.QLabel("当前信息", self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 150);")  # 半透明背景
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def update_info(self, text, parent):
        self.label.setText(text)
        self.adjust_position(parent)


    def adjust_position(self, parent):
        # 获取父窗口的坐标轴范围
        ax = parent.ax1  # 获取 K线图的坐标轴
        xlim = ax.get_xlim()  # 获取 x 轴范围
        ylim = ax.get_ylim()  # 获取 y 轴范围

        # 获取当前鼠标位置
        cursor_pos = QCursor.pos()
        
        # 设置偏移量
        offset_x = 10  # 水平偏移量
        offset_y = 10  # 垂直偏移量

        # 计算信息窗口的新位置
        new_x = int(cursor_pos.x() + offset_x)  # 转换为整数
        new_y = int(cursor_pos.y() + offset_y)  # 转换为整数

        # 确保信息窗口不超出 K线图的边界
        if new_x + self.width() > parent.width():
            new_x = parent.width() - self.width()
        if new_y + self.height() > parent.height():
            new_y = parent.height() - self.height()

        # 确保信息窗口的 y 坐标在 K线图的 y 轴范围内
        if new_y < ylim[0]:
            new_y = int(ylim[0])  # 转换为整数
        if new_y + self.height() > ylim[1]:
            new_y = int(ylim[1]) - self.height()  # 转换为整数

        # 设置新位置
        self.move(new_x, new_y)

class KlineClass(QtWidgets.QDialog):
    def __init__(self, main_module):
        super().__init__()
        self.main_module = main_module
        self.setWindowTitle("K线图")
        self.setGeometry(100, 100, 1024, 768)  # 设置窗口大小
        font_path = r"C:\WINDOWS\Fonts\MSYH.TTC"  # 替换为您系统中微软雅黑字体的路径
        self.prop = fm.FontProperties(fname=font_path)
        
        self.figure = plt.Figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.info_window = InfoWindow()  # 创建信息窗口
        self.info_window.hide()  # 初始隐藏信息窗口

        self.ax1 = self.figure.add_subplot(111)
        self.ax1.plot([0, 1, 2], [0, 1, 0], zorder=1)  # 示例数据

        layout = QtWidgets.QVBoxLayout()

        # 创建 QLabel 用于显示信息
        self.info_label = QtWidgets.QLabel("当前信息", self)
        self.info_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.info_label.setStyleSheet("background-color: rgba(255, 255, 255, 150);")  # 半透明背景
        self.info_label.setMinimumHeight(30)  # 设置最小高度
        self.info_label.setMaximumHeight(30)  # 设置最小高度
        self.info_label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)  # 使 QLabel 不响应鼠标事件
        self.info_label.move(100, 100)  # 设置 QLabel 的位置，保持在上方
        layout.addWidget(self.info_label)  # 将 QLabel 放在上方        
        layout.addWidget(self.canvas)  # 将 FigureCanvas 放在 QLabel 下方


        self.info_label.raise_()  # 确保 QLabel 在其他控件之上


        self.setLayout(layout)

        # 初始化十字光标
        self.cursor = Cursor(self.ax1, useblit=True, color='red', linewidth=1)
        self.mouse_pos = QtCore.QPoint()
        self.setMouseTracking(True)  # 允许鼠标移动事件被捕获
        self.last_k_index = None

    def paintEvent(self, event):
        # 创建绘图对象
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine))  # 设置十字光标颜色为黑色

        # 绘制十字光标线
        if not self.mouse_pos.isNull():
            # 绘制竖线
            painter.drawLine(self.mouse_pos.x(), 0, self.mouse_pos.x(), self.height())
            # 绘制横线
            painter.drawLine(0, self.mouse_pos.y(), self.width(), self.mouse_pos.y())
    def format_info(self, event):
        xmouse = int(event.xdata)
        if xmouse < len(self.filtered_rows):
            current_data = self.filtered_rows.iloc[xmouse]
            return f" {current_data.name.strftime('%Y-%m-%d')}\n" \
                   f"开盘: {current_data['open']:.2f}\n" \
                   f"最高: {current_data['high']:.2f}\n" \
                   f"最低: {current_data['low']:.2f}\n" \
                   f"收盘: {current_data['close']:.2f}"
        return ""

    def on_resize(self, event):
        # 确保图形大小正确设置
        width = event.size.width()
        height = event.size.height()
        self.figure.set_size_inches(width / self.figure.dpi, height / self.figure.dpi)
        self.canvas.draw()
    def mouseMoveEvent(self, event):
        # 更新鼠标位置并触发重绘
        self.mouse_pos = QtCore.QPoint(event.x(), event.y())
        self.update()
    def on_move(self, event):
        if event.inaxes == self.ax1:
            # 获取当前鼠标的全局位置
            global_pos = QCursor().pos()
            # 将全局屏幕坐标转换为窗口坐标
            local_pos = self.mapFromGlobal(global_pos)  # 使用 self.mapFromGlobal

            # 将窗口坐标转换为数据坐标
            xmouse, ymouse = self.ax1.transData.inverted().transform((local_pos.x(), local_pos.y()))

            # 确保十字光标线不穿过信息标签
            if local_pos.y() < self.info_label.height():
                ymouse = self.info_label.height()  # 将 ymouse 设置为信息标签的底部

            # 更新十字线位置
            self.cursor.lineh.set_ydata([ymouse, ymouse])  # 将 ymouse 包装成列表
            self.cursor.linev.set_xdata([xmouse, xmouse])  # 将 xmouse 包装成列表

            # 更新信息窗口
            info_text = self.format_info(event)
            self.info_window.update_info(info_text,self)
            self.info_window.move(QCursor.pos())  # 移动信息窗口到鼠标位置
            self.info_window.show()  # 显示信息窗口
            # 更新 K线图的标题
            self.info_label.setText(info_text.replace("\n"," "))  # 更新 QLabel 的文本~
            
            self.info_label.show()  # 显示信息标签
            # 仅在当前 K线索引与上一次不同的情况下更新标题
            current_k_index = int(xmouse)
 
            if current_k_index != self.last_k_index:
                self.ax1.set_title(info_text)  # 更新标题
                #self.canvas.draw_idle()  # 使用 draw_idle() 进行重绘
                self.last_k_index = current_k_index  # 更新上一次的 K线索引

    def show_kline(self, event):
        print("event in showkjline=", event)
        if not self.isHidden():
            print("self.popup_windows已经hidden,self.popup_window ")
            self.create_popup_window()
        else:
            print("self.popup_window非隐藏，清除之前的绘图先")
            # 删除之前的图形对象，确保干净的开始
            self.figure.clear()
            self.canvas.draw()
            self.show()
        
        if self.main_module.is_dark_mode:
            plt.style.use("dark_background")
        else:
            plt.style.use("default")
            
        plt.rcParams['font.family'] = self.prop.get_name()
        
        item = event
        code = self.main_module.table_widget.item(item, 0).text()
        print("code=", code)
        self.filtered_rows = self.main_module.grouped.get_group(code).copy()
        self.filtered_rows.reset_index(drop=True, inplace=True)
        self.filtered_rows["idx"] = self.filtered_rows.index.values
        self.filtered_rows["day"] = pd.to_datetime(self.filtered_rows["day"])
        self.filtered_rows.set_index("day", inplace=True)

        # 计算均线
        self.filtered_rows['ma5'] = self.filtered_rows['close'].rolling(window=5).mean()
        self.filtered_rows['ma10'] = self.filtered_rows['close'].rolling(window=10).mean()
        self.filtered_rows['ma20'] = self.filtered_rows['close'].rolling(window=20).mean()
        self.filtered_rows.fillna(method='ffill', inplace=True)

        # 创建网格布局并确定子图
        gs = self.figure.add_gridspec(2, 1, height_ratios=[4, 1])
        self.ax1 = self.figure.add_subplot(gs[0])

        #ax2 = self.ax1.twinx()  # 对于成交量的次坐标轴
        ax2 = self.figure.add_subplot(gs[1], sharex=self.ax1)
 
        # 创建均线的 addplot 对象
        ma5_addplot = mpf.make_addplot(self.filtered_rows['ma5'], color='white', title='ma5',ax=self.ax1)
        ma10_addplot = mpf.make_addplot(self.filtered_rows['ma10'], color='purple', title='ma10',ax=self.ax1)
        ma20_addplot = mpf.make_addplot(self.filtered_rows['ma20'], color='green', title='ma20',ax=self.ax1)


        mc = mpf.make_marketcolors(up='red', down='green', inherit=True)
        s = mpf.make_mpf_style(marketcolors=mc)

        # 确认ax1和ax2都是matplotlib.axis.Axes类型
        assert isinstance(self.ax1, plt.Axes), "self.ax1 is not an Axes object"
        assert isinstance(ax2, plt.Axes), "ax2 is not an Axes object"       


        add_plot = [ma5_addplot,ma10_addplot,ma20_addplot]
        # 绘制K线图和附加的均线图
        mpf.plot(self.filtered_rows, type="candle", style=s, ylabel='价格', ax=self.ax1, volume=ax2, addplot=add_plot)
        #mpf.plot(self.filtered_rows, type="candle",  ylabel='价格', ax=self.ax1, volume=ax2, addplot=add_plot)


        # 设置图表交互
        self.zoom_level = 1.0  # 100%
        self.ax1.tick_params(axis="both", which="major", labelsize=5)
        self.ax1.yaxis.labelpad = -5
        ax2.tick_params(axis="both", which="major", labelsize=5)
        self.canvas.mpl_connect("motion_notify_event", self.on_move)
        # self.canvas.mpl_connect("key_press_event", lambda event: self.zoom_in(event) if event.key == "up" else None)
        # self.canvas.mpl_connect("key_press_event", lambda event: self.zoom_out(event) if event.key == "down" else None)
        # self.canvas.mpl_connect("key_press_event", lambda event: self.move_data(event))
        self.canvas.mpl_connect("key_press_event", self.handle_key_press)

        self.apply_zoom()

    def handle_key_press(self, event):
        """处理键盘事件，主要用于缩放K线"""
        print("[handle_key_press] event.key =", event.key)
        if event.key == "left":
            # 向左移动一个数据
            current_x = self.crosshair_vline.get_xdata()[0]
            print("current_x", current_x)
            if current_x > self.index_min:
                current_x -= 1
            self.crosshair_vline.set_xdata([current_x])
            date = self.filtered_rows.index[int(current_x)]
            formatted_date = date.strftime("%Y-%m-%d")
            self.ax1.set_title(f"X = {int(current_x)} | Y = {current_x:.2f} | Date = {formatted_date}", fontproperties=self.prop)
            self.canvas.draw()
        elif event.key == "right":
            # 向右移动一个数据
            current_x = self.crosshair_vline.get_xdata()[0]
            print("current_x", current_x)
            if current_x < self.index_max:
                current_x += 1
            self.crosshair_vline.set_xdata([current_x])
            date = self.filtered_rows.index[int(current_x)]
            formatted_date = date.strftime("%Y-%m-%d")
            self.ax1.set_title(f"X = {int(current_x)} | Y = {current_x:.2f} | Date = {formatted_date}", fontproperties=self.prop)
            self.canvas.draw()
        elif event.key == "up":
            # 放大
            self.zoom_in(event)
        elif event.key == "down":
            # 缩小
            self.zoom_out(event)
        elif event.key == "shift+right":
            # 向左移动一个数据
            center = (self.filtered_rows["idx"].max() + self.filtered_rows["idx"].min()) / 2
            data_range = self.filtered_rows["idx"].max() - self.filtered_rows["idx"].min()
            new_center = center - data_range / 10  # 移动一个数据的十分之一
            new_range = data_range / self.zoom_level
            self.ax1.set_xlim(new_center - new_range / 2, new_center + new_range / 2)
            self.canvas.draw()
        elif event.key == "shift+left":
            # 向右移动一个数据
            center = (self.filtered_rows["idx"].max() + self.filtered_rows["idx"].min()) / 2
            data_range = self.filtered_rows["idx"].max() - self.filtered_rows["idx"].min()
            new_center = center + data_range / 10  # 移动一个数据的十分之一
            new_range = data_range / self.zoom_level
            self.ax1.set_xlim(new_center - new_range / 2, new_center + new_range / 2)
            self.canvas.draw()
    def focusOutEvent(self, event):
        print("# 当窗口失去焦点时隐藏信息标签")
        self.info_label.hide()
        self.info_window.hide()
        super().focusOutEvent(event)  # 调用父类的 focusOutEvent 方法

    def move_data(self, event):
        print("[move_data] tner, event.key=",event.key)
        if event.key == "left":
            # 向左移动一个数据
            current_x = self.crosshair_vline.get_xdata()[0]
            print("current_x", current_x)
            if current_x > self.index_min:
                current_x -= 1
            self.crosshair_vline.set_xdata([current_x])
            date = self.filtered_rows.index[int(current_x)]
            # 格式化日期为年月日
            formatted_date = date.strftime("%Y-%m-%d")
            # 设置标题
            self.ax1.set_title(f"X = {int(current_x)} | Y = {current_x:.2f} | Date = {formatted_date}", fontproperties=self.prop)

            self.canvas.draw()
        elif event.key == "right":
            # 向右移动一个数据
            current_x = self.crosshair_vline.get_xdata()[0]
            print("current_x", current_x)
            if current_x < self.index_max:
                current_x += 1
            self.crosshair_vline.set_xdata([current_x])
            date = self.filtered_rows.index[int(current_x)]
            # 格式化日期为年月日
            formatted_date = date.strftime("%Y-%m-%d")
            # 设置标题
            self.ax1.set_title(f"X = {int(current_x)} | Y = {current_x:.2f} | Date = {formatted_date}", fontproperties=self.prop)

            self.canvas.draw()
            pass
        elif event.key == "shift+right":  # 检查Shift键是否被按下
            # 向左移动一个数据
            center = (self.filtered_rows["idx"].max() + self.filtered_rows["idx"].min()) / 2
            data_range = self.filtered_rows["idx"].max() - self.filtered_rows["idx"].min()
            new_center = center - data_range / 10  # 移动一个数据的十分之一
            new_range = data_range / self.zoom_level
            self.ax1.set_xlim(new_center - new_range / 2, new_center + new_range / 2)
            self.canvas.draw()
        elif event.key == "shift+left":  # 检查Shift键是否被按下
            # 向右移动一个数据
            center = (self.filtered_rows["idx"].max() + self.filtered_rows["idx"].min()) / 2
            data_range = self.filtered_rows["idx"].max() - self.filtered_rows["idx"].min()
            new_center = center + data_range / 10  # 移动一个数据的十分之一
            new_range = data_range / self.zoom_level
            self.ax1.set_xlim(new_center - new_range / 2, new_center + new_range / 2)
            self.canvas.draw()


    def update_title(self, text):
        self.ax1.set_title(text, fontproperties=self.prop,loc="center")  # 更新 K线图的标题
        self.canvas.draw_idle()  # 重绘画布以显示更新的标题
    # 应用缩放因子到K线图中
    def apply_zoom(self):
        # 计算新的数据范围
        data_range = self.filtered_rows["idx"].max() - self.filtered_rows["idx"].min()
        new_range = data_range / self.zoom_level
        center = (self.filtered_rows["idx"].max() + self.filtered_rows["idx"].min()) / 2

        # 设置新的数据范围
        self.ax1.set_xlim(center - new_range / 2, center + new_range / 2)
        self.canvas.draw()

    # 定义放大和缩小的函数
    def zoom_in(self,event):
        self.zoom_level *= 1.1  # 放大10%
        print("zoom_in", self.zoom_level)
        self.apply_zoom()
        # self.canvas.draw()

    def zoom_out(self,event):
        self.zoom_level /= 1.1  # 缩小10%
        print("zoom_out", self.zoom_level)
        self.apply_zoom()
        # self.canvas.draw()

        # 鼠标移动事件处理函数


    # def format_info(self, event):
    #     # 根据鼠标位置格式化信息
    #     xmouse = int(event.xdata)
    #     if xmouse < len(self.filtered_rows):
    #         current_data = self.filtered_rows.iloc[xmouse]
    #         return f"Date: {current_data.name.strftime('%Y-%m-%d')}\nOpen: {current_data['open']:.2f}\nHigh: {current_data['high']:.2f}\nLow: {current_data['low']:.2f}\nClose: {current_data['close']:.2f}"
    #     return ""

    # def on_move(self, event):
    #     if event.inaxes == self.ax1:
    #         # 更新十字线位置
    #         self.mouse_pos = QtCore.QPoint(event.xdata, event.ydata)
    #         self.update()  # 触发重绘

    #     # 更新信息窗口
    #     info_text = self.format_info(event)
    #     self.info_window.update_info(info_text)
    #     self.info_window.move(QCursor.pos())  # 移动信息窗口到鼠标位置
    #     self.info_window.show()  # 显示信息窗口

        return

        self.lyypaintEvent(event)
        self.x += 1
        if event.inaxes is None:
            self.info_window.hide()  # 隐藏信息窗口
            return
        self.mouse_pos = QtCore.QPoint(event.x, event.y)
        self.update()  # 触发重绘
        return 
        xmouse = int(event.xdata)
        ymouse = event.ydata

        # 检查鼠标坐标是否在数据范围内
        if xmouse is not None and 0 <= xmouse < len(self.filtered_rows):
            # 获取当前K线的数据
            t1= time.time()
            current_data = self.filtered_rows.iloc[xmouse]
            print("spend = ", (time.time()-t1))
            price_info = f"日期: {current_data.name.strftime('%Y-%m-%d')}\n" \
                         f"开盘: {current_data['open']:.2f}\n" \
                         f"最高: {current_data['high']:.2f}\n" \
                         f"最低: {current_data['low']:.2f}\n" \
                         f"收盘: {current_data['close']:.2f}"

            # 更新信息窗口内容并显示
            self.info_window.update_info(price_info)
            self.info_window.move(QCursor.pos())  # 移动信息窗口到鼠标位置
            self.info_text.set_text(price_info)
            self.info_window.show()  # 显示信息窗口
        else:
            self.info_window.hide()  # 隐藏信息窗口
            
        print(QCursor.pos(), xmouse, ymouse)
        # 更新十字线的位置
        # 将屏幕坐标转换为数据坐标
        cursor = QCursor.pos()
        screen_x = cursor.x()
        screen_y = cursor.y()
        inv = self.ax1.transData.inverted()
        xmouse, ymouse = inv.transform((screen_x, screen_y))

        self.crosshair_vline.set_xdata([xmouse])
        self.crosshair_hline.set_ydata([ymouse])
        self.crosshair_vline_ax2.set_xdata([xmouse])
        self.crosshair_hline_ax2.set_ydata([ymouse])
                    # 更新信息文本
        self.info_text.set_text(price_info)
        self.info_text.set_position((0.5, 1.05))  # 设置文本位置
        self.canvas.draw_idle()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_module = None  # 这里需要替换为实际的主模块
    kline_window = KlineClass(main_module)
    kline_window.show()
    sys.exit(app.exec_())