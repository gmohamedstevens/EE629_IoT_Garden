import sqlite3
from sqlite3 import Error
import datetime 

# Database manager object
class Database(object):
    
    # Object initialization
    def __init__(self):
        self.conn = None
    
    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
        return conn
                
    def close_connection(self, conn):
        try:
            conn.close()
        except Error as e:
            print(e)
           
    def initialize_tables(self, conn):
        self.create_table(conn, """ CREATE TABLE IF NOT EXISTS light_sensor_data (
                                        id integer PRIMARY KEY,
                                        date text,
                                        reading real
                                    ); """)
        self.create_table(conn, """ CREATE TABLE IF NOT EXISTS moisture_sensor_data (
                                        id integer PRIMARY KEY,
                                        date text,
                                        reading real
                                    ); """)
        self.create_table(conn, """ CREATE TABLE IF NOT EXISTS image_data (
                                        id integer PRIMARY KEY,
                                        date text,
                                        image blob
                                    ); """)
           
    def create_table(self, conn, create_table_str):
        try:
            c = conn.cursor()
            c.execute(create_table_str)
        except Error as e:
            print(e)
    

    def insert_light_sensor_data(self, conn, task):
        sql = ''' INSERT INTO light_sensor_data(date, reading)
                  VALUES(?,?) '''
        cursor = conn.cursor()
        cursor.execute(sql, task)
        conn.commit()
        return cursor.lastrowid
    
    def insert_moisture_sensor_data(self, conn, task):
        sql = ''' INSERT INTO moisture_sensor_data(date, reading)
                  VALUES(?,?) '''
        cursor = conn.cursor()
        cursor.execute(sql, task)
        conn.commit()
        return cursor.lastrowid
    
    def insert_image_data(self, conn, task):
        sql = ''' INSERT INTO image_data(date, image)
                  VALUES(?,?) '''
        cursor = conn.cursor()
        cursor.execute(sql, task)
        conn.commit()
        return cursor.lastrowid
        
