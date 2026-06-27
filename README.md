🎓 Smart Attendance System

Sistem absensi mahasiswa berbasis **Face Recognition** menggunakan **Python, OpenCV, Flask, dan SQLite**.

Proyek ini dibuat sebagai tugas UAS mata kuliah **Pengolahan Citra Digital** sekaligus sebagai portofolio Computer Vision.

---

📌 Features

- 🔐 Login Admin
- 👨‍🎓 Registrasi Mahasiswa
- 📷 Pengambilan Dataset Wajah
- 🧠 Training Face Recognition
- 🎥 Absensi Real-Time Menggunakan Webcam
- 📊 Dashboard Statistik
- 📜 Riwayat Absensi
- 📥 Export Data ke Excel
- 💾 Database SQLite

---

🛠 Tech Stack

- Python 3.11
- Flask
- OpenCV
- Face Recognition
- SQLite
- Bootstrap 5
- HTML
- CSS
- JavaScript

---

📂 Project Structure

```
SmartAttendance/
│
├── app.py
├── requirements.txt
├── README.md
├── database.db
│
├── attendance/
│
├── dataset/
│
├── trainer/
│
├── static/
│   ├── css/
│   ├── js/
│   └── img/
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── register.html
│   ├── attendance.html
│   └── history.html
│
└── utils/
    ├── camera.py
    ├── recognizer.py
    └── trainer.py
```

---

🚀 Installation

Clone repository

```bash
git clone https://github.com/Ubben/Smart-Attendance-System.git
```

Masuk ke folder project

```bash
cd Smart-Attendance-System
```

Buat Virtual Environment

```bash
python -m venv venv
```

Aktifkan Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Jalankan aplikasi

```bash
python app.py
```

---

📸 Workflow

1. Login sebagai Admin
2. Registrasi Mahasiswa
3. Ambil Dataset Wajah
4. Training Model
5. Jalankan Face Recognition
6. Absensi Otomatis
7. Lihat Riwayat Absensi

---

📊 Database

### Admin

- id
- username
- password

### Mahasiswa

- id
- nim
- nama
- jurusan

### Absensi

- id
- mahasiswa
- tanggal
- jam
- status

---

🎯 Objectives

- Mengimplementasikan Face Recognition untuk sistem absensi.
- Menerapkan konsep Pengolahan Citra Digital.
- Mengintegrasikan Computer Vision dengan aplikasi web.
- Menyimpan data absensi secara otomatis.

---

👨‍💻 Author

**Ubben**

GitHub: https://github.com/Ubben
