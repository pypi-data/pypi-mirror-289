import requests
from .constants import api_url

def api_request(endpoint: str, method: str = "GET", headers: dict = None, data: dict = None):
    """Reusable function for making API requests."""
    url = f"{api_url}/{endpoint}"
    response = requests.request(method, url, headers=headers, data=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return None

# =============================================================================

def get_user_info(username: str, password: str):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "password",
        "username": username,
        "password": password,
        "scope": "",
        "client_id": "",
        "client_secret": "",
    }
    token = api_request("auth/token", method="POST", headers=headers, data=data)
    token = token["access_token"]
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}",
    }
    return token, api_request("auth/whoami", headers=headers)