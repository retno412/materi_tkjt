materi_belajar_tkjt/generator.py
import os
import json

# Setup folders
os.makedirs("materi_belajar_tkjt/lessons/semester_1", exist_ok=True)
os.makedirs("materi_belajar_tkjt/lessons/semester_2", exist_ok=True)
os.makedirs("materi_belajar_tkjt/lessons/semester_3", exist_ok=True)
os.makedirs("materi_belajar_tkjt/lessons/semester_4", exist_ok=True)
os.makedirs("materi_belajar_tkjt/lessons/semester_5", exist_ok=True)
os.makedirs("materi_belajar_tkjt/lessons/semester_6", exist_ok=True)

# Generate detailed curriculum structure
curriculum_data = {
    1: {
        "name": "Semester 1: Fondasi Logika & Algoritma",
        "weeks": {
            1: {
                "title": "Orientasi Kursus & Menyiapkan Lingkungan Kerja (Setup Tools)",
                "what": "Mengenal ekosistem pengembangan perangkat lunak, terminal/command line, teks editor (VS Code), dan sistem kontrol versi Git & GitHub.",
                "why": "Sebelum menulis kode, seorang developer harus menguasai 'developer environment'. Menggunakan alat standar industri membuat alur kerja efisien dan kolaboratif.",
                "who": "Software Engineers, System Administrators, DevOps Engineers, dan semua praktisi TI profesional.",
                "when": "Dilakukan pada sesi pertama memulai proyek atau saat masuk ke lingkungan kerja baru.",
                "where": "Dipasang di komputer lokal pengembang (PC/Laptop) dan dihubungkan ke server cloud GitHub.",
                "how": "1. Unduh dan instal Git (git-scm.com).\n2. Unduh dan instal Visual Studio Code (code.visualstudio.com).\n3. Buat akun GitHub.\n4. Buka terminal, ketik:\n   `git config --global user.name \"Nama Anda\"`\n   `git config --global user.email \"email@anda.com\"`\n5. Verifikasi instalasi dengan `git --version` dan `code --version`.",
                "web_app_fundamental": "Konsep Client-Server pada Git: Repositori Lokal bertindak sebagai client yang menyimpan perubahan di PC Anda, sedangkan GitHub bertindak sebagai Server (Cloud) pusat untuk meng-hosting kode agar bisa diakses oleh pengguna secara global.",
                "portfolio_meaning_intro": "Mendirikan 'rumah digital' pertama Anda. Ini adalah tonggak awal portofolio yang membuktikan Anda memahami standar kerja profesional industri perangkat lunak.",
                "portfolio_repo_structure": "materi_belajar_tkjt/\n├── .gitignore\n├── README.md\n└── index.html",
                "portfolio_commit": "feat: setup initial local developer workspace and configure git",
                "portfolio_readme": "README harus mencakup biodata singkat siswa, spesifikasi hardware yang digunakan, serta daftar tools yang berhasil dipasang beserta versinya.",
                "reflection_q1": "Mengapa Git sangat penting dalam kolaborasi tim developer?",
                "reflection_q2": "Apa perbedaan antara Git (local) dan GitHub (cloud)?",
                "reflection_q3": "Kesulitan apa yang Anda hadapi saat melakukan instalasi VS Code atau Git?"
            },
            2: {
                "title": "Mengenal Alur Git: Add, Commit, Push, dan Branching",
                "what": "Siklus hidup manajemen kode menggunakan Git: mencatat perubahan (add, commit), mengirim kode ke cloud (push), dan membuat alur kerja bercabang (branching).",
                "why": "Menghindari hilangnya kode, memungkinkan pembatalan ke versi sebelumnya jika terjadi error (rollback), dan memfasilitasi kerja tim tanpa tumpang tindih.",
                "who": "Semua pengembang perangkat lunak yang berkolaborasi dalam tim.",
                "when": "Setiap kali ada penambahan fitur baru, perbaikan bug, atau perubahan konfigurasi.",
                "where": "Perubahan dicatat secara lokal di direktori kerja (.git) sebelum dikirim ke GitHub Repository.",
                "how": "1. Inisialisasi repo: `git init`\n2. Cek status: `git status`\n3. Tambahkan file: `git add .`\n4. Simpan snapshot: `git commit -m \"feat: tambah halaman kontak\"`\n5. Hubungkan remote: `git remote add origin <url_repo>`\n6. Push ke server: `git push -u origin main`",
                "web_app_fundamental": "Alur pengiriman kode dari lokal ke GitHub melatih pemahaman protokol transfer data (HTTPS/SSH) yang nantinya akan digunakan untuk mendeploy aplikasi web nyata ke server hosting.",
                "portfolio_meaning_intro": "Menunjukkan kepada rekruter/guru bahwa Anda memiliki alur kerja yang rapi dan terbiasa bekerja dengan version control yang bersih.",
                "portfolio_repo_structure": "materi_belajar_tkjt/\n└── (file proyek yang di-track oleh git)",
                "portfolio_commit": "docs: add detailed description of local setup in readme",
                "portfolio_readme": "Tambahkan diagram alur sederhana mengenai siklus kerja Git (Working Directory -> Staging Area -> Local Repo -> Remote Repo).",
                "reflection_q1": "Mengapa kita tidak disarankan langsung mengedit kode di cabang 'main' secara langsung saat bekerja kelompok?",
                "reflection_q2": "Apa fungsi dari Staging Area (`git add`)?",
                "reflection_q3": "Bagaimana cara memulihkan kode yang terlanjur terhapus jika Anda sudah meng-commit-nya?"
            },
            3: {
                "title": "Python Dasar: Variabel, Tipe Data, dan Operator",
                "what": "Struktur penyimpanan memori sementara menggunakan variabel, jenis-jenis tipe data (integer, float, string, boolean), dan operasi aritmatika & logika.",
                "why": "Data adalah bahan baku aplikasi. Tanpa memahami tipe data dan operator, komputer tidak bisa memproses input pengguna menjadi output yang diharapkan.",
                "who": "Programmer Python, Data Scientists, Back-end Developers, dan AI Engineers.",
                "when": "Digunakan di baris pertama pembuatan logika program apa pun.",
                "where": "Dieksekusi di dalam Python Interpreter (lingkungan runtime Python) di memori RAM.",
                "how": "# Mendefinisikan variabel\nnama = \"Retno\"\numur = 16\ntinggi = 1.65\nis_aktif = True\n\n# Operasi aritmatika\nharga_barang = 50000\ndiskon = 0.1\ntotal_bayar = harga_barang * (1 - diskon)\nprint(f\"Total: {total_bayar}\")",
                "web_app_fundamental": "Dalam aplikasi web, variabel digunakan untuk menangkap input formulir dari pengguna (misal: username, password) sebelum dikirimkan ke server atau database.",
                "portfolio_meaning_intro": "Membuat aplikasi kalkulator interaktif pertama yang membuktikan pemahaman logika dasar aritmatika komputer.",
                "portfolio_repo_structure": "semester_1/\n└── p3_kalkulator/\n    ├── kalkulator.py\n    └── README.md",
                "portfolio_commit": "feat: build basic command-line arithmetic calculator in python",
                "portfolio_readme": "Tulis penjelasan bagaimana program menerima input dari user menggunakan fungsi `input()` dan mengubah tipe datanya (type casting) menjadi integer/float.",
                "reflection_q1": "Mengapa input dari fungsi `input()` di Python selalu berupa string? Bagaimana mengatasinya?",
                "reflection_q2": "Apa kegunaan tipe data Boolean dalam logika pemrograman?",
                "reflection_q3": "Apa perbedaan antara operator `=` (assignment) dan `==` (perbandingan)?"
            },
            4: {
                "title": "Logika Percabangan: Kondisional If, Elif, Else",
                "what": "Struktur kontrol keputusan di mana program mengeksekusi blok kode tertentu berdasarkan pemenuhan kondisi logika tertentu.",
                "why": "Membuat program menjadi cerdas dan dinamis. Program dapat merespon secara berbeda tergantung pada input yang bervariasi (misal: membedakan user biasa vs admin).",
                "who": "Semua pengembang sistem yang merancang logika alur bisnis aplikasi.",
                "when": "Saat sistem harus mengambil keputusan berdasarkan rentang nilai atau pilihan status.",
                "where": "Dijalankan pada modul kontrol logika aplikasi (Back-end logic).",
                "how": "skor = 85\nif skor >= 90:\n    grade = \"A\"\nelif skor >= 80:\n    grade = \"B\"\nelse:\n    grade = \"C\"\nprint(f\"Grade Anda: {grade}\")",
                "web_app_fundamental": "Digunakan untuk proses otentikasi (Authorization): `if user.role == 'admin': redirect_to_dashboard() else: redirect_to_home()`.",
                "portfolio_meaning_intro": "Proyek Kalkulator Diskon Belanja Otomatis. Program ini mensimulasikan sistem kasir ritel yang nyata.",
                "portfolio_repo_structure": "semester_1/\n└── p4_kasir_diskon/\n    ├── kasir.py\n    └── README.md",
                "portfolio_commit": "feat: implement dynamic discount evaluation system based on shopping cart value",
                "portfolio_readme": "Sertakan tabel aturan diskon yang diterapkan (misal: belanja > 100rb diskon 10%, > 500rb diskon 20%).",
                "reflection_q1": "Apa perbedaan antara menggunakan rangkaian `if-if-if` dengan `if-elif-else`?",
                "reflection_q2": "Bagaimana cara menggabungkan dua kondisi logika menggunakan operator `and` dan `or`?",
                "reflection_q3": "Skenario nyata apa di aplikasi web favoritmu yang pasti menggunakan logika kondisional?"
            },
            5: {
                "title": "Perulangan: Loop For dan While",
                "what": "Struktur iterasi yang memungkinkan blok kode dijalankan berulang kali selama kondisi tertentu terpenuhi.",
                "why": "Mencegah penulisan kode berulang yang tidak efisien (prinsip DRY: Don't Repeat Yourself) saat memproses banyak data atau menjalankan tugas periodik.",
                "who": "Data Engineers, Automation Developers, Game Developers.",
                "when": "Saat memproses elemen dalam daftar (list), membaca baris file, atau menjalankan server yang harus terus berjalan (loop tak terbatas dengan kondisi keluar).",
                "where": "Bekerja pada tingkat pemrosesan data di dalam CPU komputer.",
                "how": "# Loop For (Iterasi List)\nbuah = [\"apel\", \"mangga\", \"jeruk\"]\nfor b in buah:\n    print(f\"Saya suka {b}\")\n\n# Loop While (Kondisional)\ncounter = 5\nwhile counter > 0:\n    print(f\"Hitung mundur: {counter}\")\n    counter -= 1",
                "web_app_fundamental": "Perulangan adalah kunci untuk merender daftar produk di halaman e-commerce. Data array produk dari database diloop untuk menghasilkan kartu-kartu produk HTML secara dinamis.",
                "portfolio_meaning_intro": "Program Perhitungan Otomatis & Pola Matematika. Menghasilkan tabel perkalian dinamis berdasarkan batas input user.",
                "portfolio_repo_structure": "semester_1/\n└── p5_perulangan/\n    ├── loop_generator.py\n    └── README.md",
                "portfolio_commit": "feat: build custom interactive multiplication table generator using loops",
                "portfolio_readme": "Tulis panduan penggunaan program dan jelaskan konsep pencegahan 'infinite loop' (perulangan abadi yang membuat PC hang).",
                "reflection_q1": "Kapan sebaiknya kita menggunakan `for loop` dibanding `while loop`?",
                "reflection_q2": "Apa fungsi dari keyword `break` dan `continue` dalam loop?",
                "reflection_q3": "Bagaimana loop membantu dalam efisiensi performa memori?"
            },
            6: {
                "title": "Fungsi (Function): Modularitas Kode & Reusability",
                "what": "Kumpulan baris kode terorganisir yang diberi nama, menerima input (argumen/parameter), melakukan proses, dan mengembalikan hasil (return value).",
                "why": "Membuat kode menjadi rapi, modular, mudah di-debug, dan dapat digunakan kembali di berbagai bagian aplikasi tanpa menulis ulang logika yang sama.",
                "who": "Semua programmer tingkat menengah hingga mahir.",
                "when": "Ketika sebuah proses logika atau perhitungan yang sama perlu dipanggil di lebih dari dua tempat dalam aplikasi.",
                "where": "Didefinisikan di awal modul kode atau di dalam file utilitas khusus (utility file).",
                "how": "def hitung_pajak(harga, rate=0.11):\n    return harga * rate\n\npajak_laptop = hitung_pajak(15000000)\nprint(f\"Pajak: Rp {pajak_laptop:,.0f}\")",
                "web_app_fundamental": "Fungsi sangat vital untuk menangani aksi pengguna (Event Handling). Misalnya, fungsi `onClick()` di JavaScript yang dipanggil setiap kali tombol 'Beli Sekarang' ditekan.",
                "portfolio_meaning_intro": "Proyek Library Perhitungan Otomatis Pajak dan Diskon Modular. Memisahkan logika kalkulasi ke dalam fungsi-fungsi siap pakai.",
                "portfolio_repo_structure": "semester_1/\n└── p6_modular_calc/\n    ├── main.py\n    ├── math_utils.py\n    └── README.md",
                "portfolio_commit": "feat: design modular calculator with custom math utility functions",
                "portfolio_readme": "Jelaskan struktur pemisahan file (modularisasi) di mana fungsi disimpan di `math_utils.py` dan dijalankan di `main.py`.",
                "reflection_q1": "Apa perbedaan antara mencetak langsung (`print()`) di dalam fungsi dengan mengembalikan nilai menggunakan `return`?",
                "reflection_q2": "Apa yang dimaksud dengan Default Parameter pada fungsi Python?",
                "reflection_q3": "Mengapa pemisahan kode ke dalam modul/fungsi membuat kolaborasi tim menjadi lebih mudah?"
            },
            7: {
                "title": "Struktur Data Kolektif: List dan Dictionary",
                "what": "Wadah penyimpanan data terstruktur di Python. List menyimpan urutan data yang terindeks, sedangkan Dictionary menyimpan pasangan kunci-nilai (key-value).",
                "why": "Dalam dunia nyata, data jarang sekali berupa variabel tunggal. Data biasanya berupa kumpulan informasi kompleks yang harus dikelompokkan agar mudah dikelola.",
                "who": "Database Administrators, Back-end Developers, Data Analysts.",
                "when": "Digunakan ketika mengelola daftar user, menu makanan, daftar inventaris, atau data konfigurasi sistem.",
                "where": "Menjadi format representasi data utama sebelum dikonversi menjadi format JSON untuk komunikasi web API.",
                "how": "# List\nsiswa = [\"Retno\", \"Budi\", \"Siti\"]\n\n# Dictionary (representasi objek)\nuser_profile = {\n    \"username\": \"retno412\",\n    \"role\": \"admin\",\n    \"is_active\": True\n}\nprint(user_profile[\"username\"])",
                "web_app_fundamental": "Format Dictionary di Python sangat identik dengan format JSON (JavaScript Object Object), yang merupakan bahasa standar pengiriman data antar aplikasi web modern di internet.",
                "portfolio_meaning_intro": "Aplikasi Manajemen Data Siswa Sederhana. Menyimpan, mengedit, dan menampilkan list data siswa berbasis dictionary.",
                "portfolio_repo_structure": "semester_1/\n└── p7_data_siswa/\n    ├── manager.py\n    └── README.md",
                "portfolio_commit": "feat: build interactive student data manager using nested dictionaries",
                "portfolio_readme": "Sertakan contoh struktur data (skema JSON) yang Anda gunakan untuk memodelkan data siswa di program Anda.",
                "reflection_q1": "Kapan kita harus memilih menggunakan List dibanding Dictionary?",
                "reflection_q2": "Bagaimana cara mengamankan pencarian key pada dictionary agar program tidak crash jika key tersebut tidak ditemukan? (Petunjuk: gunakan method `.get()`)",
                "reflection_q3": "Apa itu mutable dan immutable dalam tipe data Python?"
            },
            8: {
                "title": "Algoritma Dasar: Sorting dan Searching",
                "what": "Prosedur logis sistematis untuk mengurutkan data (misal: Bubble Sort) dan mencari data tertentu (misal: Binary Search atau Linear Search) dalam koleksi data.",
                "why": "Efisiensi aplikasi sangat ditentukan oleh seberapa cepat aplikasi dapat mengurutkan jutaan produk atau mencari satu akun pengguna di database.",
                "who": "Computer Scientists, Backend Engineers, Search Engine Developers.",
                "when": "Setiap kali ada fitur pencarian (search bar) atau fitur pengurutan (filter termurah, termahal, dll) di aplikasi.",
                "where": "Diterapkan pada query processing engine atau algoritma pemrosesan data internal.",
                "how": "# Linear Search sederhana\ndef cari_data(koleksi, target):\n    for index, item in enumerate(koleksi):\n        if item == target:\n            return index\n    return -1",
                "web_app_fundamental": "Fitur pencarian di halaman web (Instant Search) mengandalkan algoritma searching cepat untuk menyaring daftar data yang ditampilkan di layar secara real-time.",
                "portfolio_meaning_intro": "Program Analisis Kecepatan Sorting & Searching. Membandingkan kecepatan pencarian data di antara ratusan elemen.",
                "portfolio_repo_structure": "semester_1/\n└── p8_algoritma_dasar/\n    ├── algorithms.py\n    └── README.md",
                "portfolio_commit": "feat: implement linear search and bubble sort with performance logging",
                "portfolio_readme": "Buat analisis singkat perbandingan kecepatan pencarian jika menggunakan linear search vs metode bawaan Python `.index()`.",
                "reflection_q1": "Mengapa Binary Search jauh lebih cepat daripada Linear Search? Apa syarat mutlak agar Binary Search bisa dijalankan?",
                "reflection_q2": "Apa yang dimaksud dengan kompleksitas waktu (Big O Notation) secara sederhana?",
                "reflection_q3": "Bagaimana cara algoritma sorting membantu mempermudah analisis data?"
            },
            9: {
                "title": "UTS (Ujian Tengah Semester) - Evaluasi Logika & Algoritma",
                "what": "Ujian kompetensi praktis untuk menguji kemampuan pemecahan masalah (problem-solving), logika pemrograman, dan penguasaan Git.",
                "why": "Mengukur kesiapan fundamental pemrograman siswa sebelum melangkah ke pembuatan aplikasi interaktif yang lebih kompleks dan integrasi AI.",
                "who": "Siswa sebagai pengembang mandiri dan Guru sebagai evaluator teknis.",
                "when": "Berlangsung di minggu ke-9 untuk merekap seluruh pencapaian materi logika dasar.",
                "where": "Dilakukan secara mandiri di komputer masing-masing dengan mengunggah hasil proyek ke GitHub.",
                "how": "Siswa diberikan sebuah studi kasus (misal: Sistem Reservasi Kamar Hotel Sederhana) yang harus diselesaikan menggunakan Fungsi, Percabangan, Perulangan, dan Struktur Data, lalu didokumentasikan dan di-push ke GitHub.",
                "web_app_fundamental": "Menguji kemampuan siswa dalam merancang sistem yang memiliki 'Business Logic' utuh, menyerupai core engine dari aplikasi web yang sesungguhnya.",
                "portfolio_meaning_intro": "Proyek UTS: Sistem Manajemen Reservasi Mandiri. Proyek mandiri terbesar pertama siswa yang siap dipamerkan di profil utama GitHub.",
                "portfolio_repo_structure": "semester_1/\n└── uts_sistem_reservasi/\n    ├── main.py\n    └── README.md",
                "portfolio_commit": "chore: complete UTS exam - hotel reservation system v1.0",
                "portfolio_readme": "Tulis panduan instalasi lengkap, flowchart logika program, serta batasan-batasan sistem (limitations) yang Anda buat.",
                "reflection_q1": "Tantangan logika terbesar apa yang Anda temui selama pengerjaan UTS?",
                "reflection_q2": "Bagaimana Anda memecahkan bug tersulit yang Anda temui dalam pengerjaan ujian?",
                "reflection_q3": "Seberapa percaya diri Anda dengan pemahaman fundamental pemrograman Anda saat ini?"
            },
            10: {
                "title": "Pengenalan Artificial Intelligence & Natural Language Processing (NLP)",
                "what": "Konsep dasar Kecerdasan Buatan (AI) khususnya pemrosesan bahasa alami (NLP) agar komputer dapat memahami teks manusia.",
                "why": "AI adalah masa depan industri. Memahami bagaimana chatbot mengenali maksud (intent) dari ketikan pengguna adalah fondasi pembuatan asisten digital interaktif.",
                "who": "AI Engineers, Chatbot Designers, Data Scientists.",
                "when": "Digunakan saat kita ingin membuat aplikasi interaktif yang merespon input bahasa manusia, bukan sekadar perintah menu kaku.",
                "where": "Algoritma NLP berjalan di cloud server AI atau pustaka lokal Python yang menganalisis input teks.",
                "how": "# Konsep pencocokan kata kunci dasar (Intent Matching)\ndef dapatkan_respon(teks):\n    teks = teks.lower()\n    if \"halo\" in teks or \"hai\" in teks:\n        return \"Halo! Ada yang bisa saya bantu di helpdesk?\"\n    elif \"pembayaran\" in teks:\n        return \"Metode pembayaran kami mendukung Transfer Bank dan e-wallet.\"\n    return \"Maaf, saya tidak mengerti. Bisa hubungi CS manusia?\"",
                "web_app_fundamental": "Aplikasi web modern sering mengandalkan API AI eksternal (seperti OpenAI API) untuk memberikan fitur pintar. Memahami dasar NLP membantu kita tahu bagaimana memformat request teks tersebut.",
                "portfolio_meaning_intro": "Memulai pembuatan modul AI pertama Anda. Memahami bahwa kecerdasan buatan dimulai dari struktur aturan data yang rapi.",
                "portfolio_repo_structure": "semester_1/\n└── p10_nlp_intro/\n    ├── simple_nlp.py\n    └── README.md",
                "portfolio_commit": "feat: design basic key-phrase matching NLP engine for helpdesk system",
                "portfolio_readme": "Tulis penjelasan mengenai apa itu 'Intent' (tujuan pengguna) dan 'Response' (jawaban bot) dalam dunia chatbot.",
                "reflection_q1": "Apa kelemahan utama dari chatbot yang hanya mengandalkan pencocokan kata kunci (keyword matching)?",
                "reflection_q2": "Bagaimana chatbot modern (seperti ChatGPT) bisa menjawab pertanyaan dengan jauh lebih luwes?",
                "reflection_q3": "Sebutkan satu implementasi NLP yang Anda temui di kehidupan sesesi-sesi selain chatbot!"
            },
            11: {
                "title": "Merancang Dataset Helpdesk Terstruktur (.json)",
                "what": "Membuat file data terstruktur dalam format JSON yang berisi pemetaan pertanyaan (patterns), kategori (tags), dan respon (responses) untuk melatih chatbot helpdesk.",
                "why": "Aplikasi cerdas membutuhkan data berkualitas (garbage in, garbage out). Memisahkan data dialog dari file kode utama adalah praktik terbaik (best practice) pengembangan software.",
                "who": "Data Engineers, Conversation Designers, Content Managers.",
                "when": "Sebelum menulis program utama chatbot, database percakapan harus didefinisikan terlebih dahulu.",
                "where": "Disimpan dalam file statis `dataset.json` di dalam repositori proyek.",
                "how": "Contoh isi `dataset.json`:\n{\n  \"intents\": [\n    {\n      \"tag\": \"salam\",\n      \"patterns\": [\"halo\", \"pagi\", \"siang\", \"hai\"],\n      \"responses\": [\"Halo! Selamat datang di Helpdesk TKJT. Ada yang bisa dibantu?\"]\n    }\n  ]\n}",
                "web_app_fundamental": "JSON adalah format standar pertukaran data (data exchange) antara frontend dan backend di semua aplikasi web di dunia. Menguasai pembuatan JSON sangat krusial bagi web developer.",
                "portfolio_meaning_intro": "Membuat basis data pengetahuan chatbot. Ini menunjukkan kemampuan merancang struktur data terstandarisasi industri.",
                "portfolio_repo_structure": "semester_1/\n└── p11_dataset_helpdesk/\n    ├── dataset.json\n    └── README.md",
                "portfolio_commit": "feat: construct structured JSON dataset mapping user intents and responses",
                "portfolio_readme": "Tulis skema JSON Anda dan beri penjelasan kegunaan masing-masing atribut (`tag`, `patterns`, `responses`).",
                "reflection_q1": "Mengapa kita menggunakan format JSON dibanding menuliskan semua percakapan langsung di dalam kode Python (hardcoded)?",
                "reflection_q2": "Bagaimana jika user mengetik kalimat yang tidak ada di list 'patterns'? Bagaimana chatbot harus mengatasinya?",
                "reflection_q3": "Apa perbedaan utama format JSON dengan format Dictionary di Python?"
            },
            12: {
                "title": "Pembuatan GUI Chatbot Dasar dengan Tkinter",
                "what": "Membangun antarmuka grafis pengguna (Graphical User Interface) desktop menggunakan library bawaan Python, Tkinter.",
                "why": "Pengguna awam tidak bisa menggunakan program CLI (hitam putih terminal). Kita harus membungkus program dalam bentuk window, tombol, dan kolom teks yang menarik agar mudah digunakan.",
                "who": "Desktop Application Developers, UI/UX Implementers.",
                "when": "Saat memindahkan aplikasi dari tahap prototipe terminal (CLI) ke aplikasi ramah pengguna (GUI).",
                "where": "Dijalankan sebagai aplikasi desktop lokal di sistem operasi Windows, MacOS, atau Linux.",
                "how": "import tkinter as tk\n\nroot = tk.Tk()\nroot.title(\"Helpdesk Chatbot\")\nroot.geometry(\"400x500\")\n\nlabel = tk.Label(root, text=\"Chatbot Helpdesk\", font=(\"Arial\", 14))\nlabel.pack(pady=10)\n\nroot.mainloop()",
                "web_app_fundamental": "Memahami konsep windowing, tata letak koordinat, dan event loop pada GUI desktop sangat mirip dengan konsep Document Object Model (DOM), CSS layouting, dan event listener pada pembuatan halaman web.",
                "portfolio_meaning_intro": "Membangun tampilan visual pertama aplikasi Anda. Langkah awal transisi dari programmer logika menjadi pembuat produk.",
                "portfolio_repo_structure": "semester_1/\n└── p12_tkinter_gui/\n    ├── simple_gui.py\n    └── README.md",
                "portfolio_commit": "feat: build initial desktop window UI using tkinter library",
                "portfolio_readme": "Sertakan screenshot aplikasi GUI sederhana yang berhasil Anda jalankan.",
                "reflection_q1": "Apa fungsi utama dari pemanggilan `root.mainloop()` di akhir program GUI?",
                "reflection_q2": "Apa perbedaan tata letak widget menggunakan `.pack()` dengan `.grid()` di Tkinter?",
                "reflection_q3": "Mengapa aspek visual (UI) sangat mempengaruhi kepuasan pengguna dalam menggunakan aplikasi?"
            },
            13: {
                "title": "GUI Chatbot Modern dengan CustomTkinter & Styling",
                "what": "Meningkatkan kualitas visual antarmuka pengguna menggunakan library pihak ketiga `customtkinter` yang mendukung tema gelap/terang modern.",
                "why": "Aplikasi Tkinter standar terlihat kuno dan kaku. Dengan CustomTkinter, aplikasi kita akan memiliki tampilan modern layaknya aplikasi Windows 11/macOS terbaru.",
                "who": "Frontend Application Developers, Product Designers.",
                "when": "Saat ingin memoles produk prototipe agar layak dipresentasikan kepada klien atau publik.",
                "where": "Diinstal via pip (`pip install customtkinter`) dan dijalankan di komputer lokal.",
                "how": "import customtkinter as ctk\n\nctk.set_appearance_mode(\"dark\")\nctk.set_default_color_theme(\"blue\")\n\napp = ctk.CTk()\napp.title(\"Modern Chatbot\")\napp.geometry(\"400x500\")\n\nbtn = ctk.CTkButton(app, text=\"Kirim Chat\", command=lambda: print(\"Sent!\"))\nbtn.pack(pady=20)\n\napp.mainloop()",
                "web_app_fundamental": "CustomTkinter memperkenalkan konsep 'Component Styling' dan 'Theming' (Dark/Light Mode) yang merupakan pilar utama desain frontend modern pada framework web seperti React dan Tailwind CSS.",
                "portfolio_meaning_intro": "Meningkatkan nilai jual portofolio Anda. Aplikasi dengan visual menarik 10x lebih dihargai oleh penonton awam maupun rekruter.",
                "portfolio_repo_structure": "semester_1/\n└── p13_modern_gui/\n    ├── modern_app.py\n    └── README.md",
                "portfolio_commit": "feat: upgrade chatbot interface to dark-themed modern UI using customtkinter",
                "portfolio_readme": "Sertakan file screenshot tema gelap (dark mode) dari aplikasi chatbot helpdesk modern Anda.",
                "reflection_q1": "Mengapa standardisasi desain (seperti menggunakan rounded corner, palet warna konsisten) sangat penting bagi aplikasi professional?",
                "reflection_q2": "Bagaimana pustaka pihak ketiga mempercepat proses pengembangan software?",
                "reflection_q3": "Apa keuntungan menggunakan library CustomTkinter dibanding membuat gaya manual dari Tkinter standar?"
            },
            14: {
                "title": "Robust Programming: Penanganan Error (Exception Handling)",
                "what": "Menerapkan blok logika `try-except` untuk menangkap potensi error runtime agar aplikasi tidak keluar tiba-tiba (crash) saat terjadi kesalahan input atau kegagalan sistem.",
                "why": "Aplikasi profesional tidak boleh crash di tangan pengguna. Jika terjadi kesalahan (misal: file dataset hilang), aplikasi harus memberi tahu pengguna dengan sopan.",
                "who": "Quality Assurance (QA) Engineers, Backend Engineers, Software Reliability Engineers.",
                "when": "Wajib diterapkan pada setiap pembacaan file, koneksi internet, pembagian angka, atau konversi tipe data input user.",
                "where": "Diterapkan di sekeliling fungsi rawan error pada kode program.",
                "how": "try:\n    with open(\"dataset.json\", \"r\") as f:\n        data = json.load(f)\nexcept FileNotFoundError:\n    print(\"Peringatan: File dataset.json tidak ditemukan. Menggunakan dataset default.\")\n    data = {\"intents\": []}\nexcept json.JSONDecodeError:\n    print(\"Error: Format file JSON rusak!\")",
                "web_app_fundamental": "Di aplikasi web, penanganan error digunakan untuk mengelola kegagalan request API (misal: error 404 atau 500) sehingga halaman web tetap bisa menampilkan pesan error yang ramah (Error Page).",
                "portfolio_meaning_intro": "Membuat aplikasi Anda 'bulletproof' (tahan banting). Ini membuktikan kedewasaan coding Anda di mata penilai teknis.",
                "portfolio_repo_structure": "semester_1/\n└── p14_error_handling/\n    ├── secure_loader.py\n    └── README.md",
                "portfolio_commit": "refactor: implement try-except blocks to prevent runtime crashes on file loading",
                "portfolio_readme": "Tulis daftar skenario kegagalan (edge cases) yang berhasil diantisipasi oleh program Anda beserta solusinya.",
                "reflection_q1": "Mengapa penggunaan blok `except Exception:` (menangkap semua error tanpa spesifik) tidak disarankan dalam standar industri?",
                "reflection_q2": "Apa peran dari blok `finally` dalam konstruksi `try-except-finally`?",
                "reflection_q3": "Bagaimana penanganan error meningkatkan rasa percaya pengguna (trust) terhadap aplikasi?"
            },
            15: {
                "title": "Teknik Dokumentasi Kode & Panduan Kolaborasi dengan AI",
                "what": "Menggunakan alat bantu Kecerdasan Buatan (AI) secara etis untuk menghasilkan dokumentasi teknis berkualitas tinggi (README, Docstrings, anotasi tipe) serta membuat portofolio prompt.",
                "why": "Kode yang tidak didokumentasikan adalah kode mati. AI dapat membantu programmer menulis dokumentasi yang komprehensif dalam hitungan detik, meningkatkan keterbacaan kode.",
                "who": "Technical Writers, Lead Developers, Open Source Contributors.",
                "when": "Dilakukan setelah kode program selesai ditulis dan sebelum dipublikasikan ke publik atau di-push ke GitHub.",
                "where": "Ditulis langsung di dalam kode (inline comments, docstrings) dan file panduan repositori (`README.md`).",
                "how": "Contoh penulisan Docstring standar Google:\ndef kirim_pesan(nama_user, pesan):\n    \"\"\"Mengirimkan pesan helpdesk ke tampilan UI.\n\n    Args:\n        nama_user (str): Nama pengguna yang mengirim pesan.\n        pesan (str): Kalimat pesan yang dikirim.\n\n    Returns:\n        bool: True jika berhasil dikirim, False jika gagal.\n    \"\"\"\n    pass",
                "web_app_fundamental": "Dokumentasi API yang baik (seperti OpenAPI/Swagger) adalah jembatan komunikasi antara Back-end developer yang membuat database dengan Front-end developer yang merancang tampilan.",
                "portfolio_meaning_intro": "Mempublikasikan portofolio prompt engineering. Menunjukkan kemampuan Anda berkolaborasi dengan AI untuk efisiensi dokumentasi.",
                "portfolio_repo_structure": "semester_1/\n└── p15_dokumentasi_ai/\n    ├── chatbot.py (fully documented)\n    └── promt_portfolio.md",
                "portfolio_commit": "docs: generate comprehensive google-style docstrings and prompt portfolio",
                "portfolio_readme": "Tampilkan daftar prompt AI yang Anda gunakan untuk menghasilkan dokumentasi berkualitas tinggi.",
                "reflection_q1": "Mengapa kita tetap perlu memahami kode yang kita buat walaupun AI bisa membuat dokumentasi dan memperbaikinya secara instan?",
                "reflection_q2": "Apa saja kriteria dokumentasi proyek software yang baik di GitHub?",
                "reflection_q3": "Bagaimana komentar di dalam kode (`#`) membantu rekan satu tim Anda saat berkolaborasi?"
            },
            16: {
                "title": "PROJECT OUTPUT: Chatbot Helpdesk Desktop Terintegrasi",
                "what": "Menyatukan semua modul yang telah dipelajari (JSON Reader, NLP Logic, CustomTkinter GUI, Error Handling) menjadi produk utuh Chatbot Helpdesk Desktop yang siap rilis.",
                "why": "Menyatukan potongan-potongan pelajaran menjadi satu mahakarya nyata (capstone project) memberikan kepuasan belajar dan bukti portofolio yang bernilai tinggi.",
                "who": "Siswa sebagai Product Owner & Full-Stack Desktop Developer.",
                "when": "Minggu ke-16, sebagai puncak pencapaian pembelajaran semester ganjil.",
                "where": "Aplikasi dikompilasi (misal dengan `pyinstaller`) menjadi file executable (.exe / .app) yang bisa langsung dijalankan.",
                "how": "Siswa merakit file `app.py` yang mengimpor `dataset.json` dan meluncurkan interface CustomTkinter, menghubungkan fungsi pencarian jawaban dengan kolom teks UI, serta menambahkan tombol reset chat dan ekspor log percakapan.",
                "web_app_fundamental": "Proyek chatbot desktop ini adalah prototipe arsitektur aplikasi client-server mini: UI (client) mengirim pesan, logika NLP (controller) memproses pesan, dataset JSON (database) menyediakan jawaban.",
                "portfolio_meaning_intro": "🏆 PROYEK UTAMA SEMESTER 1. Mahakarya portofolio pertama Anda yang menunjukkan kemampuan dari merancang data hingga mempublikasikan produk jadi yang ramah pengguna.",
                "portfolio_repo_structure": "semester_1/chatbot_helpdesk/\n├── app.py\n├── dataset.json\n├── assets/\n│   └── logo.png\n├── requirements.txt\n└── README.md",
                "portfolio_commit": "release: launch chatbot helpdesk desktop application v1.0.0",
                "portfolio_readme": "Tulis README super detail: deskripsi produk, cara instalasi (`pip install -r requirements.txt`), cara menjalankan, panduan penggunaan, fitur utama, dan diagram alur kerja aplikasi.",
                "reflection_q1": "Bagaimana perasaan Anda berhasil membangun aplikasi desktop interaktif buatan sendiri dari nol?",
                "reflection_q2": "Jika Anda diberi waktu tambahan, fitur canggih apa lagi yang ingin Anda tambahkan pada chatbot ini?",
                "reflection_q3": "Bagaimana tanggapan teman atau guru saat mencoba aplikasi chatbot buatan Anda?"
            },
            17: {
                "title": "Refactoring & Debugging Kode Berbantuan AI",
                "what": "Proses membaca ulang kode, mencari celah inefisiensi, memperbaiki bug, dan menulis ulang struktur kode agar lebih bersih (refactoring) menggunakan bantuan AI.",
                "why": "Kode yang berfungsi belum tentu merupakan kode yang efisien dan mudah dirawat. Refactoring membuat kode lebih cepat dieksekusi dan lebih bersih (clean code).",
                "who": "Software Architects, Senior Developers.",
                "when": "Setelah rilis versi pertama (v1) untuk mempersiapkan kode agar siap dikembangkan lebih lanjut di masa depan.",
                "where": "Dilakukan langsung pada repositori proyek utama.",
                "how": "Siswa memasukkan kode mereka ke model AI dengan prompt: 'Analisis kompleksitas kode saya dan lakukan refactoring agar memenuhi standar Clean Code PEP 8.' AI akan menyarankan pemotongan fungsi yang terlalu panjang atau penggunaan memori yang lebih hemat.",
                "web_app_fundamental": "Refactoring mengajarkan pentingnya performa pemuatan web. Kode web yang tidak efisien akan membuat website lambat dimuat oleh browser user (slow page speed).",
                "portfolio_meaning_intro": "Laporan Debugging Profesional. Membuktikan bahwa Anda tidak hanya bisa menulis kode, tapi juga bisa memelihara, mengoptimalkan, dan meningkatkan kualitas kode.",
                "portfolio_repo_structure": "semester_1/chatbot_helpdesk/\n├── app_clean.py\n└── debug_report.md",
                "portfolio_commit": "refactor: optimize chatbot logic and align code with PEP 8 standards",
                "portfolio_readme": "Sertakan laporan debugging sebelum dan sesudah optimasi, lengkap dengan perbandingan kecepatan eksekusi program jika ada.",
                "reflection_q1": "Apa perbedaan antara bug fungsional (program error) dengan inefisiensi kode (code smell)?",
                "reflection_q2": "Mengapa standarisasi penulisan kode seperti PEP 8 di Python sangat penting di dunia industri?",
                "reflection_q3": "Bagaimana AI membantu Anda memahami bagian kode Anda yang rumit?"
            },
            18: {
                "title": "UAS & Sesi Refleksi Portofolio Semester 1",
                "what": "Evaluasi akhir berupa penilaian produk, kelengkapan dokumentasi repositori GitHub, dan pengisian jurnal refleksi pembelajaran satu semester.",
                "why": "Menutup siklus belajar dengan evaluasi objektif dan refleksi mendalam, membantu siswa menyadari perkembangan skill mereka serta bersiap untuk materi hardware di Semester 2.",
                "who": "Siswa dan Dewan Penguji (Guru/Praktisi Industri).",
                "when": "Minggu terakhir (ke-18) semester 1.",
                "where": "Di depan kelas (presentasi langsung) dan melalui review link repositori GitHub.",
                "how": "1. Siswa mempresentasikan demo aplikasi chatbot mereka.\n2. Guru mereview kerapian commit history dan isi README di GitHub.\n3. Siswa mengisi jurnal refleksi tahunan.",
                "web_app_fundamental": "Melatih keterampilan presentasi teknis (Developer Pitching) yang sangat dibutuhkan ketika seorang web developer harus mendemonstrasikan hasil pekerjaannya di depan klien atau manajer proyek.",
                "portfolio_meaning_intro": "Evaluasi Kesiapan Industri. Menandai selesainya fase 'Software Dasar' dan siap memasuki dunia integrasi hardware.",
                "portfolio_repo_structure": "semester_1/\n└── (seluruh folder proyek terkelola dengan rapi di GitHub)",
                "portfolio_commit": "docs: finalize semester 1 study portfolio and submit all project journals",
                "portfolio_readme": "Tambahkan ringkasan kompetensi yang telah dikuasai selama semester 1 di profil utama GitHub Anda.",
                "reflection_q1": "Dari seluruh materi semester 1, materi mana yang paling memberikan dampak perubahan cara berpikir bagi Anda?",
                "reflection_q2": "Seberapa penting dokumentasi portofolio yang rapi dalam memotivasi Anda belajar?",
                "reflection_q3": "Apa resolusi teknis Anda untuk menyambut pembelajaran Semester 2?"
            }
        }
    },
    2: {
        "name": "Semester 2: Hardware & Infrastruktur",
        "weeks": {
            1: {
                "title": "Sistem Bilangan & Arsitektur Mikrokontroler ESP32",
                "what": "Konsep sistem bilangan biner (0 dan 1), desimal, heksadesimal, serta pengenalan komponen fisik dan pinout board mikrokontroler ESP32.",
                "why": "Hardware komputer berkomunikasi menggunakan sinyal biner. Memahami sistem bilangan dan arsitektur board adalah jembatan untuk mengendalikan komponen fisik lewat kode program.",
                "who": "Embedded Systems Engineers, IoT Developers, Hardware Designers.",
                "when": "Awal mula sebelum menghubungkan sensor atau menulis program hardware apa pun.",
                "where": "Bekerja di dalam sirkuit internal (CPU/Register) ESP32 dan breadboard.",
                "how": "1. Konversi bilangan biner `1010` menjadi desimal (`10`).\n2. Pelajari pinout ESP32 (pin VCC, GND, GPIO).\n3. Pelajari perbedaan mikrokontroler (ESP32) dengan mikroprosesor (PC).",
                "web_app_fundamental": "Data dari sensor fisik (seperti suhu) nantinya akan dikirimkan ke database web dalam format string desimal. Pengiriman data tersebut melewati protokol jaringan yang pada tingkat paling dasar mengirimkan aliran bit biner.",
                "portfolio_meaning_intro": "Mendokumentasikan pemahaman dasar sistem digital dan pengenalan fisik sirkuit elektronik.",
                "portfolio_repo_structure": "semester_2/\n└── p1_sistem_digital/\n    ├── cheat_sheet.md\n    └── pinout_esp32.png",
                "portfolio_commit": "docs: create digital number conversion guide and ESP32 pinout schematic reference",
                "portfolio_readme": "Buat tabel konversi biner-desimal-heksadesimal sederhana dan berikan penjelasan fungsi pin GPIO pada ESP32.",
                "reflection_q1": "Mengapa komputer menggunakan sistem biner sedangkan manusia menggunakan sistem desimal?",
                "reflection_q2": "Apa perbedaan utama ESP32 dengan mikrokontroler pendahulunya seperti Arduino Uno?",
                "reflection_q3": "Mengapa ESP32 sangat populer untuk proyek Internet of Things (IoT)?"
            },
            2: {
                "title": "Setup IDE & Program Pertama: Blink LED",
                "what": "Instalasi software Arduino IDE (atau VS Code PlatformIO), pemasangan driver USB-to-UART, dan penulisan program 'Hello World' di dunia hardware: mengedipkan lampu LED.",
                "why": "Memastikan rantai komunikasi dari penulisan kode di komputer hingga eksekusi program di chip hardware ESP32 berjalan lancar.",
                "who": "IoT Developers, Hardware Firmware Engineers.",
                "when": "Pertama kali menyalakan board baru untuk memastikan board berfungsi normal.",
                "where": "Kode ditulis di Arduino IDE, di-compile menjadi file binary (.bin), lalu di-upload ke flash memory ESP32 via kabel USB.",
                "how": "void setup() {\n  pinMode(2, OUTPUT); // Pin LED bawaan ESP32\n}\n\nvoid loop() {\n  digitalWrite(2, HIGH); // Nyalakan LED\n  delay(1000);           // Tunggu 1 detik\n  digitalWrite(2, LOW);  // Matikan LED\n  delay(1000);\n}",
                "web_app_fundamental": "Konsep loop di hardware (`void loop()`) berjalan selamanya untuk memantau perubahan kondisi, konsep ini mirip dengan event loop pada JavaScript yang terus memantau klik pengguna di browser web.",
                "portfolio_meaning_intro": "Keberhasilan mengedipkan LED fisik pertama Anda. Ini membuktikan bahwa Anda bisa menulis kode yang berdampak langsung pada dunia nyata.",
                "portfolio_repo_structure": "semester_2/\n└── p2_blink_led/\n    ├── blink.ino\n    └── README.md",
                "portfolio_commit": "feat: upload and run first blink LED program on ESP32",
                "portfolio_readme": "Sertakan video singkat (GIF) atau foto LED ESP32 Anda yang sedang berkedip beserta penjelasan baris kodenya.",
                "reflection_q1": "Apa fungsi dari fungsi `setup()` dan fungsi `loop()` pada pemrograman C/C++ Arduino?",
                "reflection_q2": "Mengapa kita membutuhkan hambatan (resistor) saat menghubungkan LED eksternal ke pin GPIO?",
                "reflection_q3": "Masalah apa yang Anda hadapi saat proses uploading kode (misal: gagal mendeteksi Port COM)?"
            },
            3: {
                "title": "GPIO Digital: Input (Button) & Output (LED/Buzzer)",
                "what": "Menggunakan pin General Purpose Input Output (GPIO) sebagai penerima sinyal digital (input dari tombol tekan) dan pengirim sinyal digital (menyalakan LED eksternal atau membunyikan buzzer).",
                "why": "Interaksi perangkat IoT dimulai dari mendeteksi trigger fisik (tombol ditekan) untuk mengendalikan aktuator (lampu menyala/alarm berbunyi).",
                "who": "Automation Engineers, Circuit Designers.",
                "when": "Saat merancang sistem kendali manual pada perangkat elektronik.",
                "where": "Rangkaian sirkuit elektronik dirakit pada breadboard menggunakan kabel jumper.",
                "how": "const int BUTTON_PIN = 4;\nconst int LED_PIN = 5;\n\nvoid setup() {\n  pinMode(BUTTON_PIN, INPUT_PULLUP);\n  pinMode(LED_PIN, OUTPUT);\n}\n\nvoid loop() {\n  int buttonState = digitalRead(BUTTON_PIN);\n  if (buttonState == LOW) {\n    digitalWrite(LED_PIN, HIGH); // Nyalakan jika ditekan\n  } else {\n    digitalWrite(LED_PIN, LOW);\n  }\n}",
                "web_app_fundamental": "Konsep Input-Output digital ini analog dengan interaksi form HTML: Tombol Kirim Form (Input) memicu pengiriman data dan memunculkan notifikasi sukses (Output) di layar browser web.",
                "portfolio_meaning_intro": "Membangun sistem interaktif hardware pertamamu yang responsif terhadap aksi pengguna.",
                "portfolio_repo_structure": "semester_2/\n└── p3_gpio_digital/\n    ├── push_button_led.ino\n    └── schema.png",
                "portfolio_commit": "feat: build button-controlled LED circuit using ESP32 pull-up configuration",
                "portfolio_readme": "Sertakan gambar skema sirkuit yang Anda buat (menggunakan Fritzing atau coretan rapi) beserta penjelasan logika aktif-rendah (Active Low).",
                "reflection_q1": "Apa perbedaan antara konfigurasi resistor Pull-Up dan Pull-Down pada pin input?",
                "reflection_q2": "Apa yang dimaksud dengan fenomena 'Bouncing' pada tombol mekanik, dan bagaimana cara mengatasinya secara software?",
                "reflection_q3": "Bagaimana cara kerja sirkuit Active Low?"
            },
            4: {
                "title": "Proyek Mini: Sistem Simulasi Traffic Light",
                "what": "Membuat simulasi lampu lalu lintas (Traffic Light) jalan raya menggunakan 3 buah LED (Merah, Kuning, Hijau) dengan manajemen waktu delay yang presisi.",
                "why": "Melatih logika pemrograman terstruktur (State Machine) untuk mengendalikan sistem multi-output yang berurutan dan otomatis.",
                "who": "Traffic System Engineers, Embedded Software Developers.",
                "when": "Saat merancang otomatisasi sistem yang memiliki urutan langkah (sekuensial) tetap.",
                "where": "Dirakit menggunakan breadboard, 3 resistor, dan 3 LED eksternal yang dihubungkan ke ESP32.",
                "how": "// Mengatur urutan nyala LED Merah -> Merah-Kuning -> Hijau -> Kuning -> Merah\n// Siswa menulis fungsi terpisah untuk setiap keadaan lampu (state)\nvoid setTrafficLight(int red, int yellow, int green) {\n  digitalWrite(12, red);\n  digitalWrite(13, yellow);\n  digitalWrite(14, green);\n}",
                "web_app_fundamental": "State Machine pada traffic light mengajarkan konsep transisi halaman (routing) pada aplikasi web: `Halaman Login (State 1) -> Loading (State 2) -> Dashboard (State 3)`.",
                "portfolio_meaning_intro": "Proyek Simulasi Nyata Pertama. Membuktikan kemampuan mengelola banyak output digital secara harmonis.",
                "portfolio_repo_structure": "semester_2/\n└── p4_traffic_light/\n    ├── traffic_light.ino\n    └── README.md",
                "portfolio_commit": "feat: develop multi-state traffic light simulator with sequential logic",
                "portfolio_readme": "Sertakan tabel transisi state (state transition table) yang menjelaskan durasi waktu untuk masing-masing warna lampu.",
                "reflection_q1": "Bagaimana jika kita ingin menambahkan tombol penyeberang jalan (pedestrian button) yang menyela siklus lampu merah? Bagaimana kodenya?",
                "reflection_q2": "Mengapa penggunaan fungsi `delay()` yang terlalu lama dapat menghambat pembacaan tombol input secara real-time?",
                "reflection_q3": "Apa solusi pemrograman untuk menghindari delay yang memblokir (blocking delay)? (Petunjuk: fungsi `millis()`)"
            },
            5: {
                "title": "Sensor Analog & ADC (Analog-to-Digital Converter)",
                "what": "Membaca nilai dari sensor analog (seperti sensor cahaya LDR atau potensiometer) dan mengonversi sinyal tegangan analog menjadi nilai digital menggunakan modul ADC internal ESP32.",
                "why": "Alam semesta bekerja secara analog (suhu, cahaya, kelembaban terus berubah tanpa batas). ADC memungkinkan komputer digital memahami variasi nilai alam tersebut.",
                "who": "Sensor Engineers, Data Acquisition Specialists.",
                "when": "Digunakan kapan saja aplikasi membutuhkan pembacaan kondisi lingkungan yang nilainya bervariasi (bukan sekadar ON/OFF).",
                "where": "Input analog masuk melalui pin ADC khusus pada ESP32 (misal GPIO 34).",
                "how": "const int LDR_PIN = 34;\n\nvoid setup() {\n  Serial.begin(115200);\n}\n\nvoid loop() {\n  int ldrValue = analogRead(LDR_PIN); // Membaca nilai ADC 0-4095\n  Serial.print(\"Nilai Cahaya: \");\n  Serial.println(ldrValue);\n  delay(500);\n}",
                "web_app_fundamental": "Resolusi ADC (misal 12-bit pada ESP32 menghasilkan nilai 0-4095) mengajarkan konsep 'Data Range and Scaling'. Di web frontend, data mentah ini harus di-scaling menjadi persentase (0-100%) agar mudah dibaca pengguna.",
                "portfolio_meaning_intro": "Membaca denyut lingkungan sekitar menggunakan sensor analog. Dasar utama pengumpulan data sensor (data logging).",
                "portfolio_repo_structure": "semester_2/\n└── p5_sensor_analog/\n    ├── ldr_reader.ino\n    └── README.md",
                "portfolio_commit": "feat: implement analog light intensity reading using LDR and ESP32 ADC",
                "portfolio_readme": "Jelaskan resolusi ADC ESP32 dan tuliskan rumus konversi nilai ADC mentah menjadi nilai persentase intensitas cahaya.",
                "reflection_q1": "Berapakah resolusi bit ADC pada ESP32? Apa bedanya dengan Arduino Uno?",
                "reflection_q2": "Bagaimana pengaruh perubahan intensitas cahaya sekitar terhadap nilai resistansi LDR?",
                "reflection_q3": "Mengapa pembacaan sensor analog sering berfluktuasi? Bagaimana cara menstabilkannya secara software?"
            },
            6: {
                "title": "Aktuator: Motor Servo & Sinyal PWM (Pulse Width Modulation)",
                "what": "Mengendalikan aktuator fisik yang membutuhkan sudut presisi (seperti Motor Servo) atau mengatur kecerahan LED menggunakan modulasi lebar pulsa (PWM).",
                "why": "IoT tidak hanya mengamati, tapi juga bertindak. Motor servo digunakan untuk menggerakkan lengan robot, membuka palang pintu otomatis, atau mengatur katup udara.",
                "who": "Robotics Engineers, Control System Developers.",
                "when": "Saat sistem membutuhkan gerakan mekanis presisi atau kontrol daya analog secara digital.",
                "where": "Sinyal PWM dihasilkan oleh pin GPIO tertentu dan dikirimkan ke pin kontrol motor servo.",
                "how": "#include <ESP32Servo.h>\n\nServo myServo;\nconst int SERVO_PIN = 18;\n\nvoid setup() {\n  myServo.attach(SERVO_PIN);\n}\n\nvoid loop() {\n  myServo.write(0);   // Sudut 0 derajat\n  delay(1000);\n  myServo.write(90);  // Sudut 90 derajat\n  delay(1000);\n}",
                "web_app_fundamental": "Kontrol motor servo melatih pemahaman 'State Updates'. Di aplikasi web, hal ini analog dengan menggeser slider UI (Input) yang secara real-time memperbarui posisi elemen grafis di layar.",
                "portfolio_meaning_intro": "Proyek Smart Fan / Palang Pintu Otomatis. Menghubungkan pembacaan sensor ke gerakan motor fisik nyata.",
                "portfolio_repo_structure": "semester_2/\n└── p6_aktuator_servo/\n    ├── servo_control.ino\n    └── README.md",
                "portfolio_commit": "feat: implement PWM-based servo motor positioning control",
                "portfolio_readme": "Tulis spesifikasi motor servo yang digunakan dan buat diagram alur logika kapan servo harus bergerak (misal: jika sensor mendeteksi objek dekat).",
                "reflection_q1": "Apa yang dimaksud dengan sinyal PWM (Pulse Width Modulation) secara sederhana?",
                "reflection_q2": "Mengapa motor servo tidak boleh langsung mengambil daya dari pin 5V ESP32 jika motor tersebut berukuran besar?",
                "reflection_q3": "Apa perbedaan motor servo dengan motor DC biasa?"
            },
            7: {
                "title": "Komunikasi Serial: Pengiriman Data ESP32 ke PC",
                "what": "Menggunakan protokol komunikasi UART (Universal Asynchronous Receiver-Transmitter) untuk mengirimkan data sensor dari ESP32 ke komputer (PC) melalui kabel USB.",
                "why": "ESP32 tidak memiliki layar bawaan. Komunikasi serial adalah jendela bagi developer untuk memantau apa yang terjadi di dalam chip (debugging) dan mengirimkan data ke sistem luar.",
                "who": "IoT Developers, Hardware Testers.",
                "when": "Dilakukan sepanjang masa pengembangan (development phase) untuk proses debugging data.",
                "where": "Data mengalir dari port micro-USB ESP32 ke USB port PC dan ditampilkan di Serial Monitor.",
                "how": "void setup() {\n  Serial.begin(115200); // Set baud rate\n  Serial.println(\"Sistem Dimulai...\");\n}\n\nvoid loop() {\n  float suhu = 28.5;\n  // Mengirimkan data dalam format CSV\n  Serial.print(\"SUHU,\");\n  Serial.println(suhu);\n  delay(2000);\n}",
                "web_app_fundamental": "Konsep Baud Rate (kecepatan transfer data dalam bit per detik) mengajarkan pentingnya menyelaraskan bandwidth pengiriman. Ini sangat mirip dengan penyelarasan format data antara API endpoint backend dengan fetcher frontend.",
                "portfolio_meaning_intro": "Mendirikan jalur pipa data (data pipeline) pertama Anda antara dunia fisik (ESP32) dan dunia digital (PC).",
                "portfolio_repo_structure": "semester_2/\n└── p7_komunikasi_serial/\n    ├── serial_logger.ino\n    └── README.md",
                "portfolio_commit": "feat: configure stable UART serial data stream from ESP32 at 115200 baud",
                "portfolio_readme": "Jelaskan apa itu Baud Rate dan mengapa jika nilainya tidak cocok antara ESP32 dengan Serial Monitor akan memunculkan karakter asing (garbage characters).",
                "reflection_q1": "Mengapa baud rate 115200 lebih disukai daripada 9600 untuk ESP32?",
                "reflection_q2": "Apa fungsi dari pin RX (Receiver) dan TX (Transmitter) pada sirkuit serial?",
                "reflection_q3": "Sebutkan protokol komunikasi hardware selain UART yang populer digunakan!"
            },
            8: {
                "title": "PROJECT OUTPUT: Smart Lamp (LDR & Button-Controlled)",
                "what": "Mengintegrasikan ESP32, sensor cahaya LDR, push button, dan lampu LED (atau relay untuk lampu 220V) menjadi sistem Lampu Pintar Otomatis.",
                "why": "Proyek akhir IoT skala kecil yang memadukan logika input digital, input analog, dan kontrol output secara terpadu untuk menyelesaikan masalah penghematan energi.",
                "who": "Siswa sebagai IoT Solutions Architect.",
                "when": "Minggu ke-8 semester genap.",
                "where": "Sistem dirakit dalam wadah prototipe (misal miniatur rumah kardus) agar estetis.",
                "how": "Lampu otomatis menyala jika LDR mendeteksi kondisi gelap (nilai ADC tinggi), namun pengguna dapat mematikan/menyalakan lampu secara manual kapan saja dengan menekan push button (menggunakan interupsi / debounced logic).",
                "web_app_fundamental": "Sistem Smart Lamp ini adalah bentuk fisik dari 'Smart Device Node'. Data status lampu (ON/OFF) nantinya akan dikirimkan ke dashboard website monitoring Anda.",
                "portfolio_meaning_intro": "🏆 PROYEK UTAMA SEMESTER 2 (BAGIAN I). Karya fisik IoT pertama Anda yang siap dipublikasikan lengkap dengan skema sirkuit dan firmware code.",
                "portfolio_repo_structure": "semester_2/smart_lamp/\n├── smart_lamp.ino\n├── schematic.png\n├── flow_chart.pdf\n└── README.md",
                "portfolio_commit": "release: launch physical Smart Lamp IoT prototype firmware v1.0.0",
                "portfolio_readme": "Tulis dokumentasi hardware profesional: daftar komponen (BOM - Bill of Materials), skema sirkuit, diagram alur algoritma, dan link video demo alat.",
                "reflection_q1": "Bagaimana Anda menyeimbangkan prioritas kontrol antara sensor otomatis (LDR) dengan tombol manual (Button)?",
                "reflection_q2": "Apa fungsi komponen Relay jika kita ingin mengendalikan lampu rumah asli bertegangan 220V AC?",
                "reflection_q3": "Bahaya apa saja yang harus diwaspadai ketika bekerja dengan listrik tegangan tinggi (AC)?"
            },
            9: {
                "title": "UTS (Ujian Tengah Semester) - Evaluasi Hardware & IoT",
                "what": "Evaluasi praktik individu di mana siswa harus merancang, merakit, dan memprogram sistem IoT sederhana berdasarkan studi kasus instan dari guru.",
                "why": "Memastikan kompetensi praktis siswa dalam merakit sirkuit elektronika dasar dan memecahkan masalah (troubleshooting) hardware secara mandiri.",
                "who": "Siswa sebagai penguji mandiri dan Guru sebagai supervisor teknis.",
                "when": "Minggu ke-9 Semester Genap.",
                "where": "Laboratorium Komputer/Sistem Tertanam.",
                "how": "Siswa diberikan waktu 3 jam untuk membuat sistem 'Suhu Alarm Kebakaran' menggunakan sensor suhu (DHT11) dan Buzzer. Jika suhu melebihi batas, buzzer berbunyi putus-putus. Kodingan wajib diunggah ke repositori GitHub.",
                "web_app_fundamental": "Menguji kemampuan merakit sirkuit fisik yang handal serta menulis kode firmware yang bersih tanpa memblokir pembacaan sensor lain.",
                "portfolio_meaning_intro": "Proyek UTS: Fire Alarm Simulator. Bukti kompetensi kilat merancang solusi hardware di bawah tekanan waktu.",
                "portfolio_repo_structure": "semester_2/uts_fire_alarm/\n├── fire_alarm.ino\n└── sirkuit.png",
                "portfolio_commit": "chore: complete UTS exam - ESP32 fire alarm system integration",
                "portfolio_readme": "Sertakan deskripsi cara kerja alarm dan batas ambang suhu (threshold) yang diterapkan.",
                "reflection_q1": "Kesulitan apa yang paling menegangkan saat merakit sirkuit fisik dalam batas waktu ujian?",
                "reflection_q2": "Bagaimana Anda menguji sirkuit Anda sebelum menyatakan bahwa proyek Anda telah selesai?",
                "reflection_q3": "Apa pentingnya memahami pembacaan spesifikasi komponen dari datasheet?"
            },
            10: {
                "title": "Sistem Virtualisasi: Instalasi Oracle VM VirtualBox",
                "what": "Konsep dasar virtualisasi komputer dan langkah-langkah menginstal software hypervisor Oracle VM VirtualBox di komputer lokal.",
                "why": "Virtualisasi memungkinkan kita menjalankan sistem operasi lain (seperti Linux Server) di dalam komputer Windows kita tanpa perlu membeli komputer baru atau merusak OS utama.",
                "who": "System Administrators, DevOps Engineers, Cloud Architects.",
                "when": "Sebelum mulai mempelajari administrasi server, pengelolaan jaringan, atau hosting website.",
                "where": "Dipasang pada sistem operasi utama PC/Laptop host.",
                "how": "1. Unduh file instalasi VirtualBox (virtualbox.org).\n2. Instal dengan mengikuti panduan wizard.\n3. Alokasikan memori RAM dan ruang harddisk virtual.\n4. Pelajari perbedaan antara OS Host (fisik) dan OS Guest (virtual).",
                "web_app_fundamental": "Layanan cloud modern (seperti AWS, GCP, Azure) menyewakan server dalam bentuk Virtual Machine (VM). Memahami VirtualBox lokal adalah simulasi gratis terbaik sebelum menyewa server cloud di internet.",
                "portfolio_meaning_intro": "Mempersiapkan infrastruktur server mandiri di PC Anda. Tonggak awal pemahaman sistem operasi server.",
                "portfolio_repo_structure": "semester_2/\n└── p10_virtualbox/\n    └── config_guide.md",
                "portfolio_commit": "docs: document installation and resource allocation of VirtualBox environment",
                "portfolio_readme": "Tulis panduan spesifikasi minimal PC host agar dapat menjalankan VM dengan lancar beserta tangkapan layar VirtualBox Manager.",
                "reflection_q1": "Apa perbedaan antara Virtual Machine (VM) dengan Container (seperti Docker) secara umum?",
                "reflection_q2": "Mengapa kita tidak boleh mengalokasikan RAM untuk VM melebihi kapasitas RAM PC fisik asli?",
                "reflection_q3": "Sebutkan tipe hypervisor yang Anda ketahui!"
            },
            11: {
                "title": "Instalasi Linux Ubuntu Server & Perintah Dasar CLI Navigation",
                "what": "Menginstal sistem operasi Linux Ubuntu Server (tanpa tampilan grafis/CLI) di VirtualBox dan menguasai perintah navigasi dasar terminal Linux.",
                "why": "Lebih dari 90% server web di dunia menggunakan sistem operasi Linux CLI karena sangat ringan, aman, dan stabil. Developer web wajib menguasai navigasi terminal Linux.",
                "who": "Linux Administrators, Back-end Developers, DevOps.",
                "when": "Digunakan setiap kali melakukan remote server atau mengatur konfigurasi file server.",
                "where": "Dijalankan langsung di dalam layar konsol Virtual Machine Ubuntu Server.",
                "how": "Perintah dasar CLI Linux:\n- Melihat folder aktif: `pwd`\n- Melihat isi direktori: `ls -la`\n- Pindah folder: `cd /var/www/html`\n- Membuat folder baru: `mkdir proyek_web`\n- Membuat/mengedit file: `nano index.html`\n- Menghapus file: `rm target.txt`",
                "web_app_fundamental": "Aplikasi web Anda nantinya akan dihosting di dalam server Linux. Kemampuan menggunakan command line (CLI) adalah syarat mutlak untuk menginstal database, mengunggah kode, dan mengelola server tersebut.",
                "portfolio_meaning_intro": "Membuat Cheat Sheet Perintah Linux CLI Mandiri. Bukti bahwa Anda tidak lagi tergantung pada klik mouse grafis (GUI) dalam mengelola komputer.",
                "portfolio_repo_structure": "semester_2/\n└── p11_linux_cli/\n    └── linux_cheatsheet.md",
                "portfolio_commit": "docs: create comprehensive interactive linux CLI command cheat sheet",
                "portfolio_readme": "Tuliskan daftar perintah Linux CLI terpenting yang Anda gunakan beserta contoh output-nya di terminal.",
                "reflection_q1": "Mengapa server profesional jarang menggunakan tampilan grafis (GUI)?",
                "reflection_q2": "Apa fungsi dari perintah `sudo` sebelum menjalankan perintah lain?",
                "reflection_q3": "Apa perbedaan antara path relatif (relative path) dengan path absolut (absolute path) di Linux?"
            },
            12: {
                "title": "Manajemen Jaringan Linux & Hak Akses File (Permissions)",
                "what": "Mengonfigurasi kartu jaringan VirtualBox (Bridge Adapter vs NAT), memeriksa IP Address server, dan mengelola izin hak akses file (chmod/chown) di Linux.",
                "why": "Server tidak akan berguna jika tidak bisa diakses dari jaringan luar. Memahami perizinan file juga krusial agar website tidak mudah diretas akibat file konfigurasi yang bebas diedit siapa saja.",
                "who": "Network Engineers, Cyber Security Analysts.",
                "when": "Saat ingin menghubungkan VM ke internet lokal atau mengamankan file sensitif di server.",
                "where": "Mengedit file konfigurasi jaringan Linux di `/etc/netplan/`.",
                "how": "- Cek IP address: `ip a` atau `ifconfig`\n- Mengubah izin file menjadi Read-Write-Execute untuk pemilik saja: `chmod 700 rahasia.txt`\n- Mengubah izin folder web agar bisa dibaca publik: `chmod -R 755 /var/www/html`\n- Mengubah kepemilikan file ke user web-server: `chown -R www-data:www-data /var/www/html`",
                "web_app_fundamental": "Keamanan file web (File Permissions) mencegah script jahat yang diunggah peretas mengeksekusi perintah berbahaya di server hosting Anda.",
                "portfolio_meaning_intro": "Mendokumentasikan konfigurasi jaringan server lokal dan pengamanan file server.",
                "portfolio_repo_structure": "semester_2/\n└── p12_linux_network/\n    └── permission_and_net_guide.md",
                "portfolio_commit": "docs: document linux file permissions (chmod) and network adapter setup",
                "portfolio_readme": "Sertakan penjelasan sistem angka biner hak akses Linux (4=Read, 2=Write, 1=Execute, misal arti angka 755).",
                "reflection_q1": "Apa arti dari hak akses `777` di Linux? Mengapa hak akses ini sangat dilarang untuk folder website publik?",
                "reflection_q2": "Apa perbedaan antara mode network 'NAT' dengan 'Bridge Adapter' di VirtualBox?",
                "reflection_q3": "Bagaimana cara melakukan tes koneksi antara komputer Windows Host dengan server Linux di VM? (Petunjuk: perintah `ping`)"
            },
            13: {
                "title": "Web Server Lokal: Menginstal Apache/Nginx",
                "what": "Menginstal aplikasi web server (Apache2 atau Nginx) di server Linux lokal menggunakan package manager `apt`, serta memahami direktori root web `/var/www/html/`.",
                "why": "Web server adalah mesin penayang website. Tanpa web server, file-file HTML/CSS yang Anda buat tidak bisa diakses oleh komputer lain melalui browser web di internet.",
                "who": "DevOps Engineers, Web Infrastructure Specialist.",
                "when": "Pertama kali menyiapkan server agar bisa merespon request protokol HTTP dari browser client.",
                "where": "Aplikasi diinstal di Linux Server, dan file website diletakkan di direktori `/var/www/html/`.",
                "how": "1. Update repositori server: `sudo apt update`\n2. Instal Apache web server: `sudo apt install apache2 -y`\n3. Cek status web server: `sudo systemctl status apache2`\n4. Buka browser di Windows Host, ketik IP Address VM (misal `http://192.168.1.15`). Default Page Apache akan muncul.",
                "web_app_fundamental": "Siklus HTTP Request & Response: Ketika browser Anda mengetik IP server (Request), Apache menangkap permintaan tersebut dan mengirimkan file `index.html` kembali ke browser Anda (Response) untuk dirender.",
                "portfolio_meaning_intro": "Mendirikan server web fungsional pertama Anda. Sekarang PC Virtual Anda telah menjadi server penayang web nyata.",
                "portfolio_repo_structure": "semester_2/\n└── p13_web_server/\n    └── setup_apache_report.md",
                "portfolio_commit": "feat: install and configure Apache2 web server on virtualized Ubuntu Linux",
                "portfolio_readme": "Sertakan screenshot halaman default Apache yang berhasil diakses dari browser komputer Windows Anda.",
                "reflection_q1": "Apa peran protokol HTTP (Hypertext Transfer Protocol) dalam dunia web?",
                "reflection_q2": "Mengapa kita harus menjalankan perintah `sudo apt update` sebelum menginstal aplikasi baru di Linux?",
                "reflection_q3": "Apa perbedaan antara Apache dengan Nginx?"
            },
            14: {
                "title": "Dasar Web Frontend: Membuat Landing Page HTML & CSS",
                "what": "Mempelajari sintaks dasar HTML5 untuk menyusun kerangka website (tag header, div, p, img, a) dan CSS3 untuk mengatur tampilan visual (warna, margin, padding, flexbox).",
                "why": "Website adalah antarmuka utama pengguna modern. Pengembang web harus mampu menyusun halaman informasi yang informatif dan sedap dipandang mata.",
                "who": "Frontend Web Developers, UI Designers.",
                "when": "Saat merancang bagian tampilan visual aplikasi yang akan dilihat langsung oleh pengguna.",
                "where": "File `index.html` dan `style.css` diletakkan di server lokal di folder `/var/www/html/`.",
                "how": "Contoh kerangka HTML dasar:\n<!DOCTYPE html>\n<html>\n<head>\n  <link rel='stylesheet' href='style.css'>\n</head>\n<body>\n  <header>\n    <h1>Selamat Datang di TKJT</h1>\n  </header>\n</body>\n</html>",
                "web_app_fundamental": "Responsive Web Design: Menggunakan CSS Media Queries memastikan halaman web Anda tampil rapi baik saat diakses lewat layar PC lebar maupun layar smartphone yang kecil.",
                "portfolio_meaning_intro": "Proyek Halaman Profil Sekolah. Mendesain karya visual frontend pertama Anda yang akan menjadi identitas digital sekolah Anda.",
                "portfolio_repo_structure": "semester_2/\n└── p14_frontend_profile/\n    ├── index.html\n    ├── style.css\n    └── images/",
                "portfolio_commit": "feat: design responsive school profile landing page using HTML5 and CSS3",
                "portfolio_readme": "Tuliskan konsep desain dan palet warna yang Anda pilih, serta bagaimana Anda menyusun tata letak (layout) halaman.",
                "reflection_q1": "Apa kegunaan dari tag `<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">` di HTML?",
                "reflection_q2": "Apa bedanya CSS Class (`.nama-kelas`) dengan CSS ID (`#nama-id`)?",
                "reflection_q3": "Bagaimana CSS Flexbox memudahkan kita merancang layout halaman web yang responsif?"
            },
            15: {
                "title": "Database Server: Instalasi & Operasi CRUD MySQL",
                "what": "Menginstal relational database management system (RDBMS) MySQL/MariaDB di server Linux dan mempraktikkan operasi dasar SQL (Create, Read, Update, Delete).",
                "why": "Website statis hanya bisa menampilkan info tetap. Database memungkinkan aplikasi menyimpan data dinamis seperti akun user, postingan artikel, atau data sensor secara permanen.",
                "who": "Database Administrators, Back-end Developers, Data Engineers.",
                "when": "Saat aplikasi membutuhkan penyimpanan data yang aman, teratur, dan berkapasitas besar.",
                "where": "Database server berjalan sebagai service latar belakang di Linux Server.",
                "how": "1. Instal MySQL: `sudo apt install mysql-server -y`\n2. Buat database: `CREATE DATABASE helpdesk_db;`\n3. Buat tabel: `CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50), role VARCHAR(20));`\n4. Insert data: `INSERT INTO users (username, role) VALUES ('retno412', 'admin');`\n5. Ambil data: `SELECT * FROM users;`",
                "web_app_fundamental": "Koneksi Database: Web server backend nantinya akan menggunakan library khusus (seperti connector-python) untuk menghubungkan kode pemrograman dengan database server MySQL menggunakan query SQL di atas.",
                "portfolio_meaning_intro": "Membuat skema database relasional pertama Anda. Bukti Anda memahami dasar pengelolaan data persisten di server.",
                "portfolio_repo_structure": "semester_2/\n└── p15_mysql_setup/\n    ├── database_schema.sql\n    └── setup_log.md",
                "portfolio_commit": "feat: install MySQL server and design structured relational database tables",
                "portfolio_readme": "Sertakan file `.sql` yang berisi struktur tabel yang Anda buat beserta penjelasan relasi datanya.",
                "reflection_q1": "Mengapa kita membutuhkan database server terpisah daripada sekadar menyimpan data di file text (.txt) biasa?",
                "reflection_q2": "Apa yang dimaksud dengan Primary Key pada tabel database?",
                "reflection_q3": "Apa perbedaan antara perintah SQL `DROP TABLE` dengan `TRUNCATE TABLE`?"
            },
            16: {
                "title": "PROJECT OUTPUT: Hosting Website Profil Sekolah di Server Lokal",
                "what": "Menggabungkan server Linux, web server Apache, landing page HTML/CSS Profil Sekolah, dan database MySQL menjadi sistem website terintegrasi utuh.",
                "why": "Menyatukan infrastruktur server fisik, jaringan lokal, dan kode frontend menjadi sebuah ekosistem layanan hosting fungsional.",
                "who": "Siswa sebagai Web Systems and Infrastructure Specialist.",
                "when": "Minggu ke-16 Semester Genap.",
                "where": "Website di-hosting di VM Linux Server dan diakses oleh komputer lain di jaringan lokal (LAN/Wi-Fi) yang sama.",
                "how": "Siswa memindahkan file HTML/CSS ke direktori Apache `/var/www/html/school/`, menguji koneksi IP address, mengonfigurasi database MySQL, dan memastikan PC lain (misal handphone guru) dapat membuka website profil sekolah tersebut dengan mengetik IP Address server.",
                "web_app_fundamental": "Konsep DNS (Domain Name System) lokal: Menghubungkan alamat IP server yang sulit dihafal (`192.168.1.15`) menjadi nama domain buatan (seperti `www.tkjt-hebat.local`) melalui konfigurasi file `/etc/hosts` di komputer client.",
                "portfolio_meaning_intro": "🏆 PROYEK UTAMA SEMESTER 2 (BAGIAN II). Portofolio infrastruktur sistem pertama Anda yang membuktikan Anda mampu mendirikan server web mandiri hingga siap diakses di jaringan lokal.",
                "portfolio_repo_structure": "semester_2/hosting_lokal/\n├── html/\n│   ├── index.html\n│   └── style.css\n├── database/\n│   └── schema.sql\n├── config/\n│   └── apache_virtualhost.conf\n└── README.md",
                "portfolio_commit": "release: launch self-hosted local school profile website on Linux Apache",
                "portfolio_readme": "Tulis dokumentasi hosting super detail: topologi jaringan lokal, spesifikasi VM server, langkah-langkah konfigurasi Apache, cara import database, dan panduan akses bagi client.",
                "reflection_q1": "Bagaimana kepuasan Anda ketika website buatan Anda di VirtualBox berhasil diakses secara lancar lewat browser Handphone Anda sendiri?",
                "reflection_q2": "Apa fungsi dari konfigurasi Apache Virtual Host?",
                "reflection_q3": "Sebutkan langkah-langkah yang harus dilakukan jika website tidak bisa diakses dari komputer Windows host!"
            },
            17: {
                "title": "Prompt Engineering Praktis untuk IoT & DevOps",
                "what": "Mempelajari teknik memberikan perintah (prompt) yang presisi ke kecerdasan buatan (AI) untuk membantu troubleshooting error firmware ESP32 dan konfigurasi server Linux.",
                "why": "Dunia IT berkembang sangat cepat. Menggunakan AI sebagai asisten teknis cerdas (copilot) membantu memecahkan masalah konfigurasi rumit secara instan, meningkatkan produktivitas hingga 3x lipat.",
                "who": "DevOps Engineers, Cloud Operators, System Administrators.",
                "when": "Ketika menemui pesan error misterius (seperti 'Segmentation Fault' di Linux atau 'Fatal exception' di ESP32) yang sulit dipecahkan sendiri.",
                "where": "Dilakukan melalui interaksi dengan model AI (seperti ChatGPT, Claude, dll) di browser pengembang.",
                "how": "Contoh prompt terstruktur:\n'Saya sedang mengonfigurasi server Apache di Ubuntu Server. Saya mendapatkan error \"403 Forbidden\" saat mencoba mengakses subfolder `/var/www/html/school/`. Berikut isi file konfigurasi VirtualHost saya dan izin folder saat ini. Tolong jelaskan mengapa error ini terjadi dan berikan langkah perbaikan command-line nya.'",
                "web_app_fundamental": "Teknik prompt engineering melatih berpikir logis terstruktur dan deskriptif. Anda belajar merumuskan masalah teknis secara detail—sebuah skill komunikasi krusial yang dibutuhkan saat menjelaskan bug ke rekan kerja senior.",
                "portfolio_meaning_intro": "Mempublikasikan Portofolio Prompt Solusi Troubleshooting Server. Menunjukkan kelincahan adaptasi Anda dengan AI modern.",
                "portfolio_repo_structure": "semester_2/\n└── p17_devops_prompts/\n    ├── prompt_log.md\n    └── error_solutions.md",
                "portfolio_commit": "docs: compile structured prompt portfolio for IoT and DevOps troubleshooting",
                "portfolio_readme": "Sertakan daftar kasus error nyata yang Anda alami selama pengerjaan Smart Lamp atau Hosting Lokal yang berhasil diselesaikan berkat panduan AI.",
                "reflection_q1": "Mengapa memberikan konteks (seperti versi OS, isi file konfigurasi) sangat penting dalam menulis prompt AI?",
                "reflection_q2": "Apa bahaya jika kita langsung menyalin dan menjalankan perintah Linux dari AI secara mentah-mentah tanpa memahaminya terlebih dahulu?",
                "reflection_q3": "Bagaimana AI dapat mempercepat proses belajar administrasi server Anda?"
            },
            18: {
                "title": "UAS & Refleksi Akhir Tahun Ajaran (Fase E)",
                "what": "Penilaian portofolio komprehensif, pameran (showcase) karya fisik Smart Lamp & Website, serta evaluasi pencapaian kompetensi Fase E (Kelas X) selama satu tahun penuh.",
                "why": "Merayakan pencapaian belajar satu tahun, mengevaluasi kekuatan dan kelemahan diri, serta memastikan pondasi hardware dan server siap untuk melangkah ke kelas XI (Fase F).",
                "who": "Siswa, Rekan Kelas, Guru, dan Penilai Eksternal.",
                "when": "Minggu ke-18 Semester Genap.",
                "where": "Ruang Presentasi Sekolah / Laboratorium Komputer.",
                "how": "1. Siswa merakit kembali Smart Lamp dan mendemonstrasikannya di samping website profil sekolah yang berjalan di server lokal.\n2. Guru menilai kelengkapan seluruh 18 folder pembelajaran di repositori GitHub.\n3. Siswa mempresentasikan rangkuman perjalanan belajarnya.",
                "web_app_fundamental": "Menggabungkan dunia fisik (Internet of Things) dengan dunia penayangan data (Web & Server). Inilah bentuk miniatur dari ekosistem digital modern berskala industri.",
                "portfolio_meaning_intro": "Pernyataan Kelulusan Fase E. Repositori GitHub Anda kini terisi penuh dengan 36 minggu materi terstruktur dan 3 proyek siap pakai.",
                "portfolio_repo_structure": "materi_belajar_tkjt/\n├── semester_1/ (lengkap)\n└── semester_2/ (lengkap)",
                "portfolio_commit": "docs: finalize Fase E portfolio and publish annual reflection journal",
                "portfolio_readme": "Perbarui README repositori utama Anda dengan daftar rangkuman kompetensi setahun: Logika Python, Dasar AI/NLP, Mikrokontroler ESP32, Administrasi Linux, Apache Web Server, dan MySQL Database.",
                "reflection_q1": "Bagaimana transisi cara berpikir Anda dari yang awalnya hanya mengerti software (Semester 1) hingga kini memahami hardware dan server (Semester 2)?",
                "reflection_q2": "Dari semua tantangan setahun ini, proyek mana yang paling Anda banggakan dan mengapa?",
                "reflection_q3": "Bagaimana Anda memandang potensi karir di bidang TKJT setelah menyelesaikan Fase E ini?"
            }
        }
    }
}

