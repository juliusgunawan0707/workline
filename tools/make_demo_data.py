# -*- coding: utf-8 -*-
"""
Build the demo dataset shipped with the public Workline build.

Every person, unit and document here is invented. The shape matches what the
app writes itself, so the demo exercises the real calculation paths
(COUNT_TASK, COUNT_EVIDENCE, COUNT_MEETING, PERSEN_TRIWULAN, DURASI_HARI,
SUM_JAM) rather than showing pre-baked numbers.

The free text (task, project, agenda and minutes wording) is English. Internal
keys that the app translates itself (status, priority, category, source, unit)
stay as the app's own keys, so the UI language switch still works.

Dates are anchored to ANCHOR; the in-app seeder shifts them so the newest
entry always lands on the day a visitor opens the page.

    python tools/make_demo_data.py > demo-data.json
"""
import json
import random
from datetime import date, timedelta

random.seed(20260922)                      # deterministic output
ANCHOR = date(2026, 9, 22)                 # newest task lands here

# app keys (translated for display by the app's own VALMAP)
KATEGORI = ["Rapat & Koordinasi", "Penyusunan Dokumen", "Telaah & Reviu",
            "Analisis Data", "Layanan e-Surat & Email", "Layanan TTE",
            "Monitoring & Evaluasi", "Pengembangan Aplikasi",
            "Pengembangan Kompetensi", "Administrasi Umum"]
UNIT = ["Biro Perencanaan", "Sekretariat", "Direktorat Lingkungan",
        "Direktorat Perencanaan", "Inspektorat", "Biro Keuangan",
        "Biro Umum", "UKHK", "Satker C", "Eksternal / K-L Lain"]
