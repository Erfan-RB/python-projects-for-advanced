#Download Manager
import requests
import os

def download_file(url, destination):
    response = requests.get(url)
    with open(destination,'web') as file:
        file.write(response.content)

url = "your address" 
destination = "downloaded_file.zip"
download_file(url, destination)       
