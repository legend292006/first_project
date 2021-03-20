import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MYgird(GridLayout):
    def __init__(self,**kwargs):
        super(MYgird,self).__init__(**kwargs)

        

        self.cols = 2
        self.add_widget(Label(text="name "))

        self.name= TextInput(multiline=False)
        self.add_widget(self.name)
        
        self.add_widget(Label(text="roll number "))

        self.rol= TextInput(multiline=False)
        self.add_widget(self.rol)


        self.sub=Button(text="submit",font_size=32)
        self.sub.bind(on_press=self.pre)
        self.add_widget(self.sub)

    def pre(self,instance):
        name=self.name.text
        rol=self.rol.text
        # print(f'my name is {name} my roll number is {rol}')
        self.add_widget(Label(text=f'my name is {name} my roll number is {rol}'))
        self.rol.text=""
        self.name.text=""

class myapp(App):
    def build(self):
        return MYgird()


# if __name__=='_main_':
#     myapp().run()


myapp().run()


