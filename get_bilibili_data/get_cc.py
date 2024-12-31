import tkinter,threading,get_cc_utils          #载入模块
import browser_cookie3
import ctypes
ctypes.windll.shell32.IsUserAnAdmin()
get_cc_utils.cookie = browser_cookie3.firefox()
def get(BV):
    cc_list = get_cc_utils.downAll(BV)
    return cc_list
#print(get("BV12t4y1X7oA"))
