# Afterkeep marketing batch 1 (15 Oct 2026)

## Site snapshot (crawled all 47 sitemap URLs)
- Free, independent guide to what happens to accounts, photos, passwords and crypto when you die. It has 16 tool verdicts, 15 "what happens to my X when I die" platform pages, 3 best-of lists, 5 how-to guides (including an Australian digital estate guide), plus About and Advertise pages.
- Audience: people planning ahead (30-60s, password-manager users, crypto holders) and grieving families or executors who need access now.
- Positioning: neutral, sources cited, "not legal advice". Monetised through labelled featured listings (/advertise/).
- Already strong: titles and meta descriptions on every page, canonical, OG title and description, Article, FAQPage, HowTo, Review, ItemList and Breadcrumb schema, a robots.txt that welcomes AI crawlers, a sitemap, and llms.txt.
- Gaps: no og:image anywhere (twitter:card is only "summary"); no author or person on any page; the newsletter form doesn't collect anything ("launching soon"); /advertise/thanks/ is in the sitemap with no noindex; no X or social profile linked; About is thin (231 words).

## 1. Draft X posts (for approval, not posted)
1. **Hook:** Your family can't just "log in" to your phone after you die. Apple won't unlock it, even with a death certificate, unless you set up a Legacy Contact first. Takes 2 minutes: https://afterkeep.github.io/guides/apple-legacy-contact-setup/
2. **Tip:** Google has a setting most people have never heard of: Inactive Account Manager. If you go quiet for 3-18 months, up to 10 people you chose get your Gmail, Photos and Drive. Set it once: https://afterkeep.github.io/platforms/google-gmail/
3. **Surprise fact:** X doesn't memorialise accounts, and it won't give your family access. The best they can do is ask for it to be deactivated. What happens to every major account when you die: https://afterkeep.github.io/platforms/
4. **Question:** Honest question: if you died tomorrow, could anyone in your family get into your password manager? If the answer is "uh…", start here 👇 https://afterkeep.github.io/best/best-password-managers-emergency-access/
5. **Crypto:** Self-custodied crypto with no inheritance plan is simply lost. There's no "forgot password" for a seed phrase. We compared Casa, Unchained, Vault12 and Ledger Recover: https://afterkeep.github.io/best/best-crypto-inheritance-tools/
6. **Checklist:** A 7-step digital estate checklist you can do this weekend:
1 Password manager + emergency access
2 Google Inactive Account Manager
3 Apple Legacy Contact
4 Facebook legacy contact
5 Export photos
6 Crypto plan
7 Write it down
https://afterkeep.github.io/guides/digital-estate-checklist/
7. **Aussie angle:** In Australia, your will probably doesn't mention your digital accounts, and executors hit walls. A plain-English guide to digital estates in Oz: https://afterkeep.github.io/guides/australian-digital-estate-guide/
8. **Thread outline: "I spent a week reading every big tech death policy 🧵"**
   - 1/ Hook: most platforms won't give your family your password. Here's what each one actually does.
   - 2/ Google: Inactive Account Manager, the best of the bunch.
   - 3/ Apple: Legacy Contact + access key. Without it, it's a court order.
   - 4/ Facebook/Instagram: memorialise or delete. Nobody logs in.
   - 5/ X: no memorialisation, deactivation only.
   - 6/ Microsoft: court order, and even then no guarantees.
   - 7/ Steam/Kindle: you never owned it, so nothing transfers.
   - 8/ The fix: password manager emergency access + the free settings. Full guide → https://afterkeep.github.io/

