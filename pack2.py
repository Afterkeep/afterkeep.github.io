# Content pack 2 (19 Oct 2026, AEST). Every fact here was checked against the cited official page on 19 Oct 2026.
# Services Australia blocks automated fetches, so its two pages were read via Wayback snapshots of the official URLs
# (who-to-tell page: snapshot 2 Oct 2026, page last updated 2 Sep 2026; SA116 page: snapshot 18 Jun 2026).
import html
E=html.escape
DATE="2026-10-19"; CHK="19 Oct 2026"
SNAP_D=("Snapchat Support: I'd like to report an account of a person who passed away","https://help.snapchat.com/hc/en-us/articles/27504454933908-I-d-like-to-report-an-account-of-a-person-who-passed-away")
SNAP_DEL=("Snapchat Support: How do I deactivate or delete my Snapchat account?","https://help.snapchat.com/hc/en-us/articles/7012328360596-How-do-I-deactivate-or-delete-my-Snapchat-account")
SNAP_DL=("Snapchat Support: How do I download my data from Snapchat?","https://help.snapchat.com/hc/en-us/articles/7012305371156-How-do-I-download-my-data-from-Snapchat")
SA_TELL=("Services Australia: Who to tell when someone dies","https://www.servicesaustralia.gov.au/who-to-tell-when-someone-dies")
SA116=("Services Australia: Advice of death form (SA116)","https://www.servicesaustralia.gov.au/sa116")
MG_CHK=("myGov: Death of someone close to you checklist","https://my.gov.au/en/services/health-and-disability/when-someone-close-to-you-dies/death-of-someone-close-to-you-checklist")
MG_TOU=("myGov: Terms of use (closure of inactive accounts)","https://my.gov.au/en/about/terms")
ATO_N=("ATO: Notifying us of a death and who will manage the estate","https://www.ato.gov.au/individuals-and-families/deceased-estates/notifying-us-of-a-death-and-who-will-manage-the-estate")
ATO_S=("ATO: Superannuation death benefits","https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/withdrawing-and-using-your-super/superannuation-death-benefits")
MS_S=("Moneysmart (ASIC): Who gets your super if you die","https://moneysmart.gov.au/how-super-works/who-gets-your-super-if-you-die")
ADNS=("Australian Death Notification Service","https://deathnotification.gov.au/")
TEL=("Telstra: Bereavement support","https://www.telstra.com.au/aboutus/support-in-times-of-need/bereavement-support")
OPT=("Optus: Transfer or close an Optus account due to the loss of a loved one (form, PDF)","https://www.optus.com.au/content/dam/optus/documents/for-you/support/Bereavement.Form.pdf")
VOD=("Vodafone Australia: Managing an account following a bereavement","https://www.vodafone.com.au/support/notify/bereavement")
CHECKED_AT={u:CHK for _,u in [SNAP_D,SNAP_DEL,SNAP_DL,SA_TELL,SA116,MG_CHK,MG_TOU,ATO_N,ATO_S,MS_S,TEL,OPT,VOD]}

