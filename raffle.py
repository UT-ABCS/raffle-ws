# obtain_data()
# pick_winner(items)

from __future__ import print_function

import os.path
import random
from secret import SPREADSHEET_ID, SPREADSHEET_RANGE

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

def perform_raffle():
    items = obtain_data()
    winner = pick_winner(items)
    print("The winner is {}".format(winner))

# Obtains data from the Google Sheet specified by SPREADSHEET_ID
# to raffle from
def obtain_data():
    # The list of data to be raffled from, which will be populated by
    # the Google Sheets API
    items = []

    """
    Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range=SPREADSHEET_RANGE).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        print('UT EIDs:')
        for row in values:
            # Print column B and C, which corresponds to the respondee's
            # first and last names
            # print('%s %s' % (row[1], row[2]))
            items.append('%s %s' % (row[1], row[2]))
        
    except HttpError as err:
        print(err)
    
    return items

# Picks a winner from the list specified by items
def pick_winner(items):
    # return random.choice(items) makes this method one line
    
    # Randomly select an index from items
    index = random.randrange(0, len(items))

    # Use the index to select an element from items as the winner
    winner = items[index]

    # We found the winner! Return them.
    return winner

if __name__ == "__main__":
    perform_raffle()