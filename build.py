import os, json, html, shutil
from content import *
SITE = os.environ.get("SITE_URL","https://afterkeep.example").rstrip("/")
UPDATED = "2026-10-15"; OUT="dist"
NEWS_ACTION = os.environ.get("NEWSLETTER_ACTION","")  # e.g. Buttondown/Formspree endpoint
E=html.escape
shutil.rmtree(OUT,ignore_errors=True); os.makedirs(OUT)
pages=[]; search=[]
CSS="""*{box-sizing:border-box}body{margin:0;font:17px/1.65 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:#1f2a2e;background:#f7f6f2}a{color:#2d6a6a}header,footer{background:#fff;border-bottom:1px solid #e6e3da}footer{border-top:1px solid #e6e3da;margin-top:4rem;padding:2rem 0;font-size:.9rem;color:#5b6467}.w{max-width:960px;margin:0 auto;padding:0 1.2rem}nav{display:flex;flex-wrap:wrap;gap:1rem;align-items:center;padding:.9rem 0}nav .logo{font-weight:700;font-size:1.25rem;text-decoration:none;color:#1f2a2e;margin-right:auto}nav a{text-decoration:none}h1{font-size:2.1rem;line-height:1.2;margin:2rem 0 .8rem}h2{margin-top:2.2rem}.lead{font-size:1.15rem;background:#fff;border-left:4px solid #2d6a6a;padding:1rem 1.2rem;border-radius:6px}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:1rem}.card{background:#fff;border:1px solid #e6e3da;border-radius:10px;padding:1.1rem;text-decoration:none;color:inherit;display:block}.card:hover{border-color:#2d6a6a}.card h3{margin:.1rem 0 .4rem;font-size:1.1rem}.meta{color:#6b7477;font-size:.88rem}.pc{display:grid;grid-template-columns:1fr 1fr;gap:1rem}@media(max-width:640px){.pc{grid-template-columns:1fr}h1{font-size:1.7rem}}.box{background:#fff;border:1px solid #e6e3da;border-radius:10px;padding:1rem 1.2rem}input[type=email],input[type=search]{width:100%;padding:.75rem;border:1px solid #cfcabd;border-radius:8px;font-size:1rem}button,.btn{background:#2d6a6a;color:#fff;border:0;padding:.75rem 1.2rem;border-radius:8px;font-size:1rem;cursor:pointer;text-decoration:none;display:inline-block}#results a{display:block;padding:.4rem 0}.badge{display:inline-block;background:#e4efee;color:#2d6a6a;border-radius:99px;padding:.1rem .6rem;font-size:.8rem}ol li,ul li{margin:.3rem 0}"""
def nav():
    return '<header><nav class="w"><a class="logo" href="/">Afterkeep</a><a href="/tools/">Tools</a><a href="/platforms/">Platforms</a><a href="/guides/">Guides</a><a href="/best/">Best of</a><a href="/advertise/">Get featured</a></nav></header>'
def newsletter():
    act = NEWS_ACTION or "#"
    return f'''<section class="box" id="newsletter"><h2 style="margin-top:0">Get the Afterkeep checklist updates</h2><p>One short email when platform policies change. No spam.</p><form action="{act}" method="post" onsubmit="return akSub(event)"><input type="email" name="email" required placeholder="you@example.com" aria-label="Email"> <p><button type="submit">Subscribe</button></p><p id="nl-msg" class="meta"></p></form><script>function akSub(e){{if("{NEWS_ACTION}")return true;e.preventDefault();document.getElementById("nl-msg").textContent="Thanks! Our newsletter is launching soon. Signups aren't being collected yet.";return false}}</script></section>'''
