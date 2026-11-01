# Content pack 5 (2 Nov 2026, AEST). Every fact here was checked against the cited official page on 2 Nov 2026.
# X's help centre blocks automated fetches (403), so the X refresh was checked against the Wayback Machine snapshot of the
# official URL dated 5 Oct 2026 (UTC). TikTok skipped again: no official deceased-user page could be reached.
DATE="2026-11-02"; CHK="2 Nov 2026"
RD_DEL=("Reddit Help: How do I delete my account?","https://support.reddithelp.com/hc/en-us/articles/204579509-How-do-I-delete-my-account")
RD_DATA=("Reddit Help: How do I request a copy of my Reddit data and information?","https://support.reddithelp.com/hc/en-us/articles/360043048352-How-do-I-request-a-copy-of-my-Reddit-data-and-information")
PN_DEL=("Pinterest Help: Delete or temporarily deactivate your account (incl. deceased person's account)","https://help.pinterest.com/en/article/deactivate-or-close-your-account")
PN_DATA=("Pinterest Help: Download your Pinterest data","https://help.pinterest.com/en/article/download-your-pinterest-data")
PN_REACT=("Pinterest Help: Reactivate your account","https://help.pinterest.com/en/article/reactivate-your-account")
TG_FAQ=("Telegram FAQ: account self-destruction, deleting your account","https://telegram.org/faq")
TG_EXP=("Telegram blog: Chat Export Tool (Telegram Desktop)","https://telegram.org/blog/export-and-more")
AP_SC=("Australia Post: Mail redirection for special circumstances (deceased estates)","https://auspost.com.au/personal/receiving/mail-redirection-and-mail-hold/redirection/special-circumstances")
AP_MR=("Australia Post: Mail redirection","https://auspost.com.au/personal/receiving/mail-redirection-and-mail-hold/redirection")
NSW_CS=("NSW Government: Cancel or transfer services after a death","https://www.nsw.gov.au/family-and-relationships/deaths/after-a-death/cancel-or-transfer-services")
SNSW_ADNS=("Service NSW: Use the Australian Death Notification Service","https://www.service.nsw.gov.au/referral/adns")
AER_C=("Australian Energy Regulator: Useful contacts (retailers, ombudsman schemes)","https://www.aer.gov.au/consumers/resources/useful-contacts")
ERGON=("Ergon Energy Retail: Managing accounts for a deceased estate","https://www.ergon.com.au/retail/residential/account-options/managing-accounts-for-a-deceased-estate")
ENGIE=("ENGIE: Deceased estates and bereavement support","https://engie.com.au/help-centre/policies-and-commitments/deceased-estates-and-bereavement-support")
X_URL="https://help.x.com/en/rules-and-policies/contact-x-about-a-deceased-family-members-account"
CHECKED_AT={u:CHK for _,u in [RD_DEL,RD_DATA,PN_DEL,PN_DATA,PN_REACT,TG_FAQ,TG_EXP,AP_SC,AP_MR,NSW_CS,SNSW_ADNS,AER_C,ERGON,ENGIE]}
CHECKED_AT[X_URL]="2 Nov 2026 (archived copy dated 5 Oct 2026)"

