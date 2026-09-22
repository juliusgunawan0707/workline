# Workline — Panduan Pakai

*(Sebelumnya bernama "Nusakerja" — di-rebrand ke Workline. Folder proyek diganti dari `nusakerja/` menjadi `workline/` pada 2026-09-19; URL dan data tidak berubah. Versi aplikasi ada di halaman Pengaturan — saat ini **v2.1**.)*

**Aplikasi:** buka `index.html` — satu berkas, tanpa pemasangan, tanpa server.
**Data awal:** demo bawaan (orang, unit, dan dokumen fiktif) termuat otomatis saat pertama dibuka.

## Bahasa &amp; tema

- Tombol **EN / ID** di kanan atas. Default: **English**. Pilihan tersimpan di browser Anda.
- Ikon matahari/bulan di sampingnya mengganti tema terang/gelap. Default: **gelap**.
- **Dokumen yang dihasilkan (Rekap Presensi, Notulensi, kalimat realisasi EKP) selalu dalam Bahasa Indonesia**, apa pun bahasa antarmuka yang dipilih — karena dokumen itu masuk ke sistem presensi dan EKP resmi berbahasa Indonesia. Yang berganti bahasa hanya label, tombol, dan menu.
- Font: **Poppins**.

---

## Prinsip

Catat sekali saat mengerjakan. Presensi harian, rekap SKP, dan draf EKP dihasilkan dari catatan itu — tidak ada pengetikan ulang.

```
Quick Add → To-Do → Daily Log → Tutup Hari → Rekap Presensi
                 ↘ Project ↘ SKP ↘ EKP
Kalender → Notulensi → Create Task ↗
```

---

## 1. Mencatat pekerjaan (10 detik)

Kotak di bagian atas selalu siap. Ketik satu baris lalu Enter:

```
09.00-10.30 Rapat revisi anggaran #dashboard @7 !tinggi
```

| Kode | Arti | Contoh |
|---|---|---|
| `09.00-10.30` | jam mulai–selesai (durasi terhitung otomatis) | `13.00-14.30` |
| `#nama` | project terkait (cocokkan awal nama) | `#survei`, `#dashboard` |
| `@n` | indikator SKP nomor n | `@7`, `@i8b` |
| `!prioritas` | Mendesak / Tinggi / Sedang / Rendah | `!mendesak` |
| `/kategori` | kategori pekerjaan | `/telaah`, `/layanan` |
| `besok` `kemarin` `lusa` `18/9` | tanggal | `besok` |

Chip pratinjau muncul di bawah kotak sebelum Enter — periksa hasil parsing di situ.
Kalau ada jam mulai **dan** selesai, status langsung jadi **Selesai**. Kalau tidak, statusnya Belum Dimulai dan bisa dijalankan dengan tombol **Mulai** / **Selesai** (mengisi jam otomatis).

Pintasan: `Ctrl+K` fokus ke kotak catat, `Ctrl+/` pencarian global.

---

## 2. Ritual sore — "Tutup Hari"

Ada di Dashboard, Daily Log, dan Kalender.

1. **Rekap Presensi** — dihasilkan penuh oleh perhitungan, bukan AI. Bernomor, tanpa jam, **maksimal 5 baris**, sesuai kolom presensi. Penghitung baris & karakter ada di bawah kotak (merah kalau melanggar). Tombol **Salin** langsung tempel ke aplikasi presensi.
   Kalau pekerjaan lebih dari 5, empat teratas ditulis utuh dan sisanya diringkas pada baris kelima.
   Tombol **Perhalus dengan AI** hanya memperbaiki diksi — jumlah baris wajib sama dan tidak boleh ada angka baru, kalau melanggar keluaran AI ditolak otomatis.
   Kalau Anda mengubah sendiri kalimatnya, tombol **Simpan Revisi** menyala. Lihat 2d.
2. **Kesimpulan Kegiatan** — memisahkan **Aktivitas** (yang dikerjakan), **Output** (yang dihasilkan), dan **Kesimpulan** (capaian hari itu).

---

## 2b. Pekerjaan yang belum sempat dikerjakan (v2.0)

