# Content pack 8 (23 Nov 2026, AEST). Every fact here was checked against the cited official page on 23 Nov 2026.
# Skipped again: TikTok (help and legal pages still script-rendered, no readable content), eBay (deceased-member help page
# now sits behind a bot "verify yourself" wall), Airbnb and Uber (no official deceased-account help page found/readable),
# Etsy, Patreon and Signal help centres (403 to every fetch). Computershare's "Deceased Estates Guide" PDF that search surfaces
# is the New Zealand edition (NZ$ fees, NZ addresses), so it isn't used; only Computershare's Australian checklist and forms are cited.
# Refreshed: Apple iCloud platform page, Apple Legacy Contact tool and setup guide. Re-checked all three Apple support pages
# (102631, 102431, 102678): the 3-year Legacy Contact access window is confirmed on 102678 ("three years from when Apple
# approves the first Legacy Contact account request"); added the multiple-Legacy-Contacts FAQ (any one can delete the account).
DATE="2026-11-23"; CHK="23 Nov 2026"
WP_DEC=("WordPress.com Support: Deceased site owner","https://wordpress.com/support/deceased-user/")
CS_CHK=("Computershare: Deceased Estates Checklist for Australian Residents (PDF)","https://cda-au.computershare.com/Content/1cc8284b-9ae8-4384-a2ea-04fdc840d9b9")
CS_TRM=("Computershare: Transmission Application - Transmit Securities to Executor(s)/Administrator(s) (PDF)","https://cda-au.computershare.com/Content/423c601d-07ab-436b-9d91-43f9fe0561cc")
CS_TRF=("Computershare: Standard Transfer - Transfer Securities to Beneficiary(s)/Buyer(s) (PDF)","https://cda-au.computershare.com/Content/e3f49c2a-f55d-450f-8cfb-80ad40e15742")
MUFG=("MUFG Corporate Markets: Deceased Estate Settlement Services","https://docs.investorcentre.mpms.mufg.com/deceased-estates/home/")
MS_SH=("Moneysmart (ASIC): Claim money from shares and investments","https://moneysmart.gov.au/find-unclaimed-money/claim-money-from-shares-and-investments")
MS_POO=("Moneysmart (ASIC): Proof of ownership for unclaimed money","https://moneysmart.gov.au/find-unclaimed-money/proof-of-ownership-for-unclaimed-money")
MS_BANK=("Moneysmart (ASIC): Claim money from bank accounts and bank dividends","https://moneysmart.gov.au/find-unclaimed-money/claim-money-from-bank-accounts-and-bank-dividends")
SNSW_UM=("Service NSW: Find unclaimed money with ASIC's Moneysmart","https://www.service.nsw.gov.au/transaction/find-unclaimed-money-with-asics-moneysmart")
RNSW_UM=("Revenue NSW: How to search and make a claim (unclaimed money)","https://www.revenue.nsw.gov.au/unclaimed-money/search-and-make-a-claim")
QPT_HOW=("Queensland Public Trustee: How to claim your unclaimed money","https://www.pt.qld.gov.au/other-services/unclaimed-money/how-to-claim-your-unclaimed-money")
QPT_ABT=("Queensland Public Trustee: About unclaimed money","https://www.pt.qld.gov.au/other-services/unclaimed-money/about-unclaimed-money")
ATO_ACC=("ATO: Accessing a deceased person's tax and super information","https://www.ato.gov.au/individuals-and-families/deceased-estates/accessing-a-deceased-person-s-tax-and-super-information")
SNSW_TR=("Service NSW: Transfer a vehicle registration due to the death of the registered operator","https://www.service.nsw.gov.au/transaction/transfer-a-vehicle-registration-due-to-the-death-of-the-registered-operator")
TNSW_DE=("Transport for NSW: Deceased estates and transferring vehicle registration","https://www.nsw.gov.au/driving-boating-and-transport/vehicle-registration/transferring-or-cancelling-registration/deceased-estates-and-transferring-vehicle-registration")
SNSW_NOT=("Service NSW: Notify Transport for NSW that a customer has died","https://www.service.nsw.gov.au/transaction/notify-transport-for-nsw-that-a-customer-has-died")
APPLE=["https://support.apple.com/en-us/102631","https://support.apple.com/en-us/102431","https://support.apple.com/en-us/102678"]
CHECKED_AT={u:CHK for _,u in [WP_DEC,CS_CHK,CS_TRM,CS_TRF,MUFG,MS_SH,MS_POO,MS_BANK,SNSW_UM,RNSW_UM,QPT_HOW,QPT_ABT,ATO_ACC,SNSW_TR,TNSW_DE,SNSW_NOT]}
CHECKED_AT.update({u:CHK for u in APPLE})

