import hmac
import hashlib
import os
import requests
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

load_dotenv()

# Setup Session with Retry
session = requests.Session()
retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))

# Fetch Users
response = session.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

# 1. Print first 5 users
for user in users[:5]:
    print(user.get("id"))
    print(user.get("name"))
    print(user.get("email"))

# 2. Extract nested values using .get() only
first_user = users[0] if users else {}
address = first_user.get("address") or {}
city = address.get("city", "Not Available")
zip_code = address.get("zipcode_missing", "Not Available")

print(f"City: {city} | Zip: {zip_code}")

# 3. HMAC Verification
def verify_signature(payload: str, signature: str, secret: str) -> bool:
    expected_sig = hmac.new(
        secret.encode("utf-8"),
        payload.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected_sig, signature)

secret = "my_secret_key"
payload = '{"event": "user_created"}'
valid_sig = hmac.new(secret.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256).hexdigest()

valid_test = verify_signature(payload, valid_sig, secret)
tampered_test = verify_signature(payload + "tampered", valid_sig, secret)
wrong_secret_test = verify_signature(payload, valid_sig, "wrong_secret")

print(f"Valid: {valid_test} Tampered: {tampered_test} Wrong secret: {wrong_secret_test}")