Di To-Do, grup pertama bernama **Belum Dikerjakan**: task yang tanggal rencananya sudah lewat tetapi belum selesai. Itu **bukan** "terlambat" — `tanggal` hanya hari rencana. Keterlambatan sesungguhnya diukur dari kolom **Tenggat**: task yang tenggatnya lewat mendapat chip merah **Lewat tenggat N hari**.

Tombol **Bawa ke hari ini** (pada grup Belum Dikerjakan) memunculkan task itu di Dashboard hari ini dengan chip **Dibawa**, **tanpa mengubah tanggal rencananya**:

- Tanggal rencana tetap — jadi realisasi SKP/EKP tidak berpindah triwulan.
- Penanda berlaku **satu hari** saja. Besok task itu otomatis lepas dari Dashboard; tidak ada yang perlu dibersihkan.
- **Batal bawa** tersedia di mana pun task itu terlihat. Kalau tanggalnya memang salah, ubah lewat kolom Tanggal di panel detail.

**Dasar Rekap Presensi sekarang "yang benar-benar dikerjakan pada hari itu"**, bukan "yang bertanggal hari itu":

| Kondisi task | Masuk rekap tanggal… |
|---|---|
| Selesai | hari ia **diselesaikan** (bukan hari rencana) |
| Berjalan | hari rencananya, **dan** hari ia dibawa |
| Belum Dimulai / Ditunda / Dibatalkan | tidak pernah |

Ditandai "Dibawa" saja tidak cukup masuk rekap — task harus berstatus Berjalan atau Selesai. Data lama tanpa waktu selesai memakai tanggal rencana. Kesimpulan Kegiatan dan tombol Perhalus dengan AI memakai daftar yang sama dengan Rekap.

---

## 2c. Fitur pendukung (v2.0)

- **Timer di topbar.** Task berstatus Berjalan selalu terlihat di kanan atas (judul, lama berjalan, dan "+N" bila ada lebih dari satu). Klik untuk membuka task. Kalau chip itu muncul padahal Anda sudah tidak mengerjakannya, itu pengingat bahwa ada task yang lupa diselesaikan.
- **Sapaan carry-over.** Di Dashboard, bila ada task dari hari sebelumnya yang masih Belum Dimulai atau Berjalan, muncul kartu kuning: **Bawa semua ke hari ini**, **Lihat daftar**, atau **Nanti** (disembunyikan sampai besok). Task berstatus Ditunda tidak ikut ditawarkan.
- **Template rutin.** Pengaturan → *Template rutin*, atau buka detail sebuah task lalu **Jadikan rutin**. Pola: setiap hari kerja, setiap minggu (pilih hari), atau setiap bulan (pilih tanggal; tanggal 29–31 memakai tanggal terakhir pada bulan yang lebih pendek). Task dibuat otomatis **sekali** pada hari yang cocok, saat aplikasi pertama kali dibuka hari itu, berlabel sumber *Rutin* dan chip **Rutin**. Task yang Anda hapus tidak dibuat ulang di hari yang sama, dan hari yang terlewat tidak menghasilkan tunggakan. Template tersimpan di dokumen pengaturan, jadi ikut tersinkron dan tercakup Cadangkan.
- **Analitik baru.** *Sumber pekerjaan* (berapa persen datang dari disposisi, hasil rapat, atau permintaan unit lain), *Ketepatan tenggat* (tepat waktu vs terlambat vs lewat dan belum selesai, dihitung dari waktu selesai sebenarnya), dan *Ritme kerja* (peta 12 minggu pekerjaan selesai per hari).

---

## 2d. Baru di v2.1

### Kotak Sampah — hapus tidak lagi berarti hilang

Pekerjaan, project, agenda, notulensi, dan indikator SKP yang dihapus **pindah ke Kotak Sampah**, bukan lenyap. Daftarnya ada di Pengaturan, lengkap dengan chip **hangus N hari lagi**.

