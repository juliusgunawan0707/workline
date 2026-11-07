# Workline

**Log your work once. The paperwork writes itself.**

A single-file work manager for public-sector staff. You type one line when you do
something; Workline turns that into the daily attendance recap, the quarterly
performance report (KPI, called SKP in the Indonesian civil service), the draft
performance appraisal (called EKP there), and the meeting minutes — without
anyone retyping the same work four times.

**[Open the live demo →](https://juliusgunawan0707.github.io/workline/)**

```
Quick Add → To-Do → Daily Log → Close Day → Attendance recap
                 ↘ Project ↘ SKP ↘ EKP
Calendar → Meeting notes → Create task ↗
```

---

## What it does

| | |
|---|---|
| **Quick Add** | `09.00-10.30 Budget revision meeting #dashboard @7 !high` parses into time, project, performance indicator, priority, category and date. Preview chips show the parse before you commit. |
| **Close Day** | Generates a numbered attendance recap capped at 5 lines — the exact shape the attendance system accepts — with live line and character counters. |
| **KPI / Performance appraisal** | The achievement column is *computed from logged work*, not written by a model. Six calculation methods: `COUNT_TASK`, `COUNT_EVIDENCE`, `COUNT_MEETING`, `PERSEN_TRIWULAN`, `DURASI_HARI`, `SUM_JAM`. |
| **Meeting notes** | Minutes hold discussion, decisions and follow-ups with owner and due date, and each follow-up becomes a task with one click. Turning raw notes into structured minutes uses the AI button, which needs the host runtime; without it you fill the fields in by hand. |
| **Carry forward** | Unfinished work from earlier days surfaces today without moving its planned date, so quarterly reporting stays in the right quarter. |

**Numbers are never invented.** Indicators with no logged evidence print
*"Data not available"* rather than a plausible-looking figure. The AI buttons only
rephrase wording; output is rejected automatically if the line count changes or a
new number appears.

## Running it

Open `index.html`. That is the whole install — no build, no server, no account.
Data lives in your browser's `localStorage`; **Backup** exports a JSON file and
restores it with IDs intact, so links between tasks, projects and minutes survive.

Bilingual EN/ID (English by default) and light/dark, both remembered. Generated
documents (attendance recap, appraisal wording, Excel and Word exports) follow the
interface language. The demo dataset is in English.

## About the demo data

Everything in this repository is fictional: people, units, targets and documents.
The identity numbers are deliberately impossible — every one carries birth month
`13` — so they cannot collide with a real person's.

The demo seeds itself once, only when the app is completely empty, and shifts its
dates so it always reads as the current week. Clear the data and start entering
your own; it will not be overwritten.

```
tools/make_demo_data.py  generates demo-data.json (deterministic seed)
tools/embed_demo.py      embeds the dataset and the one-time seeder
```

The script that strips identifying data from the private build is deliberately not
published: it necessarily contains the very names and internal URLs it removes.

## Note on AI features

The polish buttons call the host runtime's model API. Outside that host they are
inert by design — every deterministic path (recap generation, KPI and
appraisal calculation, follow-ups to tasks) works with no model. Structuring raw
notes into minutes is the one step that needs the model. The Excel export loads a
small library from a CDN the first time you use it.

---

Built by [Julius Gunawan](https://juliusgunawan0707.github.io/portfolio-julius/).