REDDIT=dict(slug="reddit",name="Reddit",cat="platforms",url=RD_DEL[1],
 answer="Reddit doesn't publish any process for deceased users, offers no memorialisation, and its help centre says Reddit administrators can't delete an account on someone's behalf. Deleting an account needs the account's password, and it doesn't remove posts or comments: those stay up unless they're deleted first. Without the login, the only official route is a request through Reddit's help centre.",
 steps=["Keep your Reddit username and password in a password manager with emergency access. Reddit asks for the password to delete an account.",
  "Decide now: should your posts and comments stay up or be removed? Write it in your digital estate plan, because deleting the account alone leaves them public.",
  "Want a copy kept? Request your data at reddit.com/settings/data-request while logged in on a computer. It can take up to 30 days and arrives via your Reddit inbox (or verified email).",
  "After a death, with the login: cancel any Reddit Premium subscription first, because deleting the account doesn't cancel it.",
  "Remove any posts or comments the family wants gone, then delete the account in Account Settings, Advanced, Delete Account. It can't be reactivated and the username becomes unavailable.",
  "Without the login: submit a request through Reddit's help centre (support.reddithelp.com) explaining that the user has died. Reddit doesn't publish what it will do."],
 facts=["No published deceased-user process","Admins can't delete accounts on your behalf","Deleting needs the account password","Deleting the account doesn't delete posts or comments"],
 need=["With the login: the username and password (or access to the linked Google/Apple sign-in, then set a password)","Without it: the username; Reddit publishes no document list, so have the death certificate ready"],
 timeline="After an account is deleted, Reddit says its deletion process commences within 90 days. A data copy request can take up to 30 days to prepare.",
 lost=["The account and username, permanently, once deleted","Nothing public is lost by deleting the account alone: posts and comments remain unless removed first"],
 faqs=[("What happens to my Reddit account when I die?","Nothing automatic. Reddit has no deceased-user or memorialisation process, so the account and its posts stay as they are unless someone with the password deletes them."),
  ("Can Reddit delete a dead person's account?","Reddit's help centre says administrators can't delete an account on someone's behalf. Deletion needs the account's password. Family without it can contact Reddit through its help centre, but no outcome is promised."),
  ("Does deleting a Reddit account delete posts and comments?","No. Reddit says deleting an account doesn't delete posts or comments; remove them first if you want them gone."),
  ("How do I download my Reddit data?","Go to reddit.com/settings/data-request on a computer while logged in and submit the form. Reddit may take up to 30 days and sends a download link to your Reddit inbox, or sometimes your verified email."),
  ("Does deleting the account cancel Reddit Premium?","No. Reddit says to cancel Premium before deleting the account.")],
 sources=[RD_DEL,RD_DATA],related=["/platforms/discord/","/platforms/x-twitter/","/guides/digital-estate-checklist/"])

PINTEREST=dict(slug="pinterest",name="Pinterest",cat="platforms",url=PN_DEL[1],
 answer="Pinterest will delete a deceased family member's account if you contact Pinterest and provide verification, such as an obituary or death certificate. It doesn't memorialise accounts, and it won't give out login or personal information. Once deleted, the account can't be accessed. Only the account holder can download the account's data, so save any boards you want kept while you can still log in.",
 steps=["Note your Pinterest login email in your digital estate plan, and keep the password in a password manager with emergency access.",
  "Want your boards kept? Download your data: Settings, Privacy and data, Request your data, Start request. Pinterest emails a link within 48 hours.",
  "After a death: contact Pinterest through its help centre contact form (help.pinterest.com/contact) and ask for the deceased family member's account to be deleted.",
  "Include verification such as an obituary or death certificate.",
  "With the login, the account can instead be deleted from Settings, Account management, Delete account. The profile is deactivated at once and data deleted after 7 days.",
  "Check it's gone by visiting pinterest.com/username without logging in. Logging in to a deactivated account reactivates it."],
 facts=["Deletion on request with an obituary or death certificate","No memorialisation option","No login or personal information released","Self-deletion: data permanently deleted after 7 days"],
 need=["The person's Pinterest profile or username","Verification such as an obituary or death certificate"],
 timeline="Pinterest publishes no processing time for deceased-account requests. When an account is deleted from settings, the public profile is deactivated immediately and the account and data are permanently deleted after 7 days.",
 lost=["Boards, Pins and the profile, once the account is deleted","Account data, which Pinterest only releases to the verified account holder"],
 faqs=[("What happens to my Pinterest account when I die?","It stays as it is until someone acts. Pinterest will delete a deceased family member's account after you contact it with verification such as an obituary or death certificate."),
  ("Can family get into a dead person's Pinterest?","No. Pinterest says it can't give out any personal or login information, to protect users' privacy."),
  ("Does Pinterest memorialise accounts?","No. Pinterest's help centre only describes deleting a deceased person's account."),
  ("Can family download a deceased person's Pinterest data?","Pinterest says only the account holder can access their data, after verification. Download your own data now if you want boards kept."),
  ("How long until a deleted Pinterest account is gone?","The profile is deactivated immediately and the data is permanently deleted after 7 days. It can be reactivated within those 7 days by logging in.")],
 sources=[PN_DEL,PN_DATA,PN_REACT],related=["/platforms/instagram/","/platforms/facebook/","/platforms/reddit/"])

TELEGRAM=dict(slug="telegram",name="Telegram",cat="platforms",url=TG_FAQ[1],
 answer="Telegram has no deceased-user process or legacy contact. Instead, accounts self-destruct: if an account doesn't come online for the period set in Settings (18 months by default), Telegram deletes it along with all its messages, media and contacts in the Telegram cloud. Secret chats exist only on the original device. To keep anything, export it with Telegram Desktop before it's gone.",
 steps=["Check your self-destruct period in Settings, Privacy and Security, and pick one that gives family time to export what they need.",
  "Keep the phone number, any 2-Step Verification password and the phone's passcode in a password manager with emergency access. Telegram logs in with a code sent to the number or to a logged-in device.",
  "Export chats you want kept: Telegram Desktop has an Export Telegram data tool that saves chats and media offline as HTML or JSON.",
  "Remember that secret chats are device-specific and aren't in the cloud, so they can't be exported from another device.",
  "After a death: if a device is still logged in, family can export chats with Telegram Desktop or delete the account at telegram.org/deactivate (the code arrives in Telegram, not by SMS).",
  "Otherwise, do nothing: the account deletes itself after the self-destruct period. Contacts keep their own copies of messages the person sent them."],
 facts=["No deceased-user process or legacy contact","Inactive accounts self-destruct (18 months by default)","Secret chats exist only on the original device","Export with Telegram Desktop's Export Telegram data tool"],
 need=["Access to a logged-in device, or the phone number and any 2-Step Verification password","Telegram publishes no document-based process for families"],
 timeline="If the account doesn't come online for the self-destruct period (18 months by default, adjustable in Settings), Telegram deletes it with all its cloud data. Deleting an account manually is immediate and irreversible.",
 lost=["All messages, media and contacts in the Telegram cloud when the account self-destructs or is deleted","Secret chats, which never leave the original device","Groups the person created stay, but without a creator (admins keep their rights)"],
 faqs=[("What happens to my Telegram account when I die?","If nobody logs in, it self-destructs after the period set in Settings (18 months by default) and Telegram deletes all its messages, media and contacts. Telegram publishes no process for families."),
  ("Can family get into a dead person's Telegram?","Telegram offers no family access process. Logging in needs a code sent to the phone number or a logged-in device, so plan ahead with a password manager."),
  ("How do I save Telegram chats before they're deleted?","Use Telegram Desktop's Export Telegram data tool, which saves chats and media offline as HTML or JSON. Secret chats are device-specific and can't be exported from another device."),
  ("How do I delete a deceased person's Telegram account?","With access to a logged-in device, delete it at telegram.org/deactivate (the code arrives in Telegram). Otherwise it self-deletes after the self-destruct period."),
  ("Do contacts lose messages when an account is deleted?","No. Telegram says contacts keep their copy of messages the person sent them, and groups the person created keep running.")],
 sources=[TG_FAQ,TG_EXP],related=["/platforms/whatsapp/","/platforms/discord/","/guides/access-deceased-persons-phone-and-accounts/"])

MAIL=("redirect-mail-after-death-australia","How to redirect a deceased person's mail (Australia Post)",
 "Australia Post offers up to 12 months of free mail redirection for a deceased estate. The executor or administrator, or someone legally entitled to deal with the estate, applies in person at any Post Office with a completed mail redirection form, their proof of identity, and an original or certified copy of a document proving their entitlement, such as the grant of probate, letters of administration or the will naming them executor.",
 ["Get a mail redirection form: download Australia Post's PDF or pick up a printed one at the Post Office.",
  "Gather your proof of identity.",
  "Gather proof that you're entitled to deal with the estate, as an original or certified copy of one of these: the grant of probate naming you executor; letters of administration naming you administrator; the death certificate plus an original statutory declaration of your relationship and entitlement; the will naming you executor; or an original statutory declaration giving the deceased's full name, date of death, address and your relationship and entitlement.",
  "Apply in person at any Post Office in Australia. Australia Post says deceased-estate redirections are applied for in person.",
  "Redirect to an address you check often. Bank statements, bills, renewal notices and subscription letters help you find accounts and recurring payments to close, including digital ones.",
  "Need longer than 12 months? Australia Post says its usual rates apply after the free period.",
  "Use the redirected mail to build your list of who to notify, and see our guides to banks, super, telcos and government services."],
 [("Is mail redirection free for a deceased estate?","Yes, for up to 12 months. Australia Post says executors or administrators of an estate may be eligible for free redirection, with normal rates after that."),
  ("Can I redirect a deceased person's mail online?","Australia Post's special circumstances page says to apply in person at any Post Office, with the form, your ID and proof of entitlement."),
  ("Do I need probate to redirect mail?","Not necessarily. Australia Post also accepts the will naming you executor, or the death certificate with a statutory declaration, or a statutory declaration with the required details. Originals or certified copies only."),
  ("What should the statutory declaration say?","Australia Post lists the deceased's full name and date of death, the address mail is redirected from, your relationship to the deceased, and that you're legally entitled to deal with the estate."),
  ("Why redirect a deceased person's mail?","Letters reveal accounts, bills and subscriptions the family may not know about, and stop mail piling up at an empty home.")],
 [AP_SC,AP_MR],
 ["Up to 12 months free for deceased estates","Apply in person at any Post Office","Needs the form, your ID and proof of entitlement","Originals or certified copies only"],
 ["/guides/australian-digital-estate-guide/","/guides/cancel-utilities-after-death-australia/","/guides/bank-accounts-after-death-australia/","/guides/mygov-centrelink-medicare-ato-after-death/"])

UTIL=("cancel-utilities-after-death-australia","How to cancel or transfer electricity, gas and other services after a death (Australia)",
 "Contact each provider named on the bills (electricity, gas, water, phone, internet). Energy retailers can put the account into the \"Estate of\", transfer it to a joint holder or new occupant, keep temporary supply on, or close it and send a final bill to the estate. You usually need a certified death certificate and the account details. The free Australian Death Notification Service can notify many participating banks, telcos and utilities at once once the death is registered.",
 ["Find the providers: the retailer's contact details are on each bill. Redirected mail and bank statements help you spot accounts.",
  "Once a death certificate has been issued by the state or territory registry, use the free Australian Death Notification Service to notify participating banks, phone and internet providers and utility companies in one go. They contact you within 10 working days.",
  "Call energy retailers directly too. Decide whether anyone still needs power or gas at the property.",
  "Keeping supply on: a joint account holder can usually have the account moved into their name, or a new occupant can open a new account. ENGIE and Ergon both describe this.",
  "Leaving the property empty for now: ask for the account to be kept as the \"Estate of\" or for temporary supply. Ergon says this needs the death certificate and a letter from the executor or administrator.",
  "Supply no longer needed: ask the retailer to close the account (and disconnect supply if appropriate) and send the final bill to the estate.",
  "Have ready: the deceased's full name, address, date of birth and date of death, the account number, and the executor's or solicitor's details.",
  "Stuck? Each state and territory has a free energy (and in most states water) ombudsman scheme; the AER lists them all."],
 [("Who can close or transfer a deceased person's energy account?","Usually the executor or next of kin. ENGIE, for example, accepts a primary or joint account holder, the executor, the deceased's solicitor, or a trustee or business partner."),
  ("Will the power be cut off when the account holder dies?","Not automatically. Retailers can keep supply on under the \"Estate of\", transfer the account, or arrange temporary supply until the property is sorted."),
  ("What documents do I need?","NSW Government guidance says you'll usually need a certified copy of the death certificate and the account details, plus proof of identity to transfer a service into your name. Some retailers also ask for an executor's letter."),
  ("What is the Australian Death Notification Service?","A free online service that lets you tell multiple participating organisations (banks, telcos, utilities and others) about a death in a single notification, after the death has been registered. Organisations then contact you within 10 working days."),
  ("Who pays the final energy bill?","Retailers send the final bill to the estate. Talk to the executor before paying it personally."),
  ("Where can I complain about an energy retailer?","To your state or territory energy ombudsman, which is free. For example: Energy and Water Ombudsman Queensland 1800 662 837, Energy & Water Ombudsman NSW 1800 246 545, Energy and Water Ombudsman Victoria 1800 500 509.")],
 [NSW_CS,SNSW_ADNS,AER_C,ERGON,ENGIE],
 ["Contact each retailer; details are on the bill","Options: transfer, \"Estate of\", temporary supply or close","Usually needs a certified death certificate","ADNS notifies many providers at once"],
 ["/guides/redirect-mail-after-death-australia/","/guides/mobile-phone-number-after-death-australia/","/guides/bank-accounts-after-death-australia/","/guides/australian-digital-estate-guide/"])

NEW_PLAT=[REDDIT,PINTEREST,TELEGRAM]
NEW_GUIDES=[MAIL,UTIL]
NEW_PATHS=[f"/platforms/{p['slug']}/" for p in NEW_PLAT]+[f"/guides/{g[0]}/" for g in NEW_GUIDES]
REFRESHED=["/platforms/x-twitter/"]
SHORT=[("What happens to my Reddit account when I die?","Reddit has no deceased-user process and admins can't delete accounts on your behalf; deletion needs the password and doesn't remove posts or comments.","/platforms/reddit/"),
("What happens to my Pinterest when I die?","Pinterest deletes a deceased family member's account on request with an obituary or death certificate; no memorialisation and no login details released.","/platforms/pinterest/"),
("What happens to my Telegram account when I die?","No deceased-user process; inactive accounts self-destruct after the set period (18 months by default) with all cloud data. Export with Telegram Desktop first.","/platforms/telegram/"),
("How do I redirect a deceased person's mail in Australia?","Australia Post gives executors/administrators up to 12 months free redirection; apply in person with the form, your ID and proof of entitlement (probate, will or statutory declaration).","/guides/redirect-mail-after-death-australia/"),
("How do I cancel electricity and gas after a death in Australia?","Call each retailer on the bills to transfer, keep as \"Estate of\", or close with a final bill to the estate; the Australian Death Notification Service can notify many providers at once.","/guides/cancel-utilities-after-death-australia/")]

def _add(lst,s):
    if s not in lst: lst.append(s)
def pre(enrich,growth,pack2):
    enrich.NEWP.extend(NEW_PLAT)
    enrich.GUIDE_NEW.extend(NEW_GUIDES)
    growth.SHORT.extend(SHORT)
    for p in NEW_PATHS+REFRESHED: pack2.LASTMOD[p]=DATE; pack2.REV[p]=CHK
    for p in NEW_PATHS: pack2.PUBLISHED[p]=DATE
    pack2.CHECKED_AT.update(CHECKED_AT)
    x=enrich.P["x-twitter"]
    x["extra"]=x.get("extra",[])+[("What if the X user is incapacitated, not deceased?","X can work with a person authorised to act for the user to deactivate the account. X then asks for information about the user, a copy of your ID, a copy of the account holder's ID and a Power of Attorney authorising you.")]
    _add(x["related"],"/platforms/reddit/")
    for k,new in (("instagram","/platforms/pinterest/"),("facebook","/platforms/pinterest/"),("whatsapp","/platforms/telegram/")):
        if k in enrich.P: _add(enrich.P[k].setdefault("related",[]),new)
    for p in enrich.NEWP:
        if p["slug"]=="discord": _add(p["related"],"/platforms/reddit/"); _add(p["related"],"/platforms/telegram/")
        if p["slug"]=="whatsapp": _add(p["related"],"/platforms/telegram/")
    for i,x in enumerate(enrich.GUIDE_NEW):
        s,t,an,st,f,src,tl,rel=x
        add=[]
        if s in ("australian-digital-estate-guide","what-to-do-when-someone-dies-digital-checklist","bank-accounts-after-death-australia","mygov-centrelink-medicare-ato-after-death","mobile-phone-number-after-death-australia"):
            add=["/guides/redirect-mail-after-death-australia/","/guides/cancel-utilities-after-death-australia/"]
        add=[a for a in add if a not in rel and a!=f"/guides/{s}/"]
        if add: enrich.GUIDE_NEW[i]=(s,t,an,st,f,src,tl,rel+add)
    growth.EXTRA["australian-digital-estate-guide"]=growth.EXTRA.get("australian-digital-estate-guide","").replace("bank accounts</a>","bank accounts</a> · <a href='/guides/redirect-mail-after-death-australia/'>mail redirection</a> · <a href='/guides/cancel-utilities-after-death-australia/'>utilities</a>")