WORDPRESS=dict(slug="wordpress-com",name="WordPress.com",cat="platforms",url=WP_DEC[1],
 answer="WordPress.com says it helps the family or estate decide what happens to a deceased owner's site. Email passwordhelp@wordpress.com with the owner's name or account email (if known), the site address, a short explanation and what you want: make the site private or transfer it to another owner. To transfer ownership, attach a copy of the death certificate plus a legal document showing your authority to act, or a signed, notarized statement. WordPress.com's page describes no setting to plan this in advance, so leave instructions in your digital estate plan.",
 steps=["Write down in your digital estate plan each site you run on WordPress.com: its address, the email address on the account, and whether it should be kept, made private, handed to someone or deleted.",
  "After a death, email WordPress.com at passwordhelp@wordpress.com.",
  "Include the site owner's name or the account's email address (if you know it), the site's URL, a brief explanation of the situation, and the action you want: making the site private, or transferring it to another owner.",
  "To transfer ownership to another account, attach a copy of the death certificate and either a legal document showing your authority to act for the deceased, or a signed, notarized statement giving your first and last name, current contact details, email address, relationship to the site owner and the action you're requesting.",
  "Once you have access, WordPress.com suggests options such as publishing a post to update readers, adding an 'in memoriam' page, setting up a donation form, making the site private or deleting it.",
  "Update or cancel any paid subscriptions on the site so billing doesn't continue unnoticed."],
 facts=["Contact: passwordhelp@wordpress.com","Options: make the site private or transfer it to another owner","Transfer needs a death certificate plus proof of authority or a notarized statement","No advance 'legacy' setting described on WordPress.com's page"],
 need=["The site owner's name or account email address (if known)","The site's URL","For an ownership transfer: a copy of the death certificate","For an ownership transfer: a legal document showing your authority to act, or a signed, notarized statement with your name, contact details, email, relationship and requested action"],
 timeline="WordPress.com publishes no processing time for deceased-owner requests.",
 lost=["Paid plans and add-ons keep renewing until someone updates or cancels the subscriptions","Anything deleted: WordPress.com lists deleting the site as one option once you have access, so download what you want to keep first"],
 faqs=[("Who do I contact at WordPress.com when a site owner dies?","Email passwordhelp@wordpress.com. WordPress.com says it helps the family or estate decide what happens to the site, such as making it private or transferring it to another owner."),
  ("How do I take over a deceased person's WordPress.com site?","Email passwordhelp@wordpress.com asking to transfer ownership to another account, and attach a copy of the death certificate plus a legal document showing your authority to act, or a signed, notarized statement with your name, contact details, email, relationship to the owner and the action you want."),
  ("Can WordPress.com make a deceased person's site private?","Yes. WordPress.com lists making the site private as one of the actions you can ask for when you report a deceased site owner."),
  ("What can I do with the site once I have access?","WordPress.com suggests publishing an update post, adding an 'in memoriam' page, setting up a donation form, making the site private or deleting it, and updating or cancelling billing subscriptions."),
  ("Do I need a lawyer's document to transfer the site?","Not necessarily. WordPress.com accepts either a legal document stating your authority to act for the deceased, or a signed, notarized statement with the details it lists, alongside a copy of the death certificate.")],
 sources=[WP_DEC],related=["/platforms/github/","/platforms/google-gmail/","/guides/digital-estate-checklist/","/guides/what-to-do-when-someone-dies-digital-checklist/"])

