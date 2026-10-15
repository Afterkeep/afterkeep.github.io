from PIL import Image, ImageDraw, ImageFont
import os
SECTIONS={"home":("Afterkeep","What happens to your digital life when you die"),"tools":("Tool directory","Digital legacy tools with clear verdicts"),"platforms":("Platform guides","What happens to your accounts when you die"),"guides":("How-to guides","Practical steps for your digital estate"),"best":("Best-of lists","The best digital legacy tools, compared"),"compare":("Comparisons","Side-by-side digital legacy tool comparisons"),"advertise":("Advertise","Sponsor Afterkeep: clearly labelled placements")}
B="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; R="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
def make(out):
    os.makedirs(out,exist_ok=True)
    for k,(t,s) in SECTIONS.items():
        im=Image.new("RGB",(1200,630),"#f7f6f2"); d=ImageDraw.Draw(im)
        d.rectangle([0,0,1200,18],fill="#2d6a6a"); d.rectangle([0,612,1200,630],fill="#2d6a6a")
        d.rounded_rectangle([80,90,150,160],14,fill="#2d6a6a"); d.text((100,96),"A",font=ImageFont.truetype(B,52),fill="white")
        d.text((170,100),"Afterkeep",font=ImageFont.truetype(B,46),fill="#1f2a2e")
        d.text((80,250),t,font=ImageFont.truetype(B,76),fill="#1f2a2e")
        f=ImageFont.truetype(R,40); words=s.split(); line=""; y=370
        for w in words:
            if d.textlength(line+" "+w,font=f)>1040: d.text((80,y),line.strip(),font=f,fill="#5b6467"); y+=54; line=""
            line+=" "+w
        d.text((80,y),line.strip(),font=f,fill="#5b6467")
        d.text((80,530),"afterkeep.github.io · independent digital legacy guide",font=ImageFont.truetype(R,28),fill="#2d6a6a")
        im.save(f"{out}/og-{k}.png",optimize=True)
