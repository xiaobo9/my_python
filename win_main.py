from my_win import *

if __name__ == '__main__':
    def capture_fullscreen(sys_tray_icon):
        scrap.capture_fullscreen()


    def capture_current_windows(sys_tray_icon):
        scrap.capture_current_windows()


    def capture_choose_windows(sys_tray_icon):
        scrap.capture_choose_windows()


    def bye(sys_tray_icon):
        print('退出')


    favicon = 'favicon.ico'
    options = (('抓取全屏', favicon, capture_fullscreen),
               ('抓取当前窗口', favicon, capture_current_windows),
               ('抓取所选区域', favicon, capture_choose_windows)
               )

    tray.SysTrayIcon(favicon, '抓图工具', options, on_quit=bye)
