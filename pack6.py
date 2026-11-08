# Content pack 6 (9 Nov 2026, AEST). Every fact here was checked against the cited official page on 9 Nov 2026.
# Skipped again: TikTok (official help/legal pages are script-rendered and returned no readable content; no archive copy),
# Origin Energy (deceased-estate help page renders no readable content), deathnotification.gov.au (connection timed out).
# AGL's deceased-estates page is now readable, so the utilities guide gains AGL's process (re-verified 9 Nov 2026).
DATE="2026-11-09"; CHK="9 Nov 2026"
NF_DEC=("Netflix Help: How to cancel a Netflix account for a member who has died, is incarcerated, or under guardianship","https://help.netflix.com/en/node/110165")
NF_CAN=("Netflix Help: How to cancel Netflix","https://help.netflix.com/en/node/407")
ATO_FIN=("ATO: Doing a final tax return for the deceased person","https://www.ato.gov.au/individuals-and-families/deceased-estates/doing-a-final-tax-return-for-the-deceased-person")
ATO_NOT=("ATO: Notifying us of a death and who will manage the estate","https://www.ato.gov.au/individuals-and-families/deceased-estates/notifying-us-of-a-death-and-who-will-manage-the-estate")
ATO_CL=("ATO: Checklist: what to do when someone dies","https://www.ato.gov.au/individuals-and-families/deceased-estates/checklist-what-to-do-when-someone-dies")
QLD_DC=("Queensland Government: Get a death certificate","https://www.qld.gov.au/family/deaths/get-death-certificate")
QLD_SD=("Queensland Government: Supporting documents for certificate applications","https://www.qld.gov.au/family/help-centre/proof-of-identity-and-supporting-documents/certificate-applications")
NSW_DC=("NSW Government: Death certificates","https://www.nsw.gov.au/family-and-relationships/deaths/death-certificates")
NSW_PS=("NSW Registry of Births, Deaths & Marriages: Products and services","https://www.nsw.gov.au/departments-and-agencies/births-deaths-marriages/products-and-services")
VIC_DC=("Births, Deaths and Marriages Victoria: Get a death certificate","https://www.bdm.vic.gov.au/get-death-certificate")
VIC_TP=("Births, Deaths and Marriages Victoria: Third party authority","https://www.bdm.vic.gov.au/third-party-authority")
TMR_REG=("Queensland Government: Transferring registration from a deceased registered operator","https://www.qld.gov.au/transport/registration/transfer/deceased-estate")
TMR_F5296=("TMR form F5296: Application to Transact with Registration Products on behalf of a Deceased Person (PDF)","https://www.support.transport.qld.gov.au/qt/formsdat.nsf/forms/QF5296/$file/F5296_CFD.pdf")
TMR_LIC=("Queensland Government: Surrendering a licence (incl. refund on behalf of a deceased person)","https://www.qld.gov.au/transport/licensing/driver-licensing/surrender")
AGL=("AGL: Deceased estates (if an account holder has passed away)","https://www.agl.com.au/help-support/account-setup-management/deceased-estates")
CHECKED_AT={u:CHK for _,u in [NF_DEC,NF_CAN,ATO_FIN,ATO_NOT,ATO_CL,QLD_DC,QLD_SD,NSW_DC,NSW_PS,VIC_DC,VIC_TP,TMR_REG,TMR_F5296,TMR_LIC,AGL]}