def page(path,title,desc,body,ld=None,kind="WebPage"):
    url=SITE+path
    lds=[{"@context":"https://schema.org","@type":"Article" if kind=="Article" else "WebPage","headline":title,"description":desc,"url":url,"dateModified":UPDATED,"publisher":{"@type":"Organization","name":"Afterkeep"}}]+(ld or [])
    h=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(title)} | Afterkeep</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta property="og:type" content="{'article' if kind=='Article' else 'website'}"><meta property="og:site_name" content="Afterkeep"><meta name="twitter:card" content="summary"><link rel="stylesheet" href="/style.css">{''.join('<script type="application/ld+json">'+json.dumps(x)+'</script>' for x in lds)}</head><body>{nav()}<main class="w">{body}<p class="meta">Last updated: {UPDATED}</p>{newsletter()}</main><footer><div class="w">Afterkeep is an independent guide to digital legacy. This is general information, not legal or financial advice. <a href="/about/">About &amp; disclaimer</a> · <a href="/advertise/">Advertise</a> · <a href="https://billing.stripe.com/p/login/4gM5kE5qIabKa1TgHF5os00" rel="nofollow noopener">Manage sponsorship</a> · <a href="/llms.txt">llms.txt</a></div></footer></body></html>'''
    d=OUT+path; os.makedirs(d,exist_ok=True); open(d+"index.html","w").write(h); pages.append(path)
    search.append({"t":title,"u":path,"d":desc})
def faq_ld(faqs): return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}
def faq_html(faqs): return "<h2>FAQ</h2>"+"".join(f"<h3>{E(q)}</h3><p>{E(a)}</p>" for q,a in faqs)
T={t["slug"]:t for t in TOOLS}
def tcard(t): return f'<a class="card" href="/tools/{t["slug"]}/"><span class="badge">{E(CATS[t["cat"]][0])}</span><h3>{E(t["name"])}</h3><p>{E(t["verdict"])}</p></a>'
def pcard(p): return f'<a class="card" href="/platforms/{p["slug"]}/"><h3>What happens to my {E(p["name"])} when I die?</h3><p class="meta">{E(p["answer"][:120])}…</p></a>'
GUIDES=[]
# ---- enrichment & shared helpers
import enrich
from enrich import CHECKED
for p in PLATFORMS:
    e=enrich.P.get(p["slug"],{}); p.update(e)
    if p["slug"]=="microsoft-outlook":
        p["steps"]=["Store your Microsoft password in a password manager with emergency access, so someone you trust can close the account.","Export important email and OneDrive files periodically.","After a death: if you have the password you can close the account yourself; Microsoft says you don't need to report the death.","Without access: cancel Microsoft subscriptions through the bank, and get legal advice if you need the content (a subpoena or court order is required)."]
PLATFORMS+=enrich.NEWP
TOOLS+=enrich.TOOL_NEW
T={t["slug"]:t for t in TOOLS}
TITLES={}
for t in TOOLS: TITLES[f"/tools/{t['slug']}/"]=f"{t['name']} review"
for p in PLATFORMS: TITLES[f"/platforms/{p['slug']}/"]=f"What happens to my {p['name']} when I die?"
for x in BEST: TITLES[f"/best/{x['slug']}/"]=x["title"]
TITLES["/platforms/"]="All platform guides"
G=[("google-takeout-export","How to export your Google data with Google Takeout","Google Takeout (takeout.google.com) lets you download a copy of your Gmail, Google Photos, Drive and other Google data as .zip or .tgz archives, either once or on a recurring schedule. It's free and works in any browser.",
 ["Go to takeout.google.com and sign in.","Leave everything ticked, or 'Deselect all' and pick products such as Google Photos, Mail and Drive.","Click 'Next step' and choose a destination: download link by email, or add to Drive, Dropbox, OneDrive or Box.","Choose 'Export once' or 'Export every 2 months for 1 year'.","Choose file type (.zip or .tgz) and maximum archive size (larger sizes mean fewer files).","Click 'Create export'. Large libraries can take hours or days; Google emails you when it's ready.","Download the archives before the links expire and store them on an external drive plus a second location.","Record where the backup lives in your digital estate checklist."],
 [("Does Google Takeout include Google Photos?","Yes. Select Google Photos; photos come with JSON metadata files alongside them."),("Is Google Takeout free?","Yes.")],"https://takeout.google.com"),
 ("apple-legacy-contact-setup","How to set up Apple Legacy Contact (step by step)","An Apple Legacy Contact is someone you choose who can get your iCloud data after you die, using an access key and your death certificate. It's free, takes about 3 minutes on iPhone, and you can add more than one person. They don't need an Apple device.",
 ["Make sure your device is up to date and you're signed in with your Apple Account (two-factor authentication on).","Open Settings → [your name] → Sign-In & Security → Legacy Contact.","Tap 'Add Legacy Contact' and pick someone from Contacts.","Choose how to share the access key: send it via Messages (if they use a compatible Apple device) or print a copy.","Store a printed copy of the key with your will or estate documents.","Tell your Legacy Contact what to do: visit digital-legacy.apple.com with the key and a death certificate.","Remember that Keychain passwords aren't included, so also set up emergency access in your password manager."],
 [("How many Legacy Contacts can I have?","Up to 5."),("Do Legacy Contacts need an iPhone?","No. They can use the printed access key at digital-legacy.apple.com.")],"https://support.apple.com/en-us/102631"),
 ("digital-estate-checklist","The complete digital estate checklist","A digital estate plan has four parts: an inventory of your accounts and assets, a secure way for one trusted person to get access (password manager emergency access), the built-in legacy settings on each platform, and written wishes for each account. This checklist covers all four in about an afternoon.",
 ["Inventory: list email, social, cloud storage, banks, super/pension, crypto, subscriptions, domains and devices.","Password manager: move everything into Bitwarden or Keeper and set up an emergency contact.","Google: set up Inactive Account Manager.","Apple: add a Legacy Contact and print the key.","Facebook: choose a legacy contact or deletion.","Microsoft: store your password in your password manager; Microsoft releases content only with a court order.","Crypto: document every exchange and wallet; set up an inheritance method for seed phrases (never put seed phrases in your will).","Photos: run a Google Takeout or iCloud export and keep an offline copy.","Devices: record phone and computer passcodes in your vault, not on paper with your will.","Subscriptions: note recurring payments to cancel.","Wishes: write what should happen to each account (memorialise, delete, download).","Legal: name a digital executor in your will. Laws vary by country and state, so ask a local estate lawyer.","Review every 12 months or after big life changes."],
 [("What is a digital executor?","Someone you nominate to deal with your online accounts. Whether this has legal force depends on where you live."),("Should I put passwords in my will?","No. Wills can become public documents. Use a password manager with emergency access instead.")],None)]

G=[g+([],[],[]) for g in G]+[(s,t,a,st,f,None,src,tl,rel) for (s,t,a,st,f,src,tl,rel) in enrich.GUIDE_NEW]
for g in G: TITLES[f"/guides/{g[0]}/"]=g[1]
FULL=[]
def crumbs(items):
    h='<p class="meta crumbs"><a href="/">Home</a>'+"".join(f' › <a href="{u}">{E(n)}</a>' if u else f' › {E(n)}' for n,u in items)+'</p>'
    allit=[("Home","/")]+items
    ld={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,**({"item":SITE+u} if u else {})} for i,(n,u) in enumerate(allit)]}
    return h,ld
def facts_html(f): return '<div class="box keyfacts"><h2 style="margin-top:0">Key facts</h2><ul>'+"".join(f"<li>{E(x)}</li>" for x in f)+'</ul></div>' if f else ""
def src_html(srcs):
    if not srcs: return ""
    return '<h2>Sources</h2><ul class="meta">'+"".join(f'<li><a href="{u}" rel="noopener" target="_blank">{E(n)}</a>, official source, checked {CHECKED}</li>' for n,u in srcs)+'</ul>'
def rel_html(paths):
    seen=[]; [seen.append(x) for x in paths if x in TITLES and x not in seen]
    return ('<h2>Related guides</h2><ul>'+"".join(f'<li><a href="{x}">{E(TITLES[x])}</a></li>' for x in seen)+'</ul>') if seen else ""
def lst(h2,items): return f"<h2>{E(h2)}</h2><ul>"+"".join(f"<li>{E(x)}</li>" for x in items)+"</ul>" if items else ""
def faq_html(faqs): return "<h2>Frequently asked questions</h2>"+"".join(f"<h3>{E(q)}</h3><p>{E(a)}</p>" for q,a in faqs)
def full(path,title,ans,facts,faqs,extra=""):
    FULL.append(f"## {title}\nURL: {SITE}{path}\n\n{ans}\n\n"+("Key facts:\n"+"".join(f"- {x}\n" for x in facts)+"\n" if facts else "")+extra+"".join(f"Q: {q}\nA: {a}\n\n" for q,a in faqs))
def tcard(t): return f'<a class="card" href="/tools/{t["slug"]}/"><span class="badge">{E(CATS[t["cat"]][0])}</span><h3>{E(t["name"])}</h3><p>{E(t["verdict"])}</p></a>'
def pcard(p): return f'<a class="card" href="/platforms/{p["slug"]}/"><h3>What happens to my {E(p["name"])} when I die?</h3><p class="meta">{E(p["answer"][:120])}…</p></a>'
GUIDES=[]
ARROW="↗"
# tools
for t in TOOLS:
    rel=[x for x in TOOLS if x["cat"]==t["cat"] and x is not t][:3]
    ans=f'{t["verdict"]} Best for: {t["best"]}'
    faqs=[(f"Is {t['name']} good for digital legacy planning?",t["verdict"]),(f"Who is {t['name']} best for?",t["best"]),(f"How much does {t['name']} cost?",t["pricing"]),(f"What are the downsides of {t['name']}?","; ".join(t["cons"])+"."),(f"What are alternatives to {t['name']}?",("Alternatives in the same category include "+", ".join(x["name"] for x in rel)+".") if rel else "See the Afterkeep tool directory.")]
    facts=[f"Category: {CATS[t['cat']][0]}",f"Pricing: {t['pricing']}",f"Best for: {t['best']}"]+t["pros"][:2]
    srcs=t.get("sources") or [(f"{t['name']}: official site / documentation",t["url"])]
    ch,cld=crumbs([("Tools","/tools/"),(CATS[t["cat"]][0],f"/tools/#{t['cat']}"),(t["name"],None)])
    pros="".join(f"<li>{E(x)}</li>" for x in t["pros"]); cons="".join(f"<li>{E(x)}</li>" for x in t["cons"])
    relb="/best/best-password-managers-emergency-access/" if t["cat"]=="vaults" else ("/best/best-crypto-inheritance-tools/" if t["cat"]=="crypto" else "/best/best-digital-legacy-vaults/")
    b=(f'{ch}<h1>{E(t["name"])} review: digital legacy verdict</h1><p class="lead"><strong>Verdict:</strong> {E(ans)}</p>{facts_html(facts)}'
       f'<p><a class="btn" href="{t["url"]}" rel="nofollow noopener" target="_blank">Official site / docs {ARROW}</a></p>'
       f'<h2>What are the pros and cons of {E(t["name"])}?</h2><div class="pc"><div><h3>Pros</h3><ul>{pros}</ul></div><div><h3>Cons</h3><ul>{cons}</ul></div></div>'
       f'{faq_html(faqs)}{src_html(srcs)}<h2>What are similar tools?</h2><div class="grid">{"".join(tcard(x) for x in rel)}</div>{rel_html([relb,"/guides/digital-estate-checklist/"])}')
    sw={"@context":"https://schema.org","@type":"SoftwareApplication","name":t["name"],"url":t["url"],"applicationCategory":"SecurityApplication","review":{"@type":"Review","author":{"@type":"Organization","name":"Afterkeep"},"reviewBody":t["verdict"]}}
    page(f"/tools/{t['slug']}/",f"{t['name']} for digital legacy: verdict, pros & cons",t["verdict"][:155],b,[faq_ld(faqs),sw,cld],"Article")
    full(f"/tools/{t['slug']}/",f"{t['name']} (tool review)",ans,facts+["Pros: "+"; ".join(t["pros"]),"Cons: "+"; ".join(t["cons"])],faqs,"Sources: "+", ".join(u for n,u in srcs)+"\n\n")
# platforms
for p in PLATFORMS:
    q=f"What happens to my {p['name']} when I die?"
    faqs=([(q,p["answer"])]+p["faqs"]+p.get("extra",[]))[:6]
    ch,cld=crumbs([("Platforms","/platforms/"),(p["name"],None)])
    srcs=p.get("sources") or [(f"{p['name']}: official policy",p["url"])]
    steps="".join(f"<li>{E(s)}</li>" for s in p["steps"])
    tl=('<h2>How long does it take?</h2><p>'+E(p["timeline"])+'</p>') if p.get("timeline") else ""
    b=(f'{ch}<h1>{E(q)}</h1><p class="lead"><strong>Short answer:</strong> {E(p["answer"])}</p>{facts_html(p.get("facts",[]))}'
       f'<h2>How do I prepare my {E(p["name"])} account?</h2><ol>{steps}</ol><p><a class="btn" href="{p["url"]}" rel="noopener" target="_blank">Read the official policy {ARROW}</a></p>'
       f'{lst("What documents do heirs need?",p.get("need",[]))}{tl}{lst("What can't be recovered?",p.get("lost",[]))}{faq_html(faqs)}{src_html(srcs)}'
       f'{rel_html(p.get("related",[])+["/guides/digital-estate-checklist/"])}<p class="meta">Policies change. Always confirm with the official page above. General information, not legal advice.</p>')
    page(f"/platforms/{p['slug']}/",q,p["answer"][:155],b,[faq_ld(faqs),cld],"Article")
    ex="".join(f"{h}:\n"+"".join(f"- {x}\n" for x in p.get(k,[]))+"\n" for h,k in [("Documents heirs need","need"),("What can't be recovered","lost")] if p.get(k))+(f"Timeline: {p['timeline']}\n\n" if p.get("timeline") else "")+"Sources: "+", ".join(u for n,u in srcs)+"\n\n"
    full(f"/platforms/{p['slug']}/",q,p["answer"],p.get("facts",[]),faqs,ex)
# best
for bp in BEST:
    items=[T[s] for s in bp["tools"]]
    rows="".join(f'<h3>{i+1}. <a href="/tools/{t["slug"]}/">{E(t["name"])}</a></h3><p><strong>Best for:</strong> {E(t["best"])}</p><p>{E(t["verdict"])}</p><p class="meta">Pricing: {E(t["pricing"])}</p>' for i,t in enumerate(items))
    tbl="<table style='width:100%;border-collapse:collapse;background:#fff'><tr><th align=left>Tool</th><th align=left>Best for</th></tr>"+"".join(f"<tr><td style='border-top:1px solid #eee;padding:.4rem'><a href='/tools/{t['slug']}/'>{E(t['name'])}</a></td><td style='border-top:1px solid #eee;padding:.4rem'>{E(t['best'])}</td></tr>" for t in items)+"</table>"
    il={"@context":"https://schema.org","@type":"ItemList","name":bp["title"],"itemListElement":[{"@type":"ListItem","position":i+1,"name":t["name"],"url":SITE+f"/tools/{t['slug']}/"} for i,t in enumerate(items)]}
    title=f"{bp['title']} (2026)"
    faqs=[(f"What are the {bp['title'].lower()}?",bp["answer"])]+[(f"Is {t['name']} a good choice?",t["verdict"]) for t in items[:4]]
    facts=[f"#{i+1} {t['name']}: {t['best']}" for i,t in enumerate(items)]
    ch,cld=crumbs([("Best of","/best/"),(bp["title"],None)])
    srcs=[(f"{t['name']}: official docs",t["url"]) for t in items]
    page(f"/best/{bp['slug']}/",title,bp["answer"][:155],f'{ch}<h1>{E(title)}</h1><p class="lead">{E(bp["answer"])}</p>{facts_html(facts)}<h2>How do these tools compare?</h2><div style="overflow-x:auto">{tbl}</div><h2>Which should you choose?</h2>{rows}{faq_html(faqs)}{src_html(srcs)}{rel_html(["/guides/digital-estate-checklist/","/guides/australian-digital-estate-guide/","/guides/access-deceased-persons-phone-and-accounts/"])}',[il,faq_ld(faqs),cld],"Article")
    full(f"/best/{bp['slug']}/",title,bp["answer"],facts,faqs)
# guides
GX={"google-takeout-export":[("What formats does Google Takeout use?","You can choose .zip or .tgz archives and a maximum archive size."),("Where should I store a Takeout backup?","On an external drive plus a second location, and note it in your digital estate checklist."),("Why back up if I use Inactive Account Manager?","Google can delete personal accounts that are inactive for 2 years, and family requests without a plan aren't guaranteed. An offline copy removes that risk.")],
 "apple-legacy-contact-setup":[("What data can't a Legacy Contact get?","iCloud Keychain (passwords, passkeys, payment info) and purchased movies, music, books and subscriptions."),("What will my Legacy Contact need?","The access key you generate and your death certificate. Requirements vary by country; Japan, for example, uses a family certificate."),("What devices do I need to set it up?","An Apple device running iOS 15.2, iPadOS 15.2 or macOS Monterey 12.1 or later, with two-factor authentication on.")],
 "digital-estate-checklist":[("Where should I start?","Set up emergency access in a password manager, then turn on Google Inactive Account Manager and Apple Legacy Contact. Those three cover most people's essentials."),("Is there an Australian version?","Yes. See our Australian digital estate guide on wills, executors, probate and the ATO checklist."),("How often should I update my plan?","Afterkeep suggests reviewing it at least yearly and whenever you open an important account or change devices.")]}
for slug,title,ans,steps,faqs,src,srcs,tl,rel in G:
    faqs=[(q,"You can add more than one. Apple's page doesn't state a fixed limit." if q=="How many Legacy Contacts can I have?" else a) for q,a in faqs]+GX.get(slug,[])
    faqs=faqs[:6]
    srcs=srcs or enrich.GUIDE_SRC.get(slug,[]); rel=rel or enrich.GUIDE_REL.get(slug,[])
    facts=tl or [f"{len(steps)} steps","Free to do","Based on official platform and government pages"]
    ch,cld=crumbs([("Guides","/guides/"),(title,None)])
    stp="".join(f"<li>{E(s)}</li>" for s in steps)
    b=f'{ch}<h1>{E(title)}</h1><p class="lead">{E(ans)}</p>{facts_html(facts)}<h2>What are the steps?</h2><ol>{stp}</ol>'+(f'<p><a class="btn" href="{src}" target="_blank" rel="noopener">Official source {ARROW}</a></p>' if src else "")+faq_html(faqs)+src_html(srcs)+rel_html(rel+["/platforms/","/best/best-password-managers-emergency-access/"])+'<p class="meta">General information, not legal advice. Laws vary by country and Australian state.</p>'
    howto={"@context":"https://schema.org","@type":"HowTo","name":title,"step":[{"@type":"HowToStep","text":s} for s in steps]}
    page(f"/guides/{slug}/",title,ans[:155],b,[faq_ld(faqs),howto,cld],"Article"); GUIDES.append((slug,title,ans))
    full(f"/guides/{slug}/",title,ans,facts,faqs,"Steps:\n"+"".join(f"{i+1}. {x}\n" for i,x in enumerate(steps))+"\n")
# index pages
page("/tools/","Digital legacy tool directory","Directory of digital legacy tools: password managers with emergency access, vaults, crypto inheritance and estate planning, with clear verdicts.",
 "<h1>Digital legacy tool directory</h1><p class='lead'>Every tool here helps someone you trust reach your accounts, files or crypto if you die or can't manage them yourself. Each one comes with a one-line verdict.</p>"+"".join(f"<h2 id='{k}'>{E(v[0])}</h2><p>{E(v[1])}</p><div class='grid'>{''.join(tcard(t) for t in TOOLS if t['cat']==k)}{''.join(pcard(p) for p in PLATFORMS if p['cat']==k and k in('photos','memorial'))}</div>" for k,v in CATS.items()),
 [{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"name":t["name"],"url":SITE+f"/tools/{t['slug']}/"} for i,t in enumerate(TOOLS)]}])
page("/platforms/","What happens to your accounts when you die: platform guides","Plain-English answers on what Google, YouTube, Apple, Facebook, Instagram, WhatsApp, X, Microsoft, LinkedIn, Amazon, PayPal, Steam, Coinbase and Dropbox do when a user dies.",
 "<h1>What happens to your accounts when you die?</h1><p class='lead'>Most platforms won't give family your password. Some offer legacy settings you have to switch on in advance (Google, Apple, Facebook); others only memorialise or close accounts.</p><div class='grid'>"+"".join(pcard(p) for p in PLATFORMS)+"</div>")
page("/guides/","Digital legacy how-to guides","Step-by-step guides: Google Takeout, Apple Legacy Contact, the digital estate checklist, Australian estates and accessing a deceased person's accounts.",
 "<h1>How-to guides</h1><div class='grid'>"+"".join(f"<a class='card' href='/guides/{s}/'><h3>{E(t)}</h3><p class='meta'>{E(a[:130])}…</p></a>" for s,t,a in GUIDES)+"</div>")
page("/best/","Best digital legacy tools: comparisons","Comparisons and best-for lists for digital legacy vaults, crypto inheritance and password managers with emergency access.",
 "<h1>Best-of comparisons</h1><div class='grid'>"+"".join(f"<a class='card' href='/best/{b['slug']}/'><h3>{E(b['title'])}</h3><p class='meta'>{E(b['answer'][:130])}…</p></a>" for b in BEST)+"</div>")
page("/about/","About Afterkeep & disclaimer","Afterkeep is an independent guide to managing digital life after death or incapacity. Information only, not legal or financial advice.",
 "<h1>About Afterkeep</h1><p class='lead'>Afterkeep is an independent, global guide to digital legacy: what happens to your accounts, photos, passwords and crypto when you die or can't manage them, and the tools that help.</p><p>We research using official platform policies and vendor documentation, and we link to the source on every page. When we're not sure about pricing, we say 'check current pricing' rather than guess.</p><h2>Disclaimer</h2><p><strong>Afterkeep provides general information only and is not legal, financial or tax advice.</strong> Inheritance and digital-asset laws differ by country and state (including across Australian states). Speak to a qualified estate lawyer before making decisions. Policies and prices change; always confirm with the provider.</p><h2>Independence</h2><p>Featured or sponsored listings are always labelled and never change our verdicts.</p>")
TIERS=[("Afterkeep Featured Listing",49,"https://buy.stripe.com/4gM5kE5qIabKa1TgHF5os00",["'Featured' badge on your listing","Top placement in one category"]),
("Afterkeep Category Sponsor",149,"https://buy.stripe.com/bJe6oI5qI4RqgqhgHF5os01",["Exclusive 'Sponsored' banner on one category and its best-for page","Includes a Featured Listing"]),
("Afterkeep Premium Partner",299,"https://buy.stripe.com/7sYcN63iAcjS2zr1ML5os02",["Sitewide sponsor slot","Newsletter mention","Homepage feature","Includes Category Sponsor and Featured Listing"])]
ADV_FAQ=[("How do sponsored listings work?","Pick a tier and pay monthly through Stripe. At checkout you give your tool or company name and website. We review fit, then publish the placement, clearly labelled, usually within a few business days."),
("Does sponsorship change your verdicts or rankings?","No. Verdicts, pros and cons, and the order of our best-for rankings are editorial and never for sale. Paid placement appears only in labelled Featured or Sponsored slots."),
("Can I cancel anytime?","Yes. Plans are monthly with no lock-in. Cancel yourself anytime in the customer portal (https://billing.stripe.com/p/login/4gM5kE5qIabKa1TgHF5os00): log in with your billing email. Your plan and placement stay active until the end of the paid month, with no partial refunds."),("How do I manage my sponsorship?","Use the customer portal (https://billing.stripe.com/p/login/4gM5kE5qIabKa1TgHF5os00). Log in with the email you used at checkout to cancel, update your payment method, edit billing details or download invoices."),
("Can you reject a sponsor?","Yes. We only accept products relevant to digital legacy, estate planning or memorials. If we can't accept a sponsor, we refund the payment."),
("What currency are prices in?","Australian dollars (AUD), billed monthly.")]
tiers_html="<div class='grid'>"+"".join(f"<div class='card'><h3>{E(n.replace('Afterkeep ',''))}</h3><p><strong>A${p}/month</strong></p><ul>{''.join('<li>'+E(x)+'</li>' for x in f)}</ul><p><a class='btn' href='{u}' rel='nofollow noopener'>Buy {E(n.replace('Afterkeep ',''))}</a></p></div>" for n,p,u,f in TIERS)+"</div>"
rules="<h2>How are sponsored and featured listings labelled?</h2><ul><li><strong>Featured</strong>: a paid listing in a category. It always shows a visible 'Featured' badge.</li><li><strong>Sponsored</strong>: a paid banner or slot. It always shows a visible 'Sponsored' label.</li><li>Paid placements never appear inside our editorial rankings or verdicts, and we never write paid reviews.</li><li>Affiliate links, if we ever use them, will be disclosed on the page where they appear.</li></ul><h2>Disclosure</h2><p class='box'>Afterkeep earns money from labelled sponsorships. We follow the US FTC's Endorsement Guides and the Australian Consumer Law, enforced by the ACCC, which require paid relationships to be clearly and prominently disclosed and prohibit misleading or deceptive conduct. Sponsorship never affects our editorial content.</p>"
ch,cld=crumbs([("Advertise",None)])
page("/advertise/","Advertise on Afterkeep / get featured","Sponsor Afterkeep: Featured Listing A$49/mo, Category Sponsor A$149/mo, Premium Partner A$299/mo. Clearly labelled, never changes verdicts. Cancel anytime.",
 f"{ch}<h1>Advertise / get featured</h1><p class='lead'>Afterkeep reaches people who are actively planning their digital legacy or handling a loved one's accounts. Choose a monthly plan below: A$49 Featured Listing, A$149 Category Sponsor or A$299 Premium Partner. Every placement is clearly labelled, never changes our verdicts, and you can cancel anytime.</p><div class='box keyfacts'><h2 style='margin-top:0'>Key facts</h2><ul><li>3 monthly plans, priced in AUD</li><li>Secure checkout by Stripe</li><li>Paid placements are always labelled Featured or Sponsored</li><li>Cancel anytime</li></ul></div><h2>What are the sponsorship plans?</h2>{tiers_html}<p><a class='btn' href='https://billing.stripe.com/p/login/4gM5kE5qIabKa1TgHF5os00' rel='nofollow noopener'>Manage or cancel your sponsorship</a></p><p class='meta'>Already a sponsor? Log in to the Stripe customer portal with the email you used at checkout to cancel, update your card or download invoices.</p>{rules}{faq_html(ADV_FAQ)}<p><a class='btn' href='https://billing.stripe.com/p/login/4gM5kE5qIabKa1TgHF5os00' rel='nofollow noopener'>Manage or cancel your sponsorship</a></p><p class='meta'>Already a sponsor? Log in to the Stripe customer portal with the email you used at checkout to cancel, update your card or download invoices.</p><p>Questions? Email <a href='mailto:Afterkeep800@gmail.com'>Afterkeep800@gmail.com</a>.</p>",
 [faq_ld(ADV_FAQ),cld,{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"item":{"@type":"Product","name":n,"offers":{"@type":"Offer","price":str(p),"priceCurrency":"AUD","url":u}}} for i,(n,p,u,f) in enumerate(TIERS)]}])
ch2,cld2=crumbs([("Advertise","/advertise/"),("Thanks",None)])
page("/advertise/thanks/","Thanks for sponsoring Afterkeep","Your Afterkeep sponsorship payment was received. Here's what happens next.",
 f"{ch2}<h1>Thank you for sponsoring Afterkeep</h1><p class='lead'>Your payment went through and Stripe will email your receipt. We'll review your tool or company for fit and publish your clearly labelled placement, usually within a few business days.</p><h2>What happens next?</h2><ol><li>We check the tool or company name and website you entered at checkout.</li><li>We may email you for a logo or a short description.</li><li>Your placement goes live with a Featured or Sponsored label.</li></ol><p>Your plan renews monthly and you can cancel anytime.</p><p><a class='btn' href='https://billing.stripe.com/p/login/4gM5kE5qIabKa1TgHF5os00' rel='nofollow noopener'>Manage or cancel your sponsorship</a></p><p class='meta'>Already a sponsor? Log in to the Stripe customer portal with the email you used at checkout to cancel, update your card or download invoices.</p><p> Sponsorship never changes our editorial verdicts.</p><p><a href='/'>Back to Afterkeep</a></p>",[cld2])
# home
SEARCHJS='<script>let I;fetch(\'/search.json\').then(r=>r.json()).then(j=>I=j);document.getElementById(\'q\').addEventListener(\'input\',e=>{const v=e.target.value.toLowerCase().trim(),R=document.getElementById(\'results\');if(!v||!I){R.innerHTML=\'\';return}R.innerHTML=I.filter(x=>(x.t+\' \'+x.d).toLowerCase().includes(v)).slice(0,8).map(x=>`<a href="${x.u}">${x.t}</a>`).join(\'\')||\'<p class=meta>No matches</p>\'})</script>'
bestlinks=''.join('<a class=card href=/best/%s/><h3>%s</h3></a>'%(b['slug'],E(b['title'])) for b in BEST)
cats="".join(f"<a class='card' href='/tools/#{k}'><h3>{E(v[0])}</h3><p class='meta'>{E(v[1])}</p></a>" for k,v in CATS.items())
check=["Move passwords into a manager with emergency access (<a href='/tools/bitwarden/'>Bitwarden</a>)","Turn on <a href='/tools/google-inactive-account-manager/'>Google Inactive Account Manager</a>","Add an <a href='/guides/apple-legacy-contact-setup/'>Apple Legacy Contact</a>","Choose a Facebook legacy contact","Back up photos with <a href='/guides/google-takeout-export/'>Google Takeout</a>","Plan <a href='/best/best-crypto-inheritance-tools/'>crypto inheritance</a>","Finish the <a href='/guides/digital-estate-checklist/'>full digital estate checklist</a>"]
faqs=[("What happens to my online accounts when I die?","Most platforms won't share your password. Some (Google, Apple, Facebook) let you name contacts in advance; others only memorialise or delete accounts on request. Setting things up ahead of time is what makes the difference."),("What is the best digital legacy tool?","For most people: a password manager with emergency access (such as Bitwarden) plus free Google and Apple legacy settings.")]
page("/","Afterkeep: what happens to your digital life when you die","Afterkeep explains what happens to your Google, Apple, Facebook, crypto and other accounts when you die, and ranks the tools that help your family get access.",
 f"<h1>Your digital life, handed on properly.</h1><p class='lead'>Afterkeep is a free guide to what happens to your accounts, photos, passwords and crypto when you die or can't manage them, and to the tools that make sure the right person can get to them. Start with the checklist below.</p><input type='search' id='q' placeholder='Search e.g. Instagram, crypto, Bitwarden…' aria-label='Search'><div id='results'></div><h2>Start here: 7-step checklist</h2><ol class='box'>{''.join('<li>'+c+'</li>' for c in check)}</ol><h2>Browse by category</h2><div class='grid'>{cats}</div><h2>Popular questions</h2><div class='grid'>{''.join(pcard(p) for p in PLATFORMS[:6])}</div><p><a href='/platforms/'>All platform guides →</a></p><h2>Best-of comparisons</h2><div class='grid'>{bestlinks}</div>{faq_html(faqs)}{SEARCHJS}",
 [faq_ld(faqs),{"@context":"https://schema.org","@type":"WebSite","name":"Afterkeep","url":SITE+"/"}])
open(OUT+"/style.css","w").write(CSS)
json.dump(search,open(OUT+"/search.json","w"))
open(OUT+"/sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{SITE}{p}</loc><lastmod>{UPDATED}</lastmod></url>" for p in pages)+"</urlset>")
bots=["GPTBot","ChatGPT-User","OAI-SearchBot","ClaudeBot","Claude-Web","anthropic-ai","PerplexityBot","Google-Extended","Applebot-Extended","CCBot","Bingbot","Googlebot"]
open(OUT+"/robots.txt","w").write("".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots)+f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
llms="# Afterkeep\n\n> Independent guide to digital legacy: what happens to online accounts, photos, passwords and crypto when someone dies, plus verdicts on legacy tools. General information, not legal advice.\n\n"
llms+="## Platforms\n"+"".join(f"- [What happens to my {p['name']} when I die?]({SITE}/platforms/{p['slug']}/): {p['answer'][:140]}\n" for p in PLATFORMS)
llms+="\n## Tools\n"+"".join(f"- [{t['name']}]({SITE}/tools/{t['slug']}/): {t['verdict']}\n" for t in TOOLS)
llms+="\n## Best-of\n"+"".join(f"- [{b['title']}]({SITE}/best/{b['slug']}/)\n" for b in BEST)+"\n## Guides\n"+"".join(f"- [{t}]({SITE}/guides/{s}/)\n" for s,t,a in GUIDES)
llms+="\n## Full text\n- [llms-full.txt]("+SITE+"/llms-full.txt): every answer, key fact and FAQ in plain text\n"
open(OUT+"/llms.txt","w").write(llms)
open(OUT+"/llms-full.txt","w").write("# Afterkeep: full content\n\n> General information, not legal advice. Facts checked against official sources on "+CHECKED+".\n\n"+"\n".join(FULL))
open(OUT+"/404.html","w").write(open(OUT+"/index.html").read())
print(len(pages),"pages")
