from pprint import pprint
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import urllib.parse as p
import re
import os
import pickle
import json

from color import Color as CLR

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def youtube_authenticate():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = os.path.join( os.path.dirname(__file__), 'credentials.json' )
    creds = None
    # the file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # if there are no (valid) credentials availablle, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
            creds = flow.run_local_server(port=0)
        # save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build(api_service_name, api_version, credentials=creds)

def get_video_id_from_share( shareLink ):
    """
    Return the Video ID from the video `id`
    """

    return shareLink[ shareLink.rfind( "/" ) + 1: ]

def get_video_details(youtube, **kwargs):
    return youtube.videos().list(
        part="status,contentDetails",
        **kwargs
    ).execute()

# authenticate to YouTube API
youtube = youtube_authenticate()

# def scrapeFromYoutube( videoIds ):
#   list_of_objects = [Object_1, Object_2, Object_3]
#   [x.time for x in list_of_objects]

def getVideoDetailsFromList( list ):
  for item in list:
    data = get_video_details(youtube, id = item )

    pprint( data.get( "items" ) )
    # return len( data.get( "items" ) ) > 0 and data.get( "items" )[0]["contentDetails"]["licensedContent"]
  
def getVideoDetailsFromUrl( url ):
  id = url[ url.rfind( "/" ) + 1: ]
  data = get_video_details(youtube, id = id )
  if len( data.get( "items" ) ) > 0 and data.get( "items" )[0]["status"]["embeddable"]:
    return "happy"
  if len( data.get( "items" ) ) > 0 and not data.get( "items" )[0]["contentDetails"]["licensedContent"]:
    return "unlicensed"
  elif len( data.get( "items" ) ) == 0:
    return "deleted"
  else:
    return "broken" 