NETFLIX=dict(slug="netflix",name="Netflix",cat="platforms",url=NF_DEC[1],
 answer="Netflix keeps charging the payment method on file until the membership is cancelled; nothing happens automatically when a member dies. Netflix says it can cancel the account of a friend or family member who has died. With access to the account, use Cancel Membership on the Account page. Without access, contact Netflix with the email address or phone number on the account and the full payment information currently used to pay for it.",
 steps=["Note in your digital estate plan which email address or phone number your Netflix account uses and how it's paid. That's what family will need to cancel it.",
  "After a death, with access to the account: go to the Account page, select Cancel Membership, then Finish Cancellation. Netflix emails a confirmation to the account's email address.",
  "If needed, use Sign out of all devices so the account isn't left logged in on TVs and phones.",
  "Without access: gather the email address or phone number on the Netflix account and the full payment information currently used to pay for it, then contact Netflix through help.netflix.com.",
  "If there's no cancel option on the Account page, the membership is billed through a payment partner (for example a phone, internet or TV package). Netflix says it must then be cancelled with that partner, and the Account page shows how.",
  "Check the next card or bank statement to confirm the Netflix charges have stopped."],
 facts=["Netflix will cancel on behalf of someone who has died","No login needed: give the account email or phone and payment details","Signing out or deleting the app doesn't cancel","Partner-billed memberships are cancelled through the partner"],
 need=["The email address or phone number associated with the Netflix account","The full payment information currently used to pay for Netflix"],
 timeline="Netflix publishes no processing time for cancelling on someone's behalf. After cancellation the account won't be charged again, and if there's time left in the billing period it stays usable until it cancels automatically at the end of that period.",
 lost=["Streaming for everyone using the account's profiles once the membership ends","Any remaining gift card or promotional balance is used for continued service after cancelling, until it runs out"],
 faqs=[("What happens to my Netflix account when I die?","Nothing automatic. The membership keeps billing the payment method on file until someone cancels it. Netflix says family or friends can ask it to cancel the account of a member who has died."),
  ("How do I cancel a deceased person's Netflix without the password?","Contact Netflix with the email address or phone number associated with the account and the full payment information currently used to pay for Netflix. Netflix says it can then cancel the account on their behalf."),
  ("Does signing out or deleting the Netflix app cancel the account?","No. Netflix says cancelling from the account is the only way to end the membership; signing out or deleting the app doesn't cancel it."),
  ("What if Netflix is billed through a phone or internet provider?","Netflix says memberships billed through a payment partner must be cancelled with that partner. The Account page's Membership section shows a link or instructions."),
  ("When do Netflix charges stop after cancelling?","Netflix won't charge again after cancellation. If there's time left in the billing period, the account can be used until it cancels automatically at the end of that period.")],
 sources=[NF_DEC,NF_CAN],related=["/platforms/spotify/","/platforms/paypal/","/guides/bank-accounts-after-death-australia/","/guides/what-to-do-when-someone-dies-digital-checklist/"])

