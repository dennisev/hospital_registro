# src\authentication.py
def authenticate_user(username, password):
    users = {
        'admin': 'admin',
        'usuario': 'usuario'
    }
    if username in users and users[username] == password:
        return username
    else:
        return None