Notes: keep to 0-1 hashtags at most (#DigitalLegacy only if needed). Post 1 and the thread are the best traffic bets. Before posting, check that the facts (e.g. Apple's death-certificate rule) match the linked page.

## 2. Communities, threads and accounts
| # | Where | URL | Verified | Angle |
|---|---|---|---|---|
| 1 | r/EstatePlanning | https://www.reddit.com/r/EstatePlanning/ | Thread found via search: /comments/1bjz8w6/passing_off_digital_assets_through_trust/ | Answer "digital assets in my trust/will" questions; link the checklist only where it genuinely helps |
| 2 | r/personalfinance thread "Password management after death" | https://www.reddit.com/r/personalfinance/comments/136mq5t/password_management_after_death/ | Search result | Evergreen question that recurs; the password-manager comparison is the best match |
| 3 | Bitwarden Community forum | https://community.bitwarden.com/ | HTTP 200 | Emergency Access how-to threads; the Bitwarden verdict page |
| 4 | @Bitwarden (X) | https://x.com/Bitwarden | X API | Quote-post their Emergency Access content with the "set it up for your family" angle |
| 5 | @1Password (X) | https://x.com/1Password | X API | Its Emergency Kit / family sharing tie-in to the comparison page |
| 6 | @Digitalbeyond (James Norris, The Digital Beyond) | https://x.com/Digitalbeyond · https://www.thedigitalbeyond.com/ | X API + HTTP 200 | Long-running digital-death blogger; outreach for links and mentions (needs your OK) |
| 7 | @Everplans (X) | https://x.com/Everplans | X API | Industry voice; engage with their posts; Everplans has a verdict page on the site |
| 8 | Digital Legacy Association (UK) | https://www.digitallegacyassociation.org/ | HTTP 200 | Professional body for end-of-life and palliative staff; resource-list or backlink pitch |
| 9 | The Order of the Good Death | https://www.orderofthegooddeath.com/ | HTTP 200 | Death-positive community; pitch the "access a deceased person's phone" guide as a resource |
| 10 | r/GriefSupport, r/LegalAdviceAUS, r/AusFinance, r/Bitwarden, r/Bitcoin | reddit.com/r/<name> | Real subs, but Reddit returned 403 to my fetch, so not fetch-confirmed | Grief: only help, never promo. AU subs: the Australian guide. Bitcoin: crypto inheritance |
| 11 | Hacker News | https://news.ycombinator.com/ | HTTP 200 | A "Show HN" or a write-up of big-tech death policies could do well |
| 12 | Live X conversation | e.g. https://x.com/FareedHani82255/status/2110629551919206579 (someone just set an IG legacy contact) | X search | Searching "legacy contact" daily turns up natural reply openings |

Not found on X: @DigitalLegacyAs, @GoodTrustInc. Don't use those handles.

## 3. SEO and AI-chatbot visibility
1. **Add og:image and the summary_large_image card** (SITE CHANGE). There's no image anywhere, so X and LinkedIn shares look bare. One branded template image per section would lift click-through on every post above.
2. **Add author/E-E-A-T signals** (SITE CHANGE). Add a named editor or "Afterkeep research team" with an About bio, a `Person`/`Organization` with `sameAs` (X profile), "reviewed on" dates and a methodology section. YMYL topics (death, money) are ranked heavily on trust. The About page is only 231 words.
3. **Fix the newsletter** (SITE CHANGE). The form tells people signups "aren't being collected yet". Connect Buttondown, Substack or ConvertKit, or remove the form. A "policy change alerts" list is also a reason for people to link to the site.
4. **New high-intent pages** (SITE CHANGE, maybe coordinate with the CEO bot): TikTok, Snapchat, Spotify, Discord, Microsoft Xbox, Apple Music/iTunes purchases, Netflix, Binance/Kraken, Telegram, Reddit. Also "what to do when someone dies: digital checklist for executors" (US and UK versions to go with the AU one) and "how to write digital assets into your will (sample clause)".
5. **Comparison and "vs" pages** (SITE CHANGE). Bitwarden vs 1Password emergency access, GoodTrust vs Everplans, Casa vs Unchained, Google IAM vs Apple Legacy Contact. AI chatbots get asked these head-to-head questions often, and a table with a clear verdict gets cited.
6. **Make llms.txt richer** (SITE CHANGE, small). It currently truncates descriptions mid-word (~140 chars). Write full one-sentence answers, add a "Key facts" section (e.g. "X does not memorialise accounts"), and consider /llms-full.txt with page bodies. Answer-first sentences are what LLMs quote.
7. **Housekeeping** (SITE CHANGE). Add `noindex` to /advertise/thanks/ and drop it from the sitemap; add `lastmod` to sitemap entries if they're missing; give the home page an `Organization` with logo and sameAs. Then submit to Google Search Console and Bing Webmaster Tools. Bing feeds ChatGPT and Copilot search, so it's well worth doing. Use IndexNow for updates.
8. **Off-site citations** (no site change). AI answers lean on Reddit, Wikipedia-style references and well-known resource lists. Genuinely helpful Reddit answers, plus getting listed on Digital Legacy Association and Digital Beyond resource pages, are the fastest route into chatbot recommendations. Track it by asking ChatGPT, Perplexity and Grok "best digital legacy tools" every month.

## Decisions needed from Benno
- Approve, edit or reject the 8 posts. Which X account posts them? There's no Afterkeep X profile linked from the site.
- OK to do outreach (Digital Beyond, DLA, Order of the Good Death)? Nothing has been sent.
- Hand site changes 1-7 to the CEO bot?
