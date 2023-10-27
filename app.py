from flask import Flask, render_template, request
import pandas as pd
from farcaster import Warpcast
import os

app = Flask(__name__)

def follow_user_by_id(fid, client):
    try:
        response = client.follow_user(fid)
        return f"Successfully followed user with ID {fid}"
    except Exception as e:
        return f"Failed to follow user with ID {fid}: {str(e)}"

def follow_user_by_username(username, client):
    try:
        user = client.get_user_by_username(username)
        client.follow_user(user.fid)
        return f"Successfully followed user with username {username}"
    except Exception as e:
        return f"Failed to follow user with username {username}: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mnemonic = request.form['mnemonic']
        client = Warpcast(mnemonic=mnemonic)
        google_sheet_url = 'https://docs.google.com/spreadsheets/d/1CUCgxhy1OnJzU_kwLy15T_NQHTaui8phxASpy_YYnq0/export?format=csv'
        data = pd.read_csv(google_sheet_url)

        results = []
        for _, row in data.iterrows():
            fid = row['Farcaster ID']
            username = row['Farcaster Name']
            
            if pd.notna(fid):
                result = follow_user_by_id(int(fid), client)
                results.append(result)
            elif pd.notna(username):
                result = follow_user_by_username(username, client)
                results.append(result)

        return render_template("index.html", results=results)
    return render_template("index.html", results=None)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
