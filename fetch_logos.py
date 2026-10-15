import re,io,sys,urllib.request,urllib.parse
from PIL import Image
HOME={"bitwarden":"https://bitwarden.com","1password":"https://1password.com","keeper":"https://www.keepersecurity.com","lastpass-emergency-access":"https://www.lastpass.com","dashlane":"https://www.dashlane.com","google-inactive-account-manager":"https://myaccount.google.com","apple-legacy-contact":"https://www.apple.com","trust-and-will":"https://trustandwill.com","goodtrust":"https://mygoodtrust.com","everplans":"https://www.everplans.com","prisidio":"https://www.prisidio.com","casa":"https://casa.io","unchained":"https://www.unchained.com","vault12":"https://vault12.com","ledger-recover":"https://www.ledger.com","proton-pass":"https://proton.me/pass"}
UA={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126 Safari/537.36"}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=20).read()
def _run():
  pass
res={}
if __name__=='__main__':
  for slug,home in HOME.items():
      cands=[]
      try:
          h=get(home).decode("utf8","ignore")
          for tag in re.findall(r'<link[^>]+>',h,re.I):
              rel=re.search(r'rel=["\']([^"\']+)',tag,re.I); href=re.search(r'href=["\']([^"\']+)',tag,re.I)
              if rel and href and "icon" in rel.group(1).lower():
                  sz=re.search(r'sizes=["\'](\d+)',tag); pri=(3 if "apple" in rel.group(1).lower() else 1)*1000+(int(sz.group(1)) if sz else 32)
                  if href.group(1).endswith(".svg"): pri=500
                  cands.append((pri,urllib.parse.urljoin(home+"/",html_unescape(href.group(1))) if False else urllib.parse.urljoin(home+"/",href.group(1).replace("&amp;","&"))))
      except Exception as e: print(slug,"home err",e)
      cands.sort(reverse=True); cands.append((0,home+"/apple-touch-icon.png")); cands.append((0,home+"/favicon.ico"))
      ok=False
      for _,u in cands:
          try:
              im=Image.open(io.BytesIO(get(u)))
              if hasattr(im,"n_frames") and getattr(im,"format","")=="ICO": im.size=max(im.info.get("sizes",[im.size]))
              im=im.convert("RGBA")
              if im.width<32: continue
              im=im.resize((80,80),Image.LANCZOS)
              im.save(f"assets/logos/{slug}.webp","WEBP",quality=90,method=6); res[slug]=u; ok=True; break
          except Exception as e: pass
      print(slug, res.get(slug,"FALLBACK monogram"))