TAX=("final-tax-return-deceased-person-australia","Final tax return for a deceased person in Australia (the 'date of death' return)",
 "You may need to lodge a final 'date of death' tax return covering 1 July of the income year the person died up to the date of death. The ATO says it's required if the person had tax withheld from their income (including interest or dividends), their taxable income was above the tax-free threshold, or they lodged returns in earlier years or had outstanding returns. Usually the executor or administrator (the legal personal representative) lodges it on the paper tax return for individuals, because myTax and myGov can't be used, or through a tax agent. If no return is needed, send a non-lodgment advice marked 'DECEASED' with the date of death.",
 ["Notify the ATO of the death and who will manage the estate. Use the online form plus an interview at a participating Australia Post outlet, or the paper form by mail with certified copies of the death certificate, grant of probate or letters of administration, or will. You can lodge the return once you're on the ATO's records as managing the deceased's tax affairs.",
  "Applying for probate or letters of administration? The ATO suggests waiting for the grant before sending the notification, to avoid delays. You can phone the ATO's individuals enquiries line meanwhile to pause the deceased's tax correspondence.",
  "Ask whether any earlier returns are outstanding. The ATO can tell you when you notify it; these must be lodged too.",
  "Check whether a date of death return is needed: tax withheld from income (including interest or dividends), taxable income above the tax-free threshold, or returns lodged in earlier years or outstanding. If none apply, send a non-lodgment advice form with 'DECEASED' and the date of death as the reason.",
  "Gather the information: the person's papers first. As the authorised legal personal representative you can get their tax information and TFN from the ATO; otherwise their former tax agent may help.",
  "Use the paper tax return for individuals (or a tax agent you've appointed, who can lodge online). Write 'DECEASED ESTATE' at the top of the first page, give the name as 'LEGAL REPRESENTATIVE OF [name] (DECEASED)', mark 'No' to lodging future returns, and sign 'on behalf of' the deceased.",
  "Include income and deductions up to the date of death, plus the cost of preparing the return (such as tax agent fees) even though it's incurred after the death. Income the estate receives after the death goes in a separate trust tax return.",
  "Provide for any tax owing before distributing the estate. The ATO says the executor or administrator may otherwise be personally liable."],
 [("Do you have to do a tax return for a deceased person in Australia?","Often, yes. The ATO says a date of death return is required if, in the income year they died, the person had tax withheld from income (including interest or dividends), had taxable income above the tax-free threshold, or had lodged returns in earlier years or had outstanding ones. If none apply, send a non-lodgment advice instead."),
  ("Who lodges a deceased person's final tax return?","Usually the authorised legal personal representative, meaning the executor or administrator. You must first notify the ATO of the death and be entered on its records as the person managing the deceased's tax affairs. If someone else lodges, the ATO assesses the return and decides what action to take."),
  ("Can I lodge a deceased person's tax return on myTax or myGov?","No. The ATO says myTax and myGov can only be used by the account holder for their own return, so a date of death return uses the paper tax return for individuals, even to claim a franking credit refund. A tax agent appointed by the executor or administrator can lodge online."),
  ("What period does the final tax return cover?","From 1 July of the income year the person died up to the date of death. In the ATO's example, someone who died on 4 March 2026 has a return covering 1 July 2025 to 4 March 2026."),
  ("Who receives a tax refund for a deceased person?","The ATO releases any refund or franking credits to the authorised legal personal representative. If there isn't one, it decides whether it can release them, taking into account the will or, if there's no will, the rules of succession."),
  ("What happens to a HELP debt when someone dies?","Study and training loan repayments are assessed automatically. If income in the final return is above the minimum repayment threshold, the assessment includes a final repayment; after that, any remaining debt is cancelled."),
  ("Can the deceased person's tax losses be used by the estate?","No. The ATO says tax and capital losses can't be carried forward to the deceased estate; if they can't be used in the date of death return, they lapse.")],
 [ATO_FIN,ATO_NOT,ATO_CL],
 ["Covers 1 July to the date of death","Paper return or tax agent, not myTax or myGov","Usually lodged by the executor or administrator","Provide for tax owing before distributing the estate"],
 ["/guides/mygov-centrelink-medicare-ato-after-death/","/guides/superannuation-after-death-australia/","/guides/bank-accounts-after-death-australia/","/guides/death-certificate-australia/","/guides/australian-digital-estate-guide/"])

