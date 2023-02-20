from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from homepage import HomePage


class InstagramApp(MDApp):
    def build(self):
        Window.size = [300, 600]
        self.load_all_kv_files()
        return HomePage()

    def load_all_kv_files(self):
        Builder.load_file("homepage.kv")
        Builder.load_file("appbar.kv")
        Builder.load_file('storycreator.kv')
        Builder.load_file('bottom_nav.kv')
        Builder.load_file('avatar_image.kv')
        Builder.load_file('postcard.kv')

    def on_start(self):
        self.root.dispatch('on_enter')


if __name__ == "__main__":
    InstagramApp().run()