SH=("shares-after-death-australia","What happens to shares when someone dies in Australia?",
 "Shares stay in the deceased person's name until the estate deals with them. If they're CHESS-sponsored (a HIN starting with X), the sponsoring broker handles it. If they're issuer-sponsored (an SRN), contact the company's share registry, such as Computershare or MUFG Corporate Markets. Shares can be transmitted into the executor's name or transferred straight to beneficiaries; there's no need to transmit first. For a sole holding of an Australian resident, Computershare accepts a death certificate, the will and a Small Estate Indemnity form for holdings worth up to A$50,000. Above that it needs probate. A surviving joint holder uses a separate form.",
 ["Find the holdings: look for holding statements, dividend statements and emails. Note each company, the SRN (10 digits, starting with I) or HIN, and the name and address exactly as registered.",
  "CHESS-sponsored holdings (HIN starts with X): contact the sponsoring broker. Both Computershare and MUFG say the broker deals with the estate for these.",
  "Issuer-sponsored holdings: contact the registry named on the statement. MUFG offers an online questionnaire that lists the forms and documents your situation needs.",
  "Work out what each holding is worth. Computershare's Australian checklist sets the paperwork by value: up to A$50,000 with a will, a certified death certificate, the will and a 'Small Estate Indemnity' form (or probate). Over A$50,000, probate. With no will: up to A$50,000, the death certificate and an 'Intestacy Request and Indemnity' form (or letters of administration); over that, letters of administration.",
  "Use a registry death certificate. MUFG says a medical death certificate isn't enough; it needs the certificate issued by Births, Deaths and Marriages.",
  "Add any extra forms that apply. Computershare asks for a 'Confirmation of the Deceased's Name' form if the register name differs from the legal documents, and a 'Section 1071B Statement' if probate is granted in a different state from where the shares are registered. For South Australian probate, get a Section 121A Registrar's Certificate of Disclosure.",
  "Choose the outcome: a 'Transmission Application' puts the shares in the executor's name for later distribution; a 'Standard Transfer' moves them straight to beneficiaries or buyers. Registries don't sell shares; Computershare says to contact a broker to sell.",
  "Send it properly. Computershare needs a separate form for each holding, original forms with ink signatures (no copies, fax or email) and originally certified copies of legal documents, not the originals. MUFG accepts completed forms by email or post.",
  "Check for old dividends or shares already handed to ASIC as unclaimed money; see our unclaimed money guide."],
 [("What happens to shares when someone dies in Australia?","They stay in the deceased's name until the executor or administrator has them transmitted into the executor's name, transferred to beneficiaries, or sold through a broker. CHESS-sponsored shares go through the sponsoring broker; issuer-sponsored shares go through the company's share registry."),
  ("Do you need probate to transfer shares?","Not always. Computershare's Australian checklist accepts a certified death certificate, the will and a Small Estate Indemnity form where a holding is worth up to A$50,000. Above A$50,000 it needs Australian probate (or letters of administration if there's no will)."),
  ("What's the difference between transmission and transfer?","MUFG explains that transmission moves shares from the deceased's name into the executor's name as trustee for the estate. Transfer moves them to the final beneficiaries, either from the executor or directly from the deceased. You can often transfer directly without transmitting first."),
  ("How do I know if shares are CHESS or issuer sponsored?","Check the holding statement. A HIN beginning with X means CHESS-sponsored, so contact the broker. An issuer-sponsored holding has an SRN, which Computershare describes as a 10-digit number starting with I."),
  ("Can shares be registered in the name of an estate or a child?","Not on Computershare's Standard Transfer. It says securities can't be registered in the name of a trust, a super fund, a minor, an estate or a deceased person, and a maximum of three holders can be registered."),
  ("What if the shares were held jointly?","Computershare's checklist doesn't cover joint holdings; it points to its 'Request to Register Surviving Securityholder(s)' form. MUFG lists 'transmit to surviving joint holder(s)' as one of the options.")],
 [CS_CHK,CS_TRM,CS_TRF,MUFG,MS_SH],
 ["CHESS (HIN starts with X): go through the broker","Computershare: up to A$50,000 per holding, will + death certificate + indemnity","Over A$50,000: probate or letters of administration","Registries don't sell shares; use a broker"],
 ["/guides/australian-digital-estate-guide/","/guides/unclaimed-money-deceased-estate-australia/","/guides/final-tax-return-deceased-person-australia/","/guides/bank-accounts-after-death-australia/"])

