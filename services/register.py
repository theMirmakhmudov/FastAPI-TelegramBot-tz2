import requests

def register_user(user_id, fullname, username, phone_number):
    user_data = {
        "user_id": user_id,
        "fullname": fullname,
        "username": username,
        "phone_number": phone_number
    }
    url = "http://127.0.0.1:8000/" + "user/register"
    try:
        response = requests.post(url, json=user_data)
        try:
            response_data = response.json()
        except ValueError:
            response_data = {"detail": response.text}

        return {
            "status_code": response.status_code,
            "data": response_data
        }
    except requests.exceptions.RequestException as e:
        return {
            "status_code": None,
            "data": {"detail": str(e)}
        }
