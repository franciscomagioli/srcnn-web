#!/usr/bin/python
 
import sqlite3, time
from sqlite3 import Error
 
 
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def select_all_documents(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM core_document")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_all_docs_status_0(conn):
    cur = conn.cursor()
    cur.execute("SELECT id,document FROM core_document WHERE status=0")
    rows = cur.fetchall()
    return rows

def update_doc_status_0(conn,filename):
    cur = conn.cursor()
    cur.execute("UPDATE core_document SET status  = 0 WHERE status = 1 AND document = filename")
    conn.commit()

def update_doc_status_1(conn, filename):
    cur = conn.cursor()
    cur.execute("UPDATE core_document SET status = 2 WHERE document = filename AND status = 1")
    conn.commit()

def insert_bicubic(conn, filename, or_id):
    cur = conn.cursor()
    cur.execute("INSERT INTO core_bicubicimage (document, original_id) VALUES (filename, or_id)")
    conn.commit()

def insert_srcnn(conn, filename, or_id):
    cur = conn.cursor()
    cur.execute("INSERT INTO core_srcnnimage (document, original_id) VALUES (filename, or_id)")
    conn.commit()

def execute_srcnn():
    return null

def main():
    base_dir = "/home/rune/test-web/simple-file-upload/"
    db = base_dir + "db.sqlite3"
    conn = create_connection(db)
    print("query")
    select_all_documents(conn)

    file_names = select_all_docs_status_0(conn)
    for file in file_names:
        print("Processing " + file[1])
        select_doc_status_0(conn,file[1])

        # invoke srcnn launch for each base_dir + file
        #execute_srcnn()
        select_doc_status_1(conn,file[1])

        # add processed images to DB to render in django
        print("Adding " + bicubic_filename + " to DB")
        bicubic_filename = ""
        insert_bicubic(conn, bicubic_filename, file[0])

        print("Adding " + srcnn_filename + " to DB")
        srcnn_filename = ""
        insert_srcnn(conn, srcnn_filename, file[0])


if __name__ == '__main__':
    while True:
        main2()
        time.sleep(60)
    main2()
