import requests
import tkinter as tk

url = "http://api.bitcoincharts.com/v1/markets.json"

response = requests.request("GET", url)

window = tk.Tk()
greeting = tk.Message(text=response.text)
greeting.pack()
window.mainloop()