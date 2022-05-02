from tkinter import *
from tkinter import ttk
import tkinter.filedialog as dir
from database import DataMgr
import queue,progressbar,threading,disk

class AppUI():

    def __init__(self):
        self.notify_queue = queue.Queue()
        root = Tk()
        self.master = root
        self.create_menu(root)
        self.create_content(root)
        self.path = 'C:'
        root.title("磁盘文件搜索工具")
        root.update()
        # root.resizable(False, False) 调用方法会禁止根窗体改变大小
        #以下方法用来计算并设置窗体显示时，在屏幕中心居中
        curWidth = root.winfo_width()
        curHeight = root.winfo_height()
        scnWidth, scnHeight = root.maxsize()
        tmpcnf = '+%d+%d' % ((scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
        root.geometry(tmpcnf)

        self.gress_bar = progressbar.GressBar()
        self.data_mgr = DataMgr()
        self.process_msg()
        root.mainloop()


    def create_menu(self,root):
        #创建菜单栏
        menu = Menu(root)

        file_menu = Menu(menu,tearoff=0)
        # 创建二级菜单
        file_menu.add_command(label="设置路径",command=self.open_dir)
        file_menu.add_separator()
        file_menu.add_command(label="扫描",command=self.execute_asyn)

        about_menu = Menu(menu,tearoff=0)
        about_menu.add_command(label="version:1.0")

        #在菜单栏中添加菜单
        menu.add_cascade(label="文件",menu=file_menu)
        menu.add_cascade(label="关于",menu=about_menu)
        root['menu'] = menu

    def create_content(self, root):
        lf = ttk.LabelFrame(root, text="文件搜索")
        lf.pack(fill=X, padx=15, pady=8)

        top_frame = Frame(lf)
        top_frame.pack(fill=X,expand=YES,side=TOP,padx=15,pady=8)

        self.search_key = StringVar()
        ttk.Entry(top_frame, textvariable=self.search_key,width=50).pack(fill=X,expand=YES,side=LEFT)
        ttk.Button(top_frame,text="搜索",command=self.search_file).pack(padx=15,fill=X,expand=YES)

        bottom_frame = Frame(lf)
        bottom_frame.pack(fill=BOTH,expand=YES,side=TOP,padx=15,pady=8)

        band = Frame(bottom_frame)
        band.pack(fill=BOTH,expand=YES,side=TOP)

        self.list_val = StringVar()
        listbox = Listbox(band,listvariable=self.list_val,height=18)
        listbox.pack(side=LEFT,fill=X,expand=YES)

        vertical_bar = ttk.Scrollbar(band,orient=VERTICAL,command=listbox.yview)
        vertical_bar.pack(side=RIGHT,fill=Y)
        listbox['yscrollcommand'] = vertical_bar.set

        horizontal_bar = ttk.Scrollbar(bottom_frame,orient=HORIZONTAL,command=listbox.xview)
        horizontal_bar.pack(side=BOTTOM,fill=X)
        listbox['xscrollcommand'] = horizontal_bar.set

        #给list动态设置数据，set方法传入一个元组，注意此处是设置，不是插入数据，此方法调用后，list之前的数据会被清除
        self.list_val.set(('jioj',124,"fjoweghpw",1,2,3,4,5,6))

    def process_msg(self):
        self.master.after(400,self.process_msg)
        while not self.notify_queue.empty():
            try:
                msg = self.notify_queue.get()
                if msg[0] == 1:
                    self.gress_bar.quit()

            except queue.Empty:
                pass

    def execute_asyn(self):
        #定义一个scan函数，放入线程中去执行耗时扫描
        def scan(_queue):
            if self.path:
                paths = disk.scan_file(self.path)
                self.data_mgr.batch_insert(paths)

            _queue.put((1,))

        th = threading.Thread(target=scan,args=(self.notify_queue,))
        th.setDaemon(True)
        th.start()
        #启动进度条
        self.gress_bar.start()

    def search_file(self):
        if self.search_key.get():
            result_data = self.data_mgr.query(self.search_key.get())
            if result_data:
                self.list_val.set(tuple(result_data))


    def open_dir(self):
        d = dir.Directory()
        self.path = d.show(initialdir=self.path)

if __name__ == "__main__":
    AppUI()