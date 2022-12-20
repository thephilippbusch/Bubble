import jwt, time
from typing import Dict, Union
from decouple import config

SERVER_JWT_SECRET = config("SERVER_JWT_SECRET")
SERVER_JWT_ALGORITHM = config("SERVER_JWT_ALGORITHM")

# Creates a JSON Web Token by encoding a unique ID 'uid' (can be changed)
# with the JWT Secret and Algorithm from the '.env' variables
# Optionally, an Expiration timer cna be set (Millisecs from time of creation)
def signJWT(uid: str, expires_in: Union[int, None] ) -> Dict[str, str]:
  payload = { 
    "uid": uid,
  } if expires_in is None else {
    "uid": uid,
    "expires": time.time() + expires_in
  }
  token = jwt.encode(payload, SERVER_JWT_SECRET, algorithm=SERVER_JWT_ALGORITHM)
  return token

# Decodes the passed JWT and returns the decoded token, if token
# and expiration timer are still valid
def decodeJWT(token: str) -> Dict:
  try:
    decoded_token = jwt.decode(token, SERVER_JWT_SECRET, algorithms=[SERVER_JWT_ALGORITHM])
    return decoded_token
    # Use following Return statement to activate expiring:
    # return decoded_token if decoded_token["expires"] >= time.time() else None
  except:
    return {}