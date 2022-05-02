import ctypes
import os
import time
import tkinter as tk
import tkinter.filedialog
import win32gui
from PIL import ImageGrab


def capture_fullscreen():
    pic = ImageGrab.grab()
    save_pic(pic)


def capture_current_windows():
    class RECT(ctypes.Structure):
        _fields_ = [('left', ctypes.c_long),
                    ('top', ctypes.c_long),
                    ('right', ctypes.c_long),
                    ('bottom', ctypes.c_long)]

        def __str__(self):
            return str((self.left, self.top, self.right, self.bottom))

    rect = RECT()

    HWND = win32gui.GetForegroundWindow()

    ctypes.windll.user32.GetWindowRect(HWND, ctypes.byref(rect))

    rangle = (rect.left + 2, rect.top + 2, rect.right + 2, rect.bottom + 2)

    pic = ImageGrab.grab(rangle)
    save_pic(pic)


def capture_choose_windows():
    try:
        dll_handle = ctypes.cdll.LoadLibrary("CameraDll.dll")
    except Exception:
        try:
            os.system("Rundll32.exe CameraDll.dll, CameraSubArea")
        except Exception:
            return

    else:
        try:
            dll_handle.CameraSubArea(0)
        except Exception:
            return


def save_pic(pic):
    file_name = '未命名图片' + time.strftime('%Y%m%d%H%M%S') + '.png'
    root = tk.Tk()
    root.withdraw()  # 主窗口隐藏
    filepath = tk.filedialog.asksaveasfilename(
        parent=root,
        title="设置截图保存位置",
        initialfile=file_name,
        defaultextension=".png")
    if filepath:
        try:
            pic.save(filepath)
        except ValueError as e:
            print(str(e))
    else:
        print('取消了选择')
    root.destroy()


def main():
    capture_fullscreen()


if __name__ == "__main__":
    main()
