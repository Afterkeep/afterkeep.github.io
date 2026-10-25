# Afterkeep growth pack 1 (15 Oct 2026, AEST)

**Rules:** draft only. Nothing has been posted, replied to, followed or contacted. Benno's personal X is never used. Afterkeep is a comparison/guide directory only.

**Re-crawl:** 58 URLs in the sitemap. Confirmed live:
- /compare/ (3 head-to-heads)
- /tools/ category pages (vaults, crypto, estate, platform-settings, memorial, free)
- /how-we-rate/ and /affiliate-disclosure/
- "Facts last verified" lines, logos and OG images

## 1. SEO + AI-chatbot plan

### Query tests (WebSearch, 15 Oct 2026)
**Afterkeep appeared in none of the 10 results.** That's expected for a new github.io site that isn't yet submitted to Google or Bing.

| # | Query | Who ranks / gets cited | Where Afterkeep can win |
|---|---|---|---|
| 1 | what happens to my Gmail when I die | Google Help (x3), eSafety Commissioner (AU gov) | Official docs dominate. Win the "one page, every option + documents needed" summary. Add the "deleted after 2 years inactive" fact, the IAM wait options (3/6/12/18 months) and a "closing the account prevents a later data request" warning. |
| 2 | bitwarden vs 1password emergency access | Bitwarden help, 1Password help, impulsec.com, realcostreport.com (quotes a $19.80/yr price) | Winnable: only 2 third-party pages exist, and the compare page already says the same thing. Add a dated price line, a Keeper column and a "what heirs actually do, step by step" section. |
| 3 | digital estate planning australia | QLD Public Trustee, eSafety, Justice Connect, Aitken lawyers, NSW Trustee & Guardian | Mostly government and legal pages; none compares tools. Afterkeep's AU guide is unique there. Add state-by-state notes (QLD/ACT property definitions per Justice Connect) and link to the official pages as sources. |
| 4 | best crypto inheritance tools 2026 | spark.money, web3wagmi, Unchained (vendor), Trust & Will (vendor), thebitcoinhole | Vendor-led and crowded. Afterkeep is missing **Bitkey, Nunchuk, Liana and AnchorWatch**, which all appear in rival lists. Add them. |
| 5 | best digital legacy vault 2026 | **digitalinheritanceguide.com** (direct competitor, same model), aineow, Eternal Vault (vendor), GetMemorial (vendor), gitnux | The closest competitor ranks #1. Win with independence, since 3 of the 5 are vendors ranking themselves. Add Trustworthy, MyWishes, SecureSafe, Life Ledger and Settld. |
| 6 | what happens to my iCloud when I die | Apple Support only | The AI summary adds facts the Afterkeep page should state: access lasts 3 years, the original Apple ID is disabled, Activation Lock is removed. Add these (cite Apple). |
| 7 | how to access a deceased person's iPhone | Apple Support, AARP, Reddit r/iphone, r/applehelp | Reddit plus Apple. Afterkeep's /guides/access-deceased-persons-phone-and-accounts/ fits. Add "Apple can't bypass a passcode without erasing" and an Activation Lock section. |
| 8 | digital estate checklist | digitalinheritanceguide, ABA, bank PDFs, HeirVault | Add a **printable/PDF checklist** (static file); printables earn links. |
| 9 | what happens to my Steam account when I die | Ars Technica, GamesHub, gamepressure, Steam SSA, Polygon | Press-led. Expand the page into "Steam, GOG, Epic, PlayStation, Xbox: game libraries after death", a gap Polygon covers only partly. |
| 10 | google inactive account manager vs apple legacy contact | Google Help, AP News, BBC, Android Authority, digitallegacyvault.app | Afterkeep's compare page is a strong fit. Add the 3-year Apple access window and the Google 3-18 month options, then get it indexed. |

### Next pages and edits (flag to the CEO bot: all are site changes)
1. **Facts on existing pages:**
   - Apple 3-year access window and Activation Lock removal: /platforms/apple-icloud/ and /compare/google-…-vs-apple…
   - Google IAM wait options 3/6/12/18 months: /platforms/google-gmail/ and the compare page.
