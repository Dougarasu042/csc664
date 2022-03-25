import os
import sqlite3
import hashlib
import cv2
import matplotlib.pyplot as plt
# import image_dict

def list_files(dir):  
    # files
    fl_total = []
    # dir
    di = []

    for path, dirs, files in os.walk(dir):
        for dir in dirs:
            di.append(dir)

        fl = []
        for file in files:
            fl.append(file)
            if len(fl) == 5:
                fl_total.append(fl)


    return di, fl_total


def process_img(photo):
    # hash image 
    with open(photo, "rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest()

    # print(imgId, readable_hash)

    # edge detection 
    # Read the original image
    img = cv2.imread(photo)
    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
    # Canny Edge Detection
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
    # Display Canny Edge Detection Image
    # cv2.imshow('Canny Edge Detection', edges)
    # cv2.waitKey(0)

    # create image histogram 
    hist = cv2.calcHist([edges], [0], None, [256], [0,256])
    # hist_plt = plt.hist(edges.ravel(), 256, [0, 256])
    # print(hist)
    # print()
    # print(hist_plt)

    return readable_hash, str(hist)


def store_img(imgId, image_info):
    # image_info --> ["binary", file/path, hash, hist]
    try:
        # put in db 
        sqliteConnection = sqlite3.connect('/Users/tonycao/Desktop/csc664/csc664/db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        hash, path, type, hist = image_info[2], image_info[1], image_info[0], image_info[3]

        # store in DB 
        sqlite_insert_path_query = """ INSERT INTO image_paths
                                  (id, hash, path) VALUES (?, ?, ?)"""

        # dic = image_dict.LocalDataBase()
        # dic.Save_Image(hash, path, type)

        sqlite_insert_query = """ INSERT INTO images
                                  (id, hash, hist) VALUES (?, ?, ?)"""

        # Convert data into tuple format
        insert_query_tuple = (imgId, hash, hist)
        insert_query_path_tuple = (imgId, hash, path)

        cursor.execute(sqlite_insert_query, insert_query_tuple)
        cursor.execute(sqlite_insert_path_query, insert_query_path_tuple)

        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")


# get all image paths from local folder
binary_directory = '/Users/tonycao/Desktop/csc664/csc664/app/static/app/images/binary/'
dir, files = list_files(binary_directory)
dir = [x for x in dir if not x.startswith('segmented')]
dir = ["/Users/tonycao/Desktop/csc664/csc664/app/static/app/images/binary/" + s + "/segmented/" for s in dir]
# /Users/tonycao/Desktop/csc664/csc664/app/static/app/images/binary/010312-B8-1-2/segmented/frame0001.png
binary_files = []

for a, b in zip(dir, files):
    for f in b:
        binary_files.append(a + f)
        

grey_directory = '/Users/tonycao/Desktop/csc664/csc664/app/static/app/images/grey/'
dir, files = list_files(grey_directory)
dir = [x for x in dir if not x.startswith('segmented')]
dir = ["/Users/tonycao/Desktop/csc664/csc664/app/static/app/images/grey/" + s + "/org/" for s in dir]

grey_files = []

for a, b in zip(dir, files):
    for f in b:
        grey_files.append(a + f)

# process binary image
binary_image_info = []
for file in binary_files:
    hash, hist = process_img(file)
    binary_image_info.append(["binary", file, hash, hist])


# store binary image in DB
id = 0
for img in binary_image_info:
    id += 1
    store_img(id, img)


# process grey image
grey_image_info = []
for file in grey_files:
    hash, hist = process_img(file)
    grey_image_info.append(["grey", file, hash, hist])


# store grey image in DB
for img in grey_image_info:
    id += 1
    store_img(id, img)

        
