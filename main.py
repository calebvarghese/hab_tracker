import gspread
from google.oauth2.service_account import Credentials
import os

cwd = os.getcwd()

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("creds.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1jZUBYZOyxVjhYSwupIQZ7qqOAowyR6ZYhik6Bc8gY08"
sheet = client.open_by_key(sheet_id)

test_values = sheet.sheet1.row_values(1)
print(test_values)