2. **Crypto:** add Bitkey, Nunchuk, Liana and AnchorWatch to /best/best-crypto-inheritance-tools/ and /tools/crypto/.
3. **Vaults:** add Trustworthy, MyWishes, SecureSafe, Life Ledger and Settld (notification services) to /best/best-digital-legacy-vaults/.
4. **New page /compare/bitwarden-vs-1password-vs-keeper-emergency-access/.**
5. **New page /platforms/game-libraries/** covering Steam, GOG, Epic, PSN and Xbox.
6. **New page /guides/what-to-do-when-someone-dies-digital-checklist/** (executor, first 30 days), plus a printable PDF of the digital estate checklist.
7. **Australia guide:** add a state-by-state section and the Australian Death Notification Service.
8. **llms.txt:** add a "Key facts" block with one-line answers to the 10 queries above.

### Search Console + Bing + IndexNow: steps for Benno
1. **Google Search Console** (search.google.com/search-console): Add property → **URL prefix** `https://afterkeep.github.io/`. A Domain property won't work on github.io.
2. **Verify** with the HTML-tag method. The CEO bot adds `<meta name="google-site-verification" content="…">` to the home `<head>` and deploys, then Benno clicks Verify.
3. **Sitemaps:** submit `sitemap.xml`. Then use URL Inspection → Request indexing for the home page, /compare/ pages, /best/ pages and the AU guide (about 10 a day).
4. **Bing Webmaster Tools** (bing.com/webmasters): Import from GSC (one click), or add the site and verify with the `msvalidate.01` meta tag. Submit the sitemap. Bing powers ChatGPT search and Copilot.
5. **IndexNow:**
   - Generate a key in Bing Webmaster → IndexNow. The CEO bot hosts `https://afterkeep.github.io/<key>.txt` containing the key.
   - On each deploy, POST the changed URLs to `https://api.indexnow.org/indexnow` with `{host, key, keyLocation, urlList}`, using a GitHub Action step or a curl in the build.
6. **Monitor weekly:**
   - GSC Performance (queries, impressions) and Pages → "Not indexed" reasons.
   - Ask ChatGPT, Perplexity, Grok and Copilot the 10 queries monthly and note whether they cite Afterkeep.

## 2. X posts and threads
All facts are taken from the linked live page, checked 15 Oct 2026. Lengths were counted with code using X weighting (each URL = 23 chars). The maximum is 246. P1–P10 are posts; T1/T2 are threads (index 0 = opener).

**P1** (228 chars, X-weighted; URLs count as 23)

```
Google never hands over a dead person's password.

But if you set up Inactive Account Manager, up to 10 people you choose can download the data you picked once your account goes inactive.

2-minute setup: https://afterkeep.github.io/platforms/google-gmail/
```

**P2** (239 chars, X-weighted; URLs count as 23)

```
X doesn't memorialise accounts and won't give your family access.

The most they can do is ask for deactivation, with ID and a death certificate. DMs are gone.

Download your archive now if you want your posts kept: https://afterkeep.github.io/platforms/x-twitter/
```

**P3** (246 chars, X-weighted; URLs count as 23)

```
Bitwarden vs 1Password for emergency access:

Bitwarden: trusted contacts request View or Takeover access, granted after a wait time you set.
1Password: no equivalent. You rely on a printed Emergency Kit.

Full comparison: https://afterkeep.github.io/compare/bitwarden-vs-1password-emergency-access/
```

**P4** (244 chars, X-weighted; URLs count as 23)

```
Apple Legacy Contact gives someone your photos, messages, notes and files after you die, with an access key + death certificate.

What it never includes: iCloud Keychain passwords and purchased media.

What else to know: https://afterkeep.github.io/platforms/apple-icloud/
```

**P5** (243 chars, X-weighted; URLs count as 23)

```
Your Steam library probably dies with you.

The Subscriber Agreement says accounts are 'strictly personal' and can't be transferred unless Valve permits it. Valve doesn't recognise transfers by operation of law either.

https://afterkeep.github.io/platforms/game-libraries/
```

**P6** (237 chars, X-weighted; URLs count as 23)

```
Google Inactive Account Manager or Apple Legacy Contact?

Not either-or. Both are free. Google acts automatically after inactivity, for up to 10 people. Apple needs an access key + death certificate.

Set up both: https://afterkeep.github.io/compare/google-inactive-account-manager-vs-apple-legacy-contact/
```

**P7** (233 chars, X-weighted; URLs count as 23)

```
Aussies: your executor will likely need probate or letters of administration before banks and platforms release anything. Estates typically take 6-12 months.

Leave an inventory with your will, not passwords.

https://afterkeep.github.io/guides/australian-digital-estate-guide/
```

**P8** (198 chars, X-weighted; URLs count as 23)

```
Dashlane removed its Emergency Contact feature. If you're relying on it for your family, you're not covered.

Password managers that still have real emergency access, ranked: https://afterkeep.github.io/best/best-password-managers-emergency-access/
```

**P9** (212 chars, X-weighted; URLs count as 23)

```
No Microsoft password? No content.

Microsoft won't release a deceased person's Outlook.com or OneDrive files without a subpoena or court order. Inactive accounts are frozen after 1 year.

https://afterkeep.github.io/platforms/microsoft-outlook/
```

**P10** (200 chars, X-weighted; URLs count as 23)

```
Quick question: if you died tomorrow, could one trusted person get into your password manager?

If not, that's the one fix that covers almost everything else. Free tools first: https://afterkeep.github.io/tools/free/
```

**T1.0** (174 chars, X-weighted; URLs count as 23)

```
What happens to your accounts when you die? I went through the official policies for Google, Apple, Facebook, X, Microsoft and Steam. Most won't hand over a password, ever. 🧵
```

**T1.1** (203 chars, X-weighted; URLs count as 23)

```
1/ Google: Inactive Account Manager lets up to 10 people you choose download the data you picked once your account goes inactive. Without it, family can ask, decided case by case. https://afterkeep.github.io/platforms/google-gmail/
```

**T1.2** (175 chars, X-weighted; URLs count as 23)

```
2/ Apple: a Legacy Contact uses an access key + your death certificate to get photos, messages, notes, files. No Legacy Contact? Usually a court order. https://afterkeep.github.io/platforms/apple-icloud/
```

**T1.3** (169 chars, X-weighted; URLs count as 23)

```
3/ Facebook: memorialise or delete, your choice in advance. A legacy contact can manage a memorialised profile but can't log in or read messages. https://afterkeep.github.io/platforms/facebook/
```

**T1.4** (124 chars, X-weighted; URLs count as 23)

```
4/ X: no memorialisation, no access for family. Deactivation on request with ID + death certificate. https://afterkeep.github.io/platforms/x-twitter/
```

**T1.5** (133 chars, X-weighted; URLs count as 23)

```
5/ Microsoft: Outlook.com/OneDrive content only with a subpoena or court order. Frozen after 1 year inactive. https://afterkeep.github.io/platforms/microsoft-outlook/
```

**T1.6** (90 chars, X-weighted; URLs count as 23)

```
6/ Steam: games are licences. No transfer unless Valve permits it. https://afterkeep.github.io/platforms/steam/
```

**T1.7** (136 chars, X-weighted; URLs count as 23)

```
7/ The fix: a password manager with emergency access, plus the free Google and Apple settings. 7-step checklist: https://afterkeep.github.io/guides/digital-estate-checklist/
```

**T2.0** (150 chars, X-weighted; URLs count as 23)

```
Password managers are the backbone of a digital estate plan, but not all of them let your family in. Here's how the big ones handle emergency access 🧵
```

**T2.1** (182 chars, X-weighted; URLs count as 23)

```
1/ Bitwarden: trusted contacts request View or Takeover access. Granted when you approve, or automatically after your wait time. Needs Premium or a paid plan. https://afterkeep.github.io/tools/bitwarden/
```

**T2.2** (200 chars, X-weighted; URLs count as 23)

```
2/ 1Password: no automatic emergency access. You rely on the Emergency Kit (sign-in address, email, Secret Key, password), and on family plans an organiser can recover members. https://afterkeep.github.io/tools/1password/
```

**T2.3** (178 chars, X-weighted; URLs count as 23)

```
3/ Proton Pass: up to 5 emergency contacts on paid Proton plans, with a wait of 1-30 days, and you can deny any request. Both of you need Proton accounts. https://afterkeep.github.io/tools/proton-pass/
```

**T2.4** (110 chars, X-weighted; URLs count as 23)

```
4/ Dashlane: removed its Emergency Contact feature. Not recommended for legacy access. https://afterkeep.github.io/tools/dashlane/
```

**T2.5** (61 chars, X-weighted; URLs count as 23)

```
5/ Full ranking + side-by-side table: https://afterkeep.github.io/best/best-password-managers-emergency-access/
```

## 3. Opportunities (draft replies and pitches only, not sent)
Live thread replies should come from @Afterkeep only after Benno approves, and must be useful even without the link. Reddit answers must follow each sub's self-promo rules; disclose affiliation ("I help run Afterkeep").

1. **X: @HanDoesGames, deceased family member's Activation Lock** (11 Oct 2026): https://x.com/HanDoesGames/status/2109400331398328476
   - **Why:** a live, exact-fit pain point.
   - **Draft reply:** "So sorry. If they didn't set a Legacy Contact, Apple's route is its deceased-family request at digital-legacy.apple.com, usually with a death certificate plus a court order (Apple accepts alternative documents in some countries, incl. Australia). We wrote up the steps here: https://afterkeep.github.io/guides/access-deceased-persons-phone-and-accounts/"
2. **Reddit r/iphone, "iPhone owner passed away and passwords file locked":** https://www.reddit.com/r/iphone/comments/1pi42ed/
   - **Why:** high intent. Point to Legacy Contact limits (Keychain excluded).
   - **Draft:** "One thing that catches people out: even with Apple's Legacy Contact, iCloud Keychain passwords are never included, so the passwords file won't come across that way. Apple's deceased-account request can still release photos, files and backups. Summary of what's in and out: https://afterkeep.github.io/platforms/apple-icloud/"
3. **Reddit r/applehelp, "Getting into iPhone with Face ID from deceased relative":** https://www.reddit.com/r/applehelp/comments/1scsnen/
   - **Draft:** "Apple can't bypass the passcode without erasing the phone, so the realistic path is the iCloud data rather than the device. Without a Legacy Contact, Apple needs a death certificate plus a court order or local equivalent. Steps: https://afterkeep.github.io/guides/access-deceased-persons-phone-and-accounts/"
4. **Reddit r/personalfinance, "Father passed unexpectedly… doesn't know any of his passwords":** https://www.reddit.com/r/personalfinance/comments/1s53h8w/
   - **Draft:** "Sorry for your loss. Start with his email: most accounts can be found from it. Google, Apple and Microsoft each have a deceased-user process (Microsoft needs a court order for content). Banks need a death certificate and executor documents. Per-platform checklist: https://afterkeep.github.io/guides/access-deceased-persons-phone-and-accounts/"
5. **Reddit r/EstatePlanning, "Passing off digital assets through trust":** https://www.reddit.com/r/EstatePlanning/comments/1bjz8w6/
   - **Why:** evergreen and still found by search.
   - **Draft:** "Agree with the password-manager advice. Just check yours still has emergency access (Dashlane removed it). Comparison: https://afterkeep.github.io/best/best-password-managers-emergency-access/"
6. **Hacker News Show HN** (the old threads 37042427, 33863940 and 16531492 are archived, 2018-2023, and show demand).
   - **Pitch title:** "Show HN: Afterkeep – what every big platform actually does with your account when you die"
   - **Body:** "Static site, no sign-ups or accounts (just basic Google Analytics). Each page cites the official policy. Feedback welcome on accuracy." Post at about 11pm AEST (US morning).
7. **Digital Legacy Association resources page:** https://digitallegacyassociation.org/resources-2/
   - **Pitch email:** "Subject: Free, independent platform-by-platform guide for your resources page. Hi DLA team, Afterkeep (afterkeep.github.io) is a free, independent guide that summarises each major platform's death policy and the documents families need, with official sources on every page. No sign-up, no sales. It may be useful alongside your leaflets for families and hospice staff. Happy to correct anything your team spots. Benno"
8. **The Digital Beyond (James Norris, @Digitalbeyond):** https://www.thedigitalbeyond.com/
   - **Pitch:** "Long-time reader. We built a free, source-cited directory of platform death policies and legacy tools (afterkeep.github.io). Would it fit your directory or a roundup? Glad to send updates whenever a platform changes its policy."
9. **Justice Connect (AU):** https://justiceconnect.org.au/resources/how-to-manage-your-digital-legacy/
   - **Pitch:** "Your digital legacy resource is excellent. Our Australian digital estate guide links to it as a source. If useful, our per-platform pages (Google, Apple, Facebook…) could serve as a practical 'how' companion for your readers." Note: legal non-profits rarely link to commercial sites, so frame it as free and independent.
10. **Digital Legacy Podcast:** https://digitallegacypodcast.com/
    - **Guest pitch:** "Episode idea: 'What 15 platforms actually do when you die (and the 3 settings that matter)'. Benno from Afterkeep, an independent comparison guide. We can walk through the Apple/Google differences and which password managers still have emergency access."
11. **Death and Dying in the Digital Age podcast (Niki Weiss):** https://podcasts.apple.com/us/podcast/death-and-dying-in-the-digital-age/id1775499012
    - Same pitch, plus an Australian angle (probate, Apple accepting alternative documents in AU).
12. **The Order of the Good Death:** https://www.orderofthegooddeath.com/
    - **Pitch:** a resource suggestion for their death-planning resources: "/guides/digital-estate-checklist/, a free 7-step digital checklist".
13. **Competitor watch, not outreach:** digitalinheritanceguide.com ranks #1 for "best digital legacy vault". Monitor its pages for gaps; don't copy.

## 4. @Afterkeep X account strategy
- **Handle check (X API, 15 Oct 2026):**
  - @afterkeep is **taken** (an unrelated Japanese account, "フェス太郎").
  - **Available:** @AfterkeepHQ, @AfterkeepGuide, @Afterkeep_, @GetAfterkeep, @AfterkeepApp. Avoid "App" because it isn't an app.
  - **Recommend @AfterkeepGuide** (describes the product), with @AfterkeepHQ as fallback. Availability is advisory until registered.
- **Name:** Afterkeep
- **Bio (≤160):** "Independent guide to what happens to your accounts, photos, passwords & crypto when you die, and the tools that help. Sources on every page. Not legal advice."
- **Link:** https://afterkeep.github.io/ · **Location:** Brisbane, Australia (optional)
- **Pinned post:** Thread T1 (the big-tech policies).
- **Cadence:** 1 post a day on weekdays, 1 thread a week. Mostly between 7-9am AEST, with occasional 10-11pm AEST slots for US/UK morning reach. No engagement-bait and 0-1 hashtags.
- **Content pillars:**
  1. **Platform facts:** "what happens to X when you die" (40%).
  2. **Tool verdicts and comparisons** (25%).
  3. **Australia-specific** estate and probate tips (15%).
  4. **Policy-change alerts** when a platform changes its rules (10%; fast and newsworthy).
  5. **Gentle prompts and questions** ("set this up this weekend") (10%).
- **Replies:** only to posts asking for help, and only after approval in this phase.

### 2-week calendar (AEST, starting after the account is approved and created)
| Day | Post |
|---|---|
| Mon W1 | T1 thread (pin) |
| Tue | P1 Google |
| Wed | P4 Apple |
| Thu | P3 Bitwarden vs 1Password |
| Fri | P10 question |
| Mon W2 | T2 thread |
| Tue | P2 X policy |
| Wed | P7 Australia |
| Thu | P6 Google vs Apple |
| Fri | P5 Steam |
| Sat W2 | P8 Dashlane |
| Sun W2 | P9 Microsoft |

## Decisions for Benno
1. Approve a handle (@AfterkeepGuide?) and create the account. Account creation is a manual step for Benno.
2. Approve posts and threads, and which opportunity replies and pitches to send.
3. OK to hand section 1's site changes and the GSC/Bing verification meta tags to the CEO bot?
