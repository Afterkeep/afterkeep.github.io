from PIL import Image, ImageDraw, ImageFont
import os, textwrap
B="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; R="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SECTIONS={"home":("Your digital life, handed on properly","Guides, verdicts and comparisons for your digital legacy"),"tools":("Tool directory","Digital legacy tools with clear verdicts"),"platforms":("Platform guides","What happens to your accounts when you die"),"guides":("How-to guides","Practical steps for your digital estate"),"best":("Best-of lists","The best digital legacy tools, compared"),"compare":("Comparisons","Side-by-side tool comparisons"),"advertise":("Advertise","Clearly labelled sponsorship")}
TEAL=(10,142,162); NAVY=(14,76,107); INK=(14,76,107); MUTED=(91,100,103); BG=(247,246,242)
def motif(d,kind):
    cx,cy=1000,330
    for r,a in [(250,(227,242,244)),(185,(209,234,238)),(120,(188,224,230))]: d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=a)
    s=TEAL
    if kind in("platforms",):
        d.rounded_rectangle([905,290,1095,370],40,fill=s); d.ellipse([930,245,1030,345],fill=s); d.ellipse([990,265,1070,345],fill=s)
    elif kind in("guides",):
        d.rounded_rectangle([920,250,1080,410],10,fill=s); d.rectangle([990,250,1010,410],fill=(188,224,230))
    elif kind in("best",):
        d.ellipse([930,240,1070,380],fill=s); d.polygon([(955,360),(940,440),(1000,410),(1060,440),(1045,360)],fill=s); d.ellipse([965,275,1035,345],fill=(227,242,244))
    elif kind in("compare",):
        d.rounded_rectangle([915,240,985,420],12,fill=s); d.rounded_rectangle([1015,240,1085,420],12,fill=(14,76,107))
    elif kind in("tools",):
        for x in (920,1010):
            for y in (250,340): d.rounded_rectangle([x,y,x+70,y+70],12,fill=s)
    elif kind=="advertise":
        d.polygon([(925,300),(985,300),(1060,250),(1060,410),(985,360),(925,360)],fill=s)
    else:  # shield + check
        d.polygon([(1000,225),(1085,258),(1085,330),(1000,430),(915,330),(915,258)],fill=s)
        d.line([(960,325),(990,355),(1045,295)],fill=(255,255,255),width=16,joint="curve")
def render(out,kicker,title,sub,kind):
    im=Image.new("RGB",(1200,630),(247,248,247)); d=ImageDraw.Draw(im)
    motif(d,kind)
    lg=Image.open("assets/brand/afterkeep-logo-full.png"); lg=lg.resize((round(lg.width*70/lg.height),70),Image.LANCZOS); im.paste(lg,(70,62),lg)
    d.text((72,180),kicker.upper(),font=ImageFont.truetype(B,24),fill=TEAL)
    size=64 if len(title)<28 else (52 if len(title)<50 else 44)
    f=ImageFont.truetype(B,size); y=222
    for line in textwrap.wrap(title,width=int(1500/size)):
        d.text((72,y),line,font=f,fill=INK); y+=int(size*1.22)
    fs=ImageFont.truetype(R,30)
    sub=sub.split(". ")[0].rstrip(".")+"."; ls=textwrap.wrap(sub,width=42)
    if len(ls)>2: ls=ls[:2]; ls[1]=ls[1].rstrip(" ,;:")+"…"
    for line in ls:
        d.text((72,y+16),line,font=fs,fill=MUTED); y+=42
    d.rectangle([0,600,1200,630],fill=NAVY)
    d.text((72,548),"afterkeep.github.io  ·  independent digital legacy guide",font=ImageFont.truetype(R,24),fill=TEAL)
    im.save(out,optimize=True)
def make(outdir):
    os.makedirs(outdir,exist_ok=True)
    for k,(t,s) in SECTIONS.items(): render(f"{outdir}/og-{k}.png","Afterkeep guide" if k=="home" else "Section",t,s,k)
