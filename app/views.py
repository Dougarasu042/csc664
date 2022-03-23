from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
import PIL.Image as image
import base64
import io

# Create your views here.
# request handler

def render_images(request):
    return render(request, 'hello.html')


def getImages(request):
    try:
        sqliteConnection = sqlite3.connect('/Users/tonycao/Desktop/csc664/csc664/db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_get_blob_data = """ SELECT * FROM images """
        cursor.execute(sqlite_get_blob_data)
        results = cursor.fetchone()
        img = image.open(io.BytesIO(results[2]))
        img.show()
        return HttpResponse('')
    except sqlite3.Error as error:
        print(error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")