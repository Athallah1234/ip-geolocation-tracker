# 🌍 IP Geolocation Tracker (with Weather Info)

A simple **IP Geolocation Tracker** built with **Python** and **Tkinter**.  
This application allows you to:

- Get **location details** (city, region, country, latitude, longitude) from an IP address
- Display the location on an **interactive map** using Folium
- Fetch **current weather information** from [OpenWeatherMap API](https://openweathermap.org/api)  
- Copy results to clipboard
- Save and view **search history**

--- 

## 🚀 Features

✅ Track IP geolocation (City, Region, Country, Coordinates)  
✅ Show location on an interactive **map (HTML)**  
✅ Fetch real-time **weather info** (temperature, description)  
✅ **Clipboard support** (copy results)  
✅ **Search history** stored within the session  
✅ Clean and simple **Tkinter GUI**  

--- 

## 🛠 Requirements

- Python 3.8 or later  
- Install dependencies from `requirements.txt`
```bash
pip install -r requirements.txt
```

---

## 📦 Installation & Usage

1. Clone this repository:
```bash
git clone https://github.com/username/ip-geolocation-tracker.git
cd ip-geolocation-tracker
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the program:
```bash
python run.py
```

---

## 📂 Project Structure
```python
📁 ip-geolocation-tracker
│── run.py              # Main program
│── requirements.txt    # Dependencies
│── README.md           # Documentation
│── map.html            # Auto-generated map (runtime)
```