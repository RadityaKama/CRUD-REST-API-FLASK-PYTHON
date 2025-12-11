# CRUD REST API dengan Flask & Python

Proyek ini adalah implementasi **RESTful API** sederhana menggunakan bahasa pemrograman **Python** dan framework **Flask**. Aplikasi ini menangani operasi CRUD (Create, Read, Update, Delete) untuk manajemen **Produk** dan **Kategori** produk.

Proyek ini cocok sebagai referensi belajar untuk membangun backend services, memahami struktur MVC (Model-View-Controller) pada Flask, dan integrasi database menggunakan SQLAlchemy.

## 🛠️ Teknologi yang Digunakan

* **Python 3.x** - Bahasa pemrograman utama.
* **Flask** - Microframework web.
* **Flask-SQLAlchemy** - ORM untuk interaksi database.
* **Flask-Migrate** - (Opsional) Untuk migrasi database.
* **MySQL** - Sistem manajemen database (bisa disesuaikan di config).

## 📂 Struktur Proyek

```text
.
├── app/
│   ├── __init__.py          # Inisialisasi aplikasi & DB
│   ├── controller/          # Logika bisnis (CategoryController, ProductController)
│   ├── model/               # Model Database (Category, Product)
│   ├── response.py          # Helper untuk format respons JSON
│   └── routes.py            # Definisi URL Endpoint
├── config.py                # Konfigurasi Database
├── server.py (atau app.py)  # Entry point aplikasi
└── requirements.txt         # Daftar dependency
