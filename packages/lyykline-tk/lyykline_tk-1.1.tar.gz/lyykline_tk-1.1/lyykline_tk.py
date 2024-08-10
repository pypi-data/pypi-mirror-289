import os
import sys
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import lyywmdf
import matplotlib.font_manager as fm
import mplfinance as mpf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from datetime import datetime

import lyydata
import lengstock_widget
import lengstock_plt
from ttkbootstrap import Style
from lengstock_cfg import lengstock_cfg
import lengstock_functions
import lyystkcode

os.chdir(r"D:\UserData\resource\data")
from lyylog2 import log
log("finish all import")

"""
lyy的炒股软件
"""
# pyinstaller --noconfirm -n LengStock  --distpath  "D:/Soft/_lyysoft"  --add-data "D:/Soft/Program/pythonx64/Lib/site-packages/py_mini_racer/mini_racer.dll;." -D -w -i D:\UserData\resource\com_icos\man.ico D:\UserData\Documents\BaiduSyncdisk\0LengsStock\lengstock_main.py


class Kline_Class:
    def __init__(self, main_module):
        self.main_module = main_module
        log("class kline-win init")
        self.popup_window = tk.Toplevel(self.main_module.root)
        self.popup_window.title("K线图")
        self.popup_window.geometry(self.main_module.lengstock_cfg.geometry_sub)
        # 设置Toplevel窗口样式
        # self.style.configure("Toplevel.TLabel")
        # 设置中文字体
        font_path = r"C:\WINDOWS\Fonts\MSYH.TTC"  # 替换为您系统中微软雅黑字体的路径
        self.prop = fm.FontProperties(fname=font_path)
        print("font name = ",self.prop.get_name())
        self.figure = plt.Figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.popup_window)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # 使用fill和expand属性填充整个窗口
        self.canvas.draw()
        self.last_datax: int = 0  # 存储最后的x坐标

        def on_resize(event):
            width = event.width  # 减去一些边距，以便更好地适应窗口大小
            height = event.height
            print("width", width, "height", height)
            self.figure.set_size_inches(width / 100, height / 100)  # 根据窗口大小设置图形大小
            self.figure.tight_layout()
            self.canvas.draw()

        self.popup_window.bind("<Configure>", on_resize)
        self.popup_window.withdraw()

    def update_mouse_moved_flag(self):
        self.mouse_moved = True
        # 每隔100毫秒更新一次鼠标移动标志
        self.main_module.root.after(100, self.update_mouse_moved_flag)


    def show_kline(self, event):
        if not self.popup_window.winfo_exists():
            print("self.popup_windows已经不存在,self.popup_window ")
            self.create_popup_window()
        else:
            print("self.popup_window存在，清除之前的绘图先")
            # 删除之前的图形对象
            self.figure.clear()
            self.canvas.draw()
            self.popup_window.deiconify()
        if self.main_module.is_dark_mode:
            plt.style.use("dark_background")
        else:
            plt.style.use("default")
        plt.rcParams['font.family'] = self.prop.get_name()
        item = event.widget.selection()[0]
        code = event.widget.item(item, "values")[0]
        filtered_rows = self.main_module.dfall[self.main_module.dfall["code"] == code].copy()

        # 搞这些索引操作，都是为了取索引最大最小值来判断鼠标是否超过图标范围，避免异常。有没有更好办法。直接try except效率更高。
        filtered_rows.reset_index(drop=True, inplace=True)
        filtered_rows["idx"] = filtered_rows.index.values
        # 将日期列转换为datetime类型并设置为索引
        filtered_rows["day"] = pd.to_datetime(filtered_rows["day"])

        filtered_rows.set_index("day", inplace=True)
        print(filtered_rows.tail(3))
        # 预先计算日期格式化值
        self.formatted_dates = {i: date.strftime("%Y-%m-%d") for i, date in enumerate(filtered_rows.index)}

        # 创建网格布局
        gs = self.figure.add_gridspec(2, 1, height_ratios=[4, 1])
        ax1 = self.figure.add_subplot(gs[0])
        ax2 = self.figure.add_subplot(gs[1], sharex=ax1)
        # ax1.set_xlim(left=filtered_rows["day"].min(), right=filtered_rows["day"].max() + 1)
        ax1.set_ylim([filtered_rows["low"].min(), filtered_rows["high"].max()], None)
        # 创建最低值和最高值的addplot对象
        low_addplot = mpf.make_addplot(filtered_rows["low"], panel=0, ylabel="Low")
        high_addplot = mpf.make_addplot(filtered_rows["high"], panel=0, ylabel="High")

        # 绘制K线图
        mpf.plot(filtered_rows, type="candle", style="yahoo", ax=ax1, volume=ax2)

        print("# 添加一个十字线")
        crosshair_vline = ax1.axvline(x=0, color="gray", linestyle="--")
        crosshair_hline = ax1.axhline(y=0, color="gray", linestyle="--")
        crosshair_vline_ax2 = ax2.axvline(x=0, color="gray", linestyle="--")
        crosshair_hline_ax2 = ax2.axhline(y=0, color="gray", linestyle="--")

        # 设置初始的缩放比例
        self.zoom_level = 1.0  # 100%

        def move_data(event):
            if event.key == "left":
                # 向左移动一个数据
                current_x = crosshair_vline.get_xdata()[0]
                print("current_x", current_x)
                if current_x > self.index_min:
                    current_x -= 1
                crosshair_vline.set_xdata([current_x])
                date = filtered_rows.index[int(current_x)]
                # 格式化日期为年月日
                formatted_date = date.strftime("%Y-%m-%d")
                # 设置标题
                ax1.set_title(f"X = {int(current_x)} | Y = {current_x:.2f} | Date = {formatted_date}", fontproperties=self.prop)

                self.canvas.draw()
            elif event.key == "right":
                # 向右移动一个数据
                current_x = crosshair_vline.get_xdata()[0]
                print("current_x", current_x)
                if current_x < self.index_max:
                    current_x += 1
                crosshair_vline.set_xdata([current_x])
                date = filtered_rows.index[int(current_x)]
                # 格式化日期为年月日
                formatted_date = date.strftime("%Y-%m-%d")
                # 设置标题
                ax1.set_title(f"X = {int(current_x)} | Y = {current_x:.2f} | Date = {formatted_date}", fontproperties=self.prop)

                self.canvas.draw()
                pass
            elif event.key == "shift+right":  # 检查Shift键是否被按下
                # 向左移动一个数据
                center = (filtered_rows["idx"].max() + filtered_rows["idx"].min()) / 2
                data_range = filtered_rows["idx"].max() - filtered_rows["idx"].min()
                new_center = center - data_range / 10  # 移动一个数据的十分之一
                new_range = data_range / self.zoom_level
                ax1.set_xlim(new_center - new_range / 2, new_center + new_range / 2)
                self.canvas.draw()
            elif event.key == "shift+left":  # 检查Shift键是否被按下
                # 向右移动一个数据
                center = (filtered_rows["idx"].max() + filtered_rows["idx"].min()) / 2
                data_range = filtered_rows["idx"].max() - filtered_rows["idx"].min()
                new_center = center + data_range / 10  # 移动一个数据的十分之一
                new_range = data_range / self.zoom_level
                ax1.set_xlim(new_center - new_range / 2, new_center + new_range / 2)
                self.canvas.draw()

        # 应用缩放因子到K线图中
        def apply_zoom():
            # 计算新的数据范围
            data_range = filtered_rows["idx"].max() - filtered_rows["idx"].min()
            new_range = data_range / self.zoom_level
            center = (filtered_rows["idx"].max() + filtered_rows["idx"].min()) / 2

            # 设置新的数据范围
            ax1.set_xlim(center - new_range / 2, center + new_range / 2)
            self.canvas.draw()

        # 定义放大和缩小的函数
        def zoom_in(event):
            self.zoom_level *= 1.1  # 放大10%
            print("zoom_in", self.zoom_level)
            apply_zoom()
            # self.canvas.draw()

        def zoom_out(event):
            self.zoom_level /= 1.1  # 缩小10%
            print("zoom_out", self.zoom_level)
            apply_zoom()
            # self.canvas.draw()

        # 鼠标移动事件处理函数
        def on_move(event):
            if event.inaxes is None:
                print("Mouse coordinates outside the plot.")
                return
            print(event.key, "xdata=", int(event.xdata), "ydata=", round(event.ydata, 2), self.last_datax)
            self.mouse_moved = False
            # if (event.xdata % 1 < 0.9 or event.xdata % 1 >0.1) and event.key != "shift":
            #     print("xdata not changed")
            #     return

            xmouse = self.last_datax = int(event.xdata)
            ymouse = event.ydata
            print(xmouse, ymouse)
            screen_x = self.main_module.root.winfo_pointerx()
            screen_y = self.main_module.root.winfo_pointery()
            window_width = self.main_module.root.winfo_width()
            window_height = self.main_module.root.winfo_height()
            print("# 获取Tkinter窗口的宽度和高度=", window_width, window_height)

            # 检查鼠标坐标是否超出了窗口范围
            if screen_x < 0 or screen_x > window_width or screen_y < 0 or screen_y > window_height:
                print("Mouse coordinates outside the Tkinter window.")
                print(screen_x < 0 , screen_x > window_width , screen_y < 0 , screen_y > window_height)
                # 没用，因为还没出窗口，只要出plot还会变导致异常。
                # return
            if xmouse is not None and ymouse is not None:
                # 获取数据的索引范围
                # self.index_min, self.index_max = filtered_rows.index[[0, -1]]
                self.index_min, self.index_max = filtered_rows["idx"].iloc[[0, -1]]
                # 2023-10-18 00:00:00 2024-03-01 00:00:00 94.06483516483517 0.372857142857143 <class 'pandas._libs.tslibs.timestamps.Timestamp'> <class 'pandas._libs.tslibs.timestamps.Timestamp'> <class 'numpy.f
                # 确保xmouse在索引范围内

                if self.index_min <= xmouse <= self.index_max:
                    # 使用xmouse作为索引获取对应的日期
                    formatted_date = self.formatted_dates[int(xmouse)]
                    # 设置标题
                    ax1.set_title(f"X = {int(xmouse)} | Y = {ymouse:.2f} | Date = {formatted_date}", fontproperties=self.prop)
                else:
                    print("# xmouse不在索引范围内，则不设置标题")
                    # ax1.set_title("")
                print("# 更新十字线的位置", xmouse, round(ymouse, 2))
                crosshair_vline.set_xdata([xmouse])
                crosshair_hline.set_ydata([ymouse])
                crosshair_vline_ax2.set_xdata([xmouse])
                crosshair_hline_ax2.set_ydata([ymouse])
                self.canvas.draw_idle()

        print("# 调整字体大小和标签间距")
        ax1.tick_params(axis="both", which="major", labelsize=5)
        ax1.yaxis.labelpad = -5
        ax2.tick_params(axis="both", which="major", labelsize=5)
        self.canvas.mpl_connect("motion_notify_event", on_move)
        self.canvas.mpl_connect("key_press_event", lambda event: zoom_in(event) if event.key == "up" else None)
        self.canvas.mpl_connect("key_press_event", lambda event: zoom_out(event) if event.key == "down" else None)
        self.canvas.mpl_connect("key_press_event", lambda event: move_data(event))
        apply_zoom()
        # self.canvas.draw()