DC=("death-certificate-australia","How to get a death certificate in Australia (Qld, NSW and Victoria)",
 "Usually the funeral director registers the death and orders the death certificate for the family. If you need one yourself, apply to the Registry of Births, Deaths and Marriages in the state or territory where the death was registered, with proof of identity and proof you're eligible. In Queensland, NSW and Victoria eligible applicants include the spouse or partner, parent or child; Queensland and NSW also list the executor. Each registry sets its own fees and processing times. In NSW a certificate costs $70 (standard) and in Victoria $59.10 plus postage.",
 ["Ask the funeral director first. NSW and Victoria both say the funeral director normally registers the death and orders the certificate for you; in NSW they register it within 7 days of the burial or cremation.",
  "Apply to the registry where the death was registered. Queensland's service is only for deaths registered in Queensland; for a death elsewhere, apply in that state, territory or country.",
  "Check you're eligible. Queensland: the spouse, parent or child, the person who signed the death registration, the funeral director, or an executor. NSW: a spouse or de facto partner, parent or child whose details are on the certificate, the funeral director (within 30 days of registration), the executor or the estate's solicitor. Victoria: next of kin (spouse or domestic partner, child or parent), or others with third party authority from the next of kin.",
  "Gather proof of identity. Queensland asks for 3 forms of ID including proof of home address, as certified copies if you post the application. Victoria lets you verify your identity online with two documents, or with certified copies. NSW requires proof of identity with every application.",
  "Apply. Queensland: online form, then post the documents or submit in person at a Queensland Magistrates Court or QGAP office (not Brisbane Magistrates Court) or at the Brisbane registry. NSW: online, by post or at a Service NSW centre. Victoria: apply online through BDM Victoria.",
  "Pick the right certificate. Queensland's official death certificate shows the cause of death and is used to finalise estate matters; a limited certificate may not be accepted everywhere. NSW warns that an extract certificate may not be accepted by some organisations. Victoria's package includes certificates with and without the cause of death.",
  "Use the official registry website. NSW warns that third-party websites offering to process certificate applications aren't affiliated with the Registry.",
  "Banks, super funds, telcos and the ATO will ask for the death certificate (often a certified copy), so use our guides to work through each one."],
 [("Who can get a death certificate in Australia?","It depends on the state. Queensland: the spouse, parent or child, the person who signed the death registration, the funeral director or an executor. NSW: a spouse or de facto partner, parent or child named on the certificate, the funeral director (within 30 days of registration), the executor or the estate's solicitor. Victoria: the next of kin, or others with their written authority."),
  ("How much does a death certificate cost?","NSW charges $70 for standard service and $105 for priority, both including $11 postage and handling. Victoria charges $59.10 for a death certificate (with or without the cause of death) or $95.80 for a package of both, plus $10.60 express post within Australia. Queensland's fee is shown when you apply."),
  ("How long does it take to get a death certificate?","NSW: up to 1 week for a death registration and certificate, or up to 3 weeks for a standard online application (2 weeks priority), plus 5 to 7 days for delivery. Victoria: up to 7 days for a registration and certificate in the last 3 months, otherwise up to 14 days, plus postage."),
  ("Does the funeral director get the death certificate?","Usually. NSW and Victoria both say the funeral director normally registers the death and applies for the certificate on the family's behalf."),
  ("Can I get a death certificate if I'm not family?","Sometimes. In NSW you need a letter of authority from someone recorded on the certificate (with their ID and yours) or evidence of an interest in the estate. In Victoria you need third party authority from the next of kin. Queensland lists who else can apply and the documents they need."),
  ("Which death certificate do I need for the estate?","In Queensland, the official death certificate, which shows the cause of death and is used to finalise estate matters. Limited or extract certificates may not be accepted by all organisations.")],
 [QLD_DC,QLD_SD,NSW_DC,NSW_PS,VIC_DC,VIC_TP],
 ["Funeral director usually orders it","Apply in the state where the death was registered","Needs proof of identity and eligibility","NSW $70 standard; Vic $59.10 plus postage"],
 ["/guides/what-to-do-when-someone-dies-digital-checklist/","/guides/australian-digital-estate-guide/","/guides/bank-accounts-after-death-australia/","/guides/final-tax-return-deceased-person-australia/"])

