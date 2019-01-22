#! /usr/bin/python

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
import state
from kivy import Config

Config.set('kivy', 'exit_on_escape', '1')
Config.set('graphics', 'borderless', 1)
Config.set('graphics', 'height', 80)
Config.set("graphics", "width", 150)
Config.set("graphics", "fullscreen", 'fake')

class MyLabel(Image):
    text = StringProperty('')

    def on_text(self, *_):
        # Just get large texture:
        l = Label(text=self.text, )
        l.font_size = '50dp'  # something that'll give texture bigger than phone's screen size
        l.texture_update()
        # Set it to image, it'll be scaled to image size automatically:

        self.texture = l.texture





class Display(MyLabel):
    def update(self, *args):
        try:
            one = state.state.getInstance()
            self.text = one.GetLevel()
            if one.state:
                self.color = [1,0,0,1]
            else:
                self.color = [0,1,0,1]
        except: None


class TestApp(App):
    title = "LinuxSpeachAPI"
    def build(self):
        display = Display()
        Clock.schedule_interval(display.update, 0.5)
        return display

if __name__ == '__main__':
    import test
    import threading
    t = threading.Thread(target=test.start_listening)
    t.start()
    TestApp().run()
