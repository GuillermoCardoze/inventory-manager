import sqlite3

CONN = sqlite3.connect('inventory.db')
CURSOR = CONN.cursor()
