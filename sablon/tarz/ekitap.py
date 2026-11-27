"""E-kitap kaydırmalı paylaşımları (1080x1350). Kullanım: python3 ekitap.py  -> 2026-12/ekitap/<set>-<n>.jpg"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from playwright.sync_api import sync_playwright

D = os.path.dirname(os.path.abspath(__file__)); A = f"file://{D}/../assets"; C = f"file://{D}/covers"
OUT = os.path.abspath(os.path.join(D, "../../2026-12/ekitap")); os.makedirs(OUT, exist_ok=True)
RED = "#B5121B"

def page(body, bg, fg="#16181D", wm="dark", n=None, tot=4):
    wmf = "" if wm == "dark" else "background:#F4EEE3;padding:12px 22px;border-radius:8px;box-sizing:content-box;"
    dots = "" if n is None else "<div class=dots>" + "".join(f"<i style='opacity:{1 if i==n else .3}'></i>" for i in range(1, tot+1)) + "</div>"
    return f"""<html><head><meta charset=utf-8><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;position:relative;overflow:hidden;background:{bg};color:{fg};font-family:'Liberation Sans',sans-serif}}
.wm{{position:absolute;top:52px;left:0;right:0;text-align:center;z-index:10}} .wm img{{height:48px;{wmf}}}
.h{{font-family:'Liberation Serif',serif;font-weight:700;letter-spacing:-1px}}
.r{{color:{RED}}}
.ph{{position:relative;background:#0d0d0f;border-radius:58px;padding:22px 16px;box-shadow:0 40px 60px rgba(0,0,0,.4),inset 0 0 0 3px #2a2a2e}}
.ph:after{{content:"";position:absolute;top:30px;left:50%;width:110px;height:26px;margin-left:-55px;background:#0d0d0f;border-radius:14px}}
.ph .s{{border-radius:40px;overflow:hidden;background:#fff}}
.tb{{background:#111;border-radius:36px;padding:26px;box-shadow:0 40px 60px rgba(0,0,0,.4),inset 0 0 0 3px #2c2c30}}
.tb .s{{border-radius:14px;overflow:hidden;background:#fff}}
.dots{{position:absolute;bottom:52px;left:0;right:0;display:flex;justify-content:center;gap:12px}} .dots i{{width:14px;height:14px;border-radius:50%;background:currentColor}}
.ft{{position:absolute;bottom:44px;left:80px;font-size:28px;font-weight:700;opacity:.75}}
</style></head><body><div class=wm><img src='{A}/wordmark.png'></div>{body}{dots}<div class=ft>@eyayinevi</div></body></html>"""

def phone(slug, w, extra=""):
    return f"<div class=ph style='width:{w}px;{extra}'><div class=s><img src='{C}/kapak-{slug}.jpg' style='width:100%;display:block'></div></div>"

def tablet(slug, w, extra=""):
    return f"<div class=tb style='width:{w}px;{extra}'><div class=s style='display:flex;background:#f7f3ec'><img src='{C}/kapak-{slug}.jpg' style='width:50%;display:block'><div style='width:50%;padding:34px 28px;font-family:Liberation Serif,serif;font-size:19px;line-height:1.55;color:#333'>{lorem()}</div></div></div>"

def lorem():
    return "".join(f"<div style='height:9px;background:#d8cfc0;border-radius:4px;margin-bottom:15px;width:{x}%'></div>" for x in (60,100,94,98,88,100,91,72,0,100,96,90,99,84,95,66,100,93,97,89,78))

def book(slug, h, rot=0):
    return f"<div style='display:inline-block;transform:rotate({rot}deg);filter:drop-shadow(0 30px 28px rgba(0,0,0,.38))'><img src='{C}/kapak-{slug}.jpg' style='height:{h}px;display:block;border-radius:3px 7px 7px 3px'></div>"

# ---------- SET A: koyu lacivert, cihaz odaklı (yazar = satıcı) ----------
NAVY = "#101A2E"; CRE = "#F4EEE3"
A1 = page(f"""
<div style='position:absolute;top:170px;left:80px;right:80px;color:#fff'>
 <div class=h style='font-size:112px;line-height:.98'>Kitabın artık<br><span style='color:#E2373F'>cebinde de.</span></div>
 <div style='font-size:40px;line-height:1.4;color:#c9cfdb;margin-top:28px'>E-kitabını yükle, eyayinevi.com'da sat.</div>
</div>
<div style='position:absolute;left:110px;top:640px'>{tablet("edebi-minimal", 640, "transform:rotate(-6deg)")}</div>
<div style='position:absolute;right:110px;top:600px'>{phone("sinematik", 280, "transform:rotate(5deg)")}</div>
""", NAVY, "#fff", "light", 1)

A2 = page(f"""
<div style='position:absolute;top:170px;left:80px;right:80px;color:#fff'>
 <div style='font-size:34px;font-weight:700;color:#E2373F;letter-spacing:4px'>01 · YÜKLE</div>
 <div class=h style='font-size:96px;line-height:1;margin-top:18px'>Dosyan hazırsa<br>kitabın da hazır.</div>
 <div style='font-size:38px;line-height:1.45;color:#c9cfdb;margin-top:28px'>Word dosyanı ya da metnini yükle.<br>Kapağını Müteferrika AI çizsin.</div>
</div>
<div style='position:absolute;left:0;right:0;top:760px;display:flex;justify-content:center;align-items:center;gap:50px'>
 <div style='width:300px;height:400px;background:#fffdf8;border-radius:10px;padding:34px 30px;transform:rotate(-5deg);overflow:hidden;box-shadow:0 26px 34px rgba(0,0,0,.4)'>
  <div style='font-size:22px;font-weight:700;color:#444;margin-bottom:18px'>roman_son.docx</div>{lorem()}</div>
 <div style='font-size:120px;color:#E2373F;font-weight:700'>→</div>
 {phone("gotik", 250)}
</div>
""", NAVY, "#fff", "light", 2)

A3 = page(f"""
<div style='position:absolute;top:170px;left:80px;right:80px;color:#fff;text-align:center'>
 <div style='font-size:34px;font-weight:700;color:#E2373F;letter-spacing:4px'>02 · YAYINLA</div>
 <div class=h style='font-size:96px;line-height:1;margin-top:18px'>Okurun nerede,<br>kitabın orada.</div>
 <div style='font-size:38px;color:#c9cfdb;margin-top:24px'>Telefonda, tablette, bilgisayarda.</div>
</div>
<div style='position:absolute;left:0;right:0;top:640px;height:560px'>
 <div style='position:absolute;left:150px;top:40px;width:780px;height:470px;background:#1b1b1f;border-radius:22px 22px 0 0;padding:22px;box-shadow:0 30px 50px rgba(0,0,0,.45)'>
  <div style='background:#f7f3ec;height:100%;border-radius:6px;display:flex;justify-content:center;align-items:center'>{book("klasik-gravur", 360)}</div></div>
 <div style='position:absolute;left:100px;top:532px;width:880px;height:26px;background:linear-gradient(#bfc3ca,#8d9199);border-radius:0 0 22px 22px'></div>
 <div style='position:absolute;left:70px;top:150px'>{phone("romantik-suluboya", 210, "transform:rotate(-6deg)")}</div>
 <div style='position:absolute;right:90px;top:60px'>{tablet("yagli-boya", 260, "transform:rotate(5deg)")}</div>
</div>
""", NAVY, "#fff", "light", 3)

A4 = page(f"""
<div style='position:absolute;top:170px;left:80px;right:80px;color:#fff;text-align:center'>
 <div style='font-size:34px;font-weight:700;color:#E2373F;letter-spacing:4px'>03 · SAT</div>
 <div class=h style='font-size:100px;line-height:1;margin-top:18px'>Yazar sensin.<br>Mağaza da senin.</div>
</div>
<div style='position:absolute;left:190px;right:190px;top:560px;background:#fff;color:#16181D;border-radius:30px;padding:40px;display:flex;gap:36px;box-shadow:0 40px 60px rgba(0,0,0,.45)'>
 {book("noir-roman", 330)}
 <div style='flex:1'>
  <div style='font-size:22px;font-weight:700;color:{RED};letter-spacing:2px'>E-KİTAP</div>
  <div class=h style='font-size:52px;line-height:1.02;margin-top:10px'>Senin<br>kitabın</div>
  <div style='font-size:26px;color:#6a5f53;margin-top:10px'>Yazar: Sen</div>
  <div style='margin-top:40px;background:{RED};color:#fff;font-size:30px;font-weight:700;text-align:center;padding:20px;border-radius:14px'>Satın al</div>
 </div>
</div>
<div style='position:absolute;left:0;right:0;top:1060px;text-align:center;color:#fff'>
 <div class=h style='font-size:60px'>eyayinevi.com</div>
 <div style='font-size:36px;color:#c9cfdb;margin-top:8px'>E-kitabını yükle · Satışa başla</div>
</div>
""", NAVY, "#fff", "light", 4)

# ---------- SET B: krem + kırmızı, basılı & e-kitap yan yana ----------
B1 = page(f"""
<div style='position:absolute;top:160px;left:0;right:0;text-align:center'>
 <div class=h style='font-size:110px;line-height:1'>Basılı mı?<br><span class=r>E-kitap mı?</span></div>
 <div style='font-size:42px;color:#4a4038;margin-top:24px'>İkisi de. Aynı kitap, iki raf.</div>
</div>
<div style='position:absolute;left:0;right:0;top:640px;display:flex;justify-content:center;align-items:flex-end;gap:80px'>
 {book("ebru", 520, -4)}
 {phone("ebru", 270, "transform:rotate(4deg)")}
</div>
""", CRE, n=1)

B2 = page(f"""
<div style='position:absolute;inset:0;background:{RED}'></div>
<div style='position:absolute;top:170px;left:80px;right:80px;color:#fff'>
 <div class=h style='font-size:104px;line-height:1'>Baskıyı bekleme.</div>
 <div class=h style='font-size:104px;line-height:1;color:#F4C95D'>Okur seni bekliyor.</div>
 <div style='font-size:40px;line-height:1.4;margin-top:28px;opacity:.95'>E-kitabın yayına girdiği an satışa açılır.</div>
</div>
<div style='position:absolute;right:120px;top:640px'>{phone("modern-soyut", 330, "transform:rotate(-4deg)")}</div>
<div style='position:absolute;left:100px;top:760px;color:#fff;font-size:44px;font-weight:700;line-height:1.9'>
 ✓ Kargo yok<br>✓ Stok yok<br>✓ Her yerden erişim</div>
""", RED, "#fff", "light", 2)

B3 = page(f"""
<div style='position:absolute;top:160px;left:80px;right:80px'>
 <div class=h style='font-size:96px;line-height:1'>Kapak da<br><span class=r>sana benzesin.</span></div>
 <div style='font-size:40px;color:#4a4038;margin-top:24px'>E-kitabının kapağını 80 çizim tarzından biriyle tasarla.</div>
</div>
<div style='position:absolute;left:60px;right:60px;top:690px;display:flex;justify-content:center;gap:34px'>
 {phone("murekkep-firca", 220, "transform:rotate(-5deg)")}
 {phone("neon-bilimkurgu", 220, "transform:translateY(-40px)")}
 {phone("suluboya-masal", 220, "transform:rotate(5deg)")}
</div>
""", "#EFE6D6", n=3)

B4 = page(f"""
<div style='position:absolute;top:200px;left:0;right:0;text-align:center'>
 <div class=h style='font-size:104px;line-height:1'>Kitabını yaz.<br><span class=r>Gerisini biz kuralım.</span></div>
</div>
<div style='position:absolute;left:0;right:0;top:500px;display:flex;justify-content:center'>{tablet("art-deco", 600)}</div>
<div style='position:absolute;left:0;right:0;top:1130px;text-align:center'>
 <div style='display:inline-block;background:#16181D;color:#fff;font-size:44px;font-weight:700;padding:24px 50px;border-radius:16px'>eyayinevi.com · E-kitabını yükle</div>
</div>
""", CRE, n=4)

K = {"ek-a-1": A1, "ek-a-2": A2, "ek-a-3": A3, "ek-a-4": A4, "ek-b-1": B1, "ek-b-2": B2, "ek-b-3": B3, "ek-b-4": B4}

if __name__ == "__main__":
    tmp = os.path.join(D, "out"); os.makedirs(tmp, exist_ok=True)
    names = sys.argv[1:] or list(K)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for n in names:
            f = os.path.join(tmp, n + ".html"); open(f, "w").write(K[n])
            pg.goto("file://" + f); pg.wait_for_timeout(500)
            pg.screenshot(path=os.path.join(OUT, n + ".jpg"), type="jpeg", quality=90)
        b.close()
    print("ok", len(names))
