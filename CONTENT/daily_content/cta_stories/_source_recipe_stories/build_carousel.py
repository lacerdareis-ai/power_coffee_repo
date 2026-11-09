import json, subprocess, sys, html, tempfile, shutil
from pathlib import Path
HERE = Path(__file__).parent
PC = Path("/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee")
FONTS = PC / "Sales_motor/daily_content/_brand_kit/fonts"
A = PC / "homepage_first_win/theme/assets"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
R = json.load(open(HERE / "recipes.json"))
DESC = {"01":"Rich, creamy, the daily starter.","02":"Bold, chocolatey, sweetened by dates.","03":"Smooth, vanilla, protein-forward.",
        "04":"Creamy, slightly nutty, served warm.","05":"Bright, tangy and filling.","06":"Smooth tropical, a hint of honey.",
        "07":"Light, clean and refreshing.","08":"Rich, robust, dessert-level.","09":"Peanut butter, banana, one scoop.","10":"Green, creamy, surprisingly good."}
TOTAL = 7
CSS = f"""
@font-face{{font-family:Anton;src:url('file://{FONTS}/Anton-Regular.ttf')}}
@font-face{{font-family:Inter;src:url('file://{FONTS}/Inter-Variable.ttf');font-weight:100 900}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:#0A2242}}
.s{{position:relative;width:1080px;height:1350px;background:#0A2242;color:#EEE6CA;font-family:Inter,sans-serif;overflow:hidden}}
.s.light{{background:#EEE6CA;color:#0A2242}}
.dots{{position:absolute;inset:0;background-image:radial-gradient(rgba(238,230,202,.07) 1.6px,transparent 1.8px);background-size:10px 10px}}
.light .dots{{background-image:radial-gradient(rgba(17,58,110,.06) 1.6px,transparent 1.8px)}}
.glow{{position:absolute;inset:0;background:radial-gradient(55% 40% at 85% 15%,rgba(212,163,58,.28),transparent 70%)}}
.frame{{position:absolute;inset:44px;border:3px solid rgba(238,230,202,.35);border-radius:6px}}
.light .frame{{border-color:rgba(17,58,110,.3)}}
.pg{{position:absolute;right:96px;top:88px;font:800 24px/1 Inter;letter-spacing:.18em;color:#D4A33A}}
.brand{{position:absolute;left:96px;top:88px;font:800 24px/1 Inter;letter-spacing:.18em;text-transform:uppercase;color:#C4BC9E}}
.light .brand{{color:#4A5872}}
.eb{{font:800 28px/1 Inter;letter-spacing:.2em;text-transform:uppercase;color:#D4A33A}}
.anton{{font-family:Anton;text-transform:uppercase;font-weight:400}}
.blue{{color:#429EEB}}
/* recipe slide */
.rs{{position:absolute;left:96px;right:96px;top:150px;bottom:110px;display:flex;flex-direction:column;gap:30px}}
.rc{{flex:1;border-radius:30px;padding:40px 44px;display:flex;flex-direction:column;gap:18px;position:relative}}
.rc.l{{background:#EEE6CA;color:#0A2242}} .rc.d{{background:#113A6E;color:#EEE6CA}}
.rc .top{{display:flex;align-items:center;gap:26px}}
.rc .n{{font:400 110px/.8 Anton;color:#D4A33A}}
.rc h3{{font:400 70px/.92 Anton;text-transform:uppercase}}
.rc.d h3 span{{color:#429EEB}} .rc.l h3 span{{color:#113A6E}}
.rc .tag{{font:800 22px/1 Inter;letter-spacing:.16em;text-transform:uppercase;color:#D4A33A;margin-bottom:10px}}
.rc .desc{{font:500 30px/1.3 Inter;opacity:.85}}
.rc ul{{list-style:none;display:grid;grid-template-columns:1fr 1fr;grid-auto-flow:column;grid-template-rows:repeat(var(--rows),auto);gap:8px 26px}}
.rc li{{font:500 31px/1.25 Inter;display:flex;gap:12px;align-items:baseline}}
.rc li::before{{content:"";flex:none;width:10px;height:10px;border-radius:50%;background:currentColor;opacity:.4;transform:translateY(-3px)}}
.rc li.pc{{font-weight:800}} .rc.l li.pc{{color:#113A6E}} .rc.d li.pc{{color:#D4A33A}}
.rc li.pc::before{{background:#D4A33A;opacity:1;width:14px;height:14px}}
.xc{{align-self:flex-start;font:800 21px/1 Inter;letter-spacing:.12em;text-transform:uppercase;color:#0A2242;background:#D4A33A;padding:11px 18px;border-radius:999px}}
.swipe{{position:absolute;right:96px;bottom:70px;font:800 22px/1 Inter;letter-spacing:.16em;text-transform:uppercase;color:#C4BC9E}}
/* cover */
.cv h1{{position:absolute;left:92px;top:200px;font:400 196px/.88 Anton;text-transform:uppercase;white-space:nowrap}}
.cv .sub{{position:absolute;left:96px;top:600px;width:520px;font:500 40px/1.32 Inter;color:#C4BC9E}}
.cv .mascot{{position:absolute;right:70px;bottom:120px;height:560px;filter:drop-shadow(0 18px 30px rgba(0,0,0,.35))}}
.chip{{position:absolute;left:96px;bottom:120px;font:800 26px/1 Inter;letter-spacing:.12em;text-transform:uppercase;padding:20px 28px;border-radius:999px;border:2px solid #D4A33A;color:#D4A33A}}
/* close */
.cl h2{{position:absolute;left:92px;top:170px;font:400 168px/.88 Anton;text-transform:uppercase;color:#113A6E}}
.cl h2 span{{color:#D4A33A}}
.cl .sub{{position:absolute;left:96px;top:520px;width:520px;font:500 36px/1.35 Inter;color:#13233D}}
.cl .pack{{position:absolute;left:96px;top:650px;width:270px;mix-blend-mode:multiply}}
.cl .mascot{{position:absolute;right:90px;top:520px;height:520px}}
.cl .btn{{position:absolute;left:96px;right:96px;bottom:250px;height:110px;border-radius:999px;background:#D4A33A;color:#0A2242;display:flex;align-items:center;justify-content:center;font:800 34px/1 Inter;letter-spacing:.04em}}
.cl .amz{{position:absolute;left:0;right:0;bottom:178px;display:flex;align-items:center;justify-content:center;gap:16px;font:800 24px/1 Inter;letter-spacing:.14em;text-transform:uppercase;color:#4A5872}}
.cl .amz img{{height:40px;transform:translateY(8px)}}
.cl .save{{position:absolute;left:0;right:0;bottom:120px;text-align:center;font:700 28px/1 Inter;letter-spacing:.08em;text-transform:uppercase;color:#4A5872}}
"""
def wrap(inner, cls="", n=1):
    light = "light" in cls
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="s {cls}"><div class="dots"></div>{'' if light else '<div class="glow"></div>'}<div class="frame"></div>
<span class="brand">The Power Coffee</span><span class="pg">{n:02d} / {TOTAL:02d}</span>{inner}</div></body></html>"""

def card(r, tone):
    ing = "".join(f'<li class="{"pc" if "Power Coffee" in i else ""}">{html.escape(i)}</li>' for i in r["ing"])
    xc = f'<span class="xc">⚡ {html.escape(r["extra"])}</span>' if r.get("extra") else ""
    return f"""<div class="rc {tone}"><div class="top"><span class="n">{r['n']}</span>
<div><p class="tag">{html.escape(r['tag'])}</p><h3>{html.escape(r['t1'])} <span>{html.escape(r['t2'])}</span></h3></div></div>
<p class="desc">{DESC[r['n']]}</p>{xc}<ul style="--rows:{(len(r['ing'])+1)//2}">{ing}</ul></div>"""

slides = []
slides.append(wrap(f"""<h1>10 shakes.<br><span class="blue">One scoop.</span></h1>
<p class="sub">Ten blender recipes, every one built around one scoop of Power Coffee.</p>
<img class="mascot" src="file://{A}/fw-pose-2.webp"><span class="chip">Save this for tomorrow →</span>""", "cv", 1))
for k in range(5):
    a, b = R[2*k], R[2*k+1]
    slides.append(wrap(f'<div class="rs">{card(a,"l")}{card(b,"d")}</div><span class="swipe">Swipe →</span>', "", k+2))
slides.append(wrap(f"""<h2>Get all 10<br><span>free.</span></h2>
<p class="sub">The full recipe PDF, ready for your next blender morning.</p>
<img class="pack" src="file://{A}/fw-pack.jpg"><img class="mascot" src="file://{A}/fw-pose-3.webp">
<div class="btn">www.thepowercoffee.com</div><div class="amz">Also on <img src="file:///Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/Sales_motor/daily_content/_brand_kit/logos/amazon_logo_navy.svg"></div>
<p class="save">Save it · Send it to the friend who skips breakfast</p>""", "light cl", 7))

out = HERE / "out"; out.mkdir(exist_ok=True)
only = [int(x) for x in sys.argv[1:]]
for i, h in enumerate(slides, 1):
    if only and i not in only: continue
    hp = HERE / f"slide_{i}.html"; hp.write_text(h, encoding="utf-8")
    png = out / f"carousel_{i}.png"; prof = tempfile.mkdtemp(prefix="chr")
    try:
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--user-data-dir={prof}",
            "--allow-file-access-from-files", "--force-device-scale-factor=1", "--window-size=1080,1350",
            "--virtual-time-budget=5000", "--run-all-compositor-stages-before-draw", f"--screenshot={png}", f"file://{hp}"], timeout=30, capture_output=True)
    except subprocess.TimeoutExpired: pass
    shutil.rmtree(prof, ignore_errors=True); print(i, png.exists())
