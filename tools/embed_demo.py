# -*- coding: utf-8 -*-
"""
Embed demo-data.json into the public build and wire up a one-time seeder.

Keeps Workline a single self-contained file: open index.html from anywhere
and it is already populated. The seeder runs only when every data collection
is empty and it has never run before, so a visitor who clears the data and
starts entering their own work is never overwritten.

    python tools/embed_demo.py index.html demo-data.json
"""
import io
import json
import sys

HTML = sys.argv[1] if len(sys.argv) > 1 else "index.html"
DATA = sys.argv[2] if len(sys.argv) > 2 else "demo-data.json"

s = io.open(HTML, encoding="utf-8").read()
demo = json.load(io.open(DATA, encoding="utf-8"))

anchor_marker = "async function boot(){"
if anchor_marker not in s:
    raise SystemExit("ABORT: boot() not found")

# Re-embedding: drop the previous seeder block first, so this script can be re-run
# after the dataset changes (it replaces the data, it never stacks a second copy).
seed_start = "\n/* ============================ DEMO SEED"
if "const DEMO_DATA=" in s:
    _a = s.index(seed_start)
    _b = s.index(anchor_marker)
    s = s[:_a] + s[_b:]

payload = json.dumps(demo, ensure_ascii=False, separators=(",", ":"))

seeder = """
/* ============================ DEMO SEED ============================
   Sample data for the public build. Fictional people, units and documents.
   Runs once, only when the app is completely empty, then never again -- so
   anyone who clears it and starts entering real work keeps their own data.
   Dates are stored against DEMO_DATA.anchor and shifted on first run, which
   is why the demo always reads as "this week" instead of a dead month. */
const DEMO_DATA=__PAYLOAD__;
const DEMO_FLAG=LK+"demoSeeded";
function demoGeser(rec,hari,medan){
  for(const k of medan){
    const v=rec[k]; if(!v) continue;
    const tgl=String(v).slice(0,10);
    if(!/^\\d{4}-\\d{2}-\\d{2}$/.test(tgl)) continue;
    const d=new Date(tgl+"T00:00:00Z"); d.setUTCDate(d.getUTCDate()+hari);
    rec[k]=d.toISOString().slice(0,10)+String(v).slice(10);
  }
  /* minutes carry a follow-up list, each item with its own due date: move those along too */
  if(Array.isArray(rec.tindak_lanjut)){
    for(let i=0;i<rec.tindak_lanjut.length;i++){
      const it=Object.assign({},rec.tindak_lanjut[i]);
      const tg=String(it.deadline||"");
      if(/^\\d{4}-\\d{2}-\\d{2}$/.test(tg)){
        const dd=new Date(tg+"T00:00:00Z"); dd.setUTCDate(dd.getUTCDate()+hari);
        it.deadline=dd.toISOString().slice(0,10);
      }
      rec.tindak_lanjut[i]=it;
    }
  }
  return rec;
}
function seedDemoIfEmpty(){
  try{
    if(localStorage.getItem(DEMO_FLAG)) return;
    const kosong=COLLS_DATA.every(c=>D[c].size===0);
    if(!kosong){ localStorage.setItem(DEMO_FLAG,"skip"); return; }
    const hari=Math.round(
      (new Date(todayISO()+"T00:00:00Z")-new Date(DEMO_DATA.anchor+"T00:00:00Z"))
      /86400000);
    const MEDAN={
      tasks:["tanggal","deadline","dibuat_pada","diubah_pada"],
      projects:["tanggal_mulai","target_selesai","diubah_pada"],
      meetings:["tanggal"],
      events:["tanggal"]
    };
    for(const c of ["projects","tasks","meetings","events"]){
      for(const rec of (DEMO_DATA[c]||[])){
        D[c].set(rec.id,demoGeser(Object.assign({},rec),hari,MEDAN[c]));
      }
      lsSet(c);
    }
    for(const rec of SEED_SKP_2026){ D.skp.set(rec.id,Object.assign({},rec)); }
    lsSet("skp");
    localStorage.setItem(DEMO_FLAG,"1");
  }catch(e){ /* a demo that fails to seed must not break the app */ }
}
""".replace("__PAYLOAD__", payload)

s = s.replace(anchor_marker, seeder + "\n" + anchor_marker, 1)

# run it right after local data is hydrated, before anything renders
if "hydrateLocal(); seedDemoIfEmpty();" not in s:
    if "hydrateLocal();" not in s:
        raise SystemExit("ABORT: hydrateLocal() call not found")
    s = s.replace("hydrateLocal();", "hydrateLocal(); seedDemoIfEmpty();", 1)

io.open(HTML, "w", encoding="utf-8", newline="").write(s)
print("embedded %d tasks / %d projects / %d meetings / %d events"
      % (len(demo["tasks"]), len(demo["projects"]),
         len(demo["meetings"]), len(demo["events"])))
print("index.html is now %d bytes" % len(s))
