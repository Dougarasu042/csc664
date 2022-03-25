from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import FileResponse
import sqlite3
# import PIL.Image as image
# import base64
# import io
# import sys
# sys.path.insert(0, '/Users/tonycao/Desktop/csc664/csc664/app/static')
# from init_db import process_img
import cv2
import matplotlib.pyplot as plt

# Create your views here.
# request handler
def match_image(request):
    query_image_path = request.POST.get("path").replace('.', '/Users/tonycao/Desktop/csc664/csc664/app', 1)
    # process_img(query_image_path)
    print('processing ', query_image_path)
    # edge detection 
    # Read the original image
    img = cv2.imread(query_image_path)
    # print('read image')
    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
    # print('turned grayscale')
    # Canny Edge Detection
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
    # Display Canny Edge Detection Image
    # print('done edge detection')
    # plt.switch_backend('Agg') 
    # cv2.imshow('Canny Edge Detection', edges)
    # cv2.waitKey(0) 
    hist = cv2.calcHist([edges], [0], None, [256], [0,256])
    print(hist)
    query_dict = {'a' : query_image_path}
    # print(query_dict)
    return render(request, 'index.html', {'context': query_dict})

def load_front_page(request):
    try:
        sqliteConnection = sqlite3.connect('/Users/tonycao/Desktop/csc664/csc664/db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_get_data = """ SELECT * FROM image_paths """
        cursor.execute(sqlite_get_data)
        results = cursor.fetchall()

        image_paths = {}
        for res in results:
            if res[1] not in image_paths:
                image_paths[res[1]] = ''
            image_paths[res[1]] = res[2].replace('/Users/tonycao/Desktop/csc664/csc664/app', '.')

        return render(request, 'hello.html', {'context': image_paths})
    except sqlite3.Error as error:
        print(error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")