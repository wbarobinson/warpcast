import os
from farcaster import Warpcast
from dotenv import load_dotenv # can be installed with `pip install python-dotenv`

load_dotenv()

client = Warpcast(mnemonic=os.environ.get("<MNEMONIC_ENV_VAR>"))

print(client.get_healthcheck())