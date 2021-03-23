import gspread
from oauth2client.service_account import ServiceAccountCredentials

def googleSheet():

    scope = ['https://spreadsheets.google.com/feeds']
    json_file_name = './global-ielts-online-907b5ea18a16.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
    gc = gspread.authorize(credentials)
    spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1-Qy11dtRjGZ_gb9QlEiBAht4cufbOrZR2BCB9ZDxIJg/edit#gid=1534660144'

    # 문서 불러오기
    doc = gc.open_by_url(spreadsheet_url)
    # a 시트 불러오기
    worksheet = doc.worksheet('통계(21/03월)')

    cell_data = worksheet.acell('B2').value

    print(cell_data)