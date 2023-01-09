import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import datetime

class TimeTrackingApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_time = None
        self.end_time = None
        self.break_time = None

    def update_total_hours(self):
        if self.start_time and self.end_time:
            total_time = self.end_time - self.start_time
            break_time = total_time - self.break_time
            total_hours = break_time.total_seconds() / 3600
            self.total_hours_label.text = "Total hours: {:.2f}".format(total_hours)

    def start_time_entered(self, instance, value):
        try:
            # Parse the time and minutes as integers
            hours, minutes = map(int, value.split(":"))
            # Create a datetime object using the current date and the entered time
            self.start_time = datetime.datetime.now().replace(hour=hours, minute=minutes)
            self.update_total_hours()
        except (ValueError, TypeError):
            self.total_hours_label.text = "Invalid start time"

    def end_time_entered(self, instance, value):
        try:
            # Parse the time and minutes as integers
            hours, minutes = map(int, value.split(":"))
            # Create a datetime object using the current date and the entered time
            self.end_time = datetime.datetime.now().replace(hour=hours, minute=minutes)
            self.update_total_hours()
        except (ValueError, TypeError):
            self.total_hours_label.text = "Invalid end time"

    def break_time_entered(self, instance, value):
        try:
            # Parse the time and minutes as integers
            hours, minutes = map(int, value.split(":"))
            # Create a timedelta object using the entered time
            self.break_time = datetime.timedelta(hours=hours, minutes=minutes)
            self.update_total_hours()
        except (ValueError, TypeError):
            self.total_hours_label.text = "Invalid break time"

    def build(self):
        layout = BoxLayout(orientation="vertical")

        start_time_input = TextInput(text="05:30")
        start_time_input.bind(text=self.start_time_entered)
        layout.add_widget(start_time_input)

        end_time_input = TextInput(text="14:15")
        end_time_input.bind(text=self.end_time_entered)
        layout.add_widget(end_time_input)

        break_time_input = TextInput(text="01:00")
        break_time_input.bind(text=self.break_time_entered)
        layout.add_widget(break_time_input)

        self.total_hours_label = Label(text="Total hours: 0.00")
        layout.add_widget(self.total_hours_label)

        # start - end = breaktime = total



        return layout

if __name__ == "__main__":
    TimeTrackingApp().run()