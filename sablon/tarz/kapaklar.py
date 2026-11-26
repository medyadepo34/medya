"""Profil ızgarası için farklı ilk kare (kapak) tasarımları, 1080x1350. Her paylaşım farklı düzenle açılır.
Kullanım: python3 kapaklar.py   (çıktı: 2026-11/kapak/<ad>.jpg ve Reels kapakları için <ad>-9x16.jpg)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tarz import S
from playwright.sync_api import sync_playwright
from PIL import Image, ImageFilter

D = os.path.dirname(os.path.abspath(__file__)); A = f"file://{D}/../assets"; C = f"file://{D}/covers"
OUT = os.path.abspath(os.path.join(D, "../../2026-11/kapak")); os.makedirs(OUT, exist_ok=True)
RED = "#B5121B"

def page(body, bg="#F4EEE3", fg="#16181D", wm="dark"):
    wmf = "" if wm == "dark" else "background:#F4EEE3;padding:12px 22px;border-radius:8px;box-sizing:content-box;"
    return f"""<html><head><meta charset=utf-8><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;position:relative;overflow:hidden;background:{bg};color:{fg};font-family:'Liberation Serif',serif}}
.wm{{position:absolute;top:52px;left:0;right:0;text-align:center;z-index:10}} .wm img{{height:50px;{wmf}}}
.bk{{position:relative;display:inline-block;filter:drop-shadow(0 30px 28px rgba(0,0,0,.38))}}
.bk img{{display:block;border-radius:3px 7px 7px 3px}}
.bk:before{{content:"";position:absolute;left:0;top:0;bottom:0;width:20px;z-index:2;border-radius:3px 0 0 3px;
 background:linear-gradient(to right,rgba(0,0,0,.3),rgba(255,255,255,.18) 45%,rgba(0,0,0,.06))}}
.ft{{position:absolute;bottom:44px;left:80px;right:80px;display:flex;justify-content:space-between;font-size:28px;font-weight:700;opacity:.8}}
.r{{color:{RED}}}
</style></head><body><div class=wm><img src='{A}/wordmark.png'></div>{body}</body></html>"""

def bk(slug, h, rot=0, extra=""):
    return f"<div class=bk style='transform:rotate({rot}deg);{extra}'><img src='{C}/kapak-{slug}.jpg' style='height:{h}px'></div>"

def ft(color="inherit", right="Kaydır →"):
    return f"<div class=ft style='color:{color}'><span>@eyayinevi</span><span>{right}</span></div>"

# 1) Koyu zemin, büyük soru + tek kitap
def soru(q1, q2, sub, slug, bg="#14161B"):
    return page(f"""
<div style='position:absolute;top:170px;left:80px;right:80px'>
 <div style='font-size:104px;font-weight:700;line-height:1;letter-spacing:-1px;color:#fff'>{q1}<br><span style='color:#E2373F'>{q2}</span></div>
 <div style='font-size:40px;line-height:1.4;color:#cfc8bd;margin-top:30px'>{sub}</div>
</div>
<div style='position:absolute;bottom:150px;left:0;right:0;text-align:center'>{bk(slug, 560, -4)}</div>
{ft('#cfc8bd')}""", bg=bg, wm="light")

# 2) Önce / sonra
def once_sonra(baslik, solyazi, sagyazi, slug, eltitle):
    lines = "".join(f"<div style='height:9px;background:#d9d0c1;border-radius:5px;margin-top:17px;width:{x}%'></div>" for x in (100,92,97,80,95,88,99,70,93,85,60,90,75))
    return page(f"""
<div style='position:absolute;top:160px;left:0;right:0;text-align:center;font-size:86px;font-weight:700;line-height:1.05'>{baslik}</div>
<div style='position:absolute;top:420px;left:60px;right:60px;display:flex;justify-content:space-between;align-items:flex-end'>
 <div style='text-align:center;width:440px'>
  <div style='width:380px;height:520px;margin:0 auto;background:#fffdf8;transform:rotate(-4deg);box-shadow:0 22px 26px rgba(40,25,10,.2);border-radius:4px;padding:40px 36px;overflow:hidden'>
   <div style='font-size:36px;font-weight:700;font-style:italic'>{eltitle}</div>{lines}</div>
  <div style='font-size:34px;margin-top:40px;color:#6a5f53'><b style='color:#16181D'>ÖNCE</b><br>{solyazi}</div>
 </div>
 <div style='font-size:110px;color:{RED};font-weight:700;padding-bottom:300px'>→</div>
 <div style='text-align:center;width:440px'>{bk(slug, 540, 3)}
  <div style='font-size:34px;margin-top:40px;color:#6a5f53'><b class=r>SONRA</b><br>{sagyazi}</div>
 </div>
