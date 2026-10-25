# Content pack 3 (26 Oct 2026, AEST). Every fact here was checked against the cited official page on 26 Oct 2026.
# Discord's help centre blocks automated fetches (Cloudflare), so its article was read via the Wayback snapshot of the
# official URL dated 9 Oct 2026 (article updated 21 Feb 2024). Banking Code of Practice: ABA PDF, effective 28 Feb 2025.
DATE="2026-10-26"; CHK="26 Oct 2026"
DISC=("Discord Support: Deceased or Incapacitated Users","https://support.discord.com/hc/en-us/articles/19872987802263--Deceased-or-Incapacitated-Users")
YAH=("Yahoo Help: Options available if a Yahoo account owner passes away","https://help.yahoo.com/kb/account/sln2021.html")
SP_CLOSE=("Spotify Support: Closing your account and deleting your data","https://support.spotify.com/au/article/how-can-i-close-my-spotify-account/")
SP_CANCEL=("Spotify Support: How to cancel Premium plans","https://support.spotify.com/au/article/cancel-premium/")
CODE=("Australian Banking Association: Banking Code of Practice (Part B8 Deceased estates, PDF)","https://www.ausbanking.org.au/wp-content/uploads/2024/06/Banking-Code-of-Practice_2025.pdf")
CBA=("CommBank: Deceased estate and settlement","https://www.commbank.com.au/support/deceased-estates.html")
NAB=("NAB: What happens after you've notified us of a deceased customer","https://www.nab.com.au/help-support/losing-loved-ones/steps-after-notification")
MS_URL="https://support.microsoft.com/en-us/accounts-billing/manage/accessing-outlook-com-onedrive-and-other-microsoft-services-when-someone-has-died"
CHECKED_AT={u:CHK for _,u in [DISC,YAH,SP_CLOSE,SP_CANCEL,CODE,CBA,NAB]+[("",MS_URL)]}

DISCORD=dict(slug="discord",name="Discord",cat="platforms",url=DISC[1],
 answer="Discord won't give anyone access to a deceased person's account or share its data, and it has no memorialise or transfer option. Family can ask Discord Support to delete the account: write from the account's own email, or send proof of death, proof of relationship and photo ID. Accounts unused for 2 years or more may be deleted automatically.",
 steps=["Keep the email address linked to your Discord account in a password manager with emergency access. Discord says whoever controls that email can reset the password.",
  "Write your Discord username and your wishes (delete or leave it) in your digital estate plan.",
  "After a death, with access to the account: User Settings, My Account, Account Removal, Delete Account, then enter the password.",
  "Writing from the account's own email: send Discord Support the sentence \"I confirm that I would like to delete the account associated with [email].\"",
  "Writing from another email: send the account email and username, a death certificate or coroner's report, proof of relationship and your photo ID, plus \"I request to have the account associated with [email and/or username] deleted.\"",
  "Billing questions (such as Nitro): use Discord's support form and choose Billing."],
 facts=["No account access or data for family","No memorialise or transfer option","Deletion on request with documents","Unused for 2+ years: may be deleted automatically"],
 need=["The account's email address and Discord username","From another email: death certificate or coroner's report","Proof of relationship: marriage licence, birth certificate, will, estate letter or power of attorney","Your valid photo ID or passport (scans or photocopies; you can black out birthdays and addresses but keep names visible)"],
 timeline="Discord publishes no processing time for deletion requests. Accounts not used for 2 years or more may be scheduled for deletion, and the deletion proceeds automatically as long as no one logs in.",
 lost=["Messages and data in the account, because Discord doesn't release them to family","Everything in the account once it's deleted"],
 faqs=[("Can family get into a dead person's Discord account?","Discord says it can't provide access, share data or make changes. Whoever has the account's email can reset the password, but check with the executor before using it."),
  ("Does Discord memorialise accounts?","No. Discord says it doesn't currently have a feature to memorialise or transfer accounts."),
  ("How do I delete a deceased person's Discord account?","Delete it from User Settings if you can sign in, or contact Discord Support. From another email, include the account email and username, a death certificate, proof of relationship, your photo ID and an explicit deletion statement."),
  ("Do inactive Discord accounts get deleted?","Discord says accounts unused for 2 years or more may be scheduled for deletion, with a warning sent to the account's email or phone first.")],
 sources=[DISC],related=["/platforms/snapchat/","/platforms/steam/","/guides/access-deceased-persons-phone-and-accounts/"])

YAHOO=dict(slug="yahoo-mail",name="Yahoo Mail",cat="platforms",url=YAH[1],
 answer="Yahoo won't hand over a password, and accounts can't be transferred, even after death. For US accounts, family can ask Yahoo to close the account or stop billing with a US death certificate. Getting the content needs a US court order. Yahoo's help page says it applies to US accounts only and it won't respond to non-US requests.",
 steps=["Store your Yahoo password and recovery details in a password manager with emergency access, because Yahoo won't release them.",
  "Forward or export important emails and attachments you'd want kept.",
  "List the account and any paid Yahoo services in your digital estate plan.",
  "After a death (US accounts): use Yahoo's deceased-user forms to close the account or cancel billing and premium services, uploading a US-issued death certificate.",
  "Need the emails? Yahoo requires a US court order meeting its requirements, plus the death certificate and your government ID. Get legal advice.",
  "Outside the US: Yahoo's page says it won't accept these requests, so check Yahoo Help for your region and stop payments through the bank."],
 facts=["No passwords or login details released","Accounts are non-transferable","US accounts: closure needs a US death certificate","Content: US court order required"],
 need=["To close or stop billing: the person's full name, Yahoo email, date of death and a US-issued death certificate","For content: also your government ID and a US court order"],
 timeline="Yahoo publishes no processing time. It reviews each request and contacts you if it needs more information.",
 lost=["Email content, unless a court order succeeds","Everything in the account once it's closed"],
 faqs=[("Can I get into a dead person's Yahoo Mail?","Yahoo says it can't provide passwords or login details, and accounts are non-transferable. Content requests need a US court order."),
  ("How do I close a deceased person's Yahoo account?","For US accounts, submit Yahoo's closure form with the person's name, Yahoo email, date of death and a US-issued death certificate."),
  ("What if the person lived outside the US?","Yahoo's page says it applies to US accounts only and won't respond to non-US requests. Check Yahoo Help for your region, and stop charges through the bank."),
  ("How do I stop Yahoo charging a dead person's card?","For US accounts, use Yahoo's form to suspend or cancel billing and premium services. Without a death certificate, Yahoo says to call Yahoo Customer Service on 866-265-4025.")],
 sources=[YAH],related=["/platforms/google-gmail/","/platforms/microsoft-outlook/","/guides/digital-estate-checklist/"])

SPOTIFY=dict(slug="spotify",name="Spotify",cat="platforms",url=SP_CLOSE[1],
 answer="Spotify doesn't publish a dedicated process for deceased users. With the login, family can cancel Premium (it runs to the next billing date, then switches to free) and close the account; after a 7-day reactivation window, Spotify starts deleting the data. Without the login, contact Spotify Support. If Premium is billed through a phone or internet provider, cancel with that provider.",
 steps=["Note your Spotify login email in your digital estate plan, and keep the password in a password manager with emergency access.",
  "Want playlists kept? Tell family which ones, before anyone closes the account.",
  "After a death, with the login: go to Manage your plan and select Cancel subscription. Premium stays until the next billing date, then the account switches to free.",
  "Then close the account with 'Close your account and delete your data'. Spotify emails a link that can reactivate it within 7 days; after that, deletion begins.",
  "No option to change the plan? It's billed through a partner such as a mobile or internet provider. Use the contact link under Payment on the account page.",
  "Without the login: contact Spotify Support through its help site and explain the account holder has died. Stop the card or bank payment through the bank too."],
 facts=["No dedicated deceased-user process published","Cancelled Premium runs to the next billing date","Closure: 7-day reactivation window, then deletion","Partner-billed plans are cancelled with the partner"],
 need=["With the login: nothing else","Without it: the account's email; Spotify publishes no document list, so have the death certificate ready"],
 timeline="Cancelled Premium lasts until the next billing date. After closing, the account can be reactivated for 7 days; then deletion begins. The same email can be used for a new account 14 days after closing.",
 lost=["Purchased audiobooks and future live tickets, when the account is closed","Playlists and saved music, once the data is deleted"],
 faqs=[("How do I cancel a dead person's Spotify Premium?","With the login, go to Manage your plan and select Cancel subscription. Without it, contact Spotify Support and stop the payment through the bank."),
  ("Does closing a Spotify account delete everything?","Yes, after 7 days. Spotify emails a reactivation link that works for 7 days, then starts deleting the data. Purchased audiobooks and future live tickets are lost."),
  ("What about a Spotify Family plan?","If the plan manager dies, cancelling moves any managed accounts to the free plan. Members keep their own accounts and playlists."),
  ("Why can't I cancel on the account page?","Spotify says that means the plan is with a partner company, like a mobile or internet provider. Find their contact link under Payment.")],
 sources=[SP_CLOSE,SP_CANCEL],related=["/platforms/amazon-kindle/","/platforms/youtube/","/guides/bank-accounts-after-death-australia/"])

BANK=("bank-accounts-after-death-australia","What happens to bank accounts when someone dies? (Australia)",
 "Once you tell an Australian bank about a death, it secures accounts in the person's sole name: online banking is switched off and debits are restricted. Joint account holders can usually keep using joint accounts. Under the Banking Code of Practice, banks act on a valid executor or next-of-kin instruction within 14 business days and can release money for funeral costs before probate.",
 ["Tell each bank as soon as practicable: online, by phone, in a branch, or through the Australian Death Notification Service once a death certificate exists.",
  "Expect sole-name accounts to be secured. Internet and app banking logins are removed, cards are cancelled and debits are restricted. Direct credits can still arrive.",
  "Find recurring payments. CommBank says it can give the estate representative a list of regular payments on the deceased's debit card and copies of statements; ask your bank for the same. Cancel subscriptions with each provider.",
  "Prove you can act. Banks usually want your ID plus a verified copy of the will (executor) or the death certificate naming you as next of kin.",
  "Need money for the funeral? Before probate, a representative can ask the bank to pay or reimburse funeral costs or probate filing fees, with an invoice or receipt.",
  "Ask whether a grant is needed. Each bank decides; NAB lists a $100,000 total-in-credit threshold among the cases where it needs a Grant of Representation.",
  "With the bank's documents in hand, sign its forms to close accounts and release funds. You can open a deceased estate account if the bank offers one.",
  "Planning ahead: list your banks and accounts (not passwords) in your estate inventory, and tell your executor where it is."],
 [("Can I use a joint account after my partner dies?","Usually yes. The Banking Code says a joint account holder may keep operating the account under its terms, and CommBank and NAB say joint accounts in credit continue."),
  ("How long do banks take to act?","Under the Banking Code, once verified documents are received, banks act on a valid estate representative's instruction within 14 business days. Finalising an estate can take weeks to months; CommBank says a couple of weeks to a few months."),
  ("Can the bank pay for the funeral before probate?","Yes. The Banking Code lets a representative ask for funds to pay or reimburse funeral expenses or probate filing fees, with proof of the invoice or receipt. NAB covers these up to $15,000."),
  ("Will direct debits keep coming out?","Banks restrict debits on sole accounts once notified, but some card payments may still go through. Check statements and cancel each subscription with the provider."),
  ("Can I use their online banking to pay bills?","No. Banks remove the deceased's internet and app banking logins after notification. Pay bills through the estate process instead."),
  ("Do I need probate to close a bank account?","Not always. The bank tells you if it needs a Grant of Probate or Letters of Administration; if not, it explains how to finalise the estate.")],
 [CODE,CBA,NAB],
 ["Sole accounts secured once the bank is told","Joint accounts usually continue","Instructions actioned within 14 business days","Funeral costs payable before probate"],
 ["/guides/australian-digital-estate-guide/","/guides/superannuation-after-death-australia/","/guides/mygov-centrelink-medicare-ato-after-death/"])

NEW_PLAT=[DISCORD,YAHOO,SPOTIFY]
NEW_PATHS=[f"/platforms/{p['slug']}/" for p in NEW_PLAT]+[f"/guides/{BANK[0]}/"]
REFRESHED=["/platforms/microsoft-outlook/"]
SHORT=[("What happens to my Discord account when I die?","Discord gives no access or data and has no memorialisation; family can request deletion with documents, and accounts unused 2+ years may be deleted.","/platforms/discord/"),
("What happens to my Yahoo Mail when I die?","Yahoo releases no passwords and accounts are non-transferable; US accounts can be closed with a US death certificate, content needs a US court order.","/platforms/yahoo-mail/"),
("How do I cancel a deceased person's Spotify?","Cancel Premium and close the account with the login (7-day reactivation window), or contact Spotify Support; partner-billed plans are cancelled with the partner.","/platforms/spotify/"),
("What happens to bank accounts when someone dies in Australia?","Sole accounts are secured once the bank is told, joint accounts usually continue, and banks act on valid estate instructions within 14 business days.","/guides/bank-accounts-after-death-australia/")]

def pre(enrich,growth,pack2):
    enrich.NEWP.extend(NEW_PLAT)
    enrich.GUIDE_NEW.append(BANK)
    growth.SHORT.extend(SHORT)
    for p in NEW_PATHS+REFRESHED: pack2.LASTMOD[p]=DATE; pack2.REV[p]=CHK
    for p in NEW_PATHS: pack2.PUBLISHED[p]=DATE
    pack2.CHECKED_AT.update(CHECKED_AT)
    for k,new in (("microsoft-outlook","/platforms/yahoo-mail/"),("google-gmail","/platforms/yahoo-mail/")):
        r=enrich.P[k]["related"]
        if new not in r: r.append(new)
    for p in enrich.NEWP:
        if p["slug"] in ("snapchat","steam") and "/platforms/discord/" not in p["related"]: p["related"].append("/platforms/discord/")
        if p["slug"]=="amazon-kindle" and "/platforms/spotify/" not in p["related"]: p["related"].append("/platforms/spotify/")
    for i,x in enumerate(enrich.GUIDE_NEW):
        s,t,an,st,f,src,tl,rel=x
        if s in ("australian-digital-estate-guide","what-to-do-when-someone-dies-digital-checklist","mygov-centrelink-medicare-ato-after-death") and "/guides/bank-accounts-after-death-australia/" not in rel:
            enrich.GUIDE_NEW[i]=(s,t,an,st,f,src,tl,rel+["/guides/bank-accounts-after-death-australia/"])
    growth.EXTRA["australian-digital-estate-guide"]=growth.EXTRA.get("australian-digital-estate-guide","").replace("super after death</a>","super after death</a> · <a href='/guides/bank-accounts-after-death-australia/'>bank accounts</a>")
