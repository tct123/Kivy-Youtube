from kivy.config import Config

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)

from kivymd.app import MDApp

from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty  # <--- Object Property

screen_helper = """
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Аудио"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "menu"

            OneLineListItem:
                right_icon: 'folder'
                text: "Библиотека"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "profile"
                    
Screen:
    MDToolbar:
        id: toolbar
        pos_hint: {"bottom": 1}
        elevation: 10
        title: "AudioTube"
        right_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        
    NavigationLayout:
        x: toolbar.height
    MainScreenManager: # <--- changes here
        id: screen_manager
        label_: label_welcome
        input_name: input_name
    
    
        MenuScreen:
            name: 'menu'
            
            MDLabel: 
                text: "Конверетер в аудио по ссылке"
                pos_hint:{'center_x':0.5,'center_y':0.6}
                halign: "center"
                text_color: 0, 0, 1, 1
            
            MDTextFieldRound:
                id: input_name
                hint_text: 'Ваша ссылка'
                pos_hint:{'center_x':0.5,'center_y':0.5}
                color_mode:'custom'
                line_color_focus: 0.43, 0.82, 0.83, 0.6
                size_hint: .4, .05
    
            MDRectangleFlatButton:
                text: 'Скачать'
                pos_hint: {'center_x':0.5,'center_y':0.3}
                on_press: 
                    root.ButtonFunction()
        ProfileScreen:
            name: 'profile'
            MDLabel:
                id: label_welcome
                text: "Hello,"
                halign: 'center'
            MDRectangleFlatButton:
                text: 'Назад'
                pos_hint: {'center_x':0.5,'center_y':0.1}
                on_press: root.current = 'menu'
        
    MDNavigationDrawer:
        id: nav_drawer

        ContentNavigationDrawer:
            screen_manager: screen_manager
            nav_drawer: nav_drawer

"""
class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty ( )
    nav_drawer = ObjectProperty ( )


class MainScreenManager (ScreenManager):  # This gonna be the root widget
    label_ = ObjectProperty(None)
    input_name = ObjectProperty(None)

    def ButtonFunction(self):
        self.current = 'profile'
        print(self.input_name.text)
        self.label_.text = 'Скачано'


class MenuScreen (Screen):
    pass


class ProfileScreen (Screen):
    pass


# Create the screen manager
sm = MainScreenManager()
sm.add_widget(MenuScreen(name='menu'))

sm.add_widget(ProfileScreen(name='profile'))


class DemoApp (MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "300"
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()