- Masa tahan **30 hari**, lalu dihapus permanen sendiri saat aplikasi dibuka. Tidak ada yang perlu dibersihkan manual.
- **Pulihkan** mengembalikan dokumen dengan **id yang sama**, jadi kaitannya ke project, agenda, dan notulensi tetap nyambung — bukan salinan baru.
- **Hapus permanen** dan **Kosongkan sampah** tersedia kalau Anda ingin sekarang juga; keduanya minta konfirmasi dan tidak bisa dibatalkan.
- Sampah ikut tersinkron antarperangkat dan ikut tercakup tombol **Cadangkan**.
- Konsekuensinya jujur: selama 30 hari itu, item di sampah **tetap memakan jatah 5.000 dokumen**. Angkanya terlihat sebagai baris tersendiri di meter penyimpanan.

Yang **tidak** masuk sampah: Arsip Tahunan. Mengarsipkan bukan menghapus — datanya dipindahkan ke dokumen arsip, bukan dibuang.

### Agenda dan notulensi kini ikut masuk Rekap Presensi

Sebelumnya hanya agenda berjenis **Rapat** yang bisa naik ke rekap, dan notulensi tidak pernah ikut sama sekali. Sekarang:

| Sumber | Masuk rekap? |
|---|---|
| Task berstatus Selesai / Berjalan | ya (seperti sebelumnya) |
| Agenda semua jenis **kecuali Deadline** | ya |
| Agenda berstatus **Dibatalkan** atau **Ditunda** | tidak pernah |
| Notulensi | ya, **digabung ke baris rapatnya** |

Rapat yang notulensinya sudah ada isinya ditulis sebagai satu kalimat: *"Mengikuti rapat X dan menyusun notulensinya."* Notulensi yang masih kosong hanya menghasilkan *"Mengikuti rapat X."* Digabung, bukan dipecah dua baris, karena jatah rekap cuma 5 baris — memecahnya akan menggusur pekerjaan lain.

Tenggat (**Deadline**) tetap tidak dihitung: tenggat bukan kegiatan yang dihadiri. Agenda berstatus **Terjadwal** tetap ikut dihitung, karena status itulah bawaannya dan pada praktiknya jarang diubah.

Kesimpulan Kegiatan dan umpan ke AI sekarang memakai daftar yang **sama persis** dengan Rekap Presensi.

### Simpan Revisi — aplikasi belajar diksi Anda

Di Tutup Hari, begitu Anda mengubah isi kotak Rekap Presensi, tombol **Simpan Revisi** menyala. Menekannya menyimpan pasangan *kalimat draf → kalimat versi Anda*.

Yang terjadi setelah itu:

1. **Tanpa AI, tanpa kuota.** Saat **Regenerate**, baris yang sama persis langsung ditulis dengan versi Anda. Tetap jalan walau izin AI ditolak atau kuota habis.
2. **Dengan AI.** Delapan pelajaran terakhir dikirim sebagai contoh gaya ke **Perhalus dengan AI**, supaya hasilnya mengikuti cara Anda menulis — bukan sekadar bahasa baku generik.

Aturannya sengaja ketat supaya tidak pernah salah tebak:

- Penggantian hanya dilakukan bila kalimatnya **cocok persis**. Tidak ada penebakan sebagian kata.
- Kalau jumlah baris draf dan revisi Anda berbeda, penyimpanan **ditolak** dengan penjelasan — pasangannya akan bergeser dan yang dipelajari jadi keliru.
- Merevisi ulang kalimat yang sudah pernah dipelajari **memperbarui** pelajaran lama, bukan menumpuk rantai baru.
- Maksimal 40 pelajaran; yang terlama terdorong keluar.

Semua pelajaran bisa dilihat, dihapus satu per satu, atau dihapus semua di Pengaturan → *Gaya bahasa yang dipelajari*. Tersimpan di dokumen pengaturan, jadi ikut tersinkron dan tercakup Cadangkan.

### Umpan balik tekan

Setiap tombol, chip, baris daftar, sel kalender, dan item navigasi sekarang punya reaksi saat ditekan (riak halus + skala turun). Drawer, modal, dan toast bergerak masuk; berpindah tab memunculkan kartunya bertahap. Mengetik di kotak filter **tidak** memicu animasi — hanya perpindahan tab yang memicunya. Seluruhnya otomatis mati kalau sistem Anda menyalakan *reduce motion*.

