from django.shortcuts import render
# from django.http import HttpResponse
from django.http import FileResponse
import sqlite3
import PIL.Image as image
import base64
import io
# from DB import image_dict

# Create your views here.
# request handler

def render_images(request):
    return render(request, 'hello.html')


def getImages(request):
    try:
        sqliteConnection = sqlite3.connect('/Users/tonycao/Desktop/csc664/csc664/db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_get_data = """ SELECT * FROM images_path """
        cursor.execute(sqlite_get_data)
        results = cursor.fetchall()
        image_paths = []
        for res in results:
            image_paths.append(res[2])

        img = open(image_paths[44], 'rb')
        response = FileResponse(img)
        # image_paths[0].save(response, "JPEG")
        return response
    except sqlite3.Error as error:
        print(error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")