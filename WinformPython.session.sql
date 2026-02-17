CREATE TABLE users (
    id_user SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE produk (
    id_produk SERIAL PRIMARY KEY,
    nama_produk VARCHAR(150) NOT NULL
);

ALTER TABLE users
ALTER COLUMN password TYPE VARCHAR(255);


INSERT INTO users (username, password, email, is_admin)
VALUES ('admin', 'admin123', '-', TRUE);


DROP TABLE "users";


SELECT * FROM users;