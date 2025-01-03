import requests
import sqlite3
import base64
import gzip

from decryption import decrypt_base_64, decompress_Gzip


data = requests.get("https://api.hypixel.net/skyblock/auctions").json()

def refresh_ah():
    try:
        with sqlite3.connect("items.db") as conn:
            cursor = conn.cursor()
            cursor.execute('DROP TABLE IF EXISTS Items')
            cursor.execute('''CREATE TABLE IF NOT EXISTS Items (
                                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                item_name BLOB,
                                                price INTEGER,
                                                item_uuid BLOB,
                                                item_bytes BLOB
                                                );''')
        totalPages = data["totalPages"]

        for i in range(0, totalPages):
            data = requests.get(f"https://api.hypixel.net/skyblock/auctions?page={i}").json()
            for auction in data["auctions"]:
                if auction["bin"]:
                    item_name, lbin, item_bytes, item_uuid = auction['item_name'], auction['starting_bid'], auction['item_bytes'], auction['uuid']#check how it interacts in game with /ah
                    temp = decompress_Gzip(decrypt_base_64(item_bytes))

                    cursor.execute('INSERT INTO Items (item_name, price, item_uuid, item_bytes) VALUES (?, ?, ?, ?)', (item_name, lbin, item_uuid, item_bytes))
            conn.commit()

    except sqlite3.OperationalError as e:
        print("Failed to open connection", e)

