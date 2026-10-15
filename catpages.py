import html
E=html.escape
def label_rank(l): return {"Top pick":0,"Good":1,"Use with caution":2,"Not recommended":3}.get(l,4)
def names(ts): return ", ".join(t["name"] for t in ts)
def mini(ts,CATS):
    r="".join(f'<tr><th scope="row"><a href="/tools/{t["slug"]}/">{E(t["name"])}</a></th><td>{E(CATS[t["cat"]][0])}</td><td>{E(t["price_band"])}</td><td>{E(t["trigger"])}</td><td>{E(t["region"])}</td><td>{E(t["label"])}</td></tr>' for t in ts)
    return f'<div class="ctw"><table class="ct"><caption>At a glance</caption><thead><tr><th scope="col" class="corner">Tool</th><th scope="col">Category</th><th scope="col">Price</th><th scope="col">Trigger</th><th scope="col">Region</th><th scope="col">Our verdict</th></tr></thead><tbody>{r}</tbody></table></div>'
def build(TOOLS,PLATFORMS,CATS,CD,logo,tcard,pcard):
    out=[]
    def srt(ts): return sorted(ts,key=lambda t:(label_rank(t["label"]),t["name"]))
    for slug,cat in [("vaults","vaults"),("crypto","crypto"),("estate","estate"),("platform-settings","platforms")]:
        ts=srt([t for t in TOOLS if t["cat"]==cat]); top=[t for t in ts if t["label"]=="Top pick"]
        title=CATS[cat][0]
        intro=f"{CATS[cat][1]} We list {len(ts)} tools in this category. "+(f"Our top pick{'s are' if len(top)>1 else ' is'} {names(top)}. " if top else "")+"Each fact in the table links to the official source we checked."
        faqs=[(f"Which {title.lower()} tool is best?", (f"Our top pick{'s are' if len(top)>1 else ' is'} {names(top)}. " if top else f"It depends on your needs; {names(ts[:2])} rate highest in our review. ")+"See each tool's verdict for who it suits and who should skip it."),
              (f"Are there free {title.lower()} options?", ("Yes: "+names([t for t in ts if 'Free' in t['price_band']])+" have a free option. " if any('Free' in t['price_band'] for t in ts) else "None of the tools in this category is free; all need a paid plan. ")+"Check the official pricing page before you buy."),
              ("Which of these work outside the US?", (names([t for t in ts if t['region']=='Global'])+" are available globally. " if any(t['region']=='Global' for t in ts) else "")+(names([t for t in ts if t['region']=='US'])+" are US-focused." if any(t['region']=='US' for t in ts) else "")),
              ("Does Afterkeep store my information?","No. Afterkeep is a comparison and guide directory only. We don't store passwords, documents or personal data.")]
        out.append((f"/tools/{slug}/",title,intro,CD.ftable(ts,cat,logo,f"{title}: compared"),"".join(tcard(t) for t in ts),faqs,ts))
    mem=[p for p in PLATFORMS if p["cat"]=="memorial"]
    mt='<div class="ctw"><table class="ct"><caption>Memorial and legacy options by platform</caption><thead><tr><th scope="col" class="corner">Platform</th><th scope="col">What happens</th></tr></thead><tbody>'+"".join(f'<tr><th scope="row"><a href="/platforms/{p["slug"]}/">{E(p["name"])}</a></th><td>{E(p["answer"])}</td></tr>' for p in mem)+"</tbody></table></div>"
    out.append(("/tools/memorial/",CATS["memorial"][0],CATS["memorial"][1]+f" This page covers {names(mem)}: what each platform does when someone dies and how family can memorialise or remove an account.",mt,"".join(pcard(p) for p in mem),
      [("Can I memorialise a loved one's social media account?","Facebook and Instagram offer memorialisation. Other platforms mainly offer account removal. See each platform guide for the official steps."),
       ("What do I need to memorialise or close an account?","Usually proof of death, such as a death certificate or obituary, and a link to the profile. Each platform's guide lists exactly what it asks for."),
       ("Does Afterkeep store my information?","No. Afterkeep is a comparison and guide directory only.")],[]))
    fr=srt([t for t in TOOLS if "Free" in t["price_band"]])
    out.append(("/tools/free/","Free digital legacy tools",f"These {len(fr)} tools have a free option for passing on access: {names(fr)}. Free plans often have limits, so check what the paid tier adds.",mini(fr,CATS),"".join(tcard(t) for t in fr),
      [("What is the best free digital legacy tool?",f"Start with the free built-in settings: {names([t for t in fr if t['cat']=='platforms'])}. For passwords, {names([t for t in fr if t['cat']=='vaults'][:1])} has a free plan; check whether emergency access needs a paid plan."),
       ("Are free plans enough?","For platform settings, yes. For password managers and vaults, emergency access may need a paid plan. Each tool page shows the plan required."),
       ("Does Afterkeep store my information?","No. Afterkeep is a comparison and guide directory only.")],fr))
    return out
