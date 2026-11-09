import json, subprocess, sys, html, tempfile, shutil
from pathlib import Path
HERE = Path(__file__).parent
PC = Path("/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee")
FONTS = PC / "Sales_motor/daily_content/_brand_kit/fonts"
ASSETS = PC / "homepage_first_win/theme/assets"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ACCENT = {"01":"#E8C547","02":"#8A5530","03":"#E9DDB5","04":"#93C572","05":"#C2457E",
          "06":"#F1EBDD","07":"#F2A33A","08":"#6B4330","09":"#C68B4A","10":"#6FAF4E"}
from PIL import Image
MH={i:round(265*620/Image.open(ASSETS/f'fw-pose-{i}.webp').width) for i in range(1,6)}
R = json.load(open(HERE / "recipes.json"))
only = sys.argv[1:]

CSS = f"""
@font-face{{font-family:Anton;src:url('file://{FONTS}/Anton-Regular.ttf')}}
@font-face{{font-family:Inter;src:url('file://{FONTS}/Inter-Variable.ttf');font-weight:100 900}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:#0A2242}}
.s{{position:relative;width:1080px;height:1920px;background:#0A2242;color:#EEE6CA;font-family:Inter,sans-serif;overflow:hidden}}
.glow{{position:absolute;inset:0;background:radial-gradient(60% 38% at 88% 20%,var(--a) 0%,transparent 70%);opacity:.38}}
.dots{{position:absolute;inset:0;background-image:radial-gradient(rgba(238,230,202,.07) 1.6px,transparent 1.8px);background-size:10px 10px}}
.num{{position:absolute;right:70px;top:250px;font:400 430px/1 Anton;color:transparent;-webkit-text-stroke:3px rgba(238,230,202,.12)}}
.frame{{position:absolute;inset:44px;border:3px solid rgba(238,230,202,.35);border-radius:6px;pointer-events:none}}
.top{{position:absolute;left:96px;right:96px;top:300px;display:flex;align-items:center;gap:22px}}
.eb{{font:800 30px/1 Inter;letter-spacing:.2em;text-transform:uppercase;color:#D4A33A}}
.pill{{font:700 26px/1 Inter;letter-spacing:.14em;text-transform:uppercase;padding:14px 22px;border-radius:999px;border:2px solid rgba(238,230,202,.4);color:#EEE6CA}}
.h{{position:absolute;left:92px;top:380px;width:var(--hw);font:400 210px/.9 Anton;text-transform:uppercase}}
.h span{{display:block;white-space:nowrap}}
.h .l2{{color:#429EEB}}
.desc{{position:absolute;left:96px;width:var(--dw);font:500 46px/1.3 Inter;color:#C4BC9E}}
.xc{{display:inline-block;margin-top:24px;font:800 27px/1 Inter;letter-spacing:.12em;text-transform:uppercase;color:#0A2242;background:#D4A33A;padding:15px 24px;border-radius:999px}}
.card{{position:absolute;left:80px;right:80px;background:#EEE6CA;color:#0A2242;border-radius:36px;padding:52px 56px;display:grid;grid-template-columns:1fr 290px;gap:28px;align-items:center}}
.card h4{{font:800 26px/1 Inter;letter-spacing:.2em;text-transform:uppercase;color:#113A6E;opacity:.7;margin-bottom:22px}}
.card ul{{list-style:none}}
.card li{{font:500 43px/1.25 Inter;padding:11px 0;display:flex;gap:18px;align-items:baseline}}
.card li::before{{content:"";flex:none;width:13px;height:13px;border-radius:50%;background:#113A6E;opacity:.45;transform:translateY(-4px)}}
.card li.pc{{font-weight:800;color:#113A6E}}
.card li.pc::before{{background:#D4A33A;opacity:1;width:18px;height:18px}}
.pack{{width:290px;mix-blend-mode:multiply}}
.mascot{{position:absolute;width:265px;right:84px;z-index:3;filter:drop-shadow(0 14px 24px rgba(0,0,0,.35))}}
.cta{{position:absolute;left:80px;right:80px;top:1412px;height:112px;border-radius:999px;background:#D4A33A;color:#0A2242;display:flex;align-items:center;justify-content:center;gap:18px;font:800 38px/1 Inter;letter-spacing:.06em;text-transform:uppercase}}
.url{{position:absolute;left:0;right:0;top:1548px;display:flex;align-items:center;justify-content:center;gap:28px;font:700 34px/1 Inter;letter-spacing:.02em;color:#EEE6CA}}
.url i{{display:block;width:2px;height:46px;background:rgba(238,230,202,.35)}}
.url img{{height:46px;transform:translateY(9px)}}
"""

def page(r):
    m = r.get("mascot")
    hw = 570 if m else 900
    ing = "".join(f'<li class="{"pc" if "Power Coffee" in i else ""}">{html.escape(i)}</li>' for i in r["ing"])
    xc = f'<span class="xc">⚡ {html.escape(r["extra"])}</span>' if r.get("extra") else ""
    mascot = f'<img class="mascot" id="mascot" style="height:{MH[m]}px" src="file://{ASSETS}/fw-pose-{m}.webp">' if m else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="s" style="--a:{ACCENT[r['n']]};--hw:{hw}px;--dw:{hw if m else 880}px">
<div class="glow"></div><div class="dots"></div>{'' if m else f'<div class="num">{r["n"]}</div>'}
<div class="frame"></div>
<div class="top"><span class="eb">Recipe {r['n']} / 10</span><span class="pill">{html.escape(r['tag'])}</span></div>
<h1 class="h" id="h"><span>{html.escape(r['t1'])}</span><span class="l2">{html.escape(r['t2'])}</span></h1>
<div class="desc" id="desc">{html.escape(r['desc'])}<br>{xc}</div>
{mascot}
<div class="card" id="card"><div><h4>You'll need</h4><ul>{ing}</ul></div><img class="pack" src="file://{ASSETS}/fw-pack.jpg"></div>
<div class="cta">Get all 10 recipes free →</div>
<div class="url"><span>www.thepowercoffee.com</span><i></i><img src="file:///Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/Sales_motor/daily_content/_brand_kit/logos/amazon_logo_cream.svg"></div>
</div>
<script>
document.fonts.ready.then(()=>{{
const h=document.getElementById('h'),W=h.clientWidth,d=document.getElementById('desc'),c=document.getElementById('card'),m=document.getElementById('mascot');
const lis=[...c.querySelectorAll('li')];
function fitHead(max){{let f=max;for(const s of h.children)s.style.fontSize=f+'px';
  while([...h.children].some(s=>s.scrollWidth>W)&&f>90){{f-=4;for(const s of h.children)s.style.fontSize=f+'px'}}return f}}
function layout(){{
  d.style.top=(h.offsetTop+h.offsetHeight+26)+'px';
  const db=d.offsetTop+d.offsetHeight;
  let ct;
  if(m){{m.style.top='362px';ct=Math.max(db+44,362+m.offsetHeight-36);}}
  else{{ct=Math.max(db+56,Math.round((db+1412-c.offsetHeight)/2));}}
  c.style.top=ct+'px';
  return ct+c.offsetHeight<=1372;
}}
let hmax=200,lf=43;fitHead(hmax);
while(!layout()){{ if(hmax>170){{hmax-=10;fitHead(hmax)}} else if(lf>35){{lf-=2;lis.forEach(l=>l.style.fontSize=lf+'px')}} else if(hmax>120){{hmax-=10;fitHead(hmax)}} else break; }}
document.title=(layout()?'ok':'OVERFLOW')+' lf='+lf+' h='+hmax;
}});
</script></body></html>"""

out = HERE / "out"; out.mkdir(exist_ok=True)
for r in R:
    if only and r["n"] not in only: continue
    hp = HERE / f"story_{r['n']}.html"; hp.write_text(page(r), encoding="utf-8")
    png = out / f"recipe_{r['n']}.png"
    prof = tempfile.mkdtemp(prefix="chr")
    try:
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--user-data-dir={prof}",
            "--allow-file-access-from-files", "--force-device-scale-factor=1", "--window-size=1080,1920",
            "--virtual-time-budget=3000", f"--screenshot={png}", f"file://{hp}"],
            timeout=30, capture_output=True)
    except subprocess.TimeoutExpired:
        pass
    shutil.rmtree(prof, ignore_errors=True)
    print(r["n"], png.exists())