# English wording used INSIDE task titles (same order as UNIT[:8])
UNIT_TXT = ["Planning Bureau", "Secretariat", "Environment Directorate",
            "Planning Directorate", "Inspectorate", "Finance Bureau",
            "General Affairs Bureau", "Legal and PR Unit"]
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
    ("p1", "Correspondence Digitalization", "Biro Perencanaan",
     "Move incoming and outgoing letters into the e-Surat app.",
     "In Progress", "Tinggi", ["i1"], 65),
    ("p2", "Records Governance SOP Drafting", "Biro Perencanaan",
     "Draft three SOPs that support the bureau's tasks.",
     "In Progress", "Tinggi", ["i3", "i6"], 45),
    ("p3", "Internal Service Satisfaction Survey 2026", "Sekretariat",
     "Measure how satisfied units are with secretariat services.",
     "In Progress", "Sedang", ["i10"], 30),
    ("p4", "KPI Cascading and Performance Agreements", "Biro Perencanaan",
     "Cascade key performance indicators to each unit and draft the agreements.",
     "Completed", "Mendesak", ["i8a", "i8b", "i9"], 100),
    ("p5", "Output Achievement Dashboard", "Biro Perencanaan",
     "A quarterly output tracking board that fills itself.",
     "In Progress", "Sedang", ["i4"], 55),
    ("p6", "Cooperation Agreement Review", "Sekretariat",
     "Review draft cooperation agreements submitted by units.",
     "In Progress", "Sedang", ["i7"], 40),
    ("p7", "Electronic Signature Service Strengthening", "Biro Umum",
     "Make sure e-certificates are active and users are trained.",
     "In Progress", "Tinggi", ["i2"], 70),
    ("p8", "Agency Performance Report 2026", "Biro Perencanaan",
     "Prepare material and supporting data for the annual performance report.",
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
# Titles start with an imperative verb: the English recap generator turns
# "Draft ..." into "Drafted ..." from a small verb table.
TPL = [
    ("Process {n} incoming letters in the e-Surat app",
     "Layanan e-Surat & Email", "p1", "i1", "Rutin"),
    ("Resolve e-Surat account access issue for {u} users",
     "Layanan e-Surat & Email", "p1", "i1", "Permintaan Unit Lain"),
    ("Issue electronic signature certificates for {u}",
     "Layanan TTE", "p7", "i2", "Permintaan Unit Lain"),
    ("Assist signing officials with e-signature use",
     "Layanan TTE", "p7", "i2", "Mandiri"),
    ("Draft SOP for {d}", "Penyusunan Dokumen", "p2", "i3", "Mandiri"),
    ("Review SOP draft for {d} with the submitting unit",
     "Telaah & Reviu", "p2", "i6", "Permintaan Unit Lain"),
    ("Compile the quarterly output achievement summary",
     "Analisis Data", "p5", "i4", "Rutin"),
    ("Update the output achievement dashboard",
     "Pengembangan Aplikasi", "p5", "i4", "Mandiri"),
    ("Review draft cooperation agreement with {u}",
     "Telaah & Reviu", "p6", "i7", "Disposisi Pimpinan"),
    ("Prepare material for the accountability evaluation",
     "Penyusunan Dokumen", "p8", "i5", "Disposisi Pimpinan"),
    ("Draft the key performance indicator cascading document",
     "Penyusunan Dokumen", "p4", "i8a", "Mandiri"),
    ("Draft the performance agreement for {u}",
     "Penyusunan Dokumen", "p4", "i9", "Mandiri"),
    ("Distribute the satisfaction survey questionnaire to {u}",
     "Monitoring & Evaluasi", "p3", "i10", "Mandiri"),
    ("Analyze the internal service satisfaction survey results",
     "Analisis Data", "p3", "i10", "Mandiri"),
    ("Attend coordination meeting to prepare {d}", "Rapat & Koordinasi", "", "", "Hasil Rapat"),
    ("Attend training on planning and budgeting",
     "Pengembangan Kompetensi", "", "it1a", "Disposisi Pimpinan"),
    ("Organize the {d} archive", "Administrasi Umum", "", "", "Rutin"),
]
DOK = ["Dynamic Records Management", "Official Correspondence Format",
       "Cooperation Proposals", "Monitoring and Evaluation",
       "Public Information Services"]

tasks = []
tid = 0
day = ANCHOR - timedelta(days=55)
while day <= ANCHOR:
    if day.weekday() < 5:                                  # weekdays only
        for _ in range(random.randint(1, 3)):
            tid += 1
            judul, kat, pid, ind, sumber = random.choice(TPL)
            judul = (judul.replace("{n}", str(random.randint(4, 18)))
                          .replace("{u}", random.choice(UNIT_TXT))
                          .replace("{d}", random.choice(DOK)))
            h = random.choice([8, 9, 10, 13, 14, 15])
            dur = random.choice([30, 45, 60, 90, 120])
            age = (ANCHOR - day).days
            # Leave a believable tail of unfinished work so the To-Do view,
            # the "Not done yet" group and the overdue chip all have
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
# follow-ups: (what, owner, days after the meeting). They are stored as
# {uraian, pic, deadline} objects, the shape the minutes view and
# "Create Task" read.
MTG = [
    ("SOP Drafting Coordination Meeting", "p2", "i3",
     ["Progress on the three SOP drafts", "Assigning a reviewer per document"],
     ["The Official Correspondence SOP goes to second-stage review",
      "SOP numbering follows the current correspondence format"],
     [("Revise the SOP draft", "Raka Wijaya", 7),
      ("Collect feedback from units", "Dita Ramadhani", 10)]),
    ("Quarterly Output Evaluation Meeting", "p5", "i4",
     ["Output achievement by unit", "Obstacles in collecting supporting data"],
     ["Units submit supporting data by the end of the month",
      "The dashboard is the single reference for achievement"],
     [("Update the dashboard", "Yoga Pranata", 5),
      ("Send the supporting data request letter", "Nabila Kusuma", 3)]),
    ("Satisfaction Survey Preparation Meeting", "p3", "i10",
     ["Questionnaire design", "Target respondents per unit"],
     ["The questionnaire uses eight core indicators",
      "The survey stays open for two weeks"],
     [("Finalize the questionnaire", "Intan Maharani", 4),
      ("Brief all units about the survey", "Fajar Alamsyah", 6)]),
    ("Cooperation Agreement Review Meeting", "p6", "i7",
     ["Review of the draft cooperation agreement", "Fit with the applicable rules"],
     ["Two clauses are fixed before the draft goes to leadership"],
     [("Fix the two clauses", "Sri Handayani", 5)]),
    ("Performance Agreement Finalization Meeting", "p4", "i9",
     ["Draft agreements for level 1 and level 2", "Signing schedule"],
     ["The draft agreements are approved for signing next week"],
     [("Prepare the signing documents", "Raka Wijaya", 3)]),
    ("E-Signature Service Monitoring Meeting", "p7", "i2",
     ["Number of active certificates", "Obstacles for new users"],
     ["New-user assistance is scheduled at the start of every month"],
     [("Set the assistance schedule", "Bagas Nurcahyo", 8)]),
]
LOKASI = ["Meeting Room, 3rd Floor", "Main Meeting Room", "Online (Zoom)"]

meetings, events = [], []
for k, (judul, pid, ind, bahas, putus, lanjut) in enumerate(MTG, 1):
    d = ANCHOR - timedelta(days=random.randint(3, 45))
    while d.weekday() >= 5:
        d -= timedelta(days=1)
    mid, eid = "m%d" % k, "e%d" % k
    jm = random.choice(["09:00", "10:00", "13:30"])
    js = "%02d:00" % (int(jm[:2]) + 2)
    peserta = random.sample(ORANG, 5)
    tempat = random.choice(LOKASI)
    meetings.append({
        "id": mid, "judul": judul, "tanggal": iso(d),
        "jam_mulai": jm, "jam_selesai": js,
        "tempat": tempat,
        "pimpinan": "Sri Handayani", "moderator": random.choice(ORANG),
        "peserta": peserta, "agenda": bahas, "pokok": bahas,
        "pembahasan": bahas, "keputusan": putus,
        "tindak_lanjut": [{"uraian": u, "pic": pic,
                           "deadline": iso(d + timedelta(days=off))}
                          for (u, pic, off) in lanjut],
        "kesimpulan": putus[0], "catatan_mentah": "", "lampiran": [],
        "project_id": pid, "indikator_id": ind, "event_id": eid,
        "status": "final",
    })
    events.append({
        "id": eid, "judul": judul, "jenis": "Rapat", "tanggal": iso(d),
        "jam_mulai": jm, "jam_selesai": js,
        "lokasi": tempat, "peserta": peserta,
        "project_id": pid, "indikator_id": ind, "meeting_id": mid,
        "status": "Terlaksana", "catatan": "",
    })

# extra calendar entries with no minutes attached
EXTRA = [("Supporting data submission deadline", "Deadline", 6),
         ("e-Surat app briefing", "Kegiatan", -4),
         ("Planning and budgeting training", "Kegiatan", -9),
         ("Final deadline for SOP drafts", "Deadline", 11),
         ("e-Signature user assistance", "Pekerjaan", 2),
         ("Weekly leadership meeting", "Rapat", 4),
         ("Survey closes", "Deadline", 14)]
for k, (judul, jenis, off) in enumerate(EXTRA, 100):
    d = ANCHOR + timedelta(days=off)
    events.append({
        "id": "e%d" % k, "judul": judul, "jenis": jenis, "tanggal": iso(d),
        "jam_mulai": "09:00", "jam_selesai": "11:00",
        "lokasi": "Meeting Room, 3rd Floor", "peserta": random.sample(ORANG, 3),
        "project_id": "", "indikator_id": "", "meeting_id": "",
        "status": "Terlaksana" if off < 0 else "Terjadwal", "catatan": "",
    })

out = {"versi": 1, "anchor": iso(ANCHOR), "demo": True,
       "tasks": tasks, "projects": projects,
       "meetings": meetings, "events": events}
print(json.dumps(out, ensure_ascii=False, indent=1))