</div>
{ft('#6a5f53')}""")

# 3) Tarz ızgarası (tam ekran 3x3) + kırmızı bant
def izgara(slugs, b1, b2):
    cells = "".join(f"<div style='background:url({C}/kapak-{s}.jpg) center/cover'></div>" for s in slugs[:9])
    return page(f"""
<div style='position:absolute;inset:0;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,1fr);gap:6px;background:#F4EEE3'>{cells}</div>
<div style='position:absolute;inset:0;background:linear-gradient(rgba(0,0,0,.05),rgba(0,0,0,.25))'></div>
<div style='position:absolute;left:0;right:0;top:470px;background:{RED};color:#fff;text-align:center;padding:46px 40px;box-shadow:0 20px 40px rgba(0,0,0,.35)'>
 <div style='font-size:92px;font-weight:700;line-height:1'>{b1}</div>
 <div style='font-size:42px;margin-top:18px;opacity:.95'>{b2}</div>
</div>
<div style='position:absolute;top:40px;left:50%;transform:translateX(-50%);background:#F4EEE3;padding:14px 26px;border-radius:8px'><img src='{A}/wordmark.png' style='height:44px;display:block'></div>
<div class=ft style='color:#fff;text-shadow:0 2px 6px rgba(0,0,0,.6)'><span>@eyayinevi</span><span>Kaydır →</span></div>""")

# 4) Renkli zemin, büyük tipografik alıntı + küçük kitap
def alinti(soz, alt, slug, bg, fg="#fff", acc="#F4C95D"):
    return page(f"""
<div style='position:absolute;top:150px;left:90px;font-size:300px;line-height:1;color:{acc};font-weight:700'>“</div>
<div style='position:absolute;top:340px;left:90px;right:90px;font-size:82px;line-height:1.12;font-weight:700;font-style:italic'>{soz}</div>
<div style='position:absolute;top:800px;left:90px;width:520px;font-size:38px;line-height:1.4;opacity:.9'>{alt}</div>
<div style='position:absolute;right:80px;bottom:130px'>{bk(slug, 400, 6)}</div>
{ft(fg)}""", bg=bg, fg=fg, wm="light")

# 5) Kitaplık rafı, biri öne çıkmış
def raf(slugs, hero, b1, b2):
    spines = ""
    cols = ["#7a2e2e","#2f4858","#c9a227","#3d405b","#81b29a","#8c2f39","#264653","#e07a5f","#5b4130","#1d3557","#b08a4a","#6b4226"]
    for i, c in enumerate(cols):
        h = 300 + (i * 37) % 90
        spines += f"<div style='width:52px;height:{h}px;background:{c};border-radius:3px;box-shadow:inset -8px 0 0 rgba(0,0,0,.15)'></div>"
    return page(f"""
<div style='position:absolute;top:160px;left:80px;right:80px;text-align:center'>
 <div style='font-size:96px;font-weight:700;line-height:1.02'>{b1}</div>
 <div style='font-size:40px;color:#4a4038;margin-top:22px'>{b2}</div>
</div>
<div style='position:absolute;left:70px;right:70px;top:660px;height:420px;display:flex;align-items:flex-end;gap:10px;justify-content:center'>
 {spines[:len(spines)//2]}<div style='margin:0 18px;transform:translateY(-30px)'>{bk(hero, 460, 0)}</div>{spines[len(spines)//2:]}
</div>
<div style='position:absolute;left:50px;right:50px;top:1078px;height:26px;background:linear-gradient(#5b4130,#3b291d);border-radius:3px;box-shadow:0 12px 20px rgba(40,25,10,.3)'></div>
<div style='position:absolute;top:1130px;left:0;right:0;text-align:center;font-size:34px;font-style:italic' class=r>Senin kitabın da burada olabilir.</div>
{ft('#6a5f53')}""")

# 6) Numaralı yol haritası (sayfa 1-4 başlıkları tek karede)
def yol(b1, items, slug, bg="#EFE6D6"):
    rows = "".join(f"<div style='display:flex;align-items:center;gap:30px;margin-bottom:34px'><div style='font-size:110px;font-weight:700;color:{RED};width:90px;line-height:.9'>{i+1}</div><div style='font-size:42px;font-weight:700;line-height:1.15'>{t}</div></div>" for i, t in enumerate(items))
    return page(f"""
<div style='position:absolute;top:160px;left:80px;right:80px;font-size:90px;font-weight:700;line-height:1.02'>{b1}</div>
<div style='position:absolute;top:470px;left:80px;width:560px'>{rows}</div>
<div style='position:absolute;right:50px;top:560px'>{bk(slug, 400, 5)}</div>
{ft('#6a5f53')}""", bg=bg)

# 7) Tam ekran kapak bulanık arka plan + net kitap + alt başlık
def hero(slug, b1, b2):
    return page(f"""
<div style='position:absolute;inset:-60px;background:url({C}/kapak-{slug}.jpg) center/cover;filter:blur(38px) brightness(.55)'></div>
<div style='position:absolute;top:150px;left:0;right:0;text-align:center'>{bk(slug, 700, 0)}</div>
<div style='position:absolute;bottom:130px;left:70px;right:70px;text-align:center;color:#fff'>
 <div style='font-size:84px;font-weight:700;line-height:1.02;text-shadow:0 4px 18px rgba(0,0,0,.5)'>{b1}</div>
 <div style='font-size:38px;margin-top:18px;opacity:.92'>{b2}</div>
</div>
{ft('#fff')}""", bg="#111", wm="light")

K = {
 # 1330 slider ilk kareleri
 "k-polisiye": soru("Katil kim?", "Sadece sen biliyorsun.", "Polisiyeni yükle, Müteferrika AI kapağını ve sayfalarını çizsin.", "noir-roman"),
 "k-gezi": alinti("Gezdiğim her yer bir sayfa oldu.", "Yol notlarını yükle, seyahat suluboyasıyla kitabın çizilsin.", "seyahat-suluboya", "#1F5F63"),
 "k-bilimkurgu": hero("neon-bilimkurgu", "Yıl 2187. Kitabın hazır.", "Kurduğun geleceği yükle, neon bilimkurguyla çizelim."),
 "k-siir": alinti("Dizeler defterde değil, rafta yaşar.", "Şiirlerini yükle; ebrudan mürekkep fırçaya tarzını seç.", "ebru", "#7A1F2B", acc="#E9C46A"),
 "k-cocuk": once_sonra("Bu akşamki masal,<br>yarın bir kitap.", "Aklındaki masal", "Elinde basılı kitap", "suluboya-masal", "Masalım"),
 "k-roman": raf(["x"], "sinematik", "Romanın<br><span class=r>çekmecede</span> mi?", "İlk bölüm bile yeter. Yükle, tasarla, bas."),
 "k-ani": yol("Dedenin hikâyesi<br><span class=r>4 adımda</span> kitap.", ["Anıları yükle", "Müteferrika AI çizsin", "Tarzını seç", "Kitabını bas"], "karakalem"),
 # Reels kapakları (ızgarada görünen)
 "r-fantastik": hero("mitoloji", "Kurduğun dünya artık bir kitap.", "Mitolojiden karanlık fantastiğe 80 tarz."),
 "r-roman": once_sonra("Dosyandaki roman,<br>raftaki kitap.", "Bilgisayarındaki dosya", "Basılı romanın", "sinematik", "Romanım"),
 "r-cocuk": izgara(["suluboya-masal","kece-masal","3d-oyuncak","renkli-cizgi-film","kuru-boya","sevimli-hayvanlar","pastel-boya-ruyasi","uyku-vakti","deniz-alti"], "Aynı masal, 80 tarz.", "Çocuğun hangisini seçerdi?"),
 "r-polisiye": raf(["x"], "noir-roman", "Dosya kapanmadı.<br><span class=r>Kitap açılıyor.</span>", "Polisiyeni yükle, noir tarzında basalım."),
 "r-gezi": izgara(["seyahat-suluboya","yol-hikayesi","vintage-afis","botanik-atlas","kentsel-eskiz","gokyuzu-manzaralari","minyatur","art-deco","empresyonist"], "Yol hikâyen, senin tarzın.", "Gezi kitabını 80 tarzdan biriyle bastır."),
 "r-bilimkurgu": soru("Gelecek", "senin kaleminde.", "Gezegenlerini ve robotlarını yükle, Müteferrika AI çizsin.", "uzay-akademisi", bg="#0B132B"),
 "r-ogretmen": yol("Sınıfının kitabı<br><span class=r>4 adımda.</span>", ["Hikâyeleri yükle", "Müteferrika AI çizsin", "Tarzı seç", "Kitabı bas"], "tebesir-tahtasi", bg="#E4EDE6"),
}

def reel_cover(src, dst):
    im = Image.open(src).convert("RGB")
    bg = im.resize((1080, 1920)).filter(ImageFilter.GaussianBlur(40))
    bg.paste(im, (0, (1920 - 1350) // 2)); bg.save(dst, quality=92)

if __name__ == "__main__":
    tmp = os.path.join(D, "out"); os.makedirs(tmp, exist_ok=True)
    names = sys.argv[1:] or list(K)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for n in names:
            f = os.path.join(tmp, n + ".html"); open(f, "w").write(K[n])
            pg.goto("file://" + f); pg.wait_for_timeout(500)
            out = os.path.join(OUT, n + ".jpg"); pg.screenshot(path=out, type="jpeg", quality=90)
            if n.startswith("r-"): reel_cover(out, os.path.join(OUT, n + "-9x16.jpg"))
        b.close()
    print("ok", len(names))