---

## 3. Rapat

Kalender → agenda jenis **Rapat** → tombol **Notulensi** pada baris agenda. Judul, tanggal, jam, tempat, peserta, project, dan SKP terisi otomatis dari agenda.

Di dalam notulensi ada kotak **catatan mentah**. Tulis apa adanya, lalu **Susun dengan AI** — hasilnya mengisi Pokok Pembahasan, Keputusan, Tindak Lanjut (uraian | PIC | tanggal), dan Kesimpulan. AI tidak boleh menambah fakta; yang tidak disebutkan ditulis "Belum disebutkan dalam catatan."

Setiap baris tindak lanjut punya tombol **Create Task** → task baru lahir dengan `Sumber: Hasil Rapat`, terhubung ke notulensinya, mewarisi project dan SKP, dan tenggatnya ikut hasil rapat. Task itu muncul di Dashboard sebagai "Tindak lanjut rapat belum selesai" sampai diselesaikan.

---

## 4. SKP dan EKP

Tab **SKP** memuat 14 indikator SKP 2026 Anda. Realisasi dihitung otomatis per periode dari pekerjaan yang dikaitkan ke indikator — bukan diketik.

Cara hitung tiap indikator sudah dipasang sesuai jenisnya:

| Metode | Dipakai untuk | Yang dihitung |
|---|---|---|
| `COUNT_TASK` | layanan e-Surat, layanan TTE | jumlah task berstatus Selesai |
| `COUNT_EVIDENCE` | dokumen SOP, PK, cascading, laporan, sertifikat | jumlah bukti dukung pada task terkait |
| `COUNT_MEETING` | reviu PKS & SOP | jumlah rapat yang notulensinya dikaitkan |
| `SUM_JAM` | pengembangan kompetensi | total durasi task |
| `DURASI_HARI` | waktu penyelesaian | rentang task pertama sampai selesai terakhir |
| `PERSEN_TRIWULAN` | capaian output e-Monev | triwulan terlapor ÷ triwulan berjalan |

**Agar EKP terisi, kaitkan pekerjaan ke indikator SKP** (lewat `@n` di Quick Add atau kolom "SKP / indikator terkait" di panel detail). Yang tidak dikaitkan tidak akan terhitung.

Tab **EKP** menghasilkan tabel siap tempel ke kolom "REALISASI BERDASARKAN BUKTI DUKUNG". Tombol **Rapikan kalimat dengan AI** hanya menyusun kalimat dari angka yang sudah dihitung; setiap kalimat dicek ulang dan ditolak kalau memuat angka yang tidak ada di datanya. Indikator tanpa data ditulis **"Data belum tersedia."** dan tidak pernah dikarang.

---

## 5. Batas teknis yang perlu diketahui

- **Maksimal 5.000 dokumen** per aplikasi. Terpakai sekarang: 96. Isi Kotak Sampah ikut dihitung selama 30 hari masa tahannya. Perkiraan pemakaian ~3.000/tahun, jadi rutin arsip tahunan akan dibutuhkan sekitar pertengahan tahun kedua (masuk Tahap B).
- Data tersimpan di server Anthropic, privat untuk organisasi Anda, tidak bisa dibagikan lewat tautan publik. **Notulensi sensitif: simpan poinnya saja di sini, dokumen aslinya di Drive**, lalu tautkan URL-nya di kolom bukti dukung.
- Tombol **Cadangkan** di kanan atas mengunduh seluruh data sebagai JSON. Lakukan sebulan sekali.
- Fitur AI memakai kuota Claude Anda dan minta izin sekali di awal. Kalau ditolak, semua tombol tetap berfungsi dengan versi hitungan/template — aplikasi tidak rusak.

---

## 6. Yang belum ada (Tahap B)

- Kanban dan timeline Gantt pada Projects (sekarang: daftar, detail, task, timeline aktivitas, milestone, dokumen, SKP).
- Arsip tahunan otomatis + meter penyimpanan.
- Ekspor EKP ke .docx mengikuti format lampiran (sekarang: salin tabel + unduh CSV).
- Impor agenda dari konektor Google Calendar.