CAR=("car-registration-driver-licence-after-death-queensland","Car registration and driver licence after a death in Queensland",
 "A Queensland vehicle registered in two names can be transferred free of charge to the surviving registered operator with proof of death and original evidence of identity. Otherwise the executor, administrator or next of kin transfers or cancels the registration with TMR form F5296 and either the grant of probate or letters of administration, the will (for an executor) or a statutory declaration (for next of kin). A beneficiary usually must survive the deceased by 30 days first. The driver licence can be surrendered, with a refund of the licence fee, at a transport and motoring service centre or by mail with form F4778.",
 ["Expect a letter. When TMR learns of a death (from Births, Deaths and Marriages or the next of kin) it writes to the last known address listing vehicles and personalised or customised plates to transfer or cancel, and places a restriction on them. The registration isn't cancelled, but it can't be renewed until it's transferred.",
  "Jointly registered vehicle: the surviving registered operator can transfer it into their name free of charge with proof of death (if no Registration Notice Individual Restriction letter has been received) and original evidence of identity. No other forms are needed.",
  "Otherwise, work out your authority. With a grant of probate or letters of administration, present the original or certified copies with form F5296; you don't need the will, the death certificate or the statutory declaration. If probate or administration has been applied for but not yet granted, wait for the grant.",
  "No grant? An executor named in the last valid will presents the original or a certified copy of the will and completes F5296 including the statutory declaration. With no will, the next of kin (under the Succession Act 1981) completes F5296 including the statutory declaration.",
  "TMR may ask for the original or a certified copy of the death certificate or coroner's report.",
  "To transfer or cancel: complete any extra forms listed on F5296, present original evidence of identity and pay any fees. Unattached customised plates must be cancelled. Where there are several executors or administrators, only one needs to sign and present ID.",
  "Not ready to decide? Transfer the registration temporarily into the estate, with the executor, administrator or next of kin as the second registered operator responsible for the vehicle.",
  "Driver licence: surrender it and claim a refund of the licence fee at a transport and motoring service centre with the licence (unless lost or destroyed) and one supporting document: death certificate, coroner's report, Public Trustee certificate of authority, sealed grant of probate, or advice from Births, Deaths and Marriages. Originals, or copies certified by a JP or other qualified person.",
  "By mail: send the return/surrender declaration form F4778, the licence and a certified copy of the supporting document to TMR, Emerald Customer Service Centre, PO Box 1787, Emerald QLD 4720. The refund is a cheque in the name of the licensee or their estate and can take up to 15 working days."],
 [("What happens to car registration when the owner dies in Queensland?","TMR places a restriction on vehicles and plates in the deceased's name and writes to their last known address. The registration isn't cancelled, but it can't be renewed until it's transferred to an eligible person or entity."),
  ("Can I transfer a deceased person's car before probate in Queensland?","If probate or letters of administration have been applied for, TMR says you can't finalise the registration until they're granted. If no grant is being sought, an executor can use the will, or the next of kin a statutory declaration, with form F5296. You can also transfer it temporarily into the estate."),
  ("How do I transfer a jointly registered car after a death?","The surviving registered operator can transfer it into their name free of charge with proof of death and original evidence of identity. No other forms are needed."),
  ("What is the 30-day survival period?","In most cases a beneficiary must survive the deceased by at least 30 days before receiving benefits under the will, so TMR says not to apply to transfer the registration in that time unless the will says otherwise or you're transferring it into the 'estate of' the deceased."),
  ("How do I cancel a deceased person's Queensland driver licence?","Surrender it at a transport and motoring service centre, or by mail with form F4778, with a supporting document such as the death certificate. You can apply for a refund of the licence fee, paid by cheque to the licensee or their estate within about 15 working days."),
  ("What about personalised plates?","Personalised or customised plates in the deceased's name must be transferred or cancelled along with the registration, and unattached customised plates must be cancelled.")],
 [TMR_REG,TMR_F5296,TMR_LIC],
 ["Joint registration: free transfer to the survivor","Otherwise form F5296 with probate, will or statutory declaration","30-day survival period for beneficiaries","Licence refund via service centre or form F4778"],
 ["/guides/death-certificate-australia/","/guides/australian-digital-estate-guide/","/guides/cancel-utilities-after-death-australia/","/guides/redirect-mail-after-death-australia/"])

