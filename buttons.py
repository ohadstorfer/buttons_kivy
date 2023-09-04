from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class ColorChangingButtonApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Create a blue button
        blue_button = Button(text='Blue Button', background_color=(0, 0, 0, 1))
        blue_button.bind(on_press=lambda instance: self.change_color(instance, (0, 0, 1, 1)))
        layout.add_widget(blue_button)

        # Create a red button
        red_button = Button(text='Red Button', background_color=(0, 0, 0, 1))
        red_button.bind(on_press=lambda instance: self.change_color(instance, (1, 0, 0, 1)))
        layout.add_widget(red_button)

        # Create a green button
        green_button = Button(text='Green Button', background_color=(0, 0, 0, 1))
        green_button.bind(on_press=lambda instance: self.change_color(instance, (0, 1, 0, 1)))
        layout.add_widget(green_button)

        return layout

    def change_color(self, instance, color):
        # Change the background color of the clicked button to the specified color
        instance.background_color = color

if __name__ == '__main__':
    ColorChangingButtonApp().run()