SNAP=dict(slug="snapchat",name="Snapchat",cat="memorial",url=SNAP_D[1],
 answer="Snapchat won't give anyone access to a deceased person's account, and its help page for people who have died describes no memorialisation option. Snapchat says it only accepts requests from a verified email address linked to the account. Deleting it needs a login at accounts.snapchat.com: the account is deactivated for 30 days, then permanently deleted after 30 more.",
 steps=["Save the Memories you want kept: log in at accounts.snapchat.com, open My Data, turn on 'Export your Memories', choose a date range and submit. Download the ZIP when Snapchat emails you.",
  "Keep the email address linked to your Snapchat account in a password manager with emergency access. Snapchat only accepts requests from that verified email.",
  "Write your username and your wishes (keep or delete) in your digital estate plan.",
  "After a death: Snapchat's documented route is Delete My Account at accounts.snapchat.com, which needs the login. Check with the executor before using someone else's login; otherwise contact Snapchat Support through its help site."],
 facts=["No account access for anyone, including family","No memorialisation option described by Snapchat","Requests accepted only from the account's verified email","Deletion: 30 days deactivated, then permanently deleted after 30 more days"],
 need=["Access to the account's login, or to the verified email address linked to the account","Snapchat publishes no document list for deceased users. Have the death certificate and your ID ready in case Support asks"],
 timeline="Data exports: Snapchat aims to deliver within 7 days; large downloads take longer. Deletion: the account is deactivated for 30 days (it can be reactivated in that time) and permanently deleted after 30 more days. Data that isn't downloaded in the first 30 days is permanently deleted after 60 days.",
 lost=["Anything inside the account that wasn't exported, because Snapchat doesn't grant account access","All account data after permanent deletion, apart from what Snapchat keeps for legal, security and business needs (such as purchase records)"],
 faqs=[("Can family get into a dead person's Snapchat?","No. Snapchat says its privacy policies don't allow it to grant access to the account."),
  ("Does Snapchat memorialise accounts?","Snapchat's help page for a person who passed away doesn't describe a memorialisation option. It covers requesting data by authenticated people and deleting the account."),
  ("How do I save Snapchat Memories?","Log in at accounts.snapchat.com, open My Data, turn on 'Export your Memories', pick a date range and submit. Snapchat emails a link; unzip the file and open index.html to download your Memories."),
  ("How long until a deleted Snapchat account is gone?","It's deactivated for 30 days, when it can still be reactivated, then permanently deleted after 30 more days. Snapchat says the second period is 180 days in India.")],
 extra=[("Who can ask Snapchat to act on an account?","Snapchat says it only accepts requests from a verified email address associated with the account, so access to that email matters.")],
 sources=[SNAP_D,SNAP_DEL,SNAP_DL],related=["/platforms/instagram/","/platforms/whatsapp/","/guides/access-deceased-persons-phone-and-accounts/"])

MYGOV=("mygov-centrelink-medicare-ato-after-death","myGov, Centrelink, Medicare and the ATO after a death (Australia)",
 "Tell Services Australia within 28 days by phone, with the Advice of death form (SA116) or at a service centre; it uses the form to update Medicare, Centrelink and Child Support records. You don't need to close the person's myGov account, because myGov closes unused accounts. Notify the ATO separately with a death certificate or grant of probate.",
 ["Get the death certificate from your state or territory's Births, Deaths and Marriages registry. A funeral director may register the death for you.",
  "Within 28 days, tell Services Australia: call, send the Advice of death form (SA116a for an adult, SA116b for a child), or visit a service centre. Services Australia uses the form to update Medicare, Centrelink and Child Support records.",
  "Don't sign in to their myGov. The myGov terms of use say you're not allowed to access another person's myGov account, and myGov says you don't need to close it.",
  "If you don't have documents yet, phone the ATO to say the person has died. It will pause their tax correspondence.",
  "Officially notify the ATO with its Notification of a deceased person form: online, followed by an interview at a participating Australia Post outlet, or on paper with certified copies.",
  "Executors who plan to apply for probate or letters of administration: the ATO suggests waiting for the grant before notifying it, to avoid delays. With a grant, it records you as the authorised legal personal representative (LPR).",
  "To get the person's details from Services Australia for the estate, each executor or administrator completes an Executor/Administrator Request for information form and gives proof of authority.",
  "Check whether you can get a bereavement payment or other support from Services Australia.",
  "Use the free Australian Death Notification Service to tell participating organisations at once (Telstra and Vodafone, for example, accept it)."],
 [("Do I need to close a deceased person's myGov account?","No. myGov says you don't need to close it because it closes automatically after not being used. Its terms say accounts may be closed after 24 months without a sign-in, or 6 months if no services are linked."),
  ("How long do I have to tell Services Australia about a death?","Services Australia asks to be told within 28 days. You can call, send the Advice of death form (SA116) or visit a service centre."),
  ("Can I log in to my late parent's myGov?","No. The myGov terms of use say you're not allowed to access another person's myGov account. Use the official notification forms instead."),
  ("What do I need to notify the ATO of a death?","One of: a death certificate, a grant of probate or letters of administration, or a certified copy of the will (only if you're not applying for a grant). The ATO says it takes up to 28 days to update the person's records."),
  ("Who can get the deceased's tax and super information from the ATO?","The authorised legal personal representative. Without a grant of probate or letters of administration, the ATO can't record you as the authorised LPR, which limits what it can release."),
  ("Do I tell the ATO and Services Australia separately?","Yes. myGov's checklist lists them as separate agencies to tell. The free Australian Death Notification Service can tell participating private organisations at once.")],
 [SA_TELL,SA116,MG_CHK,MG_TOU,ATO_N],
 ["Services Australia: tell it within 28 days","SA116 updates Medicare, Centrelink and Child Support records","myGov: no need to close; unused accounts close automatically","ATO: up to 28 days to update records after notification"],
 ["/guides/australian-digital-estate-guide/","/guides/superannuation-after-death-australia/","/guides/what-to-do-when-someone-dies-digital-checklist/"])

