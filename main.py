from kivymd.app import MDApp
from kivy.lang.builder import Builder
from autosupp import kv
from kivymd.uix.picker import MDThemePicker,MDTimePicker
import pywhatkit
from kivy.config import Config
from kivymd.toast import toast



Config.set('graphics','resizable', True)

class Automess(MDApp):
    def build(self):
        return Builder.load_string(kv)


    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def show_time_picker(self):

        time_dialog = MDTimePicker()
        #previous_time = datetime.strptime("00:00:00", '%H:%M:%S').time()
        #time_dialog = MDTimePicker()
        #time_dialog.set_time(previous_time)
        time_dialog.bind(time=self.get_time)
        time_dialog.open()


    def data(self):
        pass
    def get_time(self, instance,time):
        t = time
        t=str(t)
        h=t[:2]
        m=t[3:5]
        num = self.root.ids.number.text
        mess = self.root.ids.message.text
        nl=list(num)
        ml=list(mess)

        if nl==0 and ml==0:
            toast("Please Enter Both Phone Number and Message")
        else:
            pywhatkit.sendwhatmsg("+91"+num,
                                  mess,
                                  int(h),int(m))
            print("Successfully Sent!")




Automess().run()
