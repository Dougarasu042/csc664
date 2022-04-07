from django.shortcuts import render
from django.http import FileResponse
import sqlite3
import cv2
import matplotlib.pyplot as plt

def bin_img(image):
    img = cv2.imread(image)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
    return edges

# Create your views here.
# request handler
def match_image(request):
    try:
        sqliteConnection = sqlite3.connect('/Users/tonycao/Desktop/csc664/csc664/db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # process query image
        img_query_edge = bin_img('app' + request.POST.get("path"))
        contour1, heirarchy = cv2.findContours(img_query_edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        img_query_hist = cv2.imread('app' + request.POST.get("path"))
        hist_query = cv2.calcHist([img_query_hist], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
        hist_query[255, 255, 255] = 0
        cv2.normalize(hist_query, hist_query, 0, 1, cv2.NORM_MINMAX)
        # end of process query image
        
        sqlite_get_data = """ SELECT * FROM image_paths """
        cursor.execute(sqlite_get_data)
        results = cursor.fetchall()

        scores = []
        
        for res in results:
            hash_file = res[1]
            temp_file = res[2].replace('/Users/tonycao/Desktop/csc664/csc664/', '')
            img = bin_img(temp_file)
            contour2, heirarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            img_hist = cv2.imread(temp_file)
            hist = cv2.calcHist([img_hist], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
            hist[255, 255, 255] = 0
            cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)

            hist_diff = cv2.compareHist(hist_query, hist, cv2.HISTCMP_CORREL)
            cont_diff = cv2.matchShapes(contour1[0], contour2[0], cv2.CONTOURS_MATCH_I1, 0)

            scores.append((cont_diff, hist_diff, hash_file, temp_file))

        scores.sort(key=lambda y: y[1], reverse=True)

        best_match = {}
        for index, tuple in enumerate(scores):
            if tuple[2] not in best_match:
                best_match[tuple[2]] = ''
            best_match[tuple[2]] = tuple[3]

        # trim results 
        best_match = dict(list(best_match.items())[:5])
        # print(list(best_match.values())[1])
        # img = open(list(best_match.values())[1], 'rb')

        # response = FileResponse(img)

        # return response

        return render(request, 'hello.html', {'context': best_match})
    except sqlite3.Error as error:
        print(error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")


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
            image_paths[res[1]] = res[2].replace('/Users/tonycao/Desktop/csc664/csc664/app', '')
        
        return render(request, 'hello.html', {'context': image_paths})
    except sqlite3.Error as error:
        print(error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")