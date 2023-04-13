from kivymd.app import MDApp
#from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

Builder.load_file('biblescreenmanager.kv')
Builder.load_file('chapterselect.kv')
Builder.load_file('display.kv')

class BibleScreenManager(ScreenManager):
    pass
class Bible(Screen):
    def display(self,book_number):
        #print(book_number,'with',len(root[book_number]),'chapters')
        self.root.manager.screens[1].book = book_number
        self.root.manager.current = 'chapterselect'
class BibleApp(MDApp):
    def build(self):
        self.title = 'KJV Bible'
        return BibleScreenManager()
if __name__ == '__main__':
    from kivy.core.window import Window
    from kivy.utils import get_color_from_hex
    Window.clearcolor = get_color_from_hex('#FFFFFF')
    BibleApp().run()