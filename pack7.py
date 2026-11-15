# Content pack 7 (16 Nov 2026, AEST). Every fact here was checked against the cited official page on 16 Nov 2026.
# Skipped again: TikTok and Twitch (help pages are script-rendered; no readable content even with headless Chrome),
# Origin Energy, eBay, Wise, Uber, Airbnb, Ancestry (deceased-account help pages returned no readable content or 403/404),
# deathnotification.gov.au (JavaScript-only app, no readable content), Qld death certificate fee (not stated on the page).
# Refreshed: myGov/Centrelink/Medicare/ATO guide gains the passport and electoral roll step (myGov checklist and AEC FAQ, re-verified).
DATE="2026-11-16"; CHK="16 Nov 2026"
GH_DEC=("GitHub Docs: GitHub Deceased User Policy","https://docs.github.com/en/site-policy/other-site-policies/github-deceased-user-policy")
GH_SUCC=("GitHub Docs: Personal repository access and collaboration (About successors)","https://docs.github.com/en/repositories/creating-and-managing-repositories/access-to-repositories")
GH_INV=("GitHub Docs: Maintaining ownership continuity of your personal account's repositories","https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/maintaining-ownership-continuity-of-your-personal-accounts-repositories")
GH_BAK=("GitHub Docs: Backing up a repository","https://docs.github.com/en/repositories/archiving-a-github-repository/backing-up-a-repository")
PR_EA=("Proton Support: Emergency access","https://proton.me/support/emergency-access")
PR_IN=("Proton Support: Inactive accounts","https://proton.me/support/inactive-accounts")
PR_RP=("Proton Support: Recovery phrase","https://proton.me/support/recovery-phrase")
PR_TOS=("Proton: Terms of service (inactive accounts)","https://proton.me/legal/terms")
QF_TC=("Qantas Frequent Flyer: Terms and conditions (clauses 2, 8.5, 9.2)","https://www.qantas.com/en-au/frequent-flyer/join/terms-conditions")
VA_TC=("Velocity Frequent Flyer: Terms and conditions (clauses 1.2, 3.4)","https://www.velocityfrequentflyer.com/member-support/terms-conditions")
VA_DEC=("Velocity: Close the account of a deceased Velocity member","https://www.velocityfrequentflyer.com/member-support/close-the-account-of-a-deceased-velocity-member")
MG_CHK=("myGov: Death of someone close to you checklist","https://my.gov.au/en/services/health-and-disability/when-someone-close-to-you-dies/death-of-someone-close-to-you-checklist")
APO_REF=("Australian Passport Office: Refunds","https://www.passports.gov.au/help/refunds")
AEC_FAQ=("Australian Electoral Commission: Enrolment FAQs (a relative or friend has died)","https://www.aec.gov.au/faqs/enrolment.htm")
AEC_FORM=("AEC: Notification of a relative who has died (online form)","https://formupload.aec.gov.au/Form?FormId=Notificationdeath")
CHECKED_AT={u:CHK for _,u in [GH_DEC,GH_SUCC,GH_INV,GH_BAK,PR_EA,PR_IN,PR_RP,PR_TOS,QF_TC,VA_TC,VA_DEC,MG_CHK,APO_REF,AEC_FAQ,AEC_FORM]}

