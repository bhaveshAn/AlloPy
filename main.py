import kivy
kivy.require('1.8.0')
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.label import Label 
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition


class FirstScreen(Screen):
	#l=Label(text="Hello Allo")


	pass

class CountryOption(Screen):
	pass

class ScreenManagement(ScreenManager):
	pass

present=Builder.load_file("allopy.kv")


class AlloPyApp(App):
	def build(self):
		return present

if __name__ == '__main__':
	AlloPyApp().run()