SUPER=("superannuation-after-death-australia","What happens to your super when you die? (Australia)",
 "Your super doesn't automatically form part of your estate. In most cases the fund pays your balance, plus any insurance held in super, as a death benefit to your nominated beneficiary. A valid binding nomination means the fund must follow your choice; without one, the trustee decides. Check your nomination in your fund's app or website.",
 ["Log in to each super fund (website or app) and check whether you have a nomination, what type it is and whether it expires.",
  "Ask your fund which nomination types it offers. Not every fund offers every type.",
  "Choose eligible people: a spouse or partner, children of any age, someone in an interdependency relationship with you, someone financially dependent on you, or your legal personal representative (your estate).",
  "Want someone who isn't a dependant to benefit? The ATO suggests asking your fund about a binding nomination to your legal personal representative, so the money is distributed under your will. Keep your will up to date.",
  "Follow the form's signing and witnessing instructions exactly. Moneysmart warns that mistakes can make a nomination invalid.",
  "If it's a lapsing binding nomination, set a reminder. These expire after 3 years unless you renew them.",
  "List each fund, member number and any insurance in your estate inventory. Leave passwords out.",
  "After a death: the beneficiary or executor contacts each fund to report the death and ask about releasing the super, and checks whether the person had ATO-held super."],
 [("Does super go through my will?","Not automatically. Moneysmart says super doesn't automatically form part of your estate. It's distributed under your will only if it's paid to your legal personal representative (your estate)."),
  ("What is a binding death benefit nomination?","An instruction your fund must follow to pay your super to the eligible people you name. Lapsing ones must be renewed every 3 years; non-lapsing ones don't expire. Not every fund offers them."),
  ("What happens if I don't nominate anyone?","The ATO says the fund trustee may use its discretion to decide which dependants receive it, or pay it to your legal personal representative to be distributed under your will."),
  ("Who can I nominate for my super?","Your spouse or partner, your children of any age, someone in an interdependency relationship with you, anyone financially dependent on you, or your legal personal representative."),
  ("Can a non-dependant receive super as an income stream?","No. The ATO says a death benefit paid to someone who isn't a dependant must be paid as a lump sum."),
  ("How do I find a deceased person's super?","Contact the funds you know about and check whether the person had ATO-held super. The ATO can give super fund details to the authorised legal personal representative.")],
 [ATO_S,MS_S,ATO_N],
 ["Super isn't automatically part of your estate","Lapsing binding nominations expire after 3 years","Non-dependants can only receive a lump sum","The death benefit can include insurance held in super"],
 ["/guides/australian-digital-estate-guide/","/guides/mygov-centrelink-medicare-ato-after-death/","/guides/digital-estate-checklist/"])