UM=("unclaimed-money-deceased-estate-australia","How to find and claim a deceased person's unclaimed money in Australia",
 "Search ASIC's Moneysmart unclaimed money register for old bank accounts, shares and life insurance, and your state's register for other money (in Queensland, the Public Trustee; in NSW, Revenue NSW). There's no time limit on claiming money held by ASIC. Only the executor or administrator can claim for the estate. For ASIC-held shares money they use Claim form B with probate, or with a certified death certificate and will if the amount is $20,000 or less. Bank-account money is claimed through the bank's unclaimed money team.",
 ["Search ASIC's register on Moneysmart by name (or Original Transaction Number). It covers money from lost bank accounts, shares and investments, and life insurance. Service NSW notes bank accounts become unclaimed after 7 years with no deposits or withdrawals.",
  "Search the state register too. Queensland Public Trustee holds money from Queensland government agencies, businesses such as solicitors, real estate agents and nursing homes, unclaimed wages and deceased estate entitlements. It doesn't hold old bank accounts, life insurance, super or rental bonds. In NSW, search Revenue NSW's register.",
  "Note the reference: the OTN for ASIC records, or the reference number for Queensland Public Trustee.",
  "Shares and investments ('Company money') held by ASIC: the executor or administrator completes Claim form B - Representative, with all executors claiming. Provide certified ID for each, proof of the deceased's address or connection to the company, and a certified copy of probate including the full will. With a will but no probate, certified copies of the death certificate and will are enough unless the funds exceed $20,000.",
  "Old bank accounts: contact the bank that held the account and ask for its unclaimed money team. ASIC only assesses these claims when they come through the bank.",
  "Queensland Public Trustee: all executors sign the application, a Justice of the Peace witnesses it, and you post it with certified ID, linking documents, the will, the death certificate and the grant of probate or letters of administration (or a statutory declaration from all executors if there isn't one). Money is paid to an estate bank account, or by cheque to the estate.",
  "Revenue NSW: select 'Deceased estate' in its online claim. The executor or administrator provides ID, the grant (or will and death certificate) and a document linking the deceased to the address on record; all executors must be part of the claim.",
  "No will? ASIC asks you to email it first with the beneficiaries, the estate's value, place and date of death, usual residence and confirmation that no grant was made. Revenue NSW says you need formal administration and suggests contacting NSW Trustee and Guardian.",
  "Lost super is separate: once the ATO records you as the legal personal representative, its deceased estate data package includes details of any super accounts."],
 [("How do I find unclaimed money for a deceased person in Australia?","Search ASIC's unclaimed money register on Moneysmart (bank accounts, shares and investments, life insurance) and the state register, such as Queensland Public Trustee or Revenue NSW. Anyone can search a name, but only the executor or administrator can claim for the estate."),
  ("Who can claim unclaimed money for a deceased estate?","The executor or administrator. ASIC requires all executors to claim on Claim form B, Queensland Public Trustee says the executor is the only person eligible, and Revenue NSW requires all executors or administrators to be part of the claim."),
  ("Do I need probate to claim unclaimed money from ASIC?","Not for smaller amounts. For shares and investments money, ASIC accepts certified copies of the death certificate and will if the funds are $20,000 or less. Over $20,000, probate must be provided."),
  ("Is there a time limit to claim unclaimed money?","Not for money lodged with ASIC. Service NSW notes it can be claimed at any time by the rightful owner, and interest is paid from 1 July 2013."),
  ("How long does an unclaimed money claim take?","ASIC says about 60 days once it has the correct documents. Queensland Public Trustee aims for up to 28 days from receiving all documents, and Revenue NSW asks you to allow up to 28 days."),
  ("How do I claim a dead person's old bank account money?","Contact the bank that originally held the account and ask for its unclaimed money team. The bank verifies the claim and submits it to ASIC, and the funds come back through the bank.")],
 [MS_SH,MS_POO,MS_BANK,SNSW_UM,QPT_ABT,QPT_HOW,RNSW_UM,ATO_ACC],
 ["Only the executor or administrator can claim for an estate","ASIC: no time limit; about 60 days to process","ASIC shares money: will + death certificate if $20,000 or less","Bank-account money: claim through the bank"],
 ["/guides/bank-accounts-after-death-australia/","/guides/shares-after-death-australia/","/guides/superannuation-after-death-australia/","/guides/australian-digital-estate-guide/"])

