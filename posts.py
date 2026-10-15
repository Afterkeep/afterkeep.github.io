import re
B="https://afterkeep.github.io"
posts={
"P1":f"Google never hands over a dead person's password.\n\nBut if you set up Inactive Account Manager, up to 10 people you choose can download the data you picked once your account goes inactive.\n\n2-minute setup: {B}/platforms/google-gmail/",
"P2":f"X doesn't memorialise accounts and won't give your family access.\n\nThe most they can do is ask for deactivation, with ID and a death certificate. DMs are gone.\n\nDownload your archive now if you want your posts kept: {B}/platforms/x-twitter/",
"P3":f"Bitwarden vs 1Password for emergency access:\n\nBitwarden: trusted contacts request View or Takeover access, granted after a wait time you set.\n1Password: no equivalent. You rely on a printed Emergency Kit.\n\nFull comparison: {B}/compare/bitwarden-vs-1password-emergency-access/",
"P4":f"Apple Legacy Contact gives someone your photos, messages, notes and files after you die, with an access key + death certificate.\n\nWhat it never includes: iCloud Keychain passwords and purchased media.\n\nWhat else to know: {B}/platforms/apple-icloud/",
"P5":f"Your Steam library probably dies with you.\n\nThe Subscriber Agreement says accounts are 'strictly personal' and can't be transferred unless Valve permits it. Valve doesn't recognise transfers by operation of law either.\n\n{B}/platforms/steam/",
"P6":f"Google Inactive Account Manager or Apple Legacy Contact?\n\nNot either-or. Both are free. Google acts automatically after inactivity, for up to 10 people. Apple needs an access key + death certificate.\n\nSet up both: {B}/compare/google-inactive-account-manager-vs-apple-legacy-contact/",
"P7":f"Aussies: your executor will likely need probate or letters of administration before banks and platforms release anything. Estates typically take 6-12 months.\n\nLeave an inventory with your will, not passwords.\n\n{B}/guides/australian-digital-estate-guide/",
"P8":f"Dashlane removed its Emergency Contact feature. If you're relying on it for your family, you're not covered.\n\nPassword managers that still have real emergency access, ranked: {B}/best/best-password-managers-emergency-access/",
"P9":f"No Microsoft password? No content.\n\nMicrosoft won't release a deceased person's Outlook.com or OneDrive files without a subpoena or court order. Inactive accounts are frozen after 1 year.\n\n{B}/platforms/microsoft-outlook/",
"P10":f"Quick question: if you died tomorrow, could one trusted person get into your password manager?\n\nIf not, that's the one fix that covers almost everything else. Free tools first: {B}/tools/free/",
}
t1=[
"What happens to your accounts when you die? I went through the official policies for Google, Apple, Facebook, X, Microsoft and Steam. Most won't hand over a password, ever. 🧵",
f"1/ Google: Inactive Account Manager lets up to 10 people you choose download the data you picked once your account goes inactive. Without it, family can ask, decided case by case. {B}/platforms/google-gmail/",
f"2/ Apple: a Legacy Contact uses an access key + your death certificate to get photos, messages, notes, files. No Legacy Contact? Usually a court order. {B}/platforms/apple-icloud/",
f"3/ Facebook: memorialise or delete, your choice in advance. A legacy contact can manage a memorialised profile but can't log in or read messages. {B}/platforms/facebook/",
f"4/ X: no memorialisation, no access for family. Deactivation on request with ID + death certificate. {B}/platforms/x-twitter/",
f"5/ Microsoft: Outlook.com/OneDrive content only with a subpoena or court order. Frozen after 1 year inactive. {B}/platforms/microsoft-outlook/",
f"6/ Steam: games are licences. No transfer unless Valve permits it. {B}/platforms/steam/",
f"7/ The fix: a password manager with emergency access, plus the free Google and Apple settings. 7-step checklist: {B}/guides/digital-estate-checklist/",
]
t2=[
"Password managers are the backbone of a digital estate plan, but not all of them let your family in. Here's how the big ones handle emergency access 🧵",
f"1/ Bitwarden: trusted contacts request View or Takeover access. Granted when you approve, or automatically after your wait time. Needs Premium or a paid plan. {B}/tools/bitwarden/",
f"2/ 1Password: no automatic emergency access. You rely on the Emergency Kit (sign-in address, email, Secret Key, password), and on family plans an organiser can recover members. {B}/tools/1password/",
f"3/ Proton Pass: up to 5 emergency contacts on paid Proton plans, with a wait of 1-30 days, and you can deny any request. Both of you need Proton accounts. {B}/tools/proton-pass/",
f"4/ Dashlane: removed its Emergency Contact feature. Not recommended for legacy access. {B}/tools/dashlane/",
f"5/ Full ranking + side-by-side table: {B}/best/best-password-managers-emergency-access/",
]
def xlen(s): return len(re.sub(r'https?://\S+','x'*23,s))
out=[]
for k,v in posts.items(): out.append((k,v))
for i,v in enumerate(t1): out.append((f"T1.{i}",v))
for i,v in enumerate(t2): out.append((f"T2.{i}",v))
md=[]
for k,v in out:
    n=xlen(v); assert n<=280,(k,n)
    md.append(f"**{k}** ({n} chars, X-weighted; URLs count as 23)\n\n```\n{v}\n```\n")
open("posts.md","w").write("\n".join(md)); print(max(xlen(v) for k,v in out), len(out))