GITHUB=dict(slug="github",name="GitHub",cat="platforms",url=GH_DEC[1],
 answer="GitHub says it can work with an authorised person to decide what happens to a deceased user's account content. Next of kin, a pre-designated successor or another authorised individual (GitHub says this could include a collaborator or business partner) contacts GitHub Support, for example to transfer public repositories or cancel billing. If you appoint a successor in advance, they can archive or transfer your public repositories after presenting a death certificate and waiting 7 days, or an obituary and waiting 21 days. Successors can't log into your account.",
 steps=["Invite a successor: click your profile picture, then Settings, then Account. Under 'Successor settings', type their username, full name or email, select them and click Add successor. They need a GitHub account and show as 'Pending' until they agree.",
  "Back up what matters yourself. GitHub's docs describe a mirror clone (git clone --mirror) that keeps the full revision history, plus git lfs fetch --all for Large File Storage objects; wikis can be cloned the same way. Store the archives on an external drive or cloud storage.",
  "Write down your GitHub username, which repositories matter (especially private ones, because GitHub's listed successor permissions cover public repositories) and whether each should be archived, transferred or deleted.",
  "After a death: the successor, next of kin or other authorised person opens the GitHub Support portal, clicks Contact us and gives their name and contact details, the deceased's name and GitHub username, their relationship (and, if a designated successor, their own username) and the action they want.",
  "Expect GitHub to ask for more: a copy of your photo ID, a copy of the death certificate and documents showing you're authorised to act for the account.",
  "If you're the appointed successor, you can manage the public repositories 7 days after presenting a death certificate, or 21 days after presenting an obituary."],
 facts=["Successors can archive or transfer public repositories","Successors cannot log into your account","Successor wait: 7 days with a death certificate, 21 days with an obituary","Requests go through the GitHub Support portal"],
 need=["Your name and contact information","The deceased's name and GitHub username","Your relationship to them, and whether you're their designated successor (with your own GitHub username)","The action you want, such as transferring public repositories or cancelling billing","If GitHub asks: photo ID, a copy of the death certificate and proof you're authorised to act"],
 timeline="An appointed successor can manage public repositories 7 days after presenting a death certificate, or 21 days after presenting an obituary. GitHub publishes no processing time for other requests and may follow up for more information.",
 lost=["Account login: GitHub says successors cannot log into the account","Private repositories you haven't backed up or shared: GitHub's successor permissions only list public repositories, so keep your own copies"],
 faqs=[("What happens to my GitHub account when I die?","GitHub works with an authorised person, such as next of kin or a successor you appointed, to decide what happens to the account's content. They contact GitHub Support with the deceased's username and the action they want, such as transferring public repositories or cancelling billing."),
  ("What can a GitHub successor do?","Archive your public repositories, transfer them to their own personal account, or transfer them to an organization where they can create repositories. Successors cannot log into your account."),
  ("How long does a GitHub successor have to wait?","7 days after presenting a death certificate, or 21 days after presenting an obituary."),
  ("Who can contact GitHub about a deceased user?","Next of kin, a pre-designated successor or another authorised individual, which GitHub says could include a collaborator or business partner. GitHub may ask for photo ID, a death certificate and proof of authority."),
  ("How do I back up my GitHub repositories?","GitHub's docs describe a mirror clone (git clone --mirror) that keeps the revision history, plus git lfs fetch --all for Large File Storage objects. Compress the clone and store it somewhere safe, such as an external drive or cloud storage.")],
 sources=[GH_DEC,GH_SUCC,GH_INV,GH_BAK],related=["/platforms/microsoft-outlook/","/platforms/google-gmail/","/best/best-password-managers-emergency-access/","/guides/what-to-do-when-someone-dies-digital-checklist/"])

