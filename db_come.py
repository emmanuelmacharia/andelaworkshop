import psycopg2
import os

url = "dbname = 'store_manager' host = 'localhost' port = '5432' url = ''"

db_url = os.getenv('DATABASE_URL')

def connection(url):
    con = psycopg2.connect(url)
    return con

def create_table():
    query1 =
    query2 =
    queries = [query1, query2]

    for q in queries:
