import sys
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
from datetime import datetime
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader



class DigitalClockApp(App):
    def build(self):
        # Set the window icon (replace with the actual path to your icon)
        Window.set_icon('clock.png')  # This is the window icon

        # Set the background color to black
        Window.clearcolor = (0.0, 0.0, 0.0, 1)  # Black background

        self.box = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Create the profile icon (replace with your actual image path)
        self.profile_icon = Image(source='clock.png', size_hint=(None, None), size=(100, 100))
        self.profile_icon.pos_hint = {'center_x': 0.5}  # Position icon in the center
        self.box.add_widget(self.profile_icon)

        # Create the time label with the desired font size, color, bold style, and custom font
        self.time_label = Label(
            font_size='120sp',  # Adjusted size to fit on screen
            color=(0.0, 1.0, 0.0, 1),  # Greenish color for time
            halign='center',
            bold=True,
            font_name='DS-DIGII.TTF'  # Custom font
        )

        # Create the date label with white color and initially hidden
        self.date_label = Label(
            font_size='30sp',  # Slightly smaller size for the date
            color=(1, 1, 1, 1),  # White color for date
            halign='center',
            opacity=0,  # Initially hidden
            font_name='Arial'  # Custom font for date as well
        )

        # Add the time and date labels to the layout
        self.box.add_widget(self.time_label)
        self.box.add_widget(self.date_label)

        # Add the toggle button to show/hide the date
        self.toggle_button = Button(
            text='Show Date',
            font_size='20sp',
            size_hint=(None, None),
            size=(200, 50),
            background_normal='',
            background_color=(1, 0, 0, 1)  # Red background for button
        )
        self.toggle_button.bind(on_press=self.toggle_date_visibility)
        self.box.add_widget(self.toggle_button)

        # Track the date visibility status
        self.date_visible = False

        # Schedule the clock update every second
        Clock.schedule_interval(self.update_time, 1)

        # Create a solid black background for the whole window
        with self.box.canvas.before:
            self.bg_color = Color(0.0, 0.0, 0.0, 1)  # Black background
            self.bg_rect = Rectangle(size=Window.size, pos=(0, 0))

        # Load the sound (replace with your sound file path)
        self.clock_sound = SoundLoader.load('ticking-clock_1-27477.wav')

        return self.box

    def update_time(self, dt=None):
        # Update the time every second
        current_time = datetime.now().strftime("%I:%M:%S %p")
        self.time_label.text = current_time

        # Update the date
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        self.date_label.text = current_date

        # Play the sound
        if self.clock_sound:
            self.clock_sound.play()

    def toggle_date_visibility(self, instance):
        # Toggle the visibility of the date label
        if self.date_visible:
            self.date_label.opacity = 0
            self.toggle_button.text = 'Show Date'
            self.date_visible = False
        else:
            self.date_label.opacity = 1
            self.toggle_button.text = 'Hide Date'
            self.date_visible = True

    def on_resize(self, instance, value):
        # Update the background size on window resize
        self.bg_rect.size = Window.size


if __name__ == '__main__':
    DigitalClockApp().run()
