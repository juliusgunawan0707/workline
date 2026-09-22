# -*- coding: utf-8 -*-
"""
Build the demo dataset shipped with the public Workline build.

Every person, unit and document here is invented. The shape matches what the
app writes itself, so the demo exercises the real calculation paths
(COUNT_TASK, COUNT_EVIDENCE, COUNT_MEETING, PERSEN_TRIWULAN, DURASI_HARI,
SUM_JAM) rather than showing pre-baked numbers.

Dates are anchored to ANCHOR; the in-app seeder shifts them so the newest
entry always lands on the day a visitor opens the page.

    python tools/make_demo_data.py > demo-data.json
"""
import json
import random
from datetime import date, timedelta

random.seed(20260922)                      # deterministic output
ANCHOR = date(2026, 9, 22)                 # newest task lands here

KATEGORI = ["Rapat & Koordinasi", "Penyusunan Dokumen", "Telaah & Reviu",
            "Analisis Data", "Layanan e-Surat & Email", "Layanan TTE",
            "Monitoring & Evaluasi", "Pengembangan Aplikasi",
            "Pengembangan Kompetensi", "Administrasi Umum"]
UNIT = ["Biro Perencanaan", "Sekretariat", "Direktorat Lingkungan",
        "Direktorat Perencanaan", "Inspektorat", "Biro Keuangan",
        "Biro Umum", "Unit Layanan", "Satker Mitra", "Eksternal / K-L Lain"]
SUMBER = ["Mandiri", "Disposisi Pimpinan", "Hasil Rapat",
          "Permintaan Unit Lain", "Rutin"]
ORANG = ["Raka Wijaya", "Sri Handayani", "Bagas Nurcahyo", "Dita Ramadhani",
         "Fajar Alamsyah", "Nabila Kusuma", "Yoga Pranata", "Intan Maharani"]


def iso(d):
    return d.isoformat()


def stamp(d, h=8, m=0):
    return "%sT%02d:%02d:00.000Z" % (iso(d), h, m)


# --------------------------------------------------------------- projects
P = [
    ("p1", "Digitalisasi Layanan Persuratan", "Biro Perencanaan",
     "Memindahkan alur surat masuk dan keluar ke aplikasi e-Surat.",
     "In Progress", "Tinggi", ["i1"], 65),
    ("p2", "Penyusunan SOP Tata Kelola Dokumen", "Biro Perencanaan",
     "Menyusun tiga SOP pendukung tugas dan fungsi biro.",
     "In Progress", "Tinggi", ["i3", "i6"], 45),
    ("p3", "Survei Kepuasan Layanan Internal 2026", "Sekretariat",
     "Mengukur kepuasan unit kerja atas layanan kesekretariatan.",
     "In Progress", "Sedang", ["i10"], 30),
    ("p4", "Cascading IKU & Perjanjian Kinerja", "Biro Perencanaan",
     "Menurunkan indikator kinerja utama ke tiap unit dan menyusun PK.",
     "Completed", "Mendesak", ["i8a", "i8b", "i9"], 100),
    ("p5", "Dashboard Monitoring Capaian Output", "Biro Perencanaan",
     "Papan pantau capaian output triwulanan yang terisi otomatis.",
     "In Progress", "Sedang", ["i4"], 55),
    ("p6", "Reviu Dokumen Kerja Sama", "Sekretariat",
     "Menelaah draf perjanjian kerja sama yang diajukan unit kerja.",
     "In Progress", "Sedang", ["i7"], 40),
    ("p7", "Penguatan Layanan Tanda Tangan Elektronik", "Biro Umum",
     "Memastikan sertifikat elektronik aktif dan pengguna terlatih.",
     "In Progress", "Tinggi", ["i2"], 70),
    ("p8", "Laporan Kinerja Instansi 2026", "Biro Perencanaan",
     "Menyiapkan bahan dan data dukung laporan kinerja tahunan.",
     "Planning", "Sedang", ["i5"], 15),
]

projects = []
for pid, nama, unit, desc, st, pri, inds, prog in P:
    mulai = ANCHOR - timedelta(days=random.randint(60, 120))
    projects.append({
        "id": pid, "nama": nama, "unit": unit, "deskripsi": desc,
        "tujuan": desc, "status": st, "prioritas": pri,
        "indikator_ids": inds, "pic": random.choice(ORANG),
        "progress_manual": prog, "milestone": [], "dokumen": [], "catatan": "",
        "tanggal_mulai": iso(mulai),
        "target_selesai": iso(mulai + timedelta(days=random.randint(90, 180))),
        "diubah_pada": stamp(ANCHOR - timedelta(days=random.randint(1, 20))),
    })

