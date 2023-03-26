def validate_user(username, password):
    if len(username) > 3:
        if len(password) > 6:
            if username.isalpha():
                if password.isalnum():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
