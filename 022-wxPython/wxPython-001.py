import wx
 
class MyFrame(wx.Frame):
    def __init__(self,parent,title):
        super().__init__(parent,title=title,size=(400,300))
        
        self.panel = MyPanel(self)
 
 
class MyPanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent)
 
 
class MyApp(wx.App):
    def OnInit(self):
        self.frame=MyFrame(parent=None, title= "wxPython Window")
        self.frame.Show()
        return True
 
app = MyApp()

app.MainLoop()