# CRUD REST API dengan Flask & Python

Proyek ini adalah implementasi **RESTful API** sederhana menggunakan bahasa pemrograman **Python** dan framework **Flask**. Aplikasi ini menangani operasi CRUD (Create, Read, Update, Delete) untuk manajemen **Produk** dan **Kategori** produk.

Proyek ini cocok sebagai referensi belajar untuk membangun backend services, memahami struktur MVC (Model-View-Controller) pada Flask, dan integrasi database menggunakan SQLAlchemy.

## Teknologi yang Digunakan

* **Python 3.x** - Bahasa pemrograman utama.
* **Flask** - Microframework web.
* **Flask-SQLAlchemy** - ORM untuk interaksi database.
* **Flask-Migrate** - (Opsional) Untuk migrasi database.
* **MySQL** - Sistem manajemen database (bisa disesuaikan di config).

## Struktur Proyek

```
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
```

## Cara Instalasi dan Menjalankan

Ikuti langkah-langkah berikut untuk menjalankan proyek ini di lokal komputer Anda:

### 1. Clone Repositori
```bash
git clone [https://github.com/RadityaKama/CRUD-REST-API-FLASK-PYTHON.git](https://github.com/RadityaKama/CRUD-REST-API-FLASK-PYTHON.git)
cd CRUD-REST-API-FLASK-PYTHON
```

### 2. Buat Virtual Environment
Disarankan menggunakan virtual environment agar *package* tidak bercampur.
```bash
# Untuk Windows
python -m venv venv
venv\Scripts\activate

# Untuk Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
*Jika file `requirements.txt` belum ada, pastikan Anda menginstall: `flask`, `flask-sqlalchemy`, `mysqlclient` (atau driver mysql lainnya).*

### 4. Konfigurasi Database
1. Buat database baru di MySQL (misal: `flask_crud`).
2. Sesuaikan file `config.py` (atau bagian config di `__init__.py`) dengan kredensial database Anda.

### 5. Jalankan Aplikasi
```bash
flask run
# atau
python server.py
```
Aplikasi akan berjalan di `http://localhost:5000`.

## Dokumentasi API

Berikut adalah daftar *endpoint* yang tersedia dalam aplikasi ini. Gunakan aplikasi seperti **Postman** untuk melakukan pengujian.

### Categories (Kategori)

| Method | Endpoint | Deskripsi |
| :--- | :--- | :--- |
| `GET` | `/categories` | Menampilkan semua kategori |
| `POST` | `/categories` | Menambahkan kategori baru |
| `GET` | `/categories/<id>` | Menampilkan detail kategori berdasarkan ID |
| `PUT` | `/categories/<id>` | Mengupdate data kategori berdasarkan ID |
| `DELETE` | `/categories/<id>` | Menghapus kategori berdasarkan ID |

**Contoh JSON Request (POST/PUT Category):**
```json
{
    "name": "Elektronik"
}
```

---

### Products (Produk)

| Method | Endpoint | Deskripsi |
| :--- | :--- | :--- |
| `GET` | `/products` | Menampilkan semua produk |
| `POST` | `/products` | Menambahkan produk baru |
| `GET` | `/products/<id>` | Menampilkan detail produk berdasarkan ID |
| `PUT` | `/products/<id>` | Mengupdate data produk berdasarkan ID |
| `DELETE` | `/products/<id>` | Menghapus produk berdasarkan ID |

**Contoh JSON Request (POST/PUT Product):**
```json
{
    "name": "Laptop Gaming",
    "harga": 15000000,
    "description": "Laptop spesifikasi tinggi untuk gaming dan editing",
    "category_id": 1
}
```

## Kontribusi

Kontribusi selalu diterima! Jika Anda ingin menambahkan fitur atau memperbaiki bug:
1. Fork repositori ini.
2. Buat branch fitur baru (`git checkout -b fitur-baru`).
3. Commit perubahan Anda (`git commit -m 'Menambahkan fitur baru'`).
4. Push ke branch (`git push origin fitur-baru`).
5. Buat Pull Request.