# ------------------------------------------------------------------ tasks
TPL = [
    ("Memproses {n} surat masuk pada aplikasi e-Surat",
     "Layanan e-Surat & Email", "p1", "i1", "Rutin"),
    ("Menyelesaikan kendala akses akun e-Surat pengguna {u}",
     "Layanan e-Surat & Email", "p1", "i1", "Permintaan Unit Lain"),
    ("Menerbitkan sertifikat tanda tangan elektronik untuk {u}",
     "Layanan TTE", "p7", "i2", "Permintaan Unit Lain"),
    ("Pendampingan penggunaan TTE bagi pejabat penanda tangan",
     "Layanan TTE", "p7", "i2", "Mandiri"),
    ("Menyusun draf SOP {d}", "Penyusunan Dokumen", "p2", "i3", "Mandiri"),
    ("Reviu draf SOP {d} bersama unit pengusul",
     "Telaah & Reviu", "p2", "i6", "Permintaan Unit Lain"),
    ("Menyusun rekapitulasi capaian output triwulan",
     "Analisis Data", "p5", "i4", "Rutin"),
    ("Memutakhirkan dashboard monitoring capaian output",
     "Pengembangan Aplikasi", "p5", "i4", "Mandiri"),
    ("Menelaah draf perjanjian kerja sama dengan {u}",
     "Telaah & Reviu", "p6", "i7", "Disposisi Pimpinan"),
    ("Menyiapkan bahan evaluasi akuntabilitas kinerja",
     "Penyusunan Dokumen", "p8", "i5", "Disposisi Pimpinan"),
    ("Menyusun dokumen cascading indikator kinerja utama",
     "Penyusunan Dokumen", "p4", "i8a", "Mandiri"),
    ("Menyusun draf perjanjian kinerja unit {u}",
     "Penyusunan Dokumen", "p4", "i9", "Mandiri"),
    ("Menyebarkan kuesioner survei kepuasan ke unit {u}",
     "Monitoring & Evaluasi", "p3", "i10", "Mandiri"),
    ("Mengolah hasil survei kepuasan layanan internal",
     "Analisis Data", "p3", "i10", "Mandiri"),
    ("Rapat koordinasi persiapan {d}", "Rapat & Koordinasi", "", "", "Hasil Rapat"),
    ("Mengikuti pelatihan perencanaan dan penganggaran",
     "Pengembangan Kompetensi", "", "it1a", "Disposisi Pimpinan"),
    ("Merapikan arsip dokumen {d}", "Administrasi Umum", "", "", "Rutin"),
]
DOK = ["Pengelolaan Arsip Dinamis", "Tata Naskah Dinas", "Pengajuan Kerja Sama",
       "Monitoring dan Evaluasi", "Pelayanan Informasi Publik"]

