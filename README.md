CRUD REST API dengan Flask & PythonProyek ini adalah implementasi RESTful API sederhana menggunakan bahasa pemrograman Python dan framework Flask. Aplikasi ini menangani operasi CRUD (Create, Read, Update, Delete) untuk manajemen Produk dan Kategori produk.Proyek ini cocok sebagai referensi belajar untuk membangun backend services, memahami struktur MVC (Model-View-Controller) pada Flask, dan integrasi database menggunakan SQLAlchemy.Teknologi yang DigunakanPython 3.x - Bahasa pemrograman utama.Flask - Microframework web.Flask-SQLAlchemy - ORM untuk interaksi database.Flask-Migrate - (Opsional) Untuk migrasi database.MySQL - Sistem manajemen database (bisa disesuaikan di config).Struktur Proyek.
├── app/
│   ├── __init__.py          # Inisialisasi aplikasi & DB
│   ├── controller/          # Logika bisnis (CategoryController, ProductController)
│   ├── model/               # Model Database (Category, Product)
│   ├── response.py          # Helper untuk format respons JSON
│   └── routes.py            # Definisi URL Endpoint
├── config.py                # Konfigurasi Database
├── server.py (atau app.py)  # Entry point aplikasi
└── requirements.txt         # Daftar dependency
Cara Instalasi dan MenjalankanIkuti langkah-langkah berikut untuk menjalankan proyek ini di lokal komputer Anda:1. Clone RepositoriBashgit clone https://github.com/RadityaKama/CRUD-REST-API-FLASK-PYTHON.git
cd CRUD-REST-API-FLASK-PYTHON
2. Buat Virtual EnvironmentDisarankan menggunakan virtual environment agar package tidak bercampur.Bash# Untuk Windows
python -m venv venv
venv\Scripts\activate

# Untuk Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. Install DependenciesBashpip install -r requirements.txt
Jika file requirements.txt belum ada, pastikan Anda menginstall: flask, flask-sqlalchemy, mysqlclient (atau driver mysql lainnya).4. Konfigurasi DatabaseBuat database baru di MySQL (misal: flask_crud).Sesuaikan file config.py (atau bagian config di __init__.py) dengan kredensial database Anda.5. Jalankan AplikasiBashflask run
# atau
python server.py
Aplikasi akan berjalan di http://localhost:5000.Dokumentasi APIBerikut adalah daftar endpoint yang tersedia dalam aplikasi ini. Gunakan aplikasi seperti Postman untuk melakukan pengujian.Categories (Kategori)MethodEndpointDeskripsiGET/categoriesMenampilkan semua kategoriPOST/categoriesMenambahkan kategori baruGET/categories/<id>Menampilkan detail kategori berdasarkan IDPUT/categories/<id>Mengupdate data kategori berdasarkan IDDELETE/categories/<id>Menghapus kategori berdasarkan IDContoh JSON Request (POST/PUT Category):JSON{
    "name": "Elektronik"
}
Products (Produk)MethodEndpointDeskripsiGET/productsMenampilkan semua produkPOST/productsMenambahkan produk baruGET/products/<id>Menampilkan detail produk berdasarkan IDPUT/products/<id>Mengupdate data produk berdasarkan IDDELETE/products/<id>Menghapus produk berdasarkan IDContoh JSON Request (POST/PUT Product):JSON{
    "name": "Laptop Gaming",
    "harga": 15000000,
    "description": "Laptop spesifikasi tinggi untuk gaming dan editing",
    "category_id": 1
}
KontribusiKontribusi selalu diterima! Jika Anda ingin menambahkan fitur atau memperbaiki bug:Fork repositori ini.Buat branch fitur baru (git checkout -b fitur-baru).Commit perubahan Anda (git commit -m 'Menambahkan fitur baru').Push ke branch (git push origin fitur-baru).Buat Pull Request.
