from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivy.config import Config

Config.set('graphics', 'width', '720')
Config.set('graphics', 'height', '1280')
Config.set('graphics', 'resizable', False)


KV = '''
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Screen 1"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "screen1"

            OneLineListItem:
                text: "Screen 2"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "screen2"

Screen:
    MDBottomAppBar:
        MDToolbar:
            id: toolbar
            icon: "youtube"
            type: "bottom"
            elevation: 10
            title: "AudioTube"
            right_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
            mode: 'free-center'
            md_bg_color: .5, .5, .2, 1
            on_action_button: [["menu", lambda x: nav_drawer.set_state("open")]]


    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                name: "screen1"
                id: "screen1"
                text: "Библиотека"

                MDLabel:
                    text: "Библиотека"
                    icon: "book"
                    halign: "center"

            Screen:
                name: "screen2"
                id: "screen2"
                text: "Конвертер аудио"


                MDLabel:
                    text: "Конверетер в аудио по ссылке"
                    halign:"center"
                    text_color: 0, 0, 1, 1

                MDTextFieldRound:
                    id: "first_field"
                    hint_text: 'Ваша cсылка'
                    color_mode: 'accent'
                    size_hint: .4, .05
                    pos_hint: {"center_x": .5, "center_y": .45}
                    height: "400dp"
                    helper_text_mode: "on_focus"
                    line_color_focus: (1,1,1,1)

                MDRectangleFlatButton:
                    text: "Скачать"
                    text_color: 0, 0, 1, 1
                    md_bg_color: 1, 1, 1, 1 
                    pos_hint: {'center_x': 0.5, "center_y": .3}
                    on_release: root.check_data_text()


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer


'''


class ContentNavigationDrawer (BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

    def check_data_text(self):
        text = self.scr_mngr.screen2.first_field.text

        print(text)

        if text == "https":
            self.change_screen("screen1")

    def change_screen(self, screen, *args):
        self.screen_manager.current = screen


class MyApp (MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "300"
        return Builder.load_string(KV)



MyApp().run()