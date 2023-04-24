
print("============== Environment ===================")

print("-------- Installation of Kivy --------")

#pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew

print("pip install kivy")
#python -m pip install kivy[full]

print("============== Hello World ===================")

from kivy.app import App
from kivy.uix.button import Button
 
class TestApp(App):
    def build(self):
        return Button(text= " Hello Kivy World ")
 
TestApp().run()