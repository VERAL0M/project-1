from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivymd.uix.swiper import MDSwiperItem,MDSwiper
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.scrollview import ScrollView
from Kivy_AI import res
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
import os
from kivymd.uix.fitimage import FitImage
from kivymd.uix.relativelayout import RelativeLayout
from datetime import datetime
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from database import Database
from data_tg import *
db = Database()

Window.size = (360, 640)
r =None
number=None


KV = '''
<ListItemWithCheckbox>:
    id: the_list_item
    markup: True

    LeftCheckbox:
        id: check
        on_release: 
            root.mark(check, the_list_item)

    IconRightWidget:
        icon: 'trash-can-outline'
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        on_release:
            root.delete_item(the_list_item)
<DialogContent>:
    orientation: "vertical"
    spacing: "10dp"
    size_hint: 1, None
    height: "130dp"

    GridLayout:
        rows: 1

        MDTextField:
            id: task_text
            hint_text: "Add Task..."
            pos_hint: {"center_y": .4}
            max_text_length: 50
            on_text_validate: (app.add_task(task_text, date_text.text), app.close_dialog())

        MDIconButton:
            icon: 'calendar'
            on_release: root.show_date_picker()
            padding: '10dp'
    MDLabel:
        spacing: '10dp'
        id: date_text

    BoxLayout:
        orientation: 'horizontal'

        MDRaisedButton:
            text: "SAVE"
            on_release: (app.add_task(task_text, date_text.text), app.close_dialog())
        MDFlatButton:
            text: 'CANCEL'
            on_release: app.close_dialog()


<Q1> 
    FitImage:
        source: root.img
        radius: [20,]
    MDBoxLayout:
        adaptive_height: True
        spacing: "12dp"

        MagicButton:
            id: icon
            icon: "download"
            user_font_size: "56sp"
            opposite_colors: True
            adaptive_size: True
            on_press: app.file_manager_open('one')
<Q2> 
    FitImage:
        source: root.img
        radius: [20,]
    MDBoxLayout:
        adaptive_height: True
        spacing: "12dp"

        MagicButton:
            id: icon
            icon: "download"
            user_font_size: "56sp"
            opposite_colors: True
            adaptive_size: True
            on_press: app.file_manager_open('two')


<Q3> 
    FitImage:
        source: root.img
        radius: [20,]
    MDBoxLayout:
        adaptive_height: True
        spacing: "12dp"

        MagicButton:
            id: icon
            icon: "download"
            user_font_size: "56sp"
            opposite_colors: True
            adaptive_size: True
            on_press: app.file_manager_open('three')               
   
<TodoCard>
    id: qw
    padding:20,50, 30, 170

    ScrollView
        MDLabel:
            canvas.before:
                Color:
                    rgba:(0,0,0,1)
                RoundedRectangle:
                    radius:[26]
                    pos:self.pos
                    size:self.size

            id: description
            text: root.title
            markup: True
            font_size: '18sp'
            text_size: self.width, None
            size_hint_x: 1
            line_height: .8
            pos_hint:{"center_x": .5}
            size_hint_y: None
            height: self.texture_size[1]
            halign: "center"
            padding:50,50


<MagicButton@MagicBehavior+MDIconButton>

<MySwiper@MDSwiperItem>
    RelativeLayout:

                
<DrawerClickableItem@MDNavigationDrawerItem>

    text_color: "ffffff"
    icon_color: "ffffff"
    ripple_color: "ffffff"
    selected_color: "ffffff"

                
Screen:

    # MDTopAppBar:
    #     id: toolbar
    #     pos_hint: {"top": 1}
    #     elevation: 0
    #     md_bg_color: "000000"
    #     specific_text_color: "ffffff"
    #     title: ""
    #     # left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDBottomNavigation:
        


        MDBottomNavigationItem:
            id:botto
            name: 'screen 1'
            text: 'Образование'
            icon: 'school-outline'
            MDSwiper:
                id: box
                size_hint_y: .75
                height: root.height - dp(115)
                y: root.height - self.height - dp(168)
                MySwiper:
                    id: my_swiper_one
                MySwiper:
                    id: my_swiper_two
                MySwiper:
                    id: my_swiper_three

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'ИИ'
            icon: 'robot-excited-outline'
            MDFloatLayout:
                id: ai
                MDTextField:
                    id: data
                    multiline: True
                    mode: "fill"
                    radius: [26]
                    line_color_focus:1, 1,1,1
                    active_line: False
                    hint_text: "Спросите о чём-нибудь"
                    size_hint_x: .88
                    size_hint_y: .85
                    pos_hint:{"center_x": .5,"center_y": .14 }
                    max_height: "140dp"
                    cursor_color:1, 170/255, 23/255, 1
                    cursor_width: "2sp"
                    foreground_color: 1, 170/255, 23/255, 1
                    padding: 15
                    font_size:"18sp"
                MDIconButton:
                    icon: "send"
                    pos_hint: {"center_x": .86, "center_y": .07}
                    on_press: app.get_data()
            MDFloatLayout:
                id: answer

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Дневник'
            icon: 'check-bold'

            MDFloatLayout:
                MDLabel:
                    id: task_label
                    halign: 'center'
                    markup: True
                    text: "[size=48][b]Task Manager[/b][/size]"
                    pos_hint: {'y': .45}

                ScrollView:
                    pos_hint: {'center_y': .5, 'center_x': .5}
                    size_hint: .9, .8

                    MDList:
                        id: container


                MDFloatingActionButton:
                    icon: 'plus-thick'
                    on_release: app.show_task_dialog()
                    elevation_normal: 12
                    pos_hint: {'center_x': .5 , 'y': .04}



        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'Ещё'
            icon: 'dots-horizontal'

            MDLabel:
                text: 'Скоро'
                halign: 'center'

    MDNavigationLayout:
        # x: toolbar.height
    

        ScreenManager:
            id: screen_manager
            

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 18, 18, 0)

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''

colors = {
    "Teal": {
        "200": "000000",
        "500": "000000",
        "700": "000000",
    },
    "Red": {
        "200": "#C25554",
        "500": "#C25554",
        "700": "#C25554",
    },
    "Light": {
        "StatusBar": "000000",
        "AppBar": "000000",
        "Background": "000000",
        "CardsDialogs": "000000",
        "FlatButtonDown": "000000",
    },
}


class DialogContent(MDBoxLayout):
    """OPENS A DIALOG BOX THAT GETS THE TASK FROM THE USER"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = str(datetime.now().strftime('%A %d %B %Y'))
    def show_date_picker(self):

        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        date = value.strftime('%A %d %B %Y')
        self.ids.date_text.text = str(date)

class Z(MDFloatLayout):
    pass
class Q1(RelativeLayout):
    img =StringProperty()
class Q2(RelativeLayout):
    img =StringProperty()
class Q3(RelativeLayout):
    img =StringProperty()

class TodoCard(BoxLayout):
    title = StringProperty()
    
class MySwiper(MDSwiperItem):
    pass

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    '''Custom list item'''

    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        # state a pk which we shall use link the list items with the database primary keys
        self.pk = pk

    def mark(self, check, the_list_item):
        '''mark the task as complete or incomplete'''
        if check.active == True:
            the_list_item.text = '[s]'+the_list_item.text+'[/s]'
            db.mark_task_as_complete(the_list_item.pk)# here
        else:

            the_list_item.text = str(db.mark_task_as_incomplete(the_list_item.pk))# Here

    def delete_item(self, the_list_item):
        '''Delete the task'''
        self.parent.remove_widget(the_list_item)
        db.delete_task(the_list_item.pk)# Here



class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    pass
    '''Custom left container'''


class TestNavigationDrawer(MDApp):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path
        )
    task_list_dialog = None
    def build(self):

        # self.theme_cls.colors = colors
        # self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)
    def show_task_dialog(self):
        if not self.task_list_dialog:
            self.task_list_dialog = MDDialog(
                title="Create Task",
                type="custom",
                content_cls=DialogContent(),
            )

        self.task_list_dialog.open()
    def add_task(self, task, task_date):
        '''Add task to the list of tasks'''
        # print(task.text, task_date)
        created_task = db.create_task(task.text, task_date)
        self.root.ids['container'].add_widget(ListItemWithCheckbox(pk=created_task[0], text='[b]'+created_task[1]+'[/b]', secondary_text=created_task[2]))
        task.text = ''
    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()
    def on_start(self):

        self.root.ids.my_swiper_one.clear_widgets()
        self.root.ids.my_swiper_one.add_widget(Q1(img='1.jpg'))
        
        self.root.ids.my_swiper_two.clear_widgets()
        self.root.ids.my_swiper_two.add_widget(Q2(img='2.jpg'))

        self.root.ids.my_swiper_three.clear_widgets()
        self.root.ids.my_swiper_three.add_widget(Q3(img='3.jpg'))

        try:
            completed_tasks, incompleted_tasks = db.get_tasks()

            if incompleted_tasks != []:
                for task in incompleted_tasks:
                    add_task = ListItemWithCheckbox(pk=task[0],text=task[1], secondary_text=task[2])
                    self.root.ids.container.add_widget(add_task)

            if completed_tasks != []:
                for task in completed_tasks:
                    add_task = ListItemWithCheckbox(pk=task[0],text='[s]'+task[1]+'[/s]', secondary_text=task[2])
                    add_task.ids.check.active = True
                    self.root.ids.container.add_widget(add_task)
        except Exception as e:
            print(e)
            pass
        
    def get_data(self):

        self.root.ids.answer.clear_widgets()
        answer_text =str(res(self.root.ids.data.text))
        self.root.ids.answer.add_widget(TodoCard(title=answer_text))
        # print(answer_text)
        
    def file_manager_open(self, numbers):

        global number
        self.file_manager.show(os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True
        number = numbers

    def select_path(self, path: str):

        self.exit_manager()
        if number == 'one':
            self.root.ids.my_swiper_one.clear_widgets()
            self.root.ids.my_swiper_one.add_widget(Q1(img=path))
        elif number =='two':
            self.root.ids.my_swiper_two.clear_widgets()
            self.root.ids.my_swiper_two.add_widget(Q2(img=path))
        elif number =='three':
            self.root.ids.my_swiper_three.clear_widgets()
            self.root.ids.my_swiper_three.add_widget(Q3(img=path))

    def exit_manager(self, *args):

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    

TestNavigationDrawer().run()