import requests

def generate_code(user_id):
    url = "http://127.0.0.1:8000/" + f"user/login?user_id={user_id}"
    response = requests.get(url)
    verification_code = response.json()["verification_code"]
    return verification_code