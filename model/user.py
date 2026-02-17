from database.connectdb import get_connection

class UserModel:

    def get_all_users(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                SELECT id_user, username, password, email
                FROM users
                ORDER BY id_user ASC
            """

            cursor.execute(query)
            rows = cursor.fetchall()

            cursor.close()
            conn.close()

            return rows

        except Exception as e:
            print("Error get_all_users:", e)
            return []

    def get_user_by_id(self, id_user):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                SELECT id_user, username, password, email
                FROM users
                WHERE id_user = %s
            """

            cursor.execute(query, (id_user,))
            row = cursor.fetchone()

            cursor.close()
            conn.close()

            return row

        except Exception as e:
            print("Error get_user_by_id:", e)
            return None

    def get_user_by_username(self, username):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                SELECT id_user, username, password, email
                FROM users
                WHERE username = %s
            """

            cursor.execute(query, (username,))
            row = cursor.fetchone()

            cursor.close()
            conn.close()

            if row:
                return {
                    "id_user": row[0],
                    "username": row[1],
                    "password": row[2],
                    "email": row[3]
                }

            return None

        except Exception as e:
            print("Error:", e)
            return None


    def create_user(self, username, password, email):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO users (username, password, email)
                VALUES (%s, %s, %s)
            """

            cursor.execute(query, (username, password, email))
            conn.commit()

            cursor.close()
            conn.close()

            return True

        except Exception as e:
            print("Error create_user:", e)
            return False

    def update_user(self, id_user, username, password, email):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                UPDATE users
                SET username = %s,
                    password = %s,
                    email = %s
                WHERE id_user = %s
            """

            cursor.execute(query, (username, password, email, id_user))
            conn.commit()

            cursor.close()
            conn.close()

            return True

        except Exception as e:
            print("Error update_user:", e)
            return False
