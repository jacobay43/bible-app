from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
import xml.etree.ElementTree as ET

tree = ET.parse('en_kjv.xml')
root = tree.getroot()

class ChapterSelect(Screen):
    body_of_text = StringProperty()
    def search(self,b,c):
        self.body_of_text = ''
        try:
            b = int(b)
            c = int(c) - 1 #adjusted for zero-based indexing
            #v = int(v) - 1
            #body_of_text = root[b][c][v].text
            #print(root[b][c][v].text)
            """
            for t in root[b][c:]: #get content from that current chapter to the end of the book
                for index, verse in enumerate(t): #where index is verse number
                    self.body_of_text += (f'[sup]{index+1}[/sup]' + verse.text)
            """
            self.body_of_text = f'[size=30]{c+1}[/size] '
            for index, verse in enumerate(root[b][c]):
                self.body_of_text += (f'[sup]{index+1}[/sup]' + verse.text)
            #print(self.body_of_text)
            self.root.manager.screens[2].book = b
            self.root.manager.screens[2].chapter = c
            self.root.manager.screens[2].text_display.text = self.body_of_text #N.B:Too much text in a label leaves the entire label displaying all black
            self.root.manager.current = 'display'
            #print(self.root.manager.screens[2].text_display.text)
        except:
            print('Invalid chapter')
    def back(self):
        self.root.manager.current = 'books'