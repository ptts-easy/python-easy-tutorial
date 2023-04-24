import wx

print("============== Environment ===================")

print("-------- Installation of wxPython --------")

print("pip install -U wxPython")

print("-------- Checking wxPython Version --------")

wx.version()

print("============== Hello World ===================")

# First things, first. Import the wxPython package.
import wx

# Next, create an application object.
app = wx.App(False)

# Then a frame.
frm = wx.Frame(None, title="Hello World")

# Show it.
frm.Show(True)

# Start the event loop.
app.MainLoop()