import hashlib, html
P={ # 24x24 stroke icons (original, Feather-style)
"vaults":'<rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/><circle cx="12" cy="16" r="1.5"/>',
"platforms":'<path d="M17.5 19H7a5 5 0 1 1 1-9.9A6 6 0 0 1 19.5 11 4 4 0 0 1 17.5 19z"/>',
"photos":'<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="8.5" cy="9.5" r="1.5"/><path d="M21 16l-5-5-9 9"/>',
"crypto":'<path d="M12 2l8.5 5v10L12 22l-8.5-5V7z"/><path d="M9 9h4.5a2 2 0 0 1 0 4H9zm0 4h5a2 2 0 0 1 0 4H9zm1.5-6v12"/>',
"estate":'<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
"memorial":'<path d="M12 21s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.6-7 10-7 10z"/>',
"tools":'<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
"guides":'<path d="M4 4.5A2.5 2.5 0 0 1 6.5 2H20v17H6.5A2.5 2.5 0 0 0 4 21.5z"/><path d="M4 21.5A2.5 2.5 0 0 1 6.5 19H20v3H6.5"/>',
"best":'<circle cx="12" cy="9" r="6"/><path d="M8.5 14L7 22l5-3 5 3-1.5-8"/>',
"compare":'<rect x="3" y="4" width="7" height="16" rx="1.5"/><rect x="14" y="4" width="7" height="16" rx="1.5"/><path d="M6.5 9v6M17.5 9v6"/>',
"advertise":'<path d="M3 11v2a1 1 0 0 0 1 1h3l6 4V6L7 10H4a1 1 0 0 0-1 1z"/><path d="M16.5 8.5a5 5 0 0 1 0 7"/>',
"shield":'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
}
def icon(name,size=28,cls="ico"):
    return f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{P[name]}</svg>'
PAL=["#0a8ea2","#3d6b8f","#6a5a8f","#8a6d3b","#4f7a4a","#7a4f5f","#3f5f7a"]
def mono(name,size=40):
    w=[x for x in name.replace("/"," ").replace("(", " ").split() if x[0].isalnum()]
    ini=(w[0][0]+(w[1][0] if len(w)>1 else w[0][1:2])).upper() if w else "?"
    c=PAL[int(hashlib.md5(name.encode()).hexdigest(),16)%len(PAL)]
    return f'<svg class="mono" width="{size}" height="{size}" viewBox="0 0 40 40" aria-hidden="true" focusable="false"><rect width="40" height="40" rx="10" fill="{c}"/><text x="20" y="25.5" text-anchor="middle" font-family="system-ui,sans-serif" font-size="15" font-weight="700" fill="#fff">{html.escape(ini)}</text></svg>'
HERO='''<svg class="hero" viewBox="0 0 480 300" role="img" aria-label="Illustration: organised folders protected by a shield and a key" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="hg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e3f2f4"/><stop offset="1" stop-color="#f3efe4"/></linearGradient></defs><rect x="10" y="10" width="460" height="280" rx="28" fill="url(#hg)"/><g opacity=".5" fill="none" stroke="#c9dcda" stroke-width="2"><circle cx="400" cy="70" r="40"/><circle cx="400" cy="70" r="62"/></g><g transform="translate(70 70)"><path d="M0 22a10 10 0 0 1 10-10h50l14 14h96a10 10 0 0 1 10 10v104a10 10 0 0 1-10 10H10A10 10 0 0 1 0 140z" fill="#cfe6ea"/><path d="M14 44a10 10 0 0 1 10-10h60l14 14h96a10 10 0 0 1 10 10v94a10 10 0 0 1-10 10H24a10 10 0 0 1-10-10z" fill="#7fbfcb"/><path d="M28 66a10 10 0 0 1 10-10h68l14 14h94a10 10 0 0 1 10 10v84a10 10 0 0 1-10 10H38a10 10 0 0 1-10-10z" fill="#0a8ea2"/><rect x="52" y="98" width="90" height="10" rx="5" fill="#e3f2f4" opacity=".9"/><rect x="52" y="118" width="130" height="10" rx="5" fill="#e3f2f4" opacity=".6"/><rect x="52" y="138" width="70" height="10" rx="5" fill="#e3f2f4" opacity=".6"/></g><g transform="translate(322 118)"><path d="M48 0l48 18v40c0 34-26 56-48 66C26 114 0 92 0 58V18z" fill="#fff" stroke="#0a8ea2" stroke-width="5"/><path d="M28 60l14 14 28-28" fill="none" stroke="#0a8ea2" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g><g transform="translate(250 228) rotate(-20)" fill="none" stroke="#b08a3e" stroke-width="7" stroke-linecap="round"><circle cx="0" cy="0" r="16"/><path d="M16 0h56M56 0v14M68 0v10"/></g></svg>'''
