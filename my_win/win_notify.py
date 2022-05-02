import win32gui
import win32con


def notify(hwnd, msg, wparam, lparam):
    print("notify", msg)
    if lparam == win32con.WM_LBUTTONDBLCLK:
        print("双击左键", msg)
        pass
    elif lparam == win32con.WM_LBUTTONUP:
        print("左键弹起", msg)
        pass
    return True


wc = win32gui.WNDCLASS()
wc.hInstance = win32gui.GetModuleHandle(None)
wc.lpszClassName = "测试"
wc.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW
wc.lpfnWndProc = notify

classAtom = win32gui.RegisterClass(wc)

hwnd = win32gui.CreateWindow(classAtom,
                             "tst2",
                             win32con.WS_OVERLAPPEDWINDOW,
                             win32con.CW_USEDEFAULT,
                             win32con.CW_USEDEFAULT,
                             win32con.CW_USEDEFAULT,
                             win32con.CW_USEDEFAULT,
                             None,
                             None,
                             None,
                             None
                             )

notify_id = (hwnd,
             0,
             win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP,
             win32con.WM_USER + 20,
             win32gui.LoadIcon(0, win32con.IDI_APPLICATION),
             "文字"
             )

win32gui.Shell_NotifyIcon(0, notify_id)

win32gui.PumpMessages()