PROTON=dict(slug="proton-mail",name="Proton Mail",cat="platforms",url=PR_EA[1],
 answer="Proton's built-in route is Emergency Access, which you set up in advance. On any paid Proton plan you can choose up to five emergency contacts, each with a Proton Mail address, who can request access to your account if you die or are incapacitated. Access is granted automatically after the waiting period you choose (1 to 30 days) unless you deny it. Proton's help pages describe no other way for family to get in. Free accounts inactive for more than 24 months could be deleted, along with emails, files and passwords.",
 steps=["Check your plan: Proton says Emergency Access is available on all paid Proton plans, and both you and your contact must have a Proton Mail address.",
  "Add a contact: sign in at mail.proton.me, open Settings, select Recovery, scroll to Emergency access and click Add emergency contact. Enter their Proton Mail address, choose a wait time (30, 14, 7, 3, 2 or 1 day) and confirm with your password. You can add up to five.",
  "Create a recovery phrase too (Settings, Recovery, Recovery phrase, Create recovery phrase) and keep the PDF outside Proton, for example printed and stored with your important documents. Proton says not to keep it in Proton Drive or Proton Pass, because you couldn't reach them if locked out.",
  "Record in your digital estate plan your Proton address, your plan, and who your emergency contacts are.",
  "After a death: the emergency contact signs into their own Proton account, opens Settings, Recovery, Emergency access, finds the person under 'People who trust me' and clicks Request access.",
  "Once the wait time ends, they click Access account, enter their own password and choose Switch account."],
 facts=["Emergency Access: up to 5 contacts, on all paid plans","You and your contact both need a Proton Mail address","Wait time 1 to 30 days; Proton notifies you so you can deny it","Free accounts inactive over 24 months could be deleted"],
 need=["Your own Proton Mail account, with you added as their emergency contact","Your own Proton password, to switch into their account once access is granted"],
 timeline="Access is granted automatically at the end of the waiting period the account owner chose (30, 14, 7, 3, 2 or 1 day), or sooner if they approve it. For free accounts, Proton says accounts inactive for more than 24 months could be deleted and it sends reminder emails 30, 15 and 7 days before the scheduled deletion. Proton says it never deletes paid accounts for inactivity.",
 lost=["Everything in a deleted account: Proton says deletion permanently removes emails, contacts, calendars, passwords and files","The email address itself: Proton says deleted addresses generally can't be recovered"],
 faqs=[("What happens to my Proton Mail account when I die?","Unless you set up Emergency Access, Proton's help pages describe no way for family to get in. With it, a contact you chose can request access and gets it automatically after the waiting period you set. Free accounts inactive for more than 24 months could be deleted."),
  ("Is Proton Emergency Access free?","No. Proton says it's available on all paid Proton plans. You and your emergency contact must both have a Proton Mail address."),
  ("Can my emergency contact use a Gmail or Outlook address?","No. Proton says the emergency contact must have a Proton Mail email address."),
  ("Will Proton delete a free account after the owner dies?","It can. Proton says free accounts inactive for more than 24 months could be deleted, with reminder emails 30, 15 and 7 days before. Its inactive account policy doesn't apply to paid plans."),
  ("What is a Proton recovery phrase?","A 12-word, one-time backup password that lets the account holder reset their password and recover encrypted data. Keep it somewhere safe outside Proton. Emergency Access is Proton's feature for giving someone else access.")],
 sources=[PR_EA,PR_IN,PR_RP,PR_TOS],related=["/tools/proton-pass/","/platforms/google-gmail/","/platforms/yahoo-mail/","/best/best-password-managers-emergency-access/"])

FF=("frequent-flyer-points-after-death-australia","What happens to Qantas and Velocity frequent flyer points when someone dies?",
 "The points don't have to be lost. Qantas: the executor or administrator can ask Qantas in writing, within 12 months of the death, to transfer the unexpired Qantas Points to one eligible family member. Qantas closes the account when told of the death and Status Credits expire. Velocity: the executor or administrator can ask Velocity to transfer the Points to another Velocity account, redeem them, or both. There's no fixed deadline, but unused Points keep expiring, so act quickly. Status and Status Credits are forfeited.",
 ["Find the membership numbers: check the person's cards, the airline apps, statements and emails. Note them in your own digital estate plan too.",
  "Qantas: the executor or administrator writes to Qantas asking it to transfer the deceased member's unexpired Qantas Points to one eligible family member. The request must be received within 12 months of the date of death.",
  "Qantas may ask for evidence of the death, for example the grant of probate or letters of administration, and any other information it reasonably needs.",
  "Check the recipient's Qantas account is active. Transferred points take the same expiry date as the other points in that account, and Qantas Points expire at the end of the 18th consecutive month without earning or redeeming.",
  "Qantas closes the deceased member's account once notified of the death. Status Credits can't be transferred and expire on death.",
  "Velocity: email the address for the member's status (platinum@, gold@, silver@ or red@velocityfrequentflyer.com) with their Velocity number, their full name as on the account and the death certificate.",
  "Ask Velocity to transfer the Points to another Velocity account or redeem them. Velocity's terms say executors should tell it as soon as possible because unused Points continue to expire, and the person receiving a transfer must be a Velocity member.",
  "Plan to use inherited Velocity Points. Velocity treats points received as inheritance as a Short Term Activity, which only moves the recipient's Points Expiry Date to the end of the following month if that's later than their current date.",
  "Status, Status Credits and other member benefits can't be passed on in either program."],
 [("Can you inherit Qantas Frequent Flyer points?","Yes, through the estate. The executor or administrator can ask Qantas in writing to transfer the deceased member's unexpired points to one eligible family member, within 12 months of the death. Qantas may ask for the grant of probate or letters of administration."),
  ("Who counts as an eligible family member for Qantas?","A husband or wife, domestic or de facto partner, parent or step-parent, child (including foster and step-children), brother or sister (including half-siblings), grandparent, grandchild, son- or daughter-in-law, brother- or sister-in-law, father- or mother-in-law, uncle or aunt, nephew or niece, or first cousin."),
  ("Is there a deadline to claim frequent flyer points after a death?","Qantas: the request must be received within 12 months of the date of death. Velocity sets no fixed deadline, but its terms say unused Points continue to expire, so tell it as soon as possible."),
  ("Can Velocity points go to someone who isn't family?","Velocity's terms let executors or administrators ask for the Points to be transferred to 'another Velocity account'. Unlike Qantas's clause, that wording isn't limited to family members. The recipient must be a Velocity member."),
  ("Do status and Status Credits transfer after a death?","No. Qantas Status Credits expire on the member's death, and Velocity forfeits Status Credits, Status and other member benefits once it's notified of the death."),
  ("How do I tell Velocity a member has died?","Email the address for their status tier (platinum@, gold@, silver@ or red@velocityfrequentflyer.com) with their Velocity number, full name as on the account and the death certificate. Velocity will explain the next steps for a Points transfer.")],
 [QF_TC,VA_TC,VA_DEC],
 ["Qantas: executor's written request within 12 months","Qantas: transfer to one eligible family member","Velocity: transfer or redeem; act fast, points keep expiring","Status and Status Credits can't be passed on"],
 ["/guides/australian-digital-estate-guide/","/guides/death-certificate-australia/","/guides/what-to-do-when-someone-dies-digital-checklist/","/guides/bank-accounts-after-death-australia/"])

PP=("passport-electoral-roll-after-death-australia","Cancel a passport and remove someone from the electoral roll after a death (Australia)",
 "To cancel an Australian passport after the holder dies, take the passport and the death certificate to your local Australia Post office, as myGov's death checklist advises. The Australian Passport Office doesn't refund any unused validity. You don't need to tell the Australian Electoral Commission (AEC), because Births, Deaths and Marriages registries send it death information, but you can use the AEC's online 'Notification of a relative who has died' form to ask for the name to be removed from the roll.",
 ["Get the death certificate first. The funeral director usually orders it; see our death certificate guide.",
  "Passport: take the person's passport and the death certificate to your local Australia Post office to cancel it.",
  "Don't expect a refund. The Australian Passport Office says it doesn't refund portions of application fees, so the unused part of a deceased holder's passport isn't refunded.",
  "Electoral roll: you don't have to do anything. The AEC says Births, Deaths and Marriages registries give it information about people who have died.",
  "To tell the AEC yourself, use its online 'Notification of a relative who has died' form. It asks for your name, relationship, email and phone, and the person's name, date of birth, address and date of death. The form warns that giving false or misleading information is a serious offence.",
  "myGov: you don't need to close their account. myGov says it closes automatically after not being used.",
  "Tell Services Australia and the ATO separately; our myGov, Centrelink, Medicare and ATO guide covers both."],
 [("How do I cancel a deceased person's passport in Australia?","Take the passport and the death certificate to your local Australia Post office. myGov's death checklist gives this as the way to cancel a passport."),
  ("Can I get a refund on a dead person's passport?","No. The Australian Passport Office says it doesn't refund portions of application fees, so there's no refund for the unused validity when a passport holder dies."),
  ("Do I need to tell the AEC when someone dies?","No. The AEC says you don't need to notify it, because Births, Deaths and Marriages registries provide information about people who have died. You can still notify it with its online form."),
  ("How do I remove a deceased person from the electoral roll?","Usually it happens without you, using registry information. To request it yourself, complete the AEC's 'Notification of a relative who has died' online form."),
  ("What does the AEC's notification form ask for?","Your given and family names, relationship to the person, email and phone; and the person's names, date of birth, street address, suburb, state, postcode and date of death."),
  ("Do I need to close a deceased person's myGov account?","No. myGov says you don't need to close it because it closes automatically after not being used.")],
 [MG_CHK,APO_REF,AEC_FAQ,AEC_FORM],
 ["Passport: take it and the death certificate to Australia Post","No refund for unused passport validity","AEC: no need to notify; registries tell it","Optional AEC online form to remove the name"],
 ["/guides/mygov-centrelink-medicare-ato-after-death/","/guides/death-certificate-australia/","/guides/redirect-mail-after-death-australia/","/guides/what-to-do-when-someone-dies-digital-checklist/"])

