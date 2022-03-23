import sqlite3

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(imgId, type, photo):
    try:
        sqliteConnection = sqlite3.connect('/Users/tonycao/Desktop/csc664/csc664/db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO images
                                  (id, type, photo) VALUES (?, ?, ?)"""

        image = convertToBinaryData(photo)
        # Convert data into tuple format
        data_tuple = (imgId, type, image)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print(f'Image id {imgId} and file type {type} inserted successfully as a BLOB into a table')
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")

# BB
insertBLOB(1, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/010312-B8-1-2/segmented/frame0001.png")
insertBLOB(2, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/010312-B8-1-2/org/frame0001.png")

insertBLOB(3, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/010312-B8-1-2/segmented/frame0203.png")
insertBLOB(4, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/010312-B8-1-2/org/frame0203.png")

insertBLOB(5, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/010312-B8-1-2/segmented/frame0406.png")
insertBLOB(6, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/010312-B8-1-2/org/frame0406.png")

insertBLOB(7, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/010312-B8-1-2/segmented/frame0609.png")
insertBLOB(8, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/010312-B8-1-2/org/frame0609.png")

insertBLOB(9, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/010312-B8-1-2/segmented/frame0812.png")
insertBLOB(10, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/010312-B8-1-2/org/frame0812.png")

# control
insertBLOB(11, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/010312-control-000-2/segmented/frame0001.png")
insertBLOB(12, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/010312-control-000-2/org/frame0001.png")

insertBLOB(13, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/010312-control-000-2/segmented/frame0200.png")
insertBLOB(14, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/010312-control-000-2/org/frame0200.png")

insertBLOB(15, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/010312-control-000-2/segmented/frame0400.png")
insertBLOB(16, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/010312-control-000-2/org/frame0400.png")

insertBLOB(17, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/010312-control-000-2/segmented/frame0599.png")
insertBLOB(18, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/010312-control-000-2/org/frame0599.png")

insertBLOB(19, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/010312-control-000-2/segmented/frame0799.png")
insertBLOB(20, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/010312-control-000-2/org/frame0799.png")

# 2CPT
insertBLOB(21, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/032612-2CPT-10-3-B/segmented/frame0001.png")
insertBLOB(22, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/032612-2CPT-10-3-B/org/frame0001.png")

insertBLOB(23, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/032612-2CPT-10-3-B/segmented/frame0215.png")
insertBLOB(24, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/032612-2CPT-10-3-B/org/frame0215.png")

insertBLOB(25, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/032612-2CPT-10-3-B/segmented/frame0429.png")
insertBLOB(26, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/032612-2CPT-10-3-B/org/frame0429.png")

insertBLOB(27, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/032612-2CPT-10-3-B/segmented/frame0644.png")
insertBLOB(28, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/032612-2CPT-10-3-B/org/frame0644.png")

insertBLOB(29, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/032612-2CPT-10-3-B/segmented/frame0858.png")
insertBLOB(30, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/032612-2CPT-10-3-B/org/frame0858.png")

# prava
insertBLOB(31, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/032612-Prava-1-3/segmented/frame0001.png")
insertBLOB(32, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/032612-Prava-1-3/org/frame0001.png")

insertBLOB(33, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/032612-Prava-1-3/segmented/frame0192.png")
insertBLOB(34, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/032612-Prava-1-3/org/frame0192.png")

insertBLOB(35, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/032612-Prava-1-3/segmented/frame0384.png")
insertBLOB(36, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/032612-Prava-1-3/org/frame0384.png")

insertBLOB(37, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/032612-Prava-1-3/segmented/frame0575.png")
insertBLOB(38, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/032612-Prava-1-3/org/frame0575.png")

insertBLOB(39, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/032612-Prava-1-3/segmented/frame0767.png")
insertBLOB(40, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/032612-Prava-1-3/org/frame0767.png")

# PZQ
insertBLOB(41, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/032911-PZQ-10-1/segmented/frame0001.png")
insertBLOB(42, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/032612-Prava-1-3/org/frame0001.png")

insertBLOB(43, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/032911-PZQ-10-1/segmented/frame0095.png")
insertBLOB(44, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/032911-PZQ-10-1/org/frame0095.png")

insertBLOB(45, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/032911-PZQ-10-1/segmented/frame0190.png")
insertBLOB(46, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/032911-PZQ-10-1/org/frame0190.png")

insertBLOB(47, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/032911-PZQ-10-1/segmented/frame0285.png")
insertBLOB(48, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/032911-PZQ-10-1/org/frame0285.png")

insertBLOB(49, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/032911-PZQ-10-1/segmented/frame0380.png")
insertBLOB(50, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/032911-PZQ-10-1/org/frame0380.png")

# Simva
insertBLOB(51, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/040212-Simva-10-1/segmented/frame0001.png")
insertBLOB(52, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/040212-Simva-10-1/org/frame0001.png")

insertBLOB(53, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/040212-Simva-10-1/segmented/frame0205.png")
insertBLOB(54, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/040212-Simva-10-1/org/frame0205.png")

insertBLOB(55, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/040212-Simva-10-1/segmented/frame0411.png")
insertBLOB(56, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/040212-Simva-10-1/org/frame0411.png")

insertBLOB(57, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/040212-Simva-10-1/segmented/frame0616.png")
insertBLOB(58, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/040212-Simva-10-1/org/frame0616.png")

insertBLOB(59, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/040212-Simva-10-1/segmented/frame0821.png")
insertBLOB(60, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/040212-Simva-10-1/org/frame0821.png")

# Ator
insertBLOB(61, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/061112-Ator-01-1-c/segmented/frame0001.png")
insertBLOB(62, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/061112-Ator-01-1-c/org/frame0001.png")

insertBLOB(63, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/061112-Ator-01-1-c/segmented/frame0102.png")
insertBLOB(64, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/061112-Ator-01-1-c/org/frame0102.png")

insertBLOB(65, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/061112-Ator-01-1-c/segmented/frame0204.png")
insertBLOB(66, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/061112-Ator-01-1-c/org/frame0204.png")

insertBLOB(67, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/061112-Ator-01-1-c/segmented/frame0306.png")
insertBLOB(68, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/061112-Ator-01-1-c/org/frame0306.png")

insertBLOB(69, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/061112-Ator-01-1-c/segmented/frame0408.png")
insertBLOB(70, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/061112-Ator-01-1-c/org/frame0408.png")

# BB
insertBLOB(71, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/082112-B8-10-4/segmented/frame0001.png")
insertBLOB(72, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/082112-B8-10-4/org/frame0001.png")

insertBLOB(73, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/082112-B8-10-4/segmented/frame0058.png")
insertBLOB(74, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/082112-B8-10-4/org/frame0058.png")

insertBLOB(75, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/082112-B8-10-4/segmented/frame0117.png")
insertBLOB(76, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/082112-B8-10-4/org/frame0117.png")

insertBLOB(77, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/082112-B8-10-4/segmented/frame0175.png")
insertBLOB(78, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/082112-B8-10-4/org/frame0175.png")

insertBLOB(79, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/082112-B8-10-4/segmented/frame0233.png")
insertBLOB(80, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/082112-B8-10-4/org/frame0233.png")

# prom
insertBLOB(81, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/082112-Prom-1-4/segmented/frame0001.png")
insertBLOB(82, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/082112-Prom-1-4/org/frame0001.png")

insertBLOB(83, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/082112-Prom-1-4/segmented/frame0059.png")
insertBLOB(84, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/082112-Prom-1-4/org/frame0059.png")

insertBLOB(85, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/082112-Prom-1-4/segmented/frame0118.png")
insertBLOB(86, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/082112-Prom-1-4/org/frame0118.png")

insertBLOB(87, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/082112-Prom-1-4/segmented/frame0176.png")
insertBLOB(88, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/082112-Prom-1-4/org/frame0176.png")

insertBLOB(89, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/082112-Prom-1-4/segmented/frame0235.png")
insertBLOB(90, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/082112-Prom-1-4/org/frame0235.png")

# A2
insertBLOB(91, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/092611-A2-1-2/segmented/frame0001.png")
insertBLOB(92, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/092611-A2-1-2/org/frame0001.png")

insertBLOB(93, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/092611-A2-1-2/segmented/frame0074.png")
insertBLOB(94, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/092611-A2-1-2/org/frame0074.png")

insertBLOB(95, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/092611-A2-1-2/segmented/frame0148.png")
insertBLOB(96, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/092611-A2-1-2/org/frame0148.png")

insertBLOB(97, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/092611-A2-1-2/segmented/frame0221.png")
insertBLOB(98, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/092611-A2-1-2/org/frame0221.png")

insertBLOB(99, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/092611-A2-1-2/segmented/frame0295.png")
insertBLOB(100, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/092611-A2-1-2/org/frame0295.png")

# D7
insertBLOB(101, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/092611-D7-10-4/segmented/frame0001.png")
insertBLOB(102, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/092611-D7-10-4/org/frame0001.png")

insertBLOB(103, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/092611-D7-10-4/segmented/frame0073.png")
insertBLOB(104, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/092611-D7-10-4/org/frame0073.png")

insertBLOB(105, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/092611-D7-10-4/segmented/frame0146.png")
insertBLOB(106, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/092611-D7-10-4/org/frame0146.png")

insertBLOB(107, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/092611-D7-10-4/segmented/frame0219.png")
insertBLOB(108, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/092611-D7-10-4/org/frame0219.png")

insertBLOB(109, "binary", "/Users/tonycao/Desktop/csc664/csc664/DB/images/binary/092611-D7-10-4/segmented/frame0292.png")
insertBLOB(110, "grey", "/Users/tonycao/Desktop/csc664/csc664/DB/images/grey/092611-D7-10-4/org/frame0292.png")