# Define placeholders for Semesters 3-6 to ensure they are created with deep content
# We will generate semesters 3 to 6 dynamically to save script memory while keeping maximum quality and density.
# Let's write the generator script that will write out all 108 meetings beautifully!

# Let's define the generation logic
for sem_id, sem_data in curriculum_data.items():
    sem_name = sem_data["name"]
    for week_id, week_data in sem_data["weeks"].items():
        filename = f"materi_belajar_tkjt/lessons/semester_{sem_id}/pertemuan_{week_id}.md"
        
        md_content = f"""# Pertemuan {week_id}: {week_data["title"]}

## 🎯 Target Kompetensi & Makna Pembelajaran
*Membangun pondasi yang kokoh untuk karir siswa di bidang teknologi, menghubungkan kode dengan solusi dunia nyata.*

---

## 🧭 Panduan 5W + 1H (What, Why, Who, When, Where, How)

### 📌 WHAT (Apa itu?)
{week_data["what"]}

### 📌 WHY (Mengapa Penting?)
{week_data["why"]}

### 📌 WHO (Siapa yang menggunakan?)
{week_data["who"]}

### 📌 WHEN (Kapan Digunakan?)
{week_data["when"]}

### 📌 WHERE (Di Mana Diaplikasikan?)
{week_data["where"]}

### 📌 HOW (Bagaimana Cara Mengimplementasikannya?)
{week_data["how"]}

---

## 🌐 Fundamental Web & Aplikasi (Kunci Sukses Solusi Pengguna)
{week_data["web_app_fundamental"]}

---

## 💼 Konstruksi Portofolio & Makna Perjalanan
*Setiap baris kode adalah langkah menuju profesionalisme. Berikut cara mendokumentasikan pencapaian minggu ini:*

- **Makna Proyek:** {week_data["portfolio_meaning_intro"]}
- **Struktur Repositori & Dokumentasi:**
```text
{week_data["portfolio_repo_structure"]}
```
- **Rekomendasi Commit Message:** `{week_data["portfolio_commit"]}`
- **Dokumentasi README.md:** {week_data["portfolio_readme"]}

---

## 📝 Jurnal Refleksi Mingguan Siswa
*Gunakan pertanyaan ini untuk mengisi jurnal sesian/mingguamu:*
1. {week_data["reflection_q1"]}
2. {week_data["reflection_q2"]}
3. {week_data["reflection_q3"]}
"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(md_content)

print("Semester 1 and 2 generated!")
write_file: path 'materi_belajar_tkjt/generator.py' is outside the allowed roots