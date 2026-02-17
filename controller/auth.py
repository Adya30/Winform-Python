import re

class RegisterController:

    def __init__(self, user_model):
        self.user_model = user_model

    def create_user(self, username, password, email):

        if not username.strip():
            raise ValueError("Username wajib diisi")
        
        if len(username)< 4:
            raise ValueError("Username minimal 4 karakter")

        if not password.strip():
            raise ValueError("Password wajib diisi")
        
        if len(password)< 8:
            raise ValueError("Password minimal 8 karakter")

        if not email.strip():
            raise ValueError("Email wajib diisi")
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Format email tidak valid")
        
        try:
            return self.user_model.create_user(username, password, email)
        except Exception as e:
            if "duplicate key" in str(e):
                raise ValueError("Username atau Email sudah digunakan")
            else:
                raise

    def update_user(self, id_user, username, password, email):

        return self.user_model.update_user(
            id_user,
            username,
            password,
            email
        )

class LoginController:

    def __init__(self, user_model):
        self.user_model = user_model

    def login_user(self, username, password):

        if not username.strip():
            raise ValueError("Username wajib diisi")

        if not password.strip():
            raise ValueError("Password wajib diisi")

        user = self.user_model.get_user_by_username(username)

        if user is None:
            raise ValueError("Username tidak ditemukan")

        if user["password"] != password:
            raise ValueError("Password salah")

        return user


    def get_user(self, id_user):

        user = self.user_model.get_user_by_id(id_user)

        if user is None:
            raise ValueError("User tidak ditemukan")

        return user
