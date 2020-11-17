# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import wx
from FramePrincipal import FramePrincipal



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = wx.App()

    framePrincipal=FramePrincipal(None)
    framePrincipal.Show(True)
    app.MainLoop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
