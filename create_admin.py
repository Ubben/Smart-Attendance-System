import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
INSERT INTO admin(username,password)
VALUES (?,?)
""",(
    "admin",
    generate_password_hash("admin123")
))

conn.commit()

conn.close()

print("Admin berhasil dibuat")