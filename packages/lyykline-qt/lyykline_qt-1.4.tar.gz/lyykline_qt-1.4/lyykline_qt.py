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
from PyQt5.QtGui import QCursor,QFont
from PyQt5.QtCore import QPoint  
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


class Crosshair:
    def __init__(self, ax):
        self.ax = ax
        y_pos = ax.get_ylim()[0]  # 可以选择 y 轴的最小值或其他值
        x_pos = ax.get_xlim()[0]  # 可以选择 y 轴的最小值或其他值

        self.vline = ax.axvline(x=x_pos, color='blue', linewidth=1)
        self.hline = ax.axhline(y=y_pos, color='blue', linewidth=1)


    def update(self, index, price):
        self.current_index = index
        self.current_price = price
        self.vline.set_xdata([index, index])
        self.hline.set_ydata([price,price])
        #plt.draw()
    def disconnect(self):
        self.vline.set_visible(False)
        self.hline.set_visible(False)



class InfoWindow(QtWidgets.QWidget):
    def __init__(self,parent):
        super().__init__(parent)  # 将 parent 传递给 QWidget 的构造函数
        self.setWindowTitle("行情信息")
        self.setGeometry(100, 200, 120, 120)
        
        # 设置窗口为透明
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint| QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.Tool)

        #self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.Tool)

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
                        # 设置窗口标志，包含最小化、最大化和关闭按钮
        self.setWindowFlags(QtCore.Qt.Window | 
                            QtCore.Qt.WindowCloseButtonHint | 
                            QtCore.Qt.WindowMinimizeButtonHint | 
                            QtCore.Qt.WindowMaximizeButtonHint | 
                            QtCore.Qt.WindowStaysOnTopHint)
        #self.setWindowIcon(QtWidgets.QIcon('your_icon.ico'))

        font_path = r"C:\WINDOWS\Fonts\MSYH.TTC"  # 替换为您系统中微软雅黑字体的路径
        self.prop = fm.FontProperties(fname=font_path)
        
        self.figure = plt.Figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.info_window = InfoWindow(self)  # 创建信息窗口
        self.info_window.hide()  # 初始隐藏信息窗口

                # 设置字体（可选）
        font = QFont()
        font.setFamily("微软雅黑")
        self.setFont(font)

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
        self.canvas.mpl_connect("motion_notify_event", self.on_move)
        # self.canvas.mpl_connect("key_press_event", lambda event: self.zoom_in(event) if event.key == "up" else None)
        # self.canvas.mpl_connect("key_press_event", lambda event: self.zoom_out(event) if event.key == "down" else None)
        # self.canvas.mpl_connect("key_press_event", lambda event: self.move_data(event))
        self.canvas.mpl_connect("key_press_event", self.handle_key_press)
        self.canvas.mpl_connect("scroll_event", self.on_scroll)
        # 连接鼠标事件
        self.canvas.mpl_connect("button_press_event", self.on_mouse_press)
        self.canvas.mpl_connect("motion_notify_event", self.on_mouse_move)
        self.canvas.mpl_connect("button_release_event", self.on_mouse_release)

        #self.setMouseTracking(True)  # 允许鼠标移动事件被捕获
        self.last_k_index = None
        self.index_min = 0
        self.index_max = 0
        self.dragging = False
        self.last_mouse_x = None
        self.target_index = None  # 目标位置索引
        self.should_location = None




    def format_info(self, index):
        if index < len(self.filtered_rows):
            current_data = self.filtered_rows.iloc[int(index)]
            return f"{current_data.name.strftime('%Y-%m-%d')}\n" \
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

        #print("==============[on_move]=================", event.inaxes == self.ax1)
        if event.inaxes == self.ax1:
            global_pos = QCursor().pos()
            #print("global_pos", global_pos)  # global_pos PyQt5.QtCore.QPoint(3008, 601)
            local_pos = self.mapFromGlobal(global_pos)  # local= PyQt5.QtCore.QPoint(623, 233)
            xmouse, ymouse = self.ax1.transData.inverted().transform((local_pos.x(), local_pos.y()))  # xmouse 是转换后的 x 坐标
            #print("local=", local_pos)
            plt_pos = (local_pos.x(), local_pos.y())
            #print("plt_pos=", plt_pos)
            current_index = int(xmouse)
            #print("xmouse=", xmouse)
            self.update_crosshair_and_info(global_pos, plt_pos, current_index)


    def update_crosshair_and_info(self, global_pos, plt_pos, target_index, from_key=False):
        #print("[update_crosshair_and_info]", global_pos, plt_pos, target_index)
        if 0 <= target_index < len(self.filtered_rows):
            #print("[update_crosshair_and_info] pos=", plt_pos, "current_index=", target_index)  # pos=(327,332), index=11
            # 更新十字线位置
            #print("[update_crosshair_and_info] self.cursor.lineh.set_ydata([ymouse, ymouse])  # 更新水平线位置", ymouse)
            #self.cursor.lineh.set_ydata([ymouse, ymouse])  # 更新水平线位置
            #print("[update_crosshair_and_info] self.cursor.linev.set_xdata([target_index, target_index])  # 更新垂直线位置 ", target_index)
            self.cursor.linev.set_xdata([target_index, target_index])  # 更新垂直线位置
            if from_key:
                print("画条 键盘线")
                if not hasattr(self, "crosshair"):
                    self.crosshair = Crosshair(self.ax1)
                # 初始化十字光标位置
                self.crosshair.update(target_index, self.filtered_rows.iloc[target_index]['close'])
                self.canvas.draw_idle()
            else:
                if hasattr(self, "crosshair"):
                    self.crosshair.disconnect()

            # 更新信息窗口
            info_text = self.format_info(target_index)  # 使用目标索引获取信息
            self.info_window.update_info(info_text, self)

            # 获取主窗口的几何信息
            main_window_rect = self.info_window.parent().geometry()  # 获取主窗口的几何信息
            info_window_rect = self.info_window.geometry()  # 获取信息窗口的几何信息

            print("global_pos=",global_pos,"plt_pos=",plt_pos,"target_index=",target_index)
            # 计算新的位置
            new_x = global_pos.x()
            new_y = global_pos.y()

            # 确保信息窗口不超出主窗口的边界
            # 移动信息窗口到目标位置
            self.info_window.move(new_x, new_y)  # 移动信息窗口到目标位置
            self.info_window.show()  # 显示信息窗口
            self.should_location = global_pos
            self.last_k_index = target_index

    def move_crosshair(self, target_index):
        print("移动命令，收到currentx=", target_index)
        # 更新十字光标的位置
        x_pos = target_index  # K线的索引作为 x 坐标
        y_pos = self.ax1.get_ylim()[0]  # 可以选择 y 轴的最小值或其他值

        # 更新十字线的 x 和 y 坐标
        self.cursor.linev.set_xdata([x_pos, x_pos])  # 更新垂直线位置
        self.cursor.lineh.set_ydata([y_pos, self.ax1.get_ylim()[1]])  # 更新水平线位置
        # 更新信息窗口和标题
        pos = (x_pos, y_pos)  # 这里可以根据需要调整
        #time.sleep(2)
        self.update_crosshair_and_info(self.should_location or QCursor().pos(), pos, target_index)  # 更新十字光标和信息窗口
        # 重新绘制画布以更新十字光标
        self.canvas.draw_idle()  # 使用 draw_idle() 进行重绘

    def handle_key_press(self, event):
        print(f"[handle_key_press] event.key =[{event.key}]")  # 调试信息
        if event.key == "control":
            self.dragging = True  # 开始拖动
            print("enter space, dragging = ", self.dragging)
        elif event.key == "left":
            self.move_item(event, -1)
        elif event.key == "right":
            self.move_item(event, 1)
        elif event.key == "d":
            self.target_index = self.target_index + 1 if self.target_index is not None else 0
            print("you press a")
            self.move_crosshair(self.target_index)
        elif event.key == "a":
            print("you press d")
            self.target_index = self.target_index-1 if self.target_index>0 else 0
            self.move_crosshair(self.target_index)


        elif event.key == "up":
            # 放大
            self.zoom_in(event)
        elif event.key == "down":
            # 缩小
            self.zoom_out(event)
        elif event.key == "shift+right":
            # 向左移动数据范围
            center = (self.filtered_rows["idx"].max() + self.filtered_rows["idx"].min()) / 2
            data_range = self.filtered_rows["idx"].max() - self.filtered_rows["idx"].min()
            new_center = center - data_range / 10  # 移动一个数据的十分之一
            new_range = data_range / self.zoom_level
            self.ax1.set_xlim(new_center - new_range / 2, new_center + new_range / 2)
            self.canvas.draw_idle()
        elif event.key == "shift+left":
            # 向右移动数据范围
            center = (self.filtered_rows["idx"].max() + self.filtered_rows["idx"].min()) / 2
            data_range = self.filtered_rows["idx"].max() - self.filtered_rows["idx"].min()
            new_center = center + data_range / 10  # 移动一个数据的十分之一
            new_range = data_range / self.zoom_level
            self.ax1.set_xlim(new_center - new_range / 2, new_center + new_range / 2)
            self.canvas.draw_idle()



        # 更新十字线的水平位置
        if event.key in ["left", "right"]:
            ymouse = self.cursor.lineh.get_ydata()[0]  # 获取当前的 y 位置
            self.cursor.lineh.set_ydata([ymouse, ymouse])  # 更新水平线的位置


    def move_item(self, event, direction=1):
        """
        处理 K 线图中十字光标的移动和更新。

        :param event: 触发事件的对象，通常是鼠标事件
        :param direction: 移动方向，1 表示下一个 K 线，-1 表示上一个 K 线
        """
        print(f"----------------------[right]# move_item------------------------")
        self.setMouseTracking(False)  # 禁止鼠标移动事件被捕获

        # 获取当前鼠标位置
        if self.should_location is None:
            print("self.should_location 为空，取当前鼠标值")
            self.should_location = QCursor().pos()
        else:
            print("self.should_location 非空,value=", self.should_location)

        # 获取当前 K 线索引
        if self.last_k_index is None:
            print("self.target_index 为空")
            current_x = max(self.cursor.linev.get_xdata()[0], 0)  # 获取当前十字线位置
            print("获取当前十字线位置current_x=", current_x)
            self.last_k_index = current_x  # 获取当前十字线位置
            current_y = self.cursor.lineh.get_ydata()[0]  # 获取当前十字线位置
            y_pos = max(self.ax1.get_ylim()[0], 0)  # 可以选择 y 轴的最小值或其他值
        else:
            print("self.target_index 非空,value=", self.last_k_index)
            current_x = self.last_k_index  # 获取当前 K 线的索引
            current_y = self.cursor.lineh.get_ydata()[0]  # 获取当前 K 线的索引

        print("[right]current_x", current_x, "max=", len(self.filtered_rows) - 1)  # [right]current_x 47 max= 79

        # 计算下一个或上一个 K 线的索引
        next_index = current_x + direction  # 根据方向计算下一个或上一个 K 线的索引

        if 0 <= next_index < len(self.filtered_rows):  # 确保索引在有效范围内
            print("没有超过K线的最大索引 next_index=", next_index)
            x_data = next_index  # K 线的 x 坐标
            y_data = (self.ax1.get_ylim()[0] + self.ax1.get_ylim()[1]) / 2  # 选择 y 坐标
            self.should_location = self.ax1.transData.transform((x_data, y_data))  # 转换为屏幕坐标

            if isinstance(self.should_location, np.ndarray):
                self.should_location = QPoint(int(self.should_location[0]), int(self.should_location[1]))

            print("转换后self.should_location=", self.should_location, "next_index=", next_index)

            # 将全局屏幕坐标转换为窗口坐标
            local_pos = self.mapFromGlobal(self.should_location)  # 使用 self.mapFromGlobal
            print("[right] global_pos=", self.should_location, "[right] localpos=", local_pos)

            # 将窗口坐标转换为数据坐标
            xmouse, ymouse = self.ax1.transData.inverted().transform((local_pos.x(), local_pos.y()))
            print("[right] 小于最大, xmouse=", xmouse)

            self.cursor.lineh.set_ydata([next_index, next_index])  # 更新十字线位置
            self.cursor.linev.set_xdata([next_index, next_index])  # 更新十字线位置

            print("要移动到的目标位置,新current_x=", next_index)
            pos = self.ax1.transData.transform((next_index, 0))  # 获取目标位置的屏幕坐标
            print("[right] 计算目标位置的屏幕坐标 pos=", pos)  # [ 597.0778481  -352.56707383]
            print(event)

            self.should_location = self.mapToGlobal(self.should_location)
            self.update_crosshair_and_info(self.should_location, local_pos, next_index,
                                           from_key=True)  # 传递目标位置和当前索引
        else:
            print("索引超出范围，无法移动")

    def calculate_absolute_position(self, index, debug=False):
        # 将 K 线的索引转换为全局屏幕坐标
        print("[index_to_global] enter， para=",index)
        x_data = index
        y_data = (self.ax1.get_ylim()[0] + self.ax1.get_ylim()[1]) / 2  # 选择 y 坐标
        global_pos = self.ax1.transData.transform((x_data, y_data))  # 转换为屏幕坐标
        if isinstance(global_pos, np.ndarray):
            print("globalpos is numpy array")
            global_pos = QPoint(int(global_pos[0]), int(global_pos[1]))
            print("after convert , globalpos=",global_pos)
        return global_pos


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
        self.index_min = self.filtered_rows["idx"].min()  # 最小索引
        self.index_max = self.filtered_rows["idx"].max()  # 最大索引

        # 创建网格布局并确定子图
        gs = self.figure.add_gridspec(2, 1, height_ratios=[4, 1])
        self.ax1 = self.figure.add_subplot(gs[0])

        #ax2 = self.ax1.twinx()  # 对于成交量的次坐标轴
        ax2 = self.figure.add_subplot(gs[1], sharex=self.ax1)
 
        # 创建均线的 addplot 对象
        ma5_addplot = mpf.make_addplot(self.filtered_rows['ma5'], color='yellow', title='ma5',ax=self.ax1)
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
        mpf.plot(self.filtered_rows, type="candle", style=s, ylabel='价格', ax=self.ax1, volume=ax2, addplot=add_plot,)


        # 设置图表交互
        self.zoom_level = 1.0  # 100%
        self.ax1.tick_params(axis="both", which="major", labelsize=5)
        self.ax1.yaxis.labelpad = -5
        ax2.tick_params(axis="both", which="major", labelsize=5)


        self.canvas.setFocus()
        self.apply_zoom()


    def on_scroll(self, event):
        if event.button == 'up':
            self.zoom_in(event)  # 放大
        elif event.button == 'down':
            self.zoom_out(event)  # 缩小

    def on_mouse_press(self, event):
        if event.button == 1 and self.dragging:  # 左键按下
            self.last_mouse_x = event.xdata  # 记录鼠标的 x 坐标

    def on_mouse_move(self, event):
        if self.dragging and self.last_mouse_x is not None:
            # 计算鼠标移动的距离
            dx = event.xdata - self.last_mouse_x
            if dx != 0:
                # 更新 K 线图的 x 轴范围
                xlim = self.ax1.get_xlim()
                new_xlim = (xlim[0] - dx, xlim[1] - dx)
                self.ax1.set_xlim(new_xlim)
                self.canvas.draw()  # 重绘画布
                self.last_mouse_x = event.xdata  # 更新最后的鼠标 x 坐标

    def on_mouse_release(self, event):
        if event.button == 1:  # 左键释放
            self.dragging = False  # 停止拖动
            self.last_mouse_x = None  # 重置鼠标 x 坐标
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