import json, html, re
E=html.escape
D=json.load(open("data/tools.json"))
LABEL_CLS={"Top pick":"l-top","Good":"l-good","Use with caution":"l-warn","Not recommended":"l-no"}
def merge(TOOLS):
    for t in TOOLS:
        t.update(D["tools"][t["slug"]]); t["reviewed_on"]=D["reviewed_on"]
        v=t["verdict"]; s=v.split(". ")[0].rstrip(".")+"."
        t["one_liner"]=s if len(s)<=140 else s[:137].rsplit(" ",1)[0]+"…"
def pill(label): return f'<span class="vl {LABEL_CLS[label]}">{E(label)}</span>'
def card(t,CATS,logo,OFFICIAL,rel_for,compare_box=False):
    sp='<span class="vl l-sp">Sponsored</span>' if t.get("sponsored") else ""
    cb=f'<label class="cmpb"><input type="checkbox" name="t" value="{t["slug"]}" data-cat="{t["cat"]}"> Compare</label>' if compare_box else ""
    return (f'<div class="card tc" data-cat="{t["cat"]}" data-price="{E(t["price_band"])}" data-trigger="{E(t["trigger"])}" data-region="{t["region"]}" data-verdict="{E(t["label"])}" data-name="{E(t["name"])}">'
     f'<div class="ch">{logo(t)}<div><h3><a class="stretch" href="/tools/{t["slug"]}/">{E(t["name"])}</a></h3><span class="badge">{E(CATS[t["cat"]][0])}</span></div></div>'
     f'<p class="pills">{pill(t["label"])}{sp}</p><p class="ol">{E(t["one_liner"])}</p>'
     f'<dl class="kf"><dt>Price</dt><dd>{E(t["price_band"])}</dd><dt>How it works</dt><dd>{E(t["mechanism"])}</dd><dt>Trigger</dt><dd>{E(t["trigger"])}</dd><dt>Region</dt><dd>{E(t["region"])}</dd></dl>'
     f'<p class="meta cardlinks"><a class="btn sm" href="/tools/{t["slug"]}/">Read verdict</a> <a href="{OFFICIAL[t["slug"]]}" rel="{rel_for(t)}" target="_blank">Official site ↗</a>{cb}</p></div>')
def cell(v,src):
    s=f' <a class="src" href="{src}" rel="nofollow noopener" target="_blank" aria-label="Source"><sup>src</sup></a>' if src else ""
    cls=' class="y"' if v.startswith("✓") else (' class="n"' if v.startswith("✗") else "")
    v2=E(v).replace("✓",'<span aria-hidden="true">✓</span><span class="sr">Yes:</span>').replace("✗",'<span aria-hidden="true">✗</span><span class="sr">No:</span>')
    return f"<td{cls}>{v2}{s}</td>"
def ftable(tools,cat,logo,caption,extra_rows=None):
    rows=D["rows"][cat]
    head="".join(f'<th scope="col"><span class="th">{logo(t,32)}<a href="/tools/{t["slug"]}/">{E(t["name"].split(" (")[0])}</a></span></th>' for t in tools)
    body="".join(f'<tr><th scope="row">{E(r)}</th>'+"".join(cell(*t["facts"].get(r,["Not stated",None])) for t in tools)+"</tr>" for r in rows)
    if extra_rows: body+="".join(f'<tr><th scope="row">{E(r[0])}</th>'+"".join(f"<td>{E(x)}</td>" for x in r[1:])+"</tr>" for r in extra_rows)
    return f'<div class="ctw" data-ct><table class="ct"><caption>{E(caption)} <span class="cnt" aria-live="polite"></span></caption><thead><tr><th scope="col" class="corner">Feature</th>{head}</tr></thead><tbody>{body}</tbody></table></div>'
CSS=""".tc{display:flex;flex-direction:column}.tc h3{margin:0;font-size:1.05rem}.tc .ch{align-items:flex-start}.pills{margin:.2rem 0}.vl{display:inline-block;border-radius:99px;padding:.05rem .55rem;font-size:.78rem;font-weight:600;margin-right:.3rem}.l-top{background:#0e4c6b;color:#fff}.l-good{background:#e3f2f4;color:#0e4c6b}.l-warn{background:#fdf0d9;color:#7a5200}.l-no{background:#f8e1e1;color:#8a1f1f}.l-sp{background:#fff4c2;color:#5c4a00;border:1px solid #e0c96b}.ol{margin:.3rem 0 .5rem}.kf{display:grid;grid-template-columns:auto 1fr;gap:.15rem .7rem;font-size:.86rem;margin:0 0 .7rem}.kf dt{color:#6b7477}.kf dd{margin:0}.cardlinks{margin-top:auto;display:flex;gap:.8rem;align-items:center;flex-wrap:wrap}.btn.sm{padding:.4rem .8rem;font-size:.88rem;position:relative;z-index:1}.cmpb{margin-left:auto;position:relative;z-index:1;font-size:.86rem}
.ctw{overflow-x:auto;max-height:80vh;border:1px solid #e6e3da;border-radius:10px;background:#fff}.ct{border-collapse:separate;border-spacing:0;width:100%;font-size:.92rem}.ct caption{text-align:left;padding:.6rem .8rem;font-weight:600}.ct th,.ct td{padding:.55rem .7rem;border-top:1px solid #eee;vertical-align:top;text-align:left;min-width:150px}.ct thead th{position:sticky;top:0;background:#fff;z-index:2;border-bottom:2px solid #0a8ea2}.ct tbody th{position:sticky;left:0;background:#f7f8f7;z-index:1;font-weight:600;min-width:140px}.ct thead th.corner{left:0;z-index:3}.ct td.y{background:#f1f8f4}.ct td.n{background:#fbf3f3}.th{display:flex;align-items:center;gap:.4rem}.src{font-size:.7rem;text-decoration:none}.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}tr[hidden]{display:none}.difft{display:inline-flex;gap:.4rem;align-items:center;margin:.4rem 0 .6rem;font-weight:600;font-size:.92rem;cursor:pointer}.difft input{width:1.1rem;height:1.1rem;accent-color:#0e4c6b}@media(max-width:640px){.ct{font-size:.85rem}.ct th,.ct td{min-width:130px;padding:.45rem .5rem}.ct tbody th{min-width:110px;max-width:120px}.ctw{max-height:75vh}.ctw::after{content:"Swipe to see more →";display:block;font-size:.75rem;color:#6b7477;padding:.3rem .6rem}}
"""

CSS+=".fbar{display:flex;flex-wrap:wrap;gap:.6rem 1.2rem;align-items:flex-start;background:#fff;border:1px solid #dfe6e8;border-radius:12px;padding:.8rem 1rem;margin:1rem 0}.fbar fieldset{border:0;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:.3rem .5rem}.fbar legend{font-weight:700;font-size:.8rem;text-transform:uppercase;color:#0e4c6b;margin-bottom:.2rem;width:100%}.fbar label{font-size:.9rem;display:inline-flex;gap:.3rem;align-items:center;background:#eef6f7;border-radius:999px;padding:.2rem .65rem;cursor:pointer}.fbar label:has(input:checked){background:#0e4c6b;color:#fff}.fbar p{margin:0;width:100%;display:flex;gap:1rem;align-items:center}.btn2{background:none;border:1px solid #0e4c6b;color:#0e4c6b;border-radius:8px;padding:.25rem .7rem;cursor:pointer}.catl{font-size:.95rem}[hidden]{display:none!important}"
CSS+=".cnt{font-weight:400;color:#6b7477;margin-left:.4rem}.cnt:not(:empty)::before{content:\"· \"}"
CSS+=".vbox{background:#fff;border:2px solid #0a8ea2;border-radius:14px;padding:1rem 1.2rem;margin:1rem 0}.vbox h3{margin:.2rem 0;font-size:.95rem;color:#0e4c6b}.vg{display:grid;grid-template-columns:1fr 1fr;gap:1rem}@media(max-width:640px){.vg{grid-template-columns:1fr}}"
CSS+=".chooser{background:#fff;border:1px solid #dfe6e8;border-radius:14px;padding:1rem 1.2rem;margin:1.2rem 0}.chooser fieldset{border:0;padding:0;margin:0 0 .7rem;display:flex;flex-wrap:wrap;gap:.4rem}.chooser legend{font-weight:700;margin-bottom:.3rem;width:100%}.chooser label{background:#eef6f7;border-radius:999px;padding:.25rem .75rem;cursor:pointer}.chooser label:has(input:checked){background:#0e4c6b;color:#fff}#chr p:first-child{font-weight:700;font-size:1.1rem;margin:.8rem 0 .2rem}.qp{background:#eef6f7;border-radius:12px;padding:.6rem 1.2rem;margin:1rem 0}.qp h2{margin:.4rem 0;font-size:1.15rem}.toc{font-size:.95rem;margin:.6rem 0}"
CSS+=".tray{position:sticky;bottom:1rem;float:right;z-index:5;box-shadow:0 4px 14px rgba(0,0,0,.2)}.cmpb input:disabled+*,.cmpb:has(input:disabled){opacity:.45}"
