import pyodbc, validators

conn_string = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=DB/url_db.accdb;'
)
conn = pyodbc.connect(conn_string)
cursor = conn.cursor()

def add_url(url):
    if(validate_url(url)):
         return "valid URL"
    return "invalid URL"

def validate_url(url):
    return validators.url(url)