NV=("vehicle-registration-after-death-nsw","Transfer or cancel a NSW car registration after a death",
 "When a NSW registered operator dies, the registration must be transferred or cancelled at a Service NSW Centre. It can go to the executor or administrator, a beneficiary (as the executor advises), a surviving joint operator, the next of kin or a buyer. Bring your ID, an Application for Transfer of Registration and proof of death, such as the death certificate. Transfers to the executor, a beneficiary, the next of kin or a joint operator carry no transfer fee or stamp duty; a buyer pays both.",
 ["Tell Transport for NSW about the death if it isn't recorded yet. The NSW Registry of Births, Deaths and Marriages usually notifies it, but that can take time. You can email or post a document confirming the death (a death certificate, newspaper death notice, or letter from a solicitor or NSW Trustee and Guardian) or take it to a Service NSW Centre. This covers licences and registrations.",
  "Decide who the vehicle goes to: the executor or administrator, a beneficiary, the surviving joint registered operator, the next of kin, or a buyer.",
  "Gather the basics: your proof of identity, a completed Application for Transfer of Registration, and proof of death (the death certificate, a newspaper or online death notice, a letter from a solicitor or NSW Trustee and Guardian, or an Advice of Death form with the deceased's ID).",
  "To the executor or administrator: add the original or a certified copy of the will, probate or letters of administration, or signed written advice from a solicitor or NSW Trustee and Guardian.",
  "To a beneficiary: the same estate documents, plus signed advice from the executor or administrator confirming the beneficiary's name.",
  "To the next of kin: a statutory declaration giving the relationship, that to their knowledge there's no administrator and no will, why they're entitled, and that no closer relative has a better claim. A guardian completes it if the next of kin is under 18.",
  "Surviving joint operator: no extra documents. Buyer: Proof of Registration Entitlement, and the buyer pays the transfer fee and stamp duty.",
  "To cancel the registration instead, provide the will, probate or letters of administration (or a solicitor's or NSW Trustee and Guardian's written advice). A fee may apply.",
  "Take everything to a Service NSW Centre; this transfer can't be done online."],
 [("How do I transfer a car registration when someone dies in NSW?","Go to a Service NSW Centre with your ID, a completed Application for Transfer of Registration, proof of death and the documents for the person receiving it (for example the will or probate for the executor)."),
  ("Do you pay stamp duty to transfer a deceased person's car in NSW?","Not when it goes to the executor or administrator, a beneficiary, the next of kin or the surviving joint operator. A buyer pays the transfer fee and stamp duty."),
  ("Can next of kin transfer a car without a will in NSW?","Yes. The next of kin completes a statutory declaration stating their relationship, that to their knowledge there's no administrator and no will, why they're entitled, and that no closer relative is entitled."),
  ("Do I need to tell Transport for NSW about a death?","The NSW Registry of Births, Deaths and Marriages usually tells Transport for NSW, but it can take some time. You can notify it yourself by email, post or in person with a document confirming the death."),
  ("Can I transfer a deceased person's NSW registration online?","No. Service NSW says this transfer is done at a Service NSW Centre."),
  ("What if the car is sold without being transferred first?","Service NSW says that if the vehicle is sold without first being transferred to a person named in a will or other acceptable document, the new operator must meet the normal transfer requirements.")],
 [SNSW_TR,TNSW_DE,SNSW_NOT],
 ["Transfer at a Service NSW Centre, not online","No transfer fee or stamp duty for executor, beneficiary, next of kin or joint operator","Buyers pay transfer fee and stamp duty","BDM usually tells Transport for NSW, but it can take time"],
 ["/guides/car-registration-driver-licence-after-death-queensland/","/guides/death-certificate-australia/","/guides/australian-digital-estate-guide/","/guides/what-to-do-when-someone-dies-digital-checklist/"])

