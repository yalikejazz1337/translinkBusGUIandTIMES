import requests
import json
from tkinter import Tk, Button
from tkinter import *
from io import BytesIO
from PIL import Image, ImageTk
STATIC_API_KEY = '48cd7f54e35d4cf297df4e2e4cdfe9b6'

#before anything happens, get stop number  
# Create a window
stop = input("Enter the stop number: ")
stop = int(stop)

root = Tk()  # create root window
root.title("Basic GUI Layout")  # title of the GUI window
root.maxsize(1920, 1080)  # specify the max size the window can expand to
root.config(bg="skyblue")  # specify background color
#convert the stop to a int
headers = {'accept': 'application/JSON'}



def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=1)
    print(text)

longLat = requests.get('https://api.translink.ca/rttiapi/v1/stops/{}?apikey=cJvWqMTEO7u3cL3QZxvV' .format(stop),  headers=headers)
lat = longLat.json()['Latitude']
long = longLat.json()['Longitude']
#use the lat and long for image

img_url = 'https://maps.geoapify.com/v1/staticmap?style=osm-bright&width=600&height=400&center=lonlat:{},{}&zoom=15.9318&marker=lonlat:{},{};type:material;color:%23ff0000;size:medium;icon:bus-alt;icontype:awesome;strokecolor:%23000000;shadow:no&apiKey={}' .format(long, lat,long, lat, STATIC_API_KEY)


response = requests.get(img_url)
img_data = response.content

# Create left and right frames
left_frame = Frame(root, width=200, height=400, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)


# Create frames and labels in left_frame
Label(left_frame, text="BUS STOP").grid(row=0, column=0, padx=5, pady=5)

# load image to be "edited"
image = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
original_image = image  # resize image using subsample
Label(left_frame, image=original_image).grid(row=1, column=0, padx=5, pady=5)


# Create tool bar frame
tool_bar = Frame(left_frame, width=180, height=185)
tool_bar.grid(row=2, column=0, padx=5, pady=5)

# Example labels that serve as placeholders for other widgets
Label(tool_bar, text="NEXT BUS TIMES", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget

# Example labels that could be displayed under the "Tool" menu



# Get the stop information for the stop with the ID 55612

response = requests.get('https://api.translink.ca/rttiapi/v1/stops/{}/estimates?apikey=cJvWqMTEO7u3cL3QZxvV' .format(stop), headers=headers)
#print the next bus of the stop

#find index 0 of schedules and print the next available bus times, and append to a list
for i in range (0, len(response.json()[0]['Schedules'])):
    pass_times = response.json()[0]['Schedules'][i]['ExpectedLeaveTime']
    print(pass_times)
    Label(tool_bar, text=pass_times).grid(row=[i + 1], column=0, padx=5, pady=5)

#get lat and long of the stop


root.mainloop()