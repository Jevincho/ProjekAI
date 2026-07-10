# Rembg-Fuse: Background Removal & Image Editor

## 🎯 Apa itu Rembg-Fuse?

Rembg-Fuse adalah aplikasi web yang menggunakan **kecerdasan buatan (AI)** untuk:

- ✅ **Menghapus background** gambar otomatis
- ✅ **Mengubah warna background** sesuai keinginan
- ✅ **Mengedit gambar** dengan berbagai filter (brightness, contrast, blur, dll)
- ✅ Bekerja di **browser** (tidak perlu install aplikasi tambahan)

---

## 💻 Persyaratan Sistem

Sebelum mulai, pastikan Anda memiliki:

### 1. **Python 3.8+**

- Download dari: https://www.python.org/downloads/
- **Penting**: Saat install, centang ✓ **"Add Python to PATH"**

### 2. **pip** (Package Manager untuk Python)

- Biasanya sudah ada saat install Python
- Cek dengan buka Command Prompt dan ketik: `pip --version`

### 3. **Koneksi Internet**

- Untuk download model AI pertama kali (~100-500 MB tergantung model)

---

## 🚀 Cara Setup & Menjalankan

### Step 1: Download File Project

1. Download file project ini atau clone dari GitHub
2. Extract folder ke lokasi yang mudah diakses
   - Contoh: `C:\Users\YourName\Documents\rembg-fuse`

### Step 2: Buka Folder Project

- **Windows**: Buka Command Prompt atau PowerShell
- **Mac/Linux**: Buka Terminal

Navigasi ke folder project:

```bash
cd path/to/rembg-fuse-main
```

Contoh Windows:

```bash
cd C:\Users\Louis\SEM4_ArtificialIntelligence\Proyek UTS 1 - Copy\Rembg-Fuse-main
```

### Step 3: Install Dependencies (Library Python)

Jalankan perintah ini di Command Prompt/Terminal untuk install semua library yang dibutuhkan:

```bash
pip install -r web_app/requirements.txt
```

**Apa itu dependencies?**

- Dependencies adalah library/paket yang diperlukan aplikasi untuk berjalan
- Perintah di atas akan install: Flask, Pillow, Rembg, dan library lainnya
- Tunggu hingga selesai (bisa memakan waktu 5-10 menit)

### Step 4: Jalankan Aplikasi

Setelah install selesai, jalankan aplikasi dengan perintah:

**Windows (PowerShell/CMD):**

```bash
python -m flask --app web_app.app run --debug
```

**Mac/Linux:**

```bash
python3 -m flask --app web_app.app run --debug
```

### Step 5: Buka di Browser

Setelah melihat pesan seperti ini:

```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

**Buka browser** dan ketik alamat berikut:

```
http://localhost:5000
```

atau

```
http://127.0.0.1:5000
```

**Selesai! Aplikasi sudah siap digunakan** 🎉

---

## 📖 Cara Menggunakan Aplikasi

Setelah aplikasi terbuka di browser, Anda akan melihat 3 tab:

### Tab 1: 🎨 **Editor Lengkap** (TAB UTAMA)

Fitur untuk mengedit gambar dengan berbagai kontrol:

**Upload Gambar:**

- Klik area upload atau drag & drop gambar ke kotak upload
- Gambar akan ditampilkan di panel preview

**Kontrol Rotasi & Flip:**

- `↻ 90°` = Putar gambar 90 derajat ke kanan
- `↺ -90°` = Putar gambar 90 derajat ke kiri
- `↔️ Flip H` = Balik horizontal (kiri ↔ kanan)
- `↕️ Flip V` = Balik vertikal (atas ↔ bawah)

**Adjustment Sliders:**

- **☀️ Brightness** = Tingkat kecerahan (0.5 = lebih gelap, 2.0 = lebih terang)
- **📊 Contrast** = Tingkat kontras gambar
- **🌈 Saturation** = Intensitas warna (0 = grayscale, 2.0 = super colorful)
- **💨 Blur** = Efek blur (0-15 pixel)

**Resize Image:**

- Input width dan height (ukuran) gambar
- Klik "Apply" untuk mengubah ukuran

**Efek Khusus:**

- `🖤 Gray` = Ubah ke hitam putih
- `🔱 Sharp` = Perjelas detail gambar
- `🔲 Edge` = Deteksi tepi/border
- `⚫ Invert` = Balikkan warna

**Tombol Aksi:**

- `🔄 Reset Semua` = Batalkan semua perubahan, kembali ke gambar original
- `⬇️ Download` = Unduh hasil edit ke komputer

---

### Tab 2: 🗑️ **Hapus Background**

Fitur khusus untuk menghapus background gambar dengan AI:

**Cara Kerja:**

1. Pilih model AI (semakin baik modelnya, semakin lama prosesnya)
2. Upload gambar
3. Tunggu AI memproses (biasanya 10-30 detik)
4. Gambar dengan background transparan akan muncul
5. Klik "Download" untuk simpan

**Model AI yang Tersedia:**

- **U2Net-P** = Paling cepat, ukuran kecil (4 MB), cocok untuk prototipe
- **U2Net** = Standar, akurasi bagus (168 MB)
- **ISNet** = Kualitas tinggi, hasil terbaik (170 MB)
- **Silueta** = Ringan, untuk silhouette (43 MB)

---

### Tab 3: 🎯 **Set Warna Background**

Fitur untuk mengubah warna background gambar transparan:

**Cara Kerja:**

1. Upload gambar dengan background transparan (PNG hasil dari Tab 2)
2. Pilih warna background:
   - **Color Picker** = Klik kotak warna untuk pilih warna custom
   - **Preset Buttons** = 6 warna siap pakai (Putih, Hitam, Merah, Hijau, Biru, Kuning)
3. Klik `👁️ Preview` untuk lihat hasil
4. Klik "Download" untuk simpan

---

## 📋 Fitur Lengkap (20 Fitur)

1. ✅ **Remove Background** - Hapus background dengan AI
2. ✅ **Set Background Color** - Ubah warna background
3. ✅ **Rotate Image** - Putar gambar
4. ✅ **Flip Horizontal** - Balik kiri-kanan
5. ✅ **Flip Vertical** - Balik atas-bawah
6. ✅ **Adjust Brightness** - Kontrol kecerahan
7. ✅ **Adjust Contrast** - Ubah kontras
8. ✅ **Adjust Saturation** - Intensitas warna
9. ✅ **Resize Image** - Ubah ukuran gambar
10. ✅ **Blur Background** - Aplikasikan blur
11. ✅ **Grayscale** - Ubah ke hitam putih
12. ✅ **Sharpen Image** - Perjelas detail
13. ✅ **Edge Detection** - Deteksi tepi
14. ✅ **Invert Colors** - Balikkan warna
15. ✅ **Multiple AI Models** - 4+ pilihan model
16. ✅ **Color Picker** - Pilih warna custom
17. ✅ **Real-time Preview** - Lihat perubahan langsung
18. ✅ **Drag & Drop Upload** - Upload dengan mudah
19. ✅ **Download Results** - Unduh hasil
20. ✅ **Responsive Design** - Bekerja di semua perangkat

---

## 🎯 Workflow Contoh

### Scenario: Buat Foto Produk dengan Background Warna Kustom

**Step 1: Buka Tab "Hapus Background"**

- Upload foto produk Anda
- Tunggu AI memproses (~15 detik)
- Download gambar (background sudah transparan)

**Step 2: Buka Tab "Set Warna Background"**

- Upload gambar hasil Step 1
- Pilih warna background (contoh: biru)
- Klik Preview untuk lihat hasil
- Download gambar final

**Selesai!** Anda sekarang punya foto produk dengan background biru yang professional 🎉

---

## ⚠️ Troubleshooting

### ❌ Error: "ModuleNotFoundError: No module named 'rembg'"

**Solusi:**

```bash
pip install rembg
```

### ❌ Error: "ModuleNotFoundError: No module named 'flask'"

**Solusi:**

```bash
pip install flask
```

### ❌ Error: "Port 5000 already in use"

**Solusi 1:** Tutup aplikasi lain yang menggunakan port 5000

**Solusi 2:** Gunakan port berbeda:

```bash
python -m flask --app web_app.app run --debug --port 5001
```

Kemudian buka: `http://localhost:5001`

### ❌ Aplikasi lambat / memakan RAM banyak

**Solusi:**

- Gunakan model yang lebih ringan (U2Net-P)
- Kurangi ukuran gambar input sebelum di-process
- Tutup aplikasi lain yang sedang berjalan

### ❌ "Download tidak berfungsi"

**Solusi:**

- Cek apakah browser memungkinkan download
- Coba browser lain (Chrome, Firefox, Edge)
- Periksa folder Downloads

---

## 🔄 Menghentikan Aplikasi

Untuk menghentikan aplikasi, tekan di Command Prompt/Terminal:

```
CTRL + C
```

Atau tekan `Ctrl` dan `C` bersamaan.

---

## 📞 FAQ (Pertanyaan Umum)

**Q: Gambar saya tidak ter-upload?**
A: Pastikan format gambar adalah JPG, PNG, GIF, atau BMP dan ukurannya kurang dari 50MB

**Q: Proses hapus background sangat lambat?**
A: Model AI memang memakan waktu. Pertama kali dijalankan, modelnya harus diunduh (~300-500 MB). Lain kali akan lebih cepat.

**Q: Bisakah saya gunakan aplikasi ini offline?**
A: Tidak untuk proses background removal (butuh AI model). Tapi interface-nya bisa diakses offline setelah model diunduh.

**Q: Apakah file saya aman?**
A: File diproses di server lokal Anda sendiri, tidak dikirim ke cloud. Lebih aman! ✅

---

## 🔧 Struktur Folder Project

```
rembg-fuse-main/
├── web_app/              ← Aplikasi web utama
│   ├── app.py           ← Backend Flask
│   ├── requirements.txt  ← Library yang dibutuhkan
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css    ← Styling/tampilan
│   │   └── js/
│   │       └── main.js      ← Fungsi interaktif
│   ├── templates/
│   │   └── index.html       ← Halaman utama
│   ├── utils/
│   │   └── config.py        ← Konfigurasi
│   └── uploads/             ← Folder temp untuk gambar
├── Rembg/               ← Library AI untuk hapus background
├── BGSetter/            ← Library untuk set warna
└── README.md            ← Dokumentasi ini
```

---

## 📚 Pelajari Lebih Lanjut

- **Rembg Library**: https://github.com/danielgatis/rembg
- **Flask Framework**: https://flask.palletsprojects.com/
- **Python Documentation**: https://docs.python.org/3/

---

## ✨ Tips & Tricks

**Tip 1: Batch Processing**

- Anda bisa membuka beberapa tab browser dan proses gambar secara parallel

**Tip 2: Best Practices untuk Remove Background**

- Gunakan gambar dengan pencahayaan yang baik
- Background yang solid (satu warna) menghasilkan hasil terbaik
- Objek harus jelas terpisah dari background

**Tip 3: Color Setting**

- Format: RGB (0-255)
- RGB(255,255,255) = Putih
- RGB(0,0,0) = Hitam
- RGB(255,0,0) = Merah Murni

---

## 📝 Version History

- **v2.0** (Current) - Added Editor Lengkap + 20 Fitur + Real-time Preview
- **v1.0** - Basic Remove Background + Color Setting

---

## 📄 License

MIT License - Bebas digunakan untuk keperluan komersial maupun personal

---

## ❤️ Credits

- **Rembg**: https://github.com/danielgatis/rembg
- **Pillow**: Image processing library
- **Flask**: Web framework

---

## 🎉 Selesai!

Anda sudah siap menggunakan Rembg-Fuse! 🚀

**Pertanyaan atau masalah?** Cek bagian Troubleshooting di atas atau coba jalankan lagi dari Step 1.

**Happy editing!** 🎨✨

<img width="1918" height="752" alt="Screenshot 2025-08-16 172203" src="https://github.com/user-attachments/assets/bc2019c4-3a2c-426f-a128-e8de8b60f209" />