NEW_PLAT=[WORDPRESS]
NEW_GUIDES=[SH,UM,NV]
NEW_PATHS=[f"/platforms/{p['slug']}/" for p in NEW_PLAT]+[f"/guides/{g[0]}/" for g in NEW_GUIDES]
REFRESHED=["/platforms/apple-icloud/","/tools/apple-legacy-contact/","/guides/apple-legacy-contact-setup/"]
SHORT=[("What happens to my WordPress.com site when I die?","Family or the estate emails passwordhelp@wordpress.com to make it private or transfer it; a transfer needs the death certificate plus proof of authority or a notarized statement.","/platforms/wordpress-com/"),
("What happens to shares when someone dies in Australia?","CHESS holdings go through the broker; issuer-sponsored through the registry. Computershare: will + death certificate + indemnity up to A$50,000 a holding, probate above.","/guides/shares-after-death-australia/"),
("How do I claim a deceased person's unclaimed money in Australia?","Search Moneysmart (ASIC) and the state register. The executor claims; ASIC accepts will + death certificate up to $20,000, probate above. No time limit for ASIC money.","/guides/unclaimed-money-deceased-estate-australia/"),
("How do I transfer a car registration after a death in NSW?","At a Service NSW Centre with ID, the transfer application, proof of death and estate documents. No fee or stamp duty unless it goes to a buyer.","/guides/vehicle-registration-after-death-nsw/")]
APPLE_FAQ=("Can I have more than one Legacy Contact?","Yes. Apple says you can add more than one, and any one of them can make decisions about your account data after your death on their own, including permanently deleting it. A Legacy Contact doesn't need an Apple Account or device but must be over 13 (age varies by country).")

def _add(lst,s):
    if s not in lst: lst.append(s)
def pre(enrich,growth,pack2):
    enrich.NEWP.extend(NEW_PLAT)
    enrich.GUIDE_NEW.extend(NEW_GUIDES)
    growth.SHORT.extend(SHORT)
    for p in NEW_PATHS+REFRESHED: pack2.LASTMOD[p]=DATE; pack2.REV[p]=CHK
    for p in NEW_PATHS: pack2.PUBLISHED[p]=DATE
    pack2.CHECKED_AT.update(CHECKED_AT)
    a=enrich.P["apple-icloud"]; ex=a.setdefault("extra",[])
    if APPLE_FAQ not in ex: ex.insert(1,APPLE_FAQ)  # page shows 6 FAQs; the passcode point stays in the "can't be recovered" list
    for p in enrich.NEWP:
        if p["slug"]=="github": _add(p.setdefault("related",[]),"/platforms/wordpress-com/")
    links={"car-registration-driver-licence-after-death-queensland":["/guides/vehicle-registration-after-death-nsw/"],
      "bank-accounts-after-death-australia":["/guides/unclaimed-money-deceased-estate-australia/","/guides/shares-after-death-australia/"],
      "superannuation-after-death-australia":["/guides/unclaimed-money-deceased-estate-australia/"],
      "final-tax-return-deceased-person-australia":["/guides/shares-after-death-australia/"],
      "australian-digital-estate-guide":["/guides/shares-after-death-australia/","/guides/unclaimed-money-deceased-estate-australia/","/guides/vehicle-registration-after-death-nsw/"],
      "what-to-do-when-someone-dies-digital-checklist":["/guides/unclaimed-money-deceased-estate-australia/","/guides/shares-after-death-australia/","/platforms/wordpress-com/"],
      "death-certificate-australia":["/guides/vehicle-registration-after-death-nsw/"]}
    for i,x in enumerate(enrich.GUIDE_NEW):
        s,t,an,st,f,src,tl,rel=x
        add=[a for a in links.get(s,[]) if a not in rel and a!=f"/guides/{s}/"]
        enrich.GUIDE_NEW[i]=(s,t,an,st,f,src,tl,rel+add)
    growth.EXTRA["australian-digital-estate-guide"]=growth.EXTRA.get("australian-digital-estate-guide","").replace("frequent flyer points</a>","frequent flyer points</a> · <a href='/guides/shares-after-death-australia/'>shares</a> · <a href='/guides/unclaimed-money-deceased-estate-australia/'>unclaimed money</a> · <a href='/guides/vehicle-registration-after-death-nsw/'>NSW car rego</a>",1)
