from kivy.app import App
from kivy.uix.label import Label

class MehrabApp(App):
    def build(self):
        return Label(text="مهراب", font_size='30sp')

if __name__ == "__main__":
    MehrabApp().run()