---

## 📋 Daftar Isi

- [Fitur Rembg](#-fitur-rembg)
- [Fitur BGSetter](#-fitur-bgsetter)
- [Fitur Web App](#-fitur-web-app-baru) ⭐ **BARU**
- [Instalasi & Setup](#-instalasi--setup)
- [Cara Menjalankan](#-cara-menjalankan)
- [Workflow Lengkap](#-workflow-rembg--bgsetter)

---

## 🔧 Fitur Rembg

### Fitur Utama

- ✅ **AI-Powered Background Removal** - Menggunakan teknologi U-2-Net dan model AI terbaru untuk menghilangkan background dengan presisi tinggi
- 🎞️ **DaVinci Resolve Fusion Integration** - Plugin native terintegrasi langsung di DaVinci Resolve editor
- 🛠️ **Lightweight Implementation** - Script-based Python + Fuse, mudah diinstal tanpa perlu software tambahan
- 🧩 **Kompatibel** - Bekerja di Free version maupun Studio version DaVinci Resolve 18+
- 🆓 **100% Open Source** - Free dan dapat dimodifikasi sesuai kebutuhan
- 📊 **Real-time Workflow** - Lihat hasil removal langsung di Fusion editor
- 🎯 **Multiple AI Models** - Pilih dari 12+ model AI untuk berbagai keperluan

### Fitur Pendukung

- 🔄 **Automatic Model Download** - Download dan cache model secara otomatis saat pertama kali digunakan
- ⚙️ **Rembg Manager GUI** - Setup wizard yang memandu instalasi tanpa perlu command line
- 💾 **Model Selection** - Pilih model AI sesuai kebutuhan task Anda (u2net, u2netp, isnet, birefnet, dll)
- 🖥️ **GPU Support** - CUDA untuk NVIDIA dan ROCM untuk AMD untuk processing lebih cepat
- 🔧 **Manual Setup Option** - Opsi instalasi manual jika diperlukan troubleshooting
- 📝 **Logging & Debugging** - Console logging di DaVinci Resolve untuk tracking progress dan error
- 🎥 **Batch Processing Ready** - Architecture yang support multiple clips processing
- 🔄 **Model Reloading** - Switch antar model tanpa perlu restart DaVinci Resolve
- 📚 **Comprehensive Documentation** - Wiki dengan troubleshooting guide lengkap
- 🌐 **Community Support** - Repository terbuka untuk kontribusi dan Q&A

---

## 🎨 Fitur BGSetter

### Fitur Utama

- 🖼️ **Real-time Image Preview** - Lihat gambar input (original) dan output (processed) berdampingan secara live
- 🎯 **RGB Color Adjustment** - Atur warna background dengan slider RGB (0-255) dengan kontrol penuh
- 🎨 **Instant Preview Update** - Preview gambar output berubah seketika saat menggeser slider warna tanpa delay
- 💾 **Direct Output Save** - Simpan gambar hasil langsung ke file explorer dengan satu klik tombol
- 🖱️ **Multiple Color Input Methods** - Pilih warna melalui slider RGB, color picker dialog, atau preset buttons

### Fitur Pendukung

- 🎯 **Preset Color Buttons** - 6 warna siap pakai: White, Black, Red, Green, Blue, Yellow untuk quick selection
- 🌈 **Windows Color Picker** - Dialog native untuk memilih warna custom dari unlimited color palette
- 📐 **RGB Value Display** - Real-time display nilai RGB saat ini (0-255) dan format Hex color (#RRGGBB)
- 🏷️ **Image Information** - Tampilkan dimensi gambar (width x height pixels) dan info file
- 📊 **Status Logging** - Log lengkap semua operasi, processing time, dan error messages untuk debugging
- 🔄 **Live Preview Update** - Setiap gerakan slider langsung update preview tanpa wait/refresh
- 💡 **User-Friendly UI** - Interface modern dengan dark theme yang nyaman untuk mata
- ⚡ **Fast Processing** - Processing cepat dengan hasil berkualitas tinggi tanpa kompresi
- 📦 **PNG Support** - Full support PNG format dengan alpha channel (transparency/transparan)
- 🧹 **Clear All** - Reset semua input, preview, dan kembali ke state awal dengan satu tombol
- 🔒 **Prevent Errors** - Validasi input untuk mencegah file mismatch atau invalid operations
- 🎞️ **Batch Processing Ready** - Core logic support multiple images, GUI dapat diperluas untuk batch

---

## 🌐 Fitur Web App ⭐ **BARU**

### Fitur Utama

- 🎯 **Dual Functionality** - Hapus background dan ubah warna dalam satu website
- 🎨 **Modern Interface** - Design modern dengan dark theme yang elegan
- 📱 **Fully Responsive** - Sempurna di desktop, tablet, dan mobile devices
- ⚡ **Real-time Processing** - Hasilkan output dalam hitungan detik
- 👁️ **Color Live Preview** - Lihat preview warna sebelum disimpan
- 🐉 **Drag & Drop** - Upload gambar dengan drag & drop yang mudah
- 🚀 **Production Ready** - Siap deploy ke production (Heroku, Docker, AWS, dsb)
- 📊 **Multiple AI Models** - Pilih dari 4+ model AI untuk hasil optimal
- 💾 **Direct Download** - Download hasil langsung ke perangkat
- 🔐 **Secure** - File diproses dan dihapus otomatis

### Fitur Teknis

- ✅ **Flask Backend** - Framework Python yang ringan dan powerful
- 🎪 **REST API** - API lengkap untuk integrasi ke aplikasi lain
- 🐳 **Docker Support** - Docker & Docker Compose ready
- 📦 **Gunicorn WSGI** - Production-grade server
- 🌍 **Nginx Compatible** - Siap dengan Nginx reverse proxy
- 🔄 **Automatic Cleanup** - Hapus file lama otomatis
- 📝 **Comprehensive Logging** - Complete logging untuk debugging
- 🛡️ **Input Validation** - Validasi file dan size
- 💬 **API Documentation** - Dokumentasi API lengkap

---

## 📦 AI Models yang Tersedia di Rembg

| Model                 | Tipe         | Ukuran | Kegunaan                                                      |
| --------------------- | ------------ | ------ | ------------------------------------------------------------- |
| **u2net**             | General      | 168 MB | Segmentasi umum berkualitas tinggi, semua jenis background    |
| **u2netp**            | Lightweight  | 4 MB   | Fast processing dengan resource rendah, ideal untuk real-time |
| **u2net_human_seg**   | Specialized  | 168 MB | Background removal khusus foto manusia/portrait               |
| **u2net_cloth_seg**   | Specialized  | 168 MB | Segmentasi pakaian dan cloth areas                            |
| **isnet-general-use** | General      | 170 MB | Segmentasi general purpose dengan akurasi bagus               |
| **isnet-anime**       | Anime        | 168 MB | Optimized untuk anime-style images dan illustrations          |
| **silueta**           | Silhouette   | 43 MB  | Untuk silhouette, outline, dan shadow effects                 |
| **sam**               | Advanced     | 400 MB | Segment Anything Model - versatile untuk berbagai objek       |
| **birefnet-general**  | High-Quality | 928 MB | Hasil maksimal untuk general use dengan akurasi tertinggi     |
| **birefnet-portrait** | Portrait     | 928 MB | Specialized untuk portrait/wajah dengan detail halus          |
| **ben2-base**         | Efficient    | 213 MB | Background removal yang balance antara speed dan quality      |

---

## ⚙️ Instalasi & Setup

### Prerequisites

- **Python**: 3.8 atau lebih tinggi (recommended: 3.11+)
- **pip**: Package manager (biasanya sudah terinstall dengan Python)
- **OS**: Windows 7+, Linux, atau macOS
- **RAM**: 4GB minimum (8GB recommended untuk model besar)
- **Storage**: 500MB+ untuk model downloads

### Step 1: Download & Setup Project

```bash
# Clone atau download repository
git clone https://github.com/Akascape/Rembg-Fuse.git
cd Rembg-Fuse
```

### Step 2: Install Rembg Dependencies

```bash
# Masuk ke folder Rembg
cd Rembg

# Install rembg package
pip install rembg
```

**Optional - GPU Support:**

- NVIDIA CUDA: `pip install rembg[gpu]`
- AMD ROCM: `pip install rembg[rocm]`

### Step 3: Install BGSetter Dependencies

```bash
# Masuk ke folder BGSetter
cd ../BGSetter

# Install dependencies
pip install -r requirements.txt
```

**Packages yang diinstall:**

- `Pillow >= 10.0.0` - Image processing library
- `NumPy >= 1.24.0` - Numerical computing

### Step 4: (Optional) Setup Rembg untuk DaVinci Resolve

Jika ingin gunakan plugin di DaVinci Resolve:

1. Copy folder `Rembg` ke plugin directory DaVinci Resolve:
   - Windows: `C:\Program Files\DaVinci Resolve\Fusion\Plugins\`
   - Linux: `/opt/DaVinci/Fusion/Plugins/`
   - macOS: `/Applications/DaVinci Resolve/Fusion/Plugins/`

2. Restart DaVinci Resolve

3. Buka Fusion page, cari "Rembg" di node menu (Shift+Spacebar)

---

## 🚀 Cara Menjalankan

### REMBG - 3 Pilihan Setup

#### Pilihan 1️⃣: Automatic Setup (RECOMMENDED - Paling Mudah)

```bash
cd Rembg
python rembg_manager.py
```

**Apa yang terjadi:**

- GUI wizard akan membuka
- Follow step-by-step instructions
- Download model otomatis
- Setup selesai dalam beberapa klik

#### Pilihan 2️⃣: Manual Setup (Untuk Advanced User)

```bash
# Di Python atau Jupyter
import rembg

# Download model u2net
rembg.new_session("u2net")

# Ulangi untuk model lain jika perlu
rembg.new_session("u2netp")
rembg.new_session("birefnet-general")
```

Kemudian tambahkan model names ke `Rembg/models.txt` (satu per line)

#### Pilihan 3️⃣: Direct Use dalam Script Python

```python
from rembg import remove
from PIL import Image

# Buka gambar original
input_img = Image.open("photo.jpg")

# Remove background menggunakan model u2net_human_seg
output_img = remove(input_img, model_name="u2net_human_seg")

# Simpan hasil (dengan alpha channel)
output_img.save("photo_no_background.png")
print("✅ Background removed successfully!")
```

---

### BGSETTER - Jalankan Aplikasi GUI

```bash
cd BGSetter
python bg_setter_gui.py
```

Atau **double-click** file `bg_setter_gui.py`

**GUI akan terbuka dengan:**

- Panel kiri: Control untuk RGB adjustment
- Panel kanan: Preview original image + processed image
- Status log untuk tracking operasi

---

### 🌐 WEB APP - Jalankan Interface Modern (RECOMMENDED untuk Production)

Rembg-Fuse sekarang tersedia sebagai **website modern yang siap production** dengan interface yang user-friendly!

#### Quick Start Web App

**Windows:**

```bash
# Double-click file ini
launch_web.bat
```

**macOS/Linux:**

```bash
# Jalankan script
bash launch_web.sh
```

**Manual (Semua OS):**

```bash
# Install dependencies
pip install -r web_app/requirements.txt

# Jalankan development server
python -m flask --app web_app.app run --debug
```

Kemudian buka browser: **http://localhost:5000**

#### Fitur Web App

✨ **Features:**

- 🎨 Modern dark theme interface
- 📱 Responsive design (mobile/tablet/desktop)
- 🎯 Drag & drop file upload
- ⚡ Real-time processing
- 👁️ Live preview dengan color picker
- 📊 Support multiple AI models
- 💾 Direct download hasil processing
- 🚀 Production-ready (siap deploy)

#### Deployment Web App

**Docker Deployment:**

```bash
# Build image
docker build -t rembg-fuse .

# Run container
docker run -p 5000:5000 rembg-fuse
```

**Docker Compose:**

```bash
docker-compose up -d
```

**Heroku Deployment:**

```bash
heroku create your-app-name
git push heroku main
```

**Detailed Deployment Guide:** Lihat [DEPLOYMENT.md](./DEPLOYMENT.md)

**Web App Documentation:** Lihat [web_app/README.md](./web_app/README.md)

---

## 🎯 Workflow Rembg → BGSetter

### Workflow Lengkap: Hapus Background & Atur Warna Custom

#### Scenario: Foto Produk → Remove BG → Set Custom Color

**Step 1: Persiapkan Gambar Input**

- Siapkan foto/gambar asli (JPG, PNG, atau format lain)
- Simpan di folder mudah diakses

**Step 2: Remove Background dengan Rembg**

```python
from rembg import remove
from PIL import Image

# Buka gambar original
print("Opening image...")
img = Image.open("product_photo.jpg")

# Hilangkan background
print("Removing background...")
img_no_bg = remove(img, model_name="u2net")

# Simpan hasil (HARUS PNG untuk preserve transparency!)
img_no_bg.save("product_no_bg.png")
print("✅ Step 1 Done: photo_no_bg.png")
```

**Output**: File `product_no_bg.png` dengan background transparan

**Step 3: Jalankan BGSetter**

```bash
cd BGSetter
python bg_setter_gui.py
```

**Step 4: Gunakan BGSetter untuk Set Warna**

1. **Buka Gambar**
   - Klik tombol "Select Input Image"
   - Pilih file `product_no_bg.png`
   - Gambar muncul di panel preview sebelah kiri

2. **Pilih Warna Background**
   - Option A: Geser **RGB Sliders** untuk custom color dengan preview real-time
   - Option B: Klik **"Choose Color"** untuk buka Windows color picker
   - Option C: Klik salah satu **Preset Button** (White, Black, Red, dll)

3. **Lihat Preview Real-time**
   - Panel sebelah kanan akan menampilkan hasil dengan warna yang dipilih
   - Update instantly saat Anda menggeser slider!

4. **Simpan Hasil**
   - Klik **"Save Output Image"**
   - Pilih lokasi penyimpanan
   - Gambar final tersimpan dengan background color custom

**Output**: File PNG final dengan background color sesuai keinginan

**Step 5: Gunakan Gambar Final**

- Import ke DaVinci Resolve untuk video editing
- Atau gunakan di aplikasi lain (Photoshop, web, dll)

---

## 💡 Tips & Tricks

### Rembg Tips:

- ✅ Gunakan `u2net` untuk hasil terbaik (168 MB, processing lebih lama)
- ✅ Gunakan `u2netp` untuk kecepatan (4 MB, lightweight)
- ✅ Gunakan `u2net_human_seg` untuk foto manusia
- ✅ Gunakan GPU support untuk processing 5-10x lebih cepat
- ✅ Try multiple models untuk mendapat hasil terbaik

### BGSetter Tips:

- ✅ Selalu gunakan **PNG input** (dengan transparency/alpha channel)
- ✅ RGB Value: 0 = min, 255 = max brightness
  - 255,255,255 = White
  - 0,0,0 = Black
  - 255,0,0 = Pure Red
- ✅ Gunakan **Preset buttons** untuk quick color selection
- ✅ Gunakan **RGB Sliders** untuk fine-tuning warna
- ✅ Preview update real-time → lihat perubahan langsung tanpa delay!
- ✅ Check RGB display untuk nilai pasti dari warna yang dipilih

### Workflow Best Practices:

1. Rembg untuk remove background → output PNG
2. BGSetter untuk set warna custom → output PNG final
3. Import ke DaVinci Resolve / aplikasi editing lain
4. Atau gunakan multiple BGSetter output dengan warna berbeda untuk variations

---

## 🎞️ Video Demo

[<img src="https://img.youtube.com/vi/Lv8DGq7qbx4/0.jpg" width=40% height=40%>](https://youtu.be/Lv8DGq7qbx4)

---

## 🌱 Project Info

| Aspek                  | Keterangan                                           |
| ---------------------- | ---------------------------------------------------- |
| **Rembg Version**      | 0.3                                                  |
| **BGSetter Version**   | 2.0                                                  |
| **DaVinci Resolve**    | Free or Studio: 18+                                  |
| **Python Requirement** | 3.8 - 3.13                                           |
| **License**            | MIT                                                  |
| **Copyright**          | 2026                                                 |
| **Rembg Author**       | Akash Bora                                           |
| **Rembg Library**      | [Daniel Gatis](https://github.com/danielgatis/rembg) |

---

## 🐞 Troubleshooting

### ModuleNotFoundError: No module named 'rembg'

```bash
pip install rembg
```

### No module named 'PIL' atau 'pillow'

```bash
pip install pillow
```

### Tkinter error (GUI tidak muncul)

- **Windows**: Usually built-in
- **Linux**: `sudo apt-get install python3-tk`
- **macOS**: `brew install python-tk`

### BGSetter preview tidak update

- Pastikan file PNG sudah ter-load dengan benar
- Check input label menunjukkan filename
- Resize window jika canvas terlalu kecil

### Rembg processing sangat lambat

- Install GPU support: `pip install rembg[gpu]`
- Atau gunakan model lebih ringan: `u2netp`

### Memory error saat processing

- Gunakan model lebih ringan/lightweight
- Kurangi ukuran/resolusi gambar input sebelumnya

### DaVinci Resolve tidak menemukan Rembg plugin

- Pastikan folder `Rembg` di lokasi plugin yang benar
- Restart DaVinci Resolve
- Check console untuk error messages

---

## 📂 Struktur Folder Project

```
Rembg-Fuse/
├── README.md                     ← Dokumentasi lengkap (file ini)
├── LICENSE                       ← MIT License
│
├── Rembg/                        ← Background Removal Modul
│   ├── bg_remover.py            ← Core removal logic
│   ├── rembg_manager.py         ← Setup wizard GUI
│   ├── models.txt               ← List model terdownload
│   └── Rembg.fuse               ← Plugin untuk DaVinci Resolve
│
└── BGSetter/                     ← Background Color Setter Modul
    ├── bg_setter_gui.py         ← Main GUI aplikasi (RUN THIS!)
    ├── bg_setter.py             ← Core color setting logic
    ├── requirements.txt         ← Python dependencies
    └── README.md                ← BGSetter documentation
```

---

## 🚀 Quick Start

**Untuk user yang terburu-buru:**

```bash
# 1. Setup BGSetter (3 minutes)
cd BGSetter
pip install -r requirements.txt

# 2. Run aplikasi
python bg_setter_gui.py

# 3. Load image → Atur warna → Save hasil ✅
```

---

## 📚 Full Documentation

- 📖 [BGSetter README](./BGSetter/README.md) - Dokumentasi BGSetter
- 🎬 [Rembg Official Repo](https://github.com/danielgatis/rembg) - Dokumentasi Rembg Library
- 🔧 [Troubleshooting Wiki](https://github.com/Akascape/Rembg-Fuse/wiki/Troubleshooting-Guide) - Panduan troubleshooting

---

## 🤝 Contributing

Kontribusi welcome! Anda dapat:

- 🐛 Report bugs
- 💡 Suggest features
- 📝 Submit pull requests
- 📚 Improve documentation

---

## ❤️ Credits & Support

- **Rembg Plugin**: Akash Bora
- **Rembg Library**: [Daniel Gatis](https://github.com/danielgatis/rembg)
- **BGSetter**: Custom development

**Get more Resolve plugins at [www.akascape.com](https://www.akascape.com) 👈**

---

## 📄 License

MIT License - Lihat file [LICENSE](./LICENSE) untuk detailnya

---

## 🎉 Selesai!

Anda sudah siap menggunakan **Rembg-Fuse**! 🚀

**Next Step**: Buka terminal dan jalankan:

```bash
cd BGSetter
python bg_setter_gui.py
```

**Questions?** Cek troubleshooting section atau baca dokumentasi di folder masing-masing.

---

**Last Updated**: April 2026  
**Status**: Production Ready ✅
