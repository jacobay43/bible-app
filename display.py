from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
import xml.etree.ElementTree as ET

tree = ET.parse('en_kjv.xml')
root = tree.getroot()

class Display(Screen):
    book = NumericProperty()
    chapter = NumericProperty()
    def previous_chapter(self):
        #self.root.manager.current = 'chapterselect'
        if self.chapter > 0:
            self.chapter -= 1
        else:
            return
        self.text_display.text = f'[size=30]{self.chapter+1}[/size] '
        for index, verse in enumerate(root[self.book][self.chapter]):
            self.text_display.text += (f'[sup]{index+1}[/sup]' + verse.text)
    def next_chapter(self):
        if self.chapter < (len(root[self.book])-1): #-1 to adjust for zero-based indexing
            self.chapter += 1
        else:
            return
        self.text_display.text = f'[size=30]{self.chapter+1}[/size] '
        for index, verse in enumerate(root[self.book][self.chapter]):
            self.text_display.text += (f'[sup]{index+1}[/sup]' + verse.text)
    def go_to_books(self):
        self.root.manager.current = 'books'