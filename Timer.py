# _*_ coding:utf-8 _*_
import wx
from datetime import datetime


class TimerFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600, 400), pos=(500, 500))
        # 绑定事件(自动刷新)
        self.Bind(wx.EVT_IDLE, self.flush)
        # 设置面板
        panel = wx.Panel(self)
        panel.SetBackgroundColour('black')
        # 绑定字体
        self.greet = wx.StaticText(panel, label='', pos=(157, 110))
        self.timeStr = wx.StaticText(panel, label='', pos=(157, 170))
        self.timeStr.SetForegroundColour('white')
        self.greet.SetForegroundColour('white')
        # 字体样式
        font = wx.Font(30, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.timeStr.SetFont(font)
        self.greet.SetFont(font)
        # 显示窗口
        self.Show(True)

    def flush(self, e):
        # 显示问候语
        hour = int(datetime.now().strftime("%H"))
        if 7 <= hour < 12:
            self.greet.SetLabel("上午好,  Second")
        if 12 <= hour < 13:
            self.greet.SetLabel("中午好,  Second")
        if 13 <= hour < 19:
            self.greet.SetLabel("下午好,  Second")
        if 19 <= hour < 22:
            self.greet.SetLabel("晚上好,  Second")
        if hour >= 22 or hour < 7:
            self.greet.SetLabel("晚安,  Second")
        # 获取时间
        now = datetime.now().strftime("%Y-%m-%d \n%H:%M:%S")
        self.timeStr.SetLabel(str(now))


app = wx.App(False)
frame = TimerFrame(None, 'clock')
app.MainLoop()