tasks = []
tid = 0
day = ANCHOR - timedelta(days=55)
while day <= ANCHOR:
    if day.weekday() < 5:                                  # weekdays only
        for _ in range(random.randint(1, 3)):
            tid += 1
            judul, kat, pid, ind, sumber = random.choice(TPL)
            judul = (judul.replace("{n}", str(random.randint(4, 18)))
                          .replace("{u}", random.choice(UNIT[:8]))
                          .replace("{d}", random.choice(DOK)))
            h = random.choice([8, 9, 10, 13, 14, 15])
            dur = random.choice([30, 45, 60, 90, 120])
            age = (ANCHOR - day).days
            # Leave a believable tail of unfinished work so the To-Do view,
            # the "Belum Dikerjakan" group and the overdue chip all have
            # something to show. A demo where everything is done is a demo
            # of an empty screen.
            if age > 7:
                status = "Selesai" if random.random() < .86 else random.choice(
                    ["Belum Dimulai", "Berjalan", "Ditunda"])
            elif age > 1:
                status = random.choices(
                    ["Selesai", "Berjalan", "Belum Dimulai"],
                    weights=[55, 25, 20])[0]
            else:
                status = random.choices(
                    ["Selesai", "Berjalan", "Belum Dimulai"],
                    weights=[35, 30, 35])[0]
            selesai = status == "Selesai"
            jm = "%02d:%02d" % (h, random.choice([0, 15, 30]))
            js = ""
            if selesai:
                em = int(jm[3:]) + dur
                js = "%02d:%02d" % (h + em // 60, em % 60)
            elif status == "Belum Dimulai":
                jm = ""
            # a quarter of open work carries a deadline; some already passed
            deadline = ""
            if not selesai and random.random() < .45:
                deadline = iso(day + timedelta(days=random.choice(
                    [-3, -1, 2, 5, 9, 14])))
            tasks.append({
                "id": "t%03d" % tid, "judul": judul, "deskripsi": "",
                "kategori": kat, "project_id": pid, "indikator_id": ind,
                "prioritas": random.choice(["Mendesak", "Tinggi", "Sedang",
                                            "Sedang", "Rendah"]),
                "status": status,
                "sumber": sumber, "unit_terkait": random.choice(UNIT[:8]),
                "tanggal": iso(day), "jam_mulai": jm, "jam_selesai": js,
                "deadline": deadline, "output": "", "catatan": "", "bukti": [],
                "dibuat_pada": stamp(day, 7, 30),
                "diubah_pada": stamp(day, h + 2, 0),
            })
    day += timedelta(days=1)

# --------------------------------------------------------------- meetings
MTG = [
    ("Rapat Koordinasi Penyusunan SOP", "p2", "i3",
     ["Progres penyusunan tiga draf SOP", "Pembagian penelaah per dokumen"],
     ["Draf SOP Tata Naskah Dinas disepakati masuk reviu tahap dua",
      "Format penomoran SOP mengikuti tata naskah yang berlaku"],
     ["Perbaikan draf SOP | Raka Wijaya | +7",
      "Pengumpulan masukan unit | Dita Ramadhani | +10"]),
    ("Rapat Evaluasi Capaian Output Triwulan", "p5", "i4",
     ["Realisasi capaian output per unit", "Kendala pengumpulan data dukung"],
     ["Unit menyampaikan data dukung paling lambat akhir bulan",
      "Dashboard dipakai sebagai rujukan tunggal capaian"],
     ["Pemutakhiran dashboard | Yoga Pranata | +5",
      "Surat permintaan data dukung | Nabila Kusuma | +3"]),
    ("Rapat Persiapan Survei Kepuasan Layanan", "p3", "i10",
     ["Rancangan kuesioner", "Target responden per unit"],
     ["Kuesioner memakai delapan indikator inti",
      "Survei dibuka selama dua minggu"],
     ["Finalisasi kuesioner | Intan Maharani | +4",
      "Sosialisasi ke unit | Fajar Alamsyah | +6"]),
    ("Rapat Reviu Dokumen Kerja Sama", "p6", "i7",
     ["Telaah draf perjanjian kerja sama", "Kesesuaian dengan ketentuan"],
     ["Dua klausul diperbaiki sebelum diajukan ke pimpinan"],
     ["Perbaikan klausul | Sri Handayani | +5"]),
    ("Rapat Penetapan Perjanjian Kinerja", "p4", "i9",
     ["Draf PK eselon 1 dan eselon 2", "Jadwal penandatanganan"],
     ["Draf PK disetujui untuk ditandatangani pekan depan"],
     ["Penyiapan dokumen tanda tangan | Raka Wijaya | +3"]),
    ("Rapat Pemantauan Layanan TTE", "p7", "i2",
     ["Jumlah sertifikat aktif", "Kendala pengguna baru"],
     ["Pendampingan pengguna baru dijadwalkan tiap awal bulan"],
     ["Jadwal pendampingan | Bagas Nurcahyo | +8"]),
]

meetings, events = [], []
for k, (judul, pid, ind, bahas, putus, lanjut) in enumerate(MTG, 1):
    d = ANCHOR - timedelta(days=random.randint(3, 45))
    while d.weekday() >= 5:
        d -= timedelta(days=1)
    mid, eid = "m%d" % k, "e%d" % k
    jm = random.choice(["09:00", "10:00", "13:30"])
    js = "%02d:00" % (int(jm[:2]) + 2)
    peserta = random.sample(ORANG, 5)
    meetings.append({
        "id": mid, "judul": judul, "tanggal": iso(d),
        "jam_mulai": jm, "jam_selesai": js,
        "tempat": random.choice(["Ruang Rapat Lantai 3", "Ruang Rapat Utama",
                                 "Daring (Zoom)"]),
        "pimpinan": "Sri Handayani", "moderator": random.choice(ORANG),
        "peserta": peserta, "agenda": bahas, "pokok": bahas,
        "pembahasan": bahas, "keputusan": putus, "tindak_lanjut": lanjut,
        "kesimpulan": putus[0], "catatan_mentah": "", "lampiran": [],
        "project_id": pid, "indikator_id": ind, "event_id": eid,
        "status": "final",
    })
    events.append({
        "id": eid, "judul": judul, "jenis": "Rapat", "tanggal": iso(d),
        "jam_mulai": jm, "jam_selesai": js,
        "lokasi": meetings[-1]["tempat"], "peserta": peserta,
        "project_id": pid, "indikator_id": ind, "meeting_id": mid,
        "status": "Terlaksana", "catatan": "",
    })

# extra calendar entries with no minutes attached
EXTRA = [("Batas penyampaian data dukung triwulan", "Deadline", 6),
         ("Sosialisasi aplikasi e-Surat", "Kegiatan", -4),
         ("Pelatihan perencanaan dan penganggaran", "Kegiatan", -9),
         ("Batas akhir penyampaian draf SOP", "Deadline", 11),
         ("Pendampingan pengguna TTE", "Pekerjaan", 2),
         ("Rapat pimpinan mingguan", "Rapat", 4),
         ("Penutupan survei kepuasan", "Deadline", 14)]
for k, (judul, jenis, off) in enumerate(EXTRA, 100):
    d = ANCHOR + timedelta(days=off)
    events.append({
        "id": "e%d" % k, "judul": judul, "jenis": jenis, "tanggal": iso(d),
        "jam_mulai": "09:00", "jam_selesai": "11:00",
        "lokasi": "Ruang Rapat Lantai 3", "peserta": random.sample(ORANG, 3),
        "project_id": "", "indikator_id": "", "meeting_id": "",
        "status": "Terlaksana" if off < 0 else "Terjadwal", "catatan": "",
    })

out = {"versi": 1, "anchor": iso(ANCHOR), "demo": True,
       "tasks": tasks, "projects": projects,
       "meetings": meetings, "events": events}
print(json.dumps(out, ensure_ascii=False, indent=1))
