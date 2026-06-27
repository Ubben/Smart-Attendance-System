import sqlite3
from config import Config


def get_connection():
    conn = sqlite3.connect(Config.DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # ==========================
    # Tabel Admin
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # ==========================
    # Tabel Mahasiswa
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mahasiswa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nim TEXT UNIQUE NOT NULL,
        nama TEXT NOT NULL,
        jurusan TEXT NOT NULL
    )
    """)

    # ==========================
    # Tabel Absensi
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS absensi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mahasiswa_id INTEGER,
        tanggal TEXT,
        jam TEXT,
        status TEXT,
        FOREIGN KEY(mahasiswa_id) REFERENCES mahasiswa(id)
    )
    """)

    conn.commit()
    conn.close()