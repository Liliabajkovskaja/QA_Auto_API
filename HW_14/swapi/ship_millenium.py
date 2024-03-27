import json
import requests
import os



class MillenniumFalcon:
    BASE_URL = "https://swapi.dev/api/starships/"
    STARSHIP_NAME = "Millennium Falcon"


    def __init__(self):
        self.current_directory = os.path.dirname(os.path.abspath(__file__))

    def get_starship_data(self, url):
        response = requests.get(url)
        data = response.json()
        return data

    def get_planet_data(self, url):
        response = requests.get(url)
        data = response.json()
        return data

    def get_pilot_data(self, url):
        response = requests.get(url)
        data = response.json()
        homeworld_url = data['homeworld']
        homeworld_data = self.get_planet_data(homeworld_url)
        homeworld_info = {
            'name': homeworld_data['name'],
            'url': homeworld_url
        }
        return {
            'name': data['name'],
            'height': data['height'],
            'mass': data['mass'],
            'homeworld': homeworld_info
        }

    def get_needed_starship(self, starship_data):
        millennium_falcon_url = None
        for ship in starship_data['results']:
            if ship["name"] == self.STARSHIP_NAME:
                millennium_falcon_url = ship["url"]
                break
        millennium_falcon_data = self.get_starship_data(millennium_falcon_url)
        return millennium_falcon_data

    def save_to_json(self, data, file_name):
        file_path = os.path.join(self.current_directory, file_name)
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)


    def execute(self):
        ships_data = self.get_starship_data(self.BASE_URL)
        millennium_falcon_data = self.get_needed_starship(ships_data)

        pilots_data = []
        for pilot_url in millennium_falcon_data['pilots']:
            pilot_data = self.get_pilot_data(pilot_url)
            pilots_data.append(pilot_data)

        data_to_save = {
            'name': millennium_falcon_data['name'],
            'max_atmosphering_speed': millennium_falcon_data['max_atmosphering_speed'],
            'starship_class': millennium_falcon_data['starship_class'],
            'pilots': pilots_data
        }
        self.save_to_json(data_to_save, 'millennium_falcon.json')
        print("Data successfully saved to file 'millennium_falcon.json'")




if __name__ == "__main__":
    data_retriever = MillenniumFalcon()
    data_retriever.execute()
