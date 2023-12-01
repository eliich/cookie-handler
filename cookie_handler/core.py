import json

def read_and_modify_cookies(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            cookies = json.load(file)
            for cookie in cookies:
                if cookie['sameSite'] not in ['Strict', 'Lax', 'None']:
                    cookie['sameSite'] = 'None'  # Adjust as needed
            return cookies
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