TELCO=("mobile-phone-number-after-death-australia","Telstra, Optus and Vodafone after a death: keep or cancel the mobile number? (Australia)",
 "Telstra, Optus and Vodafone all let an authorised person, such as the executor or next of kin, cancel a deceased customer's services or transfer the mobile number into their own name. All three also offer a copy of the voicemail greeting (Vodafone: where available). Ask for it before you cancel or transfer, and consider keeping the number until the person's accounts are sorted.",
 ["Check you can act. Telstra, Optus and Vodafone accept the executor, administrator or trustee, the lawyer handling the will, next of kin, or an authorised representative on the account. Optus and Vodafone also accept a power of attorney.",
  "Gather documents. Telstra and Vodafone ask for the will or a grant of representation (probate or letters of administration); next of kin may show a birth certificate instead. Administrators show the letters of administration.",
  "List each service (mobile, home internet, email) and decide whether to cancel or transfer it.",
  "Ask for a copy of the voicemail greeting first. Telstra warns it may already be deleted once a transfer or closure has been requested.",
  "Notify the telco. Telstra and Vodafone accept notifications through the Australian Death Notification Service. Directly: Telstra online form, email, post, store or 1800 775 932; Optus Bereavement Care form by email or post; Vodafone on 1555 or 1300 650 410.",
  "Transferring the number? Expect a credit check. Optus asks for at least 100 points of ID and Vodafone says you'll need to meet its credit requirements.",
  "Keep the deceased's Telstra email? Telstra says you need to transfer it to a new account using its Bereavement Support form.",
  "Telstra sends the final bill in the name of 'The Estate of the deceased' to the address the notifier nominates."],
 [("Can I keep my late partner's mobile number?","Usually, by transferring it into your name. Telstra, Optus and Vodafone all offer transfers through their bereavement processes. Optus and Vodafone say a credit check or their credit requirements apply."),
  ("Can I get a copy of their voicemail greeting?","Yes. Telstra, Optus and Vodafone all offer a digital copy (Vodafone says where available). Ask before you cancel or transfer: Telstra says the greeting may already be deleted after a transfer or closure request, and Optus says custom greetings reset on transfer."),
  ("Why not cancel the number straight away?","Many banks, email providers and government services send sign-in or recovery codes by SMS. Keeping the number while accounts are closed through official processes can make that admin easier. Check with the executor before using codes to get into any account."),
  ("Does the Australian Death Notification Service notify Telstra and Vodafone?","Yes. Telstra and Vodafone both accept ADNS notifications and say they'll contact you within 10 business days. Optus's bereavement form is returned by email or post."),
  ("How long does it take?","Telstra and Optus say their specialist team will contact you within 10 business days, and Vodafone says the same for ADNS notifications. None publishes a fixed completion time."),
  ("Who can close a deceased person's phone account?","The executor, administrator or trustee, the lawyer handling the will, next of kin, or an authorised representative on the account. Optus and Vodafone also accept a power of attorney.")],
 [TEL,OPT,VOD],
 ["Telstra, Optus and Vodafone: cancel or transfer","Voicemail greeting copy available on request","Transfers: credit check (Optus, Vodafone)","Response within 10 business days"],
 ["/guides/mygov-centrelink-medicare-ato-after-death/","/guides/access-deceased-persons-phone-and-accounts/","/guides/what-to-do-when-someone-dies-digital-checklist/"])

