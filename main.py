# https://cloud.google.com/text-to-speech/docs/basics

import requests
import base64
# import json
# from google.auth import default
# from google.auth.transport.requests import Request

# credentials, project_id = default()
# credentials.refresh(Request())
# access_token = credentials.token

# Define API endpoint
# url = "https://texttospeech.googleapis.com/v1/text:synthesize"

# Request payload
# data = {
#     "input": {
#         'ssml':'<speak>The <say-as interpret-as=\"characters\">SSML</say-as> standard\
#           is defined by the <sub alias=\"World Wide Web Consortium\">W3C</sub>.</speak>'
#     },
#     'voice':{
#       'languageCode':'en-us',
#       'name':'en-US-Standard-B',
#       'ssmlGender':'MALE'
#     },
#     "audioConfig": {
#         "audioEncoding": "MP3"
#     }
# }

# Headers with access token and project ID

# Make the POST request
# response = requests.post(url, headers=headers, data=json.dumps(data))

# Check the response
# if response.status_code == 200:
#     response_data = response.json()
#     print(response_data)
#     audio_content = response_data['audioContent']
#     with open("output.mp3", "wb") as audio_file:
#         audio_file.write(base64.b64decode(audio_content))
#     print("Audio file saved successfully.")
# else:
#     print(f"Error: {response.status_code}, {response.text}")
#
# with open("name.pdf","r") as file:
#     data=file.read()

# import requests
# from google.auth import default
# from google.auth.transport.requests import Request
# import base64
#
# credentials,project_id=default()
# # credentials.refresh(Request())
# credentials.refresh(Request())
# import os
# from flask import send_file
# import json
#
# access_token=credentials.token
# print(access_token)
#
# headers = {
#     "Authorization": f"Bearer {access_token}",
#     "x-goog-user-project": project_id,
#     "Content-Type": "application/json; charset=utf-8"
# }
# data = {
#     "input": {
#         'ssml':'hello my name is john'
#     },
#     'voice':{
#       'languageCode':'en-us',
#       'name':'en-US-Standard-B',
#       'ssmlGender':'MALE'
#     },
#     "audioConfig": {
#         "audioEncoding": "MP3"
#     }
# }
#
# url = "https://texttospeech.googleapis.com/v1/text:synthesize"


# response = requests.post(url, headers=headers, data=json.dumps(data))
# print(response.status_code)
# if response.status_code==200:
#     audioContent=response.json()['audioContent']
#     with open("voice2.mp3","wb") as audio:
#         audio.write(base64.b64decode(audioContent))
#         print("Audio created successfully")





# import requests
# from google.auth import default
# from google.auth.transport.requests import Request
# import base64

from google.auth import default
from google.auth.transport.requests import Request
import json
import requests
import base64

credentials,project_id=default()
credentials.refresh(Request())
access_token=credentials.token
print(access_token,"token")

header={"Authorization":f"Bearer {access_token}",
         "x-goog-user-project": f"{project_id}",
        "Content-Type": "application/json; charset=utf-8"}

url="https://texttospeech.googleapis.com/v1/text:synthesize"

data ={
  "input":{
    "text":"I have created the new audio file"
  },
  "voice":{
    "languageCode":"en-gb",
    "name":"en-GB-Standard-A",
    "ssmlGender":"FEMALE"
  },
  "audioConfig":{
    "audioEncoding":"MP3"
  }
}

response=requests.post(url,data=json.dumps(data),headers=header)
print(response.json())
if response.status_code==200:
    print("hi")
    with open("new_audio.mp3","wb") as file:
        file.write(base64.b64decode(response.json()['audioContent']))
        print("success")

# from pypdf2 import PdfReader
# data=PdfReader('text_file.pdf')
# print(data.pages[0].extract_text())
# text=''
# for page in doc:
#   print(page.getText())

# from PyPDF2 import PdfReader
# input1 = PdfReader(open('text_file.pdf', 'rb'))
# # Print the details of the PdfReader object
# print(input1)
#
# # Optionally, you can print the number of pages and metadata
# print(f'Number of pages: {len(input1.pages)}')
# print(f'Title: {input1.getDocumentInfo().title}')
# print(f'Author: {input1.getDocumentInfo().author}')


# from pymupdf import pymupdf
#
# with pymupdf.open('text_file.pdf','rb') as doc:
#     print(f'Number of pages: {len(doc)}')
#     for page in doc:
#         text = page.get_text()
#         print(text)