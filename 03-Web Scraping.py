#Web Scraping Images 
import requests
image_url = "enter your image url here"
output_filename = "photo.png"

response = requests.get(image_url)

if response.status_code == 200:
    with open(output_filename, "wb") as file:
        file.write(response.content)
    print(f"Image Download Successfully as {output_filename}")
else:
    print("Failed to download the image")        
