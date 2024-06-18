from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    
    def search_image(self):
        self.manager.current_screen.ids.img.source = 'files/nature.jpg'
    
    
class Rootwidget(ScreenManager):
    pass

class MainApp(App):
    
    def build(self):
        return Rootwidget()
    

MainApp().run()