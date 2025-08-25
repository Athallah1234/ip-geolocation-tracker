import tkinter as tk
from tkinter import ttk, scrolledtext
import geocoder
import folium
import webbrowser
import os

class GeolocationTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("IP Geolocation Tracker")

        self.create_widgets()
        self.history = []

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ip_label = ttk.Label(frame, text="Enter IP Address:")
        ip_label.grid(row=0, column=0, sticky=tk.W)

        self.ip_entry = ttk.Entry(frame, width=20)
        self.ip_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

        get_location_button = ttk.Button(frame, text="Get Geolocation", command=self.get_geolocation)
        get_location_button.grid(row=0, column=2, sticky=tk.W)

        clear_button = ttk.Button(frame, text="Clear", command=self.clear_entries)
        clear_button.grid(row=0, column=3, sticky=tk.W)

        copy_button = ttk.Button(frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.grid(row=0, column=4, sticky=tk.W)

        history_button = ttk.Button(frame, text="View History", command=self.view_history)
        history_button.grid(row=0, column=5, sticky=tk.W)

        result_label = ttk.Label(frame, text="")
        result_label.grid(row=1, column=0, columnspan=7, sticky=tk.W)
        self.result_label = result_label

    def get_geolocation(self):
        ip_address = self.ip_entry.get()
        try:
            location = geocoder.ip(ip_address)
            latitude, longitude = location.latlng

            altitude_info = f"Altitude: {location.altitude}\n" if hasattr(location, 'altitude') else ""
            address_info = f"Address: {location.address}\n" if hasattr(location, 'address') else ""
            province_info = f"Province: {location.province}\n" if hasattr(location, 'province') else ""
            district_info = f"District: {location.district}\n" if hasattr(location, 'district') else ""

            self.result_label.config(text=f"IP: {ip_address}\n"
                                          f"City: {location.city}\n"
                                          f"Region: {location.state}\n"
                                          f"Country: {location.country}\n"
                                          f"{province_info}"
                                          f"{district_info}"
                                          f"Lat/Long: {location.latlng}\n"
                                          f"{altitude_info}"
                                          f"{address_info}")

            # Show location on the map
            self.show_on_map(location.latlng)

            # Add to history
            self.history.append(f"IP: {ip_address}, City: {location.city}, Region: {location.state}, Country: {location.country}, Address: {location.address}")

        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")
            self.clear_map()

    def show_on_map(self, latlng):
        # Create a map centered around the given coordinates
        my_map = folium.Map(location=latlng, zoom_start=10)

        # Add a marker for the location
        folium.Marker(location=latlng, popup="IP Location").add_to(my_map)

        # Save the map to an HTML file
        my_map.save("map.html")

        # Open the map in the default web browser
        webbrowser.open("map.html")

    def copy_to_clipboard(self):
        geolocation_info = self.result_label.cget("text")
        self.root.clipboard_clear()
        self.root.clipboard_append(geolocation_info)
        self.root.update()

    def clear_map(self):
        # Delete the map file
        try:
            os.remove("map.html")
        except FileNotFoundError:
            pass

    def clear_entries(self):
        self.ip_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.clear_map()

    def view_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Search History")

        history_text = scrolledtext.ScrolledText(history_window, wrap=tk.WORD, width=40, height=10)
        history_text.pack(expand=True, fill=tk.BOTH)

        for entry in self.history:
            history_text.insert(tk.END, entry + "\n")
        history_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = GeolocationTracker(root)
    root.mainloop()
