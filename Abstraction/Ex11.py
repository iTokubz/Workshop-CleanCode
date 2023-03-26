def validate_user(username, password):
    if len(username) < 6 or len(password) < 8:
        return False
    if not username.isalnum():
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True
def create_user(username, password):
    if not validate_user(username, password):
        return None
