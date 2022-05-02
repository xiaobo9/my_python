import calendar
import datetime
from tkinter import *


class MyCalendar:
    def __init__(self):
        self.root = Tk()
        root = self.root

        now = datetime.datetime.now()
        # 默认日期
        self.Year = now.year
        self.Month = now.month

        month_cal = calendar.monthcalendar(self.Year, self.Month)
        Button(root, text='Previous', command=self.previous_month).grid(row=len(month_cal) + 3, column=0)
        Button(root, text='Next', command=self.next_month).grid(row=len(month_cal) + 3, column=6)

        self.draw_cal()

    def start(self):
        self.root.mainloop()

    def draw_cal(self):
        year = self.Year
        month = self.Month
        root = self.root

        # 首行放置“年、月”的位置
        Label(root, text=str(year) + "年").grid(row=0, column=2)
        Label(root, text=str(month) + "月").grid(row=0, column=4)

        # labels列表：放置“星期”的标题
        labels = [['周一', '周二', '周三', '周四', '周五', '周六', '周日']]

        # 用calendar库计算日历
        month_cal = calendar.monthcalendar(year, month)
        print(len(month_cal))
        print(month_cal)
        # 把日历加到labels列表中
        for i in range(len(month_cal)):
            labels.append(month_cal[i])

        # 先把界面清空
        for r in range(7):
            for c in range(7):
                Label(root, width=5, padx=5, pady=5, text=' ').grid(row=r + 1, column=c)

        # 放置日历
        for r in range(len(month_cal) + 1):
            for c in range(7):
                if labels[r][c] == 0:
                    labels[r][c] = ' '

                Label(root, width=5, padx=5, pady=5, text=str(labels[r][c])).grid(row=r + 1, column=c)  # 网格布局

    def previous_month(self):
        self.Month = self.Month - 1
        if self.Month < 1:
            self.Month = self.Month + 12
            self.Year = self.Year - 1
        self.draw_cal()

    def next_month(self):
        self.Month = self.Month + 1
        if self.Month > 12:
            self.Month = self.Month - 12
            self.Year = self.Year + 1
        self.draw_cal()


if __name__ == "__main__":
    MyCalendar().start()
