#!/usr/bin/env python3

import psycopg2
from config import config

def connect():
    """
        Connect to the database.
    """
    
    conn = None

    try:
        params = config()

        print("[SCRIPT]\tConnecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        print("[SCRIPT]\tSELECT * FROM test :")
        cur.execute("SELECT * FROM test;")

        res = cur.fetchall()
        print(res)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("[SCRIPT]\tDatabase connection closed")

if __name__ == '__main__':
    connect()

