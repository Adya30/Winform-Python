import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="Winform",
            user="postgres",
            password="12345"
        )
        print("Koneksi berhasil ke PostgreSQL")
        return conn

    except Exception as e:
        print("Koneksi gagal:", e)
        return None

if __name__ == "__main__":
    conn = get_connection()

    if conn:
        print("Koneksi sukses!")
        conn.close()
    else:
        print("Koneksi gagal!")
