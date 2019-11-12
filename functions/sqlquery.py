import os
import sqlite3
#import pandas as pd

#data_url = 'addresses.csv'
#headers = ['serv_id','deg_min','deg_max','sleep_min','sleep_max','extra']
#data_table = pd.read_csv(data_url, header=None, names=headers, converters={'zip': str})

# Clear example.db if it exists
#if os.path.exists('example.db'):
#    os.remove('example.db')

# Create a database
conn = sqlite3.connect('/home/fabrice/servocontroller/servo.db',check_same_thread=False)

# Add the data to our database
#data_table.to_sql('data_table', conn, dtype={
#    'serv_id':'VARCHAR(256)',
#    'deg_min':'VARCHAR(256)',
#    'deg_max':'VARCHAR(256)',
#    'sleep_min':'VARCHAR(256)',
#	'sleep_max':'VARCHAR(2)',
#	'extra':'VARCHAR(5)',
#})

conn.row_factory = sqlite3.Row

def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()

def sql_delete(query,var):
    cur = conn.cursor()
    cur.execute(query,var)

def sql_query2(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows
