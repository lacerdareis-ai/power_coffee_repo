import json, subprocess, sys, html, tempfile, shutil
from pathlib import Path
HERE=Path(__file__).parent
PC=Path("/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee")
FONTS=PC/"Sales_motor/daily_content/_brand_kit/fonts"; A=PC/"homepage_first_win/theme/assets"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
S=json.load(open(HERE/"stories.json")); only=sys.argv[1:]
CSS=f"""
@font-face{{font-family:Anton;src:url('file://{FONTS}/Anton-Regular.ttf')}}
@font-face{{font-family:Inter;src:url('file://{FONTS}/Inter-Variable.ttf');font-weight:100 900}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:#0A2242}}
.s{{position:relative;width:1080px;height:1920px;background:#0A2242;color:#EEE6CA;font-family:Inter,sans-serif;overflow:hidden}}
.dots{{position:absolute;inset:0;background-image:radial-gradient(rgba(238,230,202,.07) 1.6px,transparent 1.8px);background-size:10px 10px}}
.glow{{position:absolute;inset:0;background:radial-gradient(60% 30% at 85% 18%,rgba(212,163,58,.25),transparent 70%)}}
.frame{{position:absolute;inset:44px;border:3px solid rgba(238,230,202,.35);border-radius:6px}}
.eb{{position:absolute;left:96px;top:300px;display:flex;align-items:center;gap:18px;font:800 28px/1 Inter;letter-spacing:.2em;text-transform:uppercase;color:#D4A33A}}
.eb::before{{content:"";width:44px;height:3px;background:#D4A33A}}
.h{{position:absolute;left:92px;top:360px;width:896px;font:400 176px/.9 Anton;text-transform:uppercase}}
.h span{{display:block;white-space:nowrap}} .h .l2{{color:#429EEB}}
.sub{{position:absolute;left:96px;width:880px;font:500 42px/1.32 Inter;color:#C4BC9E}}
.photo{{position:absolute;left:80px;right:80px;border-radius:32px;background-size:cover;box-shadow:0 30px 60px rgba(0,0,0,.35);border:4px solid #EEE6CA}}
.mascot{{position:absolute;right:56px;width:250px;filter:drop-shadow(0 14px 24px rgba(0,0,0,.4));z-index:3}}
.cta{{position:absolute;left:80px;right:80px;top:1412px;height:112px;border-radius:999px;background:#D4A33A;color:#0A2242;display:flex;align-items:center;justify-content:center;font:800 36px/1 Inter;letter-spacing:.04em;text-transform:uppercase;padding:0 30px;text-align:center}}
.url{{position:absolute;left:0;right:0;top:1548px;display:flex;align-items:center;justify-content:center;gap:28px;font:700 34px/1 Inter;letter-spacing:.02em;color:#EEE6CA}}
.url i{{display:block;width:2px;height:46px;background:rgba(238,230,202,.35)}}
.url img{{height:46px;transform:translateY(9px)}}
"""
def page(s):
    m=s.get("mascot")
    mascot=f'<img class="mascot" id="m" src="file://{A}/fw-pose-{m}.webp">' if m else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s">
<div class="dots"></div><div class="glow"></div><div class="frame"></div>
<div class="eb">{html.escape(s['eb'])}</div>
<h1 class="h" id="h"><span>{html.escape(s['t1'])}</span><span class="l2">{html.escape(s['t2'])}</span></h1>
<p class="sub" id="sub">{html.escape(s['sub'])}</p>
<div class="photo" id="ph" style="background-image:url('file://{A}/{s['img']}');background-position:{s['pos']};background-size:{s.get('size','cover')}"></div>{mascot}
<div class="cta">{html.escape(s['cta'])}</div><div class="url"><span>www.thepowercoffee.com</span><i></i><img src="file:///Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/Sales_motor/daily_content/_brand_kit/logos/amazon_logo_cream.svg"></div>
</div><script>
document.fonts.ready.then(()=>{{const h=document.getElementById('h'),W=h.clientWidth;let f=176;
const fit=()=>[...h.children].some(x=>x.scrollWidth>W);while(fit()&&f>100){{f-=4;for(const x of h.children)x.style.fontSize=f+'px'}}
const sub=document.getElementById('sub');sub.style.top=(h.offsetTop+h.offsetHeight+30)+'px';
const ph=document.getElementById('ph');const top=sub.offsetTop+sub.offsetHeight+50;ph.style.top=top+'px';ph.style.height=(1372-top)+'px';
const m=document.getElementById('m');if(m){{m.style.top=(1372-m.offsetHeight+30)+'px'}}
document.title='ph '+(1372-top);}});
</script></body></html>"""
out=HERE/"out";out.mkdir(exist_ok=True)
for s in S:
    if only and s["n"] not in only: continue
    hp=HERE/f"story_{s['n']}.html";hp.write_text(page(s),encoding="utf-8");png=out/f"story_{s['n']}.png";prof=tempfile.mkdtemp()
    try: subprocess.run([CHROME,"--headless=new","--disable-gpu","--hide-scrollbars",f"--user-data-dir={prof}","--allow-file-access-from-files","--force-device-scale-factor=1","--window-size=1080,1920","--virtual-time-budget=5000","--run-all-compositor-stages-before-draw",f"--screenshot={png}",f"file://{hp}"],timeout=30,capture_output=True)
    except subprocess.TimeoutExpired: pass
    shutil.rmtree(prof,ignore_errors=True);print(s["n"],png.exists())
