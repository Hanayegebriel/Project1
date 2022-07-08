# This program is Project on YOUTUBE API 
# It Is used to report and print title and other information of Videos saved in the
import requests 
import json
import pandas as pd 
import sqlalchemy as db 
from sqlalchemy import create_engine

channel_id = 'UCD8NXAvIQO0DkJdsS6AjtzQ'
#'UCK89621dcBWuk5IGv5tJ_Yg'
API_KEY = 'AIzaSyAvf6K8yyZzpkMhcRsK17g4eDWZbNj36pU'

#url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}'
#url2 = f'&key={API_KEY}'

url = f'https://youtube.googleapis.com/youtube/v3/playlists?part=snippet%2CcontentDetails%'
url2 =  f'20%2Cid%20%2C%20status&channelId={channel_id}&key={API_KEY}'
url3 = url + url2
response1 = requests.get(url3)
response2 = response1.json()
item  = response2['items']

# storing the list of playlist by forming data frame 
frame =pd.DataFrame.from_dict(item)

#create a database 
engine = db.create_engine('sqlite:///playlist_info.db')
dataframe_name.to_sql('table_name', con=engine, if_exists='replace', index=False)
'''
for i in range (0, len(item)):
  print("The ID of the playlist", item[i]['snippet']['title'] , "is",item[i]['id'])

#requesting the user to input from the user to get the titles and owner of specific video 
print("Input specific playlist you want to retrieve titles of videos, owner of video")
id_choice = input()


url4 ='https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails%20%20&'
url5 = f'part=id&part=status&part=snippet&playlistId={id_choice}&key={API_KEY}'
url6 = url4 + url5
response3 = requests.get(url6)
file_format = response3.json()
item2 = file_format['items']
for i in range(0, len(item2)):
  print("title" ,item2[i]['snippet']['title'])
  #print("discription of video" , item2[i]['snippet']['description']) 
'''