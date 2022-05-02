import hashlib
import tkinter as tk
import time

LOG_LINE_NUM = 0


class MyGui:
    def __init__(self, window):
        self.window = window

        # 得到屏幕宽度
        sw = window.winfo_screenwidth()
        # 得到屏幕高度
        sh = window.winfo_screenheight()
        # 窗口宽高为100
        ww = 1068
        wh = 681
        window.geometry("%dx%d+%d+%d" % (ww, wh, (sw - ww) / 2, (sh - wh) / 2))

        window.title("文本处理工具_v1.2")  # 窗口名
        # 290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        # win.geometry('320x160+10+10')
        # win.geometry('1068x681+10+10')
        # 窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        # win["bg"] = "pink"
        window.attributes("-alpha", 0.9)  # 虚化，值越小虚化程度越高

        main_menu = tk.Menu(window)
        menu_file = tk.Menu(main_menu)
        main_menu.add_cascade(label="文件", menu=menu_file)
        menu_file.add_command(label="新建", command=self.new)
        menu_file.add_command(label="打开", command=self.open)
        menu_file.add_separator()  # 分割线
        menu_file.add_command(label="退出", command=window.destroy)

        menu_edit = tk.Menu(main_menu)  # 菜单分组 menuEdit
        main_menu.add_cascade(label="编辑", menu=menu_edit)
        menu_edit.add_command(label="剪切", command=self.cut)
        menu_edit.add_command(label="复制", command=self.cop)
        menu_edit.add_command(label="粘贴", command=self.pas)
        window.config(menu=main_menu)

        frame = tk.Frame(window)
        frame.grid()
        # frame = window
        # input
        tk.Label(frame, text="待处理数据").grid(row=0, column=0)
        self.init_data_Text = tk.Text(frame)
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)

        # output
        tk.Label(frame, text="输出结果").grid(row=0, column=12)
        self.result_data_Text = tk.Text(frame)
        self.result_data_Text.grid(row=1, column=12, rowspan=20, columnspan=10)

        # log
        tk.Label(frame, text="日志").grid(row=12, column=0)
        self.log_data_text = tk.Text(frame)
        self.log_data_text.grid(row=13, column=0, rowspan=10, columnspan=10)

        # 按钮
        md5_btn = tk.Button(frame, text="MD5", bg="lightblue", width=10, command=self.str_trans_to_md5)
        md5_btn.grid(row=1, column=11)

    def new(self):
        self.write_log_to_text("new")

    def open(self):
        self.write_log_to_text("open")

    def cut(self):
        s = '剪切'
        self.write_log_to_text(s)

    def cop(self):
        s = '复制'
        self.write_log_to_text(s)

    def pas(self):
        s = '粘贴'
        self.write_log_to_text(s)

    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0, tk.END).strip().replace("\n", "").encode()
        if src:
            try:
                md5 = hashlib.md5()
                md5.update(src)
                self.result_data_Text.delete(1.0, tk.END)
                self.result_data_Text.insert(1.0, md5.hexdigest())
                self.write_log_to_text("INFO:str_trans_to_md5 success")
            except Exception as e:
                self.result_data_Text.delete(1.0, tk.END)
                self.result_data_Text.insert(1.0, "字符串转MD5失败" + str(e))
        else:
            self.write_log_to_text("ERROR:str_trans_to_md5 failed")

    # 日志动态打印
    def write_log_to_text(self, message):
        global LOG_LINE_NUM
        current = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        msg_text = current + " " + str(message) + "\n"  # 换行
        if LOG_LINE_NUM <= 7:
            self.log_data_text.insert(tk.END, msg_text)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_text.delete(1.0, 2.0)
            self.log_data_text.insert(tk.END, msg_text)


def gui_start():
    init_window = tk.Tk()  # 实例化出一个父窗口
    MyGui(init_window)
    init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()
