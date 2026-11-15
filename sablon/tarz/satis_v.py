"""Satış akışının temalı varyasyonları (4 kart, 1080x1350). Aynı 4 adım, farklı örnek metin ve kapaklar.
Kullanım: python3 satis_v.py [tema ...]   (çıktı: 2026-11/tarz/sv-<tema>-1..4.jpg)
Reels: python3 reel.py sv-<tema>-reel sv-<tema>-1 sv-<tema>-2 sv-<tema>-3 sv-<tema>-4"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tarz import doc, cover_html, C
from satis import head, foot, manuscript, R, OUT
from playwright.sync_api import sync_playwright

# tema: (adım1 açıklama, el yazması 1, el yazması 2, adım2 kapakları(3), adım3 ızgara(6), seçilen, adım4 kapağı)
V = {
 "roman": ("Romanın çekmecede mi?<br>Dosyanı yükle, gerisi bizde.", "Romanım", "1. Bölüm",
           ["noir-roman", "sinematik", "edebi-minimal"], ["noir-roman", "gerilim", "yagli-boya", "sinematik", "romantik-suluboya", "edebi-minimal"], "sinematik", "sinematik"),
 "cocuk": ("Çocuğuna anlattığın masal,<br>birkaç paragraf yeter.", "Masalım", "Kahramanım",
           ["kece-masal", "suluboya-masal", "3d-oyuncak"], ["renkli-cizgi-film", "suluboya-masal", "kuru-boya", "3d-oyuncak", "kece-masal", "sevimli-hayvanlar"], "suluboya-masal", "suluboya-masal"),
 "ani": ("Anıların, eski defterin,<br>ailenin hikâyesi.", "Anılarım", "Dedemin Defteri",
         ["kolaj-sanati", "karakalem", "vintage-afis"], ["kolaj-sanati", "karakalem", "vintage-afis", "botanik-atlas", "seyahat-suluboya", "yol-hikayesi"], "karakalem", "karakalem"),
 "siir": ("Şiirlerin, denemelerin,<br>defterindeki dizeler.", "Şiirlerim", "Dizeler",
          ["ebru", "murekkep-firca", "tipografik"], ["ebru", "murekkep-firca", "tipografik", "edebi-minimal", "empresyonist", "linol-edebi"], "ebru", "ebru"),
 "ogretmen": ("Öğrencilerinin hikâyeleri,<br>sınıfının defteri.", "Sınıfımız", "4-B Hikâyeleri",
              ["tebesir-tahtasi", "takim-ruhu", "mizah-karikatur"], ["tebesir-tahtasi", "mizah-karikatur", "takim-ruhu", "eskiz-defteri", "animasyon-filmi", "manga-esintisi"], "tebesir-tahtasi", "tebesir-tahtasi"),
 "fantastik": ("Kurduğun dünya,<br>haritan, kahramanların.", "Dünyam", "Kayıp Krallık",
               ["mitoloji", "karanlik-fantastik", "ejderha-diyari"], ["karanlik-fantastik", "mitoloji", "neon-bilimkurgu", "ejderha-diyari", "gercekustu-genc", "distopya"], "mitoloji", "mitoloji"),
}


def k1(v):
    body, m1, m2 = V[v][0], V[v][1], V[v][2]
    arrow = ("<div style='width:120px;height:120px;border-radius:50%;background:var(--red);color:#fff;font-size:76px;"
             "font-weight:700;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 0 #7d0c12'>↑</div>")
    return doc(f"""{head(1, f"Hikâyeni<br>{R}yükle.</span>", body)}
<div style='position:absolute;top:730px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:70px'>
 {manuscript(320, -6, m1)}{arrow}{manuscript(320, 5, m2)}
</div>
{foot()}""")


def k2(v):
    fan = "".join(f"<div style='margin:0 -22px;transform:rotate({r}deg) translateY({y}px)'>{cover_html(s, 260)}</div>"
                  for s, r, y in zip(V[v][3], (-10, 0, 10), (30, 0, 30)))
    spark = "<div style='font-size:90px;color:var(--red);font-weight:700;line-height:1'>→</div>"
    return doc(f"""{head(2, f"{R}Müteferrika AI</span><br>senin için<br>çalışsın.", "Kapak, karakter ve sayfalar<br>senin için çizilsin.")}
<div style='position:absolute;top:840px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:40px'>
 {manuscript(220, -4, V[v][1])}{spark}<div style='display:flex;align-items:flex-end'>{fan}</div>
</div>
{foot()}""")


def k3(v):
    cells = ""
    for s in V[v][4]:
        on = s == V[v][5]
        ring = ("outline:8px solid var(--red);outline-offset:8px;border-radius:6px;" if on else "opacity:.55;")
        badge = ("<div style='position:absolute;top:-26px;right:-26px;width:64px;height:64px;border-radius:50%;background:var(--red);"
                 "color:#fff;font-size:40px;font-weight:700;display:flex;align-items:center;justify-content:center;z-index:5'>✓</div>" if on else "")
        cells += f"<div style='position:relative;{ring}'>{badge}<img src='{C}/kapak-{s}.jpg' style='height:235px;display:block;border-radius:3px 6px 6px 3px;box-shadow:0 14px 18px rgba(40,25,10,.25)'></div>"
    return doc(f"""{head(3, f"Kendi<br>{R}tarzını</span> seç.", "80 tarzdan ruhuna uyanı seç,<br>kitabını kendi zevkine göre tasarla.")}
<div style='position:absolute;top:690px;left:90px;right:90px;display:flex;flex-wrap:wrap;justify-content:center;align-items:flex-end;gap:44px 46px'>{cells}</div>
{foot()}""")


def k4(v):
    stack = "".join(f"<div style='margin:0 -6px'>{cover_html(V[v][6], h)}</div>" for h in (300, 340, 300))
    return doc(f"""{head(4, f"Kitabını<br>{R}bas.</span>", "Her sayfayı onayla,<br>kitabın elinde olsun.")}
<div style='position:absolute;top:740px;left:0;right:0;display:flex;justify-content:center;align-items:flex-end;height:345px'>{stack}</div>
<div class=shelf style='top:1082px'></div>
<div class=cta style='bottom:120px'>DM at · Kitabını birlikte başlatalım</div>
{foot("Hikâyen senin, kitabın senin")}""")


if __name__ == "__main__":
    temalar = sys.argv[1:] or list(V)
    tmp = os.path.join(os.path.dirname(__file__), "out"); os.makedirs(tmp, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for v in temalar:
            for i, fn in enumerate((k1, k2, k3, k4), 1):
                n = f"sv-{v}-{i}"; f = os.path.join(tmp, n + ".html"); open(f, "w").write(fn(v))
                pg.goto("file://" + f); pg.wait_for_timeout(400)
                pg.screenshot(path=os.path.join(OUT, n + ".jpg"), type="jpeg", quality=90)
        b.close()
    print("ok", temalar)
