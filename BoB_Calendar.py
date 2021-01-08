from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import copy

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main(calendarid):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    time = '2021-01-03T00:00:00.000000Z'
    print('Getting the upcoming 300 events')

    #change the calendarId to target calendar's ID
    events_result = service.events().list(calendarId=calendarid, timeMin=time,
                                        maxResults=300, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
        print(event)


def Copy_To_My_Calendar():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    time = '2021-01-03T00:00:00.000000Z'
    print('Getting the upcoming 300 events')

    #change the calendarID to target calendar's ID
    events_result = service.events().list(calendarId='4dsrggphdhlgs0h3lrd880v2io@group.calendar.google.com', timeMin=time,
                                        maxResults=300, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    # target events
    target_events = []

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        
        # if name start with "[공]" append to ret
        if event['summary'][:3] == "[공]":
            #print(start, event['summary'])
            target_events.append(copy.deepcopy(event))
            event.pop('iCalUID')
            event.pop('sequence')
            event.pop('htmlLink')
            event.pop('id')
            event.pop('kind')
            event.pop('etag')
            event.pop('creator')
            event.pop('created')
            event.pop('updated')
            event.pop('organizer')
            #print(event)

    for event in target_events:
        try:
            events_inserted = service.events().insert(calendarId='neplqpk76mi4ahtrmu2ru29g44@group.calendar.google.com', body=event).execute()
        except Exception as e:
            if "identifier already exists" in str(e):
                print("Already Exists")
            else:
                print(e)
        print(events_inserted)

def Add_Alert_To_Events():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    time = '2021-01-03T00:00:00.000000Z'
    print('Getting the upcoming 300 events')

    #change the calendarId to target calendar's ID
    events_result = service.events().list(calendarId='neplqpk76mi4ahtrmu2ru29g44@group.calendar.google.com', timeMin=time,
                                        maxResults=300, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    for event in events:
        event_with_alert = copy.deepcopy(event)
        event_with_alert['reminders'] = {
                                                                'useDefault': False,
                                                                'overrides': [
                                                                {'method': 'popup', 'minutes': 10},
                                                                ]
                                                            }
        events_result = service.events().update(calendarId='neplqpk76mi4ahtrmu2ru29g44@group.calendar.google.com', eventId=event.get('id'), body=event_with_alert).execute()
        print(events_result)

if __name__ == '__main__':
    #main('neplqpk76mi4ahtrmu2ru29g44@group.calendar.google.com')
    Add_Alert_To_Events()
    print("DONE")