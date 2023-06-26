import tkinter as tk
import requests

API_KEY = 'YOUR_API_KEY_HERE'

class WeatherApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Weather App')

        self.location_entry = tk.Entry(self)
        self.location_entry.pack(pady=10)

        self.weather_label = tk.Label(self, font=('Arial', 18))
        self.weather_label.pack(pady=5)

        self.temperature_label = tk.Label(self, font=('Arial', 14))
        self.temperature_label.pack(pady=5)

        self.fetch_button = tk.Button(self, text='Get Weather', command=self.fetch_weather)
        self.fetch_button.pack(pady=10)

    def fetch_weather(self):
        location = self.location_entry.get()
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric'
        
        try:
            response = requests.get(url)
            data = response.json()

            if data['cod'] == 200:
                weather_description = data['weather'][0]['description']
                temperature = data['main']['temp']

                self.weather_label.config(text=f'Weather: {weather_description}')
                self.temperature_label.config(text=f'Temperature: {temperature}°C')
            else:
                self.weather_label.config(text='Error: Invalid location')
                self.temperature_label.config(text='')
        except requests.exceptions.RequestException:
            self.weather_label.config(text='Error: Connection error')
            self.temperature_label.config(text='')

# Run the app
if __name__ == '__main__':
    app = WeatherApp()
    app.mainloop()