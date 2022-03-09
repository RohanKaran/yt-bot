import json
import os

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file',
          'https://www.googleapis.com/auth/drive']

cred = os.getenv("CREDS")
creds = Credentials.from_service_account_info(json.loads(cred))


def write(arr):
    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values()
        result.append(spreadsheetId="1GeLnS9bZQFpUkiGNMgzasJ17xJ8N46Hqb1OR0U9n0kU",
                      range='Sheet1!A1', valueInputOption='RAW', body={"values": arr}).execute()
        # values = result.get('values', [])
    except HttpError as err:
        print(err)
