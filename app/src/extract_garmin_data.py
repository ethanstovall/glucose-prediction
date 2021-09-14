import sqlite3
from sqlite3 import Error
from util.PathConfig import path_config

def extract_data():
    db_dir = getattr(path_config, 'db_dir')

    print(db_dir)

if __name__ == '__main__':
    extract_data()