from pyrogram import Client
from pyrogram.errors import UsernameNotOccupied
import time

api_id = "29433225"
api_hash = "cbbfb104d4f4f43d3c78be56c1db2cf6"
token = "6882490925:AAE-S1M79DcEKPQvRZmc2ytl_xzk_yT-5Cc"
def check_username(app, username):
    try:
        user = app.resolve_peer(username)
        print(False)
    except UsernameNotOccupied:
        print(f"Username: {username} - Available")
    except Exception as e:
        print(e)

def main():
    app = Client(None, api_id=api_id, api_hash=api_hash, bot_token=token, no_updates=True, in_memory=True)
    app.start()
    try:
        while True:
            username = input("Enter username to check: ")
            check_username(app, username)
    finally:
        app.stop()

if __name__ == "__main__":
    main()