TROWS=[("Telstra","Online Bereavement Support form, email bereavement@support-team.telstra.com, post, store, or 1800 775 932; also via ADNS","Within 10 business days","Yes, on request","Telstra email can be transferred to a new account",TEL[1]),
("Optus","Bereavement Care form to BereavementCare@optus.com.au or PO Box 888, North Ryde NSW 1670","Within 10 business days","Yes, on the form","Transfer needs a credit check and 100 points of ID",OPT[1]),
("Vodafone","1555 or 1300 650 410 (business: 135 888); also via ADNS","Within 10 business days (ADNS)","Where available","Transfer needs you to meet credit requirements",VOD[1])]
TTABLE="<h2 id='telcos'>How do Telstra, Optus and Vodafone compare?</h2><div class='ctw'><table class='ct'><caption>Bereavement processes (official pages, checked "+CHK+")</caption><thead><tr><th scope='col' class='corner'>Telco</th><th scope='col'>How to notify</th><th scope='col'>Response</th><th scope='col'>Voicemail copy</th><th scope='col'>Transfer notes</th></tr></thead><tbody>"+"".join(f"<tr><th scope='row'><a href='{u}' rel='noopener' target='_blank'>{E(n)} ↗</a></th><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td><td>{E(d)}</td></tr>" for n,a,b,c,d,u in TROWS)+"</tbody></table></div><p class='meta'>Using another provider? Check its own bereavement or deceased-customer page.</p>"
SA_BOX="<div class='box'><p><strong>Australia-specific guides:</strong> <a href='/guides/mygov-centrelink-medicare-ato-after-death/'>myGov, Centrelink, Medicare and the ATO</a> · <a href='/guides/superannuation-after-death-australia/'>super after death</a> · <a href='/guides/mobile-phone-number-after-death-australia/'>Telstra, Optus and Vodafone</a></p></div>"
NEW_GUIDES=[MYGOV,SUPER,TELCO]
NEW_PATHS=["/platforms/snapchat/"]+[f"/guides/{g[0]}/" for g in NEW_GUIDES]
REFRESHED=["/guides/australian-digital-estate-guide/"]
LASTMOD={p:DATE for p in NEW_PATHS+REFRESHED}
PUBLISHED={p:DATE for p in NEW_PATHS}
SHORT=[("What happens to my Snapchat when I die?","Snapchat gives no one access and describes no memorialisation; deletion needs the login (30 days deactivated, then deleted after 30 more).","/platforms/snapchat/"),
("Do I need to close a deceased person's myGov account?","No. myGov closes unused accounts. Tell Services Australia within 28 days (SA116) and notify the ATO separately.","/guides/mygov-centrelink-medicare-ato-after-death/"),
("What happens to my super when I die (Australia)?","It isn't automatically part of your estate; the fund pays a death benefit, following a valid binding nomination if you made one.","/guides/superannuation-after-death-australia/"),
("Can I keep a deceased person's mobile number (Telstra, Optus, Vodafone)?","Usually yes, by transfer through the telco's bereavement process; ask for the voicemail greeting copy first.","/guides/mobile-phone-number-after-death-australia/")]

def pre(enrich,growth):
    enrich.NEWP.append(SNAP)
    enrich.GUIDE_NEW.extend(NEW_GUIDES)
    growth.EXTRA[TELCO[0]]=TTABLE
    growth.EXTRA["australian-digital-estate-guide"]=growth.EXTRA.get("australian-digital-estate-guide","")+SA_BOX
    growth.SHORT.extend(SHORT)
    for k in ("instagram","x-twitter"):
        r=enrich.P[k]["related"]
        if "/platforms/snapchat/" not in r: r.append("/platforms/snapchat/")
    for i,x in enumerate(enrich.GUIDE_NEW):
        s,t,an,st,f,src,tl,rel=x
        if s=="australian-digital-estate-guide":
            # Refresh (19 Oct 2026): Services Australia 28-day step and official ATO notification route, both from official pages.
            st=list(st)
            j=next(k for k,v in enumerate(st) if v.startswith("Phone the ATO"))
            st[j]="Phone the ATO to pause tax correspondence, then officially notify it with a death certificate or grant (online with an Australia Post interview, or by paper form). The ATO says records take up to 28 days to update."
            st.insert(j,"Tell Services Australia within 28 days (Advice of death form SA116, phone or a service centre) so it can update Medicare, Centrelink and Child Support records. You don't need to close their myGov account.")
            enrich.GUIDE_NEW[i]=(s,t,an,st,f,src+[SA_TELL,SA116,ATO_N],tl,rel+["/guides/mygov-centrelink-medicare-ato-after-death/","/guides/superannuation-after-death-australia/","/guides/mobile-phone-number-after-death-australia/"])
        if s=="what-to-do-when-someone-dies-digital-checklist":
            enrich.GUIDE_NEW[i]=(s,t,an,st,f,src,tl,rel+["/guides/mobile-phone-number-after-death-australia/","/guides/mygov-centrelink-medicare-ato-after-death/"])
    enrich.GUIDE_REL["digital-estate-checklist"]=enrich.GUIDE_REL["digital-estate-checklist"]+["/guides/superannuation-after-death-australia/"]