NEW_PLAT=[NETFLIX]
NEW_GUIDES=[TAX,DC,CAR]
NEW_PATHS=[f"/platforms/{p['slug']}/" for p in NEW_PLAT]+[f"/guides/{g[0]}/" for g in NEW_GUIDES]
REFRESHED=["/guides/cancel-utilities-after-death-australia/"]
SHORT=[("What happens to my Netflix account when I die?","It keeps billing until cancelled. Netflix will cancel a deceased member's account if you give the account email or phone and the full payment details.","/platforms/netflix/"),
("Do you need to lodge a tax return for someone who died in Australia?","Often: a 'date of death' return (1 July to date of death) is needed if tax was withheld, income was above the tax-free threshold, or they lodged before. Paper form or tax agent; not myTax.","/guides/final-tax-return-deceased-person-australia/"),
("How do I get a death certificate in Australia?","The funeral director usually orders it. Otherwise apply to the Births, Deaths and Marriages registry where the death was registered, with ID and proof of eligibility (NSW $70; Vic $59.10 plus postage).","/guides/death-certificate-australia/"),
("How do I transfer a deceased person's car registration in Queensland?","Joint owners transfer free with proof of death and ID; otherwise the executor, administrator or next of kin uses TMR form F5296 with probate, the will or a statutory declaration. Surrender the licence with form F4778.","/guides/car-registration-driver-licence-after-death-queensland/")]

AGL_STEP="AGL customers: AGL says the easiest way to tell it is its NotifyNOW online platform (run by bereavement specialists Phillips & Cohen Associates, which can also notify other registered companies), or chat or phone. It asks for your details and relationship, the executor's details, the account details and what to do with the service."
AGL_FAQ=("How do I close a deceased person's AGL account?","Tell AGL through its NotifyNOW online platform, or by chat or phone. Have your name and contact details, your relationship to the account holder, the executor's name and details, the deceased's account details and what you want done. If supply stays on, Phillips & Cohen Associates manages the process; for a transfer AGL contacts the new account holder; closing the account triggers a final bill.")

def _add(lst,s):
    if s not in lst: lst.append(s)
def pre(enrich,growth,pack2):
    enrich.NEWP.extend(NEW_PLAT)
    enrich.GUIDE_NEW.extend(NEW_GUIDES)
    growth.SHORT.extend(SHORT)
    for p in NEW_PATHS+REFRESHED: pack2.LASTMOD[p]=DATE; pack2.REV[p]=CHK
    for p in NEW_PATHS: pack2.PUBLISHED[p]=DATE
    pack2.CHECKED_AT.update(CHECKED_AT)
    for p in enrich.NEWP:
        if p["slug"] in ("spotify","paypal"): _add(p.setdefault("related",[]),"/platforms/netflix/")
    links={"mygov-centrelink-medicare-ato-after-death":["/guides/final-tax-return-deceased-person-australia/","/guides/death-certificate-australia/"],
      "superannuation-after-death-australia":["/guides/final-tax-return-deceased-person-australia/"],
      "australian-digital-estate-guide":["/guides/death-certificate-australia/","/guides/final-tax-return-deceased-person-australia/","/guides/car-registration-driver-licence-after-death-queensland/"],
      "what-to-do-when-someone-dies-digital-checklist":["/guides/death-certificate-australia/","/guides/final-tax-return-deceased-person-australia/"],
      "bank-accounts-after-death-australia":["/guides/death-certificate-australia/"],
      "redirect-mail-after-death-australia":["/guides/car-registration-driver-licence-after-death-queensland/"],
      "cancel-utilities-after-death-australia":["/guides/death-certificate-australia/"]}
    for i,x in enumerate(enrich.GUIDE_NEW):
        s,t,an,st,f,src,tl,rel=x
        add=[a for a in links.get(s,[]) if a not in rel and a!=f"/guides/{s}/"]
        if s=="cancel-utilities-after-death-australia":
            st=list(st); f=list(f); src=list(src)
            if AGL_STEP not in st: st.insert(3,AGL_STEP)
            if AGL_FAQ not in f: f.insert(2,AGL_FAQ)
            if AGL not in src: src.append(AGL)
        enrich.GUIDE_NEW[i]=(s,t,an,st,f,src,tl,rel+add)
    growth.EXTRA["australian-digital-estate-guide"]=growth.EXTRA.get("australian-digital-estate-guide","").replace("utilities</a>","utilities</a> · <a href='/guides/death-certificate-australia/'>death certificates</a> · <a href='/guides/final-tax-return-deceased-person-australia/'>final tax return</a> · <a href='/guides/car-registration-driver-licence-after-death-queensland/'>Qld car rego and licence</a>",1)
