import pyodbc, validators, datetime

conn_string = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=DB/url_db.accdb;'
)

conn = pyodbc.connect(conn_string)
cursor = conn.cursor()

# Validate URL, check if URL already exists, returns ID for generating short URL.
def insert_url(url):
    if(__validate_url(url)):
        url_check = __get_id(url)
        if url_check is None:
            insert_date = str(datetime.datetime.now())
            insert_statement = "INSERT INTO Urls (OriginalUrl, DateCreated) VALUES ('"+url+"', '"+insert_date+"');"
            cursor.execute(insert_statement)
            conn.commit()
            new_id = __get_inserted_id(url, insert_date)
            return str(new_id) 
        return url_check
    return None

# Searches DB for URL with given ID
def get_url(id):
    select_statement = "SELECT OriginalUrl FROM URls WHERE ID = "+id+";"
    result = cursor.execute(select_statement).fetchval()
    if result is not None:
        return result
    return None

# Used to check if URL already exists in DB
def __get_id(url):
    select_statement = "SELECT ID FROM Urls WHERE OriginalUrl = '"+url+"';"
    result = cursor.execute(select_statement).fetchval()
    if result is not None:
        return result
    return None

# Validates the URL, returns boolean
def __validate_url(url):
    return validators.url(url)

# Returns ID of the inserted URL
def __get_inserted_id(url, insert_date):
    select_statement = "SELECT ID FROM Urls WHERE OriginalUrl = '"+url+"' AND DateCreated = '"+insert_date+"';"
    response = cursor.execute(select_statement).fetchval()
    return response

