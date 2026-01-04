import mysql.connector as sl 

def get_connection():
    return sl.connect(
        host="localhost",
        user="root",
        passwd="12345",
        database="RMS"
    )
    