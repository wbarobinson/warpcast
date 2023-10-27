import pandas as pd
from farcaster import Warpcast

def follow_user_by_id(fid, client):
    try:
        response = client.follow_user(fid)
        print(f"Successfully followed user with ID {fid}")
    except Exception as e:
        print(f"Failed to follow user with ID {fid}: {str(e)}")

def follow_user_by_username(username, client):
    try:
        user = client.get_user_by_username(username)
        client.follow_user(user.fid)
        print(f"Successfully followed user with username {username}")
    except Exception as e:
        print(f"Failed to follow user with username {username}: {str(e)}")

if __name__ == "__main__":
    mnemonic = input("Please enter your mnemonic (just the 12 words with spaces between them): ")

    client = Warpcast(mnemonic=mnemonic)
    google_sheet_url = 'https://docs.google.com/spreadsheets/d/1CUCgxhy1OnJzU_kwLy15T_NQHTaui8phxASpy_YYnq0/export?format=csv'
    data = pd.read_csv(google_sheet_url)

    for _, row in data.iterrows():
        fid = row['Farcaster ID']
        username = row['Farcaster Name']
        
        if pd.notna(fid):
            follow_user_by_id(int(fid), client)
        elif pd.notna(username):
            follow_user_by_username(username, client)

    print(client.get_healthcheck())
