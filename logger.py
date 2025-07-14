import os
import gspread
import json
import base64
from oauth2client.service_account import ServiceAccountCredentials

def log_to_sheet(token_symbol, action, tx_hash):
    creds_data = base64.b64decode(os.getenv("GOOGLE_SHEET_CREDENTIALS_JSON")).decode()
    creds_json = json.loads(creds_data)
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(os.getenv("GOOGLE_SHEET_ID")).sheet1
    sheet.append_row([token_symbol, action, tx_hash])