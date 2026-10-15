import os, html
from fetch_logos import HOME as _H
OFFICIAL={"bitwarden":"https://bitwarden.com/","1password":"https://1password.com/","keeper":"https://www.keepersecurity.com/","lastpass-emergency-access":"https://www.lastpass.com/","dashlane":"https://www.dashlane.com/","google-inactive-account-manager":"https://myaccount.google.com/inactive","apple-legacy-contact":"https://support.apple.com/en-us/102631","trust-and-will":"https://trustandwill.com/","goodtrust":"https://mygoodtrust.com/","everplans":"https://www.everplans.com/","prisidio":"https://www.prisidio.com/","casa":"https://casa.io/","unchained":"https://www.unchained.com/","vault12":"https://vault12.com/","ledger-recover":"https://www.ledger.com/ledger-recover","proton-pass":"https://proton.me/pass"}
def rel_for(t): return "sponsored noopener" if t.get("sponsored") or t.get("featured") else "nofollow noopener"
def logo(t,size=40):
    from icons import mono
    n=t["name"].split(" (")[0]
    if os.path.exists(f"assets/logos/{t['slug']}.webp"):
        return f'<img class="logo-img" src="/assets/logos/{t["slug"]}.webp" width="{size}" height="{size}" alt="{html.escape(n)} logo" loading="lazy" decoding="async">'
    return mono(t["name"],size)
