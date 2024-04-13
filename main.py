import sqlite3
import hashlib
import time
from datetime import datetime

import os
import json

from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.label import MDLabel
from kivymd.uix.imagelist import MDSmartTile
from kivymd.uix.button import MDIconButton, MDRectangleFlatIconButton, MDFillRoundFlatIconButton, MDRaisedButton,MDRoundFlatIconButton
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.card import MDCard
from kivy.uix.label import Label
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.fitimage import FitImage
from kivy.uix.textinput import TextInput
from kivymd.uix.scrollview import ScrollView
from kivy.uix.video import Video
from kivy.animation import Animation
from kivy.clock import Clock, mainthread
from kivy.uix.modalview import ModalView
from kivymd.uix.list import MDList, OneLineListItem, IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox

import server

Window.size = (1080 / 3, 1920 / 3)

class ContentNavigationDrawer(MDBoxLayout):
    pass


class MDSmartTileArticle(ButtonBehavior, MDSmartTile):
    article_id = NumericProperty(0)


class TwoLineListItemArticle(TwoLineListItem):
    pass
                
class file_manager():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path, preview=True, icon_folder="images/folder.png",
            ext=['.png', '.jpg'])

class EdaApp(MDApp):
    dialog = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path, preview=True, icon_folder="images/folder.png",
            ext=['.png', '.jpg'])
        self.Mori = []
    def file_manager_open(self):
        self.file_manager.show(os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True
    
    def select_path(self, path: str):
        self.exit_manager()
        toast(path)
        self.path = path

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()
    
    
    
    account = {
        "username": None,
        "password": None,
        'email': None
    }
    screens = ['main']

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Light"
        self.title = "RecipeHub"
        self.icon = "images/green_logo.png"
        return Builder.load_file("style.kv")

    def on_start(self):
        if self.user_init() == 0:
            self.screen('start')
            self.on_open_start_screen()
    
    # Инициализации
    # region Inits

    def user_init(self):
        data = None
        with open('data.json') as json_file:
            data = json.load(json_file)
        print(data)
        if data['username'] == 'None':
            print('None')
            return 0
        else:
            self.account = data
            return 1

    # endregion

    # Стартовый экран
    # region start_screen
    def on_open_start_screen(self):

        anim1 = Animation(
            pos_hint={'center_x': 0.5},
            color=(1, 1, 1, 1),
            duration=1,
            t='in_out_quad',
            s=0
        )
        anim2 = (Animation(duration=0.25) +
                 Animation(
                     pos_hint={'center_x': 0.5},
                     text_color=(1, 1, 1, 1),
                     line_color=(1, 1, 1, 1),
                     duration=1,
                     t='in_out_quad',
                     s=0
                 ))
        anim3 = (Animation(duration=0.4) +
                 Animation(
                     pos_hint={'center_x': 0.5},
                     text_color=(1, 1, 1, 1),
                     line_color=(1, 1, 1, 1),
                     duration=1,
                     t='in_out_quad',
                     s=0
                 ))
        anim1.start(self.root.ids.start_screen_label)
        anim2.start(self.root.ids.start_screen_log_in_btn)
        anim3.start(self.root.ids.start_screen_sign_up_btn)

    def to_log_in(self):
        anim = Animation(
            pos_hint={'center_x': -1},
            duration=1,
            t='in_out_quad',
            s=0
        )
        anim.start(self.root.ids.start_screen_label)
        anim = Animation(duration=0.1) + Animation(
            pos_hint={'center_x': -1},
            duration=1,
            t='in_out_quad',
            s=0
        )
        anim.start(self.root.ids.start_screen_log_in_btn)
        anim = Animation(duration=0.2) + Animation(
            pos_hint={'center_x': -1},
            duration=1,
            t='in_out_quad',
            s=0
        )
        anim.start(self.root.ids.start_screen_sign_up_btn)
        anim = Animation(
            pos_hint={'center_x': 2},
            duration=1,
            t='in_out_quad',
            s=0
        )
        anim.start(self.root.ids.sign_up_card)

        lic = self.root.ids.log_in_card
        lic.pos_hint = {'center_x': 1.5, 'center_y': 0.5}
        anim = Animation(
            pos_hint={'center_x': 0.5},
            duration=1,
            t='in_out_quad',
            s=0
        )
        anim.start(lic)

    def to_sign_up(self):
        anim = Animation(
            pos_hint={'center_x': -1},
            duration=1,
            t='in_out_quad',
            s=0
        )
        anim.start(self.root.ids.start_screen_label)
        anim = Animation(duration=0.1) + Animation(
            pos_hint={'center_x': -1},
            duration=1,
            t='in_out_quad',
            s=0
        )
        anim.start(self.root.ids.start_screen_log_in_btn)
        anim = Animation(duration=0.2) + Animation(
            pos_hint={'center_x': -1},
            duration=1,
            t='in_out_quad',
            s=0
        )
        anim.start(self.root.ids.start_screen_sign_up_btn)
        anim = Animation(
            pos_hint={'center_x': 2},
            duration=1,
            t='in_out_quad',
            s=0
        )
        anim.start(self.root.ids.log_in_card)

        suc = self.root.ids.sign_up_card
        suc.pos_hint = {'center_x': 1.5, 'center_y': 0.5}
        anim = Animation(
            pos_hint={'center_x': 0.5},
            duration=1,
            t='in_out_quad',
            s=0
        )
        anim.start(suc)

    # endregion

    # Функции экрана
    # region screens_functions
    def screen(self, current_screen):
        if current_screen not in ['login', 'signup']:
            self.screens.append(self.root.ids.screen_manager.current)

        if current_screen in ['account', 'friends', 'my_recipes', 'create_new'] and self.account['username'] is None:
            self.screens.append(current_screen)
            self.root.ids.screen_manager.current = 'login'
        elif current_screen == 'start':
            self.on_open_start_screen()
        else:
            self.root.ids.screen_manager.current = current_screen
        self.close_nav()

    def screen_back(self):
        self.root.ids.screen_manager.current = self.screens[len(self.screens) - 1]
        self.screens.pop(len(self.screens) - 1)

    def close_nav(self):
        self.root.ids.nav_drawer.set_state("close")

    # endregion

    # Чтение рецептов
    # region reading_recipes
    def read_box_r(self, name):
        with open(f"resips/{name}.json", "r") as f:
            ds = json.load(f)
        self.root.ids.getto_r.text = ds["Ingridient"]
        self.root.ids.name_resipe_r.text = ds["Name"]
        self.root.ids.kr_op_r.text = ds["kr_op"]
        self.root.ids.tyryry_r.text = ds["cooking"]
        self.screen("reading_r")
    # endregion

    # Аккаунт
    # region account
    # Вход в аккаунт
    def log_in(self, username, password):
        request = server.log_in(username, password)
        print(request)
        if request == 'Successful':
            self.account["username"] = username
            self.account["password"] = password
            self.root.ids.account_username.text = '@' + username
            self.screen('account')
            toast('Успешный вход')
        elif request == 'Invalid password':
            toast('Неверный пароль')
        elif request == 'The user does not exist':
            toast('Неверный логин')

    # Регистрация в аккаунт
    def sign_up(self, username, password, email):
        request = server.sign_up(username, password, email)
        if request == 'Successful':
            self.log_in(username, password)
            toast('Успешная регистрация')
        elif request == 'Username is occupied':
            toast('Имя пользователя занято')

    # endregion

    # Редактор рецептов
    # region recipes_editor
    def widget_creat(self, icon, name):
        smart = MDSmartTile(radius=24,
            box_radius=[0, 0, 24, 24],
            box_color=(1, 1, 1, .2),
            source=icon,
            pos_hint={"center_x": .5, "center_y": .5},
            size_hint=(None, None),
            size=("120dp", "120dp"),)
        smart.add_widget(MDLabel(bold=True, color=(1,1,1,1), text=name))
        smart.bind(on_press=(lambda x: self.read_box_r(name)))
        self.root.ids.fydra.add_widget(smart)

    def saver(self):
        ing = self.root.ids.getto.text
        name = self.root.ids.name_resipe.text
        kr_op = self.root.ids.kr_op.text
        tyry = self.root.ids.tyryry.text
        
        try:
            slovar = {"Name": name, "Ingridient": ing, "kr_op": kr_op, "cooking": tyry, "path_icon": self.path}

            with open(f"resips/{name}.json", "w") as f:
                f.write(json.dumps(slovar))

            self.widget_creat(self.path, name)
        except:
            toast("Ошибка изображение")
    def colora_metall(self, x):
        print(x.md_bg_color)
        if x.md_bg_color != [1,0,0,1]:
            x.md_bg_color = (1,0,0,1)
            self.Mori.append(x.text)
            print(self.Mori) 
        else:
            x.md_bg_color = "orange"
            i = str(x.text)
            if i in self.Mori:
                self.Mori.remove(i)
    
    def ingridient(self):
        pingvi = ",".join(self.Mori)
        self.root.ids.getto.text = pingvi
    def open_list_product(self):
        with open("List_ingridient.txt", "r", encoding="utf-8") as f:
            i_list = f.read()
        self.i_list = i_list.split(" ")

    def editor_add_widget(self, widget, *args):
        if widget == 'Label':
            self.root.ids.editor_widgets_card.add_widget(
                TextInput()
            )
    
    
    # endregion

    # ЭТА ФУНКЦИЯ НУЖНА ДЛЯ РАБОТЫ РЕГИОНОВ И ВСЕГДА ДОЛЖНА БЫТЬ САМОЙ ПОСЛЕДНЕЙ В КЛАССЕ
    def end_function(self):
        pass

if __name__ == '__main__':
    EdaApp().run()
