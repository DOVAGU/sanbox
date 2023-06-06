"""
Name:Meng Qingwei
Date:6/7
Brief Project Description:GUI panel for Travel Tracker
GitHub URL:https://github.com/JCUS-CP1404/cp1404---travel-tracker---assignment-2-DOVAGU
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty

from placecollection import PlaceCollection
from place import Place

class TravelTrackerApp(App):
    spinner = ObjectProperty()
    name_input = ObjectProperty()
    country_input = ObjectProperty()
    priority_input = ObjectProperty()
    status_label = StringProperty()
    places_container = ObjectProperty()

    def build(self):
        self.title = "Travel Tracker"
        self.place_collection = PlaceCollection()
        self.place_collection.load_places("places_backup.csv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        self.root = BoxLayout(orientation='horizontal')

        # Left side widgets
        left_side = BoxLayout(orientation='vertical', size_hint=(0.3, 1))

        # Spinner
        self.spinner = Spinner(text='Sort by', values=('name', 'country', 'priority'))
        self.spinner.bind(text=self.on_spinner_select)
        left_side.add_widget(self.spinner)

        # Text input fields
        input_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.name_input = TextInput(hint_text='Name')
        self.country_input = TextInput(hint_text='Country')
        self.priority_input = TextInput(hint_text='Priority')
        input_layout.add_widget(self.name_input)
        input_layout.add_widget(self.country_input)
        input_layout.add_widget(self.priority_input)

        # Add Place button
        add_place_button = Button(text='Add Place')
        add_place_button.bind(on_release=self.add_place)
        input_layout.add_widget(add_place_button)

        left_side.add_widget(input_layout)
        self.root.add_widget(left_side)

        # Right side widgets
        self.places_container = BoxLayout(orientation='vertical', size_hint=(0.7, 1))
        self.update_places_container()
        self.root.add_widget(self.places_container)

        return self.root

    def on_spinner_select(self, spinner, text):
        key = lambda place: getattr(place, text)
        self.place_collection.sort_places(key)
        self.update_places_container()

    def add_place(self, *args):
        name = self.name_input.text
        country = self.country_input.text
        priority = self.priority_input.text

        if not name or not country or not priority:
            self.status_label = "All fields must be completed"
        elif not priority.isdigit():
            self.status_label = "Please enter a valid number"
        elif int(priority) < 1:
            self.status_label = "Priority must be > 0"
        else:
            place = Place(name, country, int(priority))
            self.place_collection.add_place(place)
            self.clear_input_fields()
            self.update_places_container()

    def update_places_container(self):
        self.places_container.clear_widgets()
        for place in self.place_collection.places:
            button = Button(text=place.name, background_color=(0.5, 0.5, 0.5, 1))
            button.bind(on_release=self.toggle_visited)
            if place.visited:
                button.background_color = (0.2, 0.8, 0.2, 1)
            self.places_container.add_widget(button)

        self.status_label = f"{self.place_collection.get_number_of_unvisited_places()} places to visit"

    def toggle_visited(self, button):
        place_name = button.text
        place = next((place for place in self.place_collection.places if place.name == place_name), None)
        if place:
            self.place_collection.mark_place_visited(place)
            self.update_places_container()
            if place.is_visited:
                self.status_label = f"You visited {place.name}. Great travelling!"
            else:
                self.status_label = f"You need to visit {place.name}. Get going!"

    def clear_input_fields(self):
        self.name_input.text = ""
        self.country_input.text = ""
        self.priority_input.text = ""
        self.status_label = ""

    def on_stop(self):
        self.place_collection.save_places("places_backup.csv")

if __name__ == '__main__':
    TravelTrackerApp().run()