NEW_PLAT=[GITHUB,PROTON]
NEW_GUIDES=[FF,PP]
NEW_PATHS=[f"/platforms/{p['slug']}/" for p in NEW_PLAT]+[f"/guides/{g[0]}/" for g in NEW_GUIDES]
REFRESHED=["/guides/mygov-centrelink-medicare-ato-after-death/"]
SHORT=[("What happens to my GitHub account when I die?","An appointed successor can archive or transfer your public repositories 7 days after presenting a death certificate (21 with an obituary), but can't log in. Others contact GitHub Support.","/platforms/github/"),
("What happens to my Proton Mail when I die?","Only Emergency Access (paid plans, up to 5 Proton Mail contacts, 1-30 day wait) gives someone access. Free accounts inactive over 24 months could be deleted.","/platforms/proton-mail/"),
("Can you inherit Qantas or Velocity points?","Qantas: executor asks in writing within 12 months to move unexpired points to one eligible family member. Velocity: executor asks to transfer or redeem, quickly. Status is lost.","/guides/frequent-flyer-points-after-death-australia/"),
("How do I cancel a deceased person's passport in Australia?","Take it and the death certificate to Australia Post; no refund for unused validity. The AEC is told of deaths by BDM registries, or use its online form.","/guides/passport-electoral-roll-after-death-australia/")]

MG_STEP="Cancel their passport by taking it and the death certificate to a local Australia Post office. You don't need to tell the Australian Electoral Commission: Births, Deaths and Marriages registries pass on death information (or use the AEC's online notification form)."

def _add(lst,s):
    if s not in lst: lst.append(s)
def pre(enrich,growth,pack2):
    enrich.NEWP.extend(NEW_PLAT)
    enrich.GUIDE_NEW.extend(NEW_GUIDES)
    growth.SHORT.extend(SHORT)
    for p in NEW_PATHS+REFRESHED: pack2.LASTMOD[p]=DATE; pack2.REV[p]=CHK
    for p in NEW_PATHS: pack2.PUBLISHED[p]=DATE
    pack2.CHECKED_AT.update(CHECKED_AT)
    for k,new in (("google-gmail","/platforms/proton-mail/"),("microsoft-outlook","/platforms/github/")):
        if k in enrich.P: _add(enrich.P[k].setdefault("related",[]),new)
    for p in enrich.NEWP:
        if p["slug"]=="yahoo-mail": _add(p.setdefault("related",[]),"/platforms/proton-mail/")
    links={"mygov-centrelink-medicare-ato-after-death":["/guides/passport-electoral-roll-after-death-australia/"],
      "australian-digital-estate-guide":["/guides/passport-electoral-roll-after-death-australia/","/guides/frequent-flyer-points-after-death-australia/"],
      "what-to-do-when-someone-dies-digital-checklist":["/guides/passport-electoral-roll-after-death-australia/","/guides/frequent-flyer-points-after-death-australia/","/platforms/github/"],
      "death-certificate-australia":["/guides/passport-electoral-roll-after-death-australia/"],
      "redirect-mail-after-death-australia":["/guides/passport-electoral-roll-after-death-australia/"],
      "bank-accounts-after-death-australia":["/guides/frequent-flyer-points-after-death-australia/"]}
    for i,x in enumerate(enrich.GUIDE_NEW):
        s,t,an,st,f,src,tl,rel=x
        add=[a for a in links.get(s,[]) if a not in rel and a!=f"/guides/{s}/"]
        if s=="mygov-centrelink-medicare-ato-after-death":
            st=list(st); src=list(src)
            if MG_STEP not in st: st.insert(3,MG_STEP)
            for z in (AEC_FAQ,):
                if z not in src: src.append(z)
        enrich.GUIDE_NEW[i]=(s,t,an,st,f,src,tl,rel+add)
    growth.EXTRA["australian-digital-estate-guide"]=growth.EXTRA.get("australian-digital-estate-guide","").replace("Qld car rego and licence</a>","Qld car rego and licence</a> · <a href='/guides/passport-electoral-roll-after-death-australia/'>passport and electoral roll</a> · <a href='/guides/frequent-flyer-points-after-death-australia/'>frequent flyer points</a>",1)
