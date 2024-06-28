import getpass

def get_active_user():
    try:
        user = getpass.getuser()
        print(user)
        return user
    except Exception as e:
        print(f"Fehler beim Abrufen des Benutzernamens: {e}")
        return None
    
get_active_user()
