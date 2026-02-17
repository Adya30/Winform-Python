from database.connectdb import get_connection

class UserModel:

    def get_all_users(self):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            SELECT id_user, username, password, email, is_admin
            FROM users
            ORDER BY id_user ASC
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows

    def get_user_by_id(self, id_user):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            SELECT id_user, username, password, email, is_admin
            FROM users
            WHERE id_user = %s
        """

        cursor.execute(query, (id_user,))
        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if row:
            return {
                "id_user": row[0],
                "username": row[1],
                "password": row[2],
                "email": row[3],
                "is_admin": row[4]
            }

        return None

    def get_user_by_username(self, username):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            SELECT id_user, username, password, email, is_admin
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
                "email": row[3],
                "is_admin": row[4]
            }

        return None

    def create_user(self, username, password, email):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO users (username, password, email, is_admin)
            VALUES (%s, %s, %s, FALSE)
        """

        cursor.execute(query, (username, password, email))

        conn.commit()
        cursor.close()
        conn.close()

        return True

    def create_admin(self, username, password, email):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO users (username, password, email, is_admin)
            VALUES (%s, %s, %s, TRUE)
        """

        cursor.execute(query, (username, password, email))

        conn.commit()
        cursor.close()
        conn.close()

        return True

    def update_user(self, id_user, username, password, email, is_admin):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            UPDATE users
            SET username = %s,
                password = %s,
                email = %s,
                is_admin = %s
            WHERE id_user = %s
        """

        cursor.execute(
            query,
            (username, password, email, is_admin, id_user)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return True