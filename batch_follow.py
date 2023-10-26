import os
from pydantic import PositiveInt
from farcaster import Warpcast
from dotenv import load_dotenv # can be installed with `pip install python-dotenv`

load_dotenv()

client = Warpcast(mnemonic=os.environ.get("<MNEMONIC_ENV_VAR>"))

def follow_user(fid: PositiveInt) -> str:
    """Follow a user

    Args:
        fid (PositiveInt): Farcaster ID of the user to follow

    Returns:
        str: Status of the follow
    """
    body = FollowsPutRequest(target_fid=fid)
    response = client._put(
        "follows",
        json=body.dict(by_alias=True, exclude_none=True),
    )
    return StatusResponse(**response).result

# List of Farcaster IDs to follow
farcaster_ids_to_follow = [4985]  # Replace with actual IDs

# Batch follow
for fid in farcaster_ids_to_follow:
    status = follow_user(fid)
    print(f"Followed {fid}: {status}")

print(client.get_healthcheck())