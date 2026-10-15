# Afterkeep comparison UX spec, prioritised (15 Oct 2026)

**Constraint:** static directory only. No accounts, no user data, no vault. Filtering is plain HTML category pages plus a small vanilla JS file (under 5 KB, no framework). Each tool's data lives in one JSON or YAML source per tool, which the build step uses to generate every page.

## Current state (re-crawled, 50 URLs)
- **New since batch 1:** a /compare/ hub plus 3 head-to-heads (Bitwarden vs 1Password, GoodTrust vs Everplans, Google IAM vs Apple Legacy Contact), a brand logo, 40px tool logos on /tools/, per-page 1200×630 OG images, "By the Afterkeep research team · Reviewed on", a working-looking newsletter, and /advertise/thanks/ removed from the sitemap.
- **Still missing:**
  - /tools/ is one long list with no filter. Cards show category, name, verdict and links, but no price or key facts.
  - Best-of tables have only 2 columns (Tool, Best for), with no feature rows.
  - Compare tables have a single `<tr>` header, no sticky header and no "differences" toggle.
  - No rating or score, no "how we rate" page, and no "last verified" date per fact.

## Sources used
- NN/g, "Comparison Tables" (2024): https://www.nngroup.com/articles/comparison-tables/ (options as columns, sticky headers, show-only-differences, scannable cells).
- NN/g, "Explicitly State the Difference": https://www.nngroup.com/articles/explicit-differences/
- Baymard, "Optimize comparison for scanning": https://baymard.com/research-articles/user-friendly-comparison-tools (hide or highlight identical rows, sticky column headings).
- Baymard, "Provide comparison features": https://baymard.com/research-articles/provide-comparison-features (persistent compare checkboxes, compare tray).
- NerdWallet methodology: https://www.nerdwallet.com/methodology (published rubrics, star ratings within a category, partner disclosure).
- Wirecutter editorial standards and comparison-tables post: https://www.nytimes.com/wirecutter/editorial-standards/ · https://www.nytimes.com/wirecutter/blog/comparison-tables/ (picks by role, most important attribute first, colour-coded cells, independence firewall).
- **From general knowledge, not fetched this session:** Trivago, Healthcare.gov plan compare, Canstar, Finder, iSelect, G2, Capterra and PCMag. These patterns are well known (filter rails, plan-compare up to 3, Canstar star-rating badges, G2 category grids, PCMag "Bottom line" and pros/cons boxes), but I didn't verify their current page versions.

---

## P1. Scannable listing cards with key facts (all tool lists)
- **Pattern:** a logo, a one-line verdict and 3-4 key facts on the card, with no click needed. From G2, Capterra, Finder and Canstar.
- **Build:** a shared `ToolCard` on /tools/, /best/*, the category pages and the "alternatives" blocks.
  - Fields: `logo`, `name`, `category`, `verdict_label` (Top pick / Good / Use with caution / Not recommended), `one_liner` (≤140 chars), `price_band` (Free · Free + paid · Paid), `legacy_mechanism` (e.g. "Trusted contact + wait time"), `trigger` (Inactivity · Death certificate · Manual request), `region` (Global/US/AU), `reviewed_on`.
  - CTAs: "Read verdict" (primary) and "Official site ↗" (secondary, `rel="nofollow noopener"`, with `sponsored` if paid).
- **Why:** people decide on the list without opening 16 tabs. This is today's biggest gap: cards have no facts.

## P2. Real feature-row comparison tables on best-of and compare pages
- **Pattern:** options as columns and attributes as rows, ordered most important first, with short cell values and ✓/✗ plus text. From NN/g, Wirecutter, Healthcare.gov and PCMag.
- **Build:** replace the 2-column best-of table with a `<table>` that uses `<th scope="col">` per tool and `<th scope="row">` per attribute.
  - **Vaults rows, in order:** Built-in emergency access · How a contact gets in · Wait time configurable · Access levels · Contact needs an account? · Max contacts · Plan required · Price band · Open source/audited · Known issues.
  - **Crypto rows:** Custody model · Key sharing method · Heir needs tech skills? · Inheritance protocol docs · Supported assets · Fees · Jurisdiction.
  - **Estate rows:** Will/trust creation · Countries supported · Digital asset inventory · Document vault · Price model.
  - Cell rules: limits stay as visible text ("Up to 5"), and ✓/✗ always carries words for screen readers.
- **Why:** the 2-column table restates "best for" and can't support a choice. Ordered rows make the trade-off clear.

## P3. Sticky headers + "Show only differences" toggle (compare and best-of tables)
- **Pattern:** sticky column headings with logo and name, plus hide or highlight identical rows. From Baymard and NN/g (Best Buy, B&H, Staples).
- **Build:**
  - CSS: `thead th{position:sticky;top:0;background:#fff}` and a sticky first column on mobile. Use `border-collapse:separate`.
  - About 30 lines of JS: a checkbox labelled "Show only differences" sets `hidden` on any `tr` whose cells match, then updates the caption "Showing 6 of 10 features".
  - Mobile under 640px: horizontal scroll with the sticky row label, or a "swipe between tools" stacked card view.
- **Why:** shorter tables and less scrolling memory load. It's cheap and fully static.

## P4. Client-side filter rail + static category pages (/tools/)
- **Pattern:** a filter rail with live counts. From Trivago, Capterra, Finder and iSelect. Plus crawlable category landing pages, as in G2.
- **Build:**
  - Each card gets `data-cat data-price data-trigger data-region data-verdict`.
  - Filter chips at the top (on mobile they collapse into a single "Filters (2)" button): Category · Price (Free / Free+paid / Paid) · How it triggers · Works in Australia/US/UK · Recommended only.
  - Plus a sort `<select>`: Afterkeep pick (default) · Price · A–Z.
  - Live result count ("7 tools") and a "Clear filters" link. Filter state lives in the URL hash (`#cat=vaults&price=free`) so links can be shared. Never use localStorage or cookies.
  - Also generate static pages /tools/vaults/, /tools/crypto/, /tools/estate/, /tools/platform-settings/, /tools/memorial/ and /tools/free/. Each has its own H1, intro, mini comparison table and FAQ. Replace today's `#vaults` anchors with these.
  - Without JS, all cards still show.
- **Why:** narrowing by the factor that matters ("free", "my phone is Apple"). Category pages also rank for "best X" queries.

## P5. Verdict box + transparent rating method
- **Pattern:** "Bottom line" with pros/cons, "Our pick / Also great / Budget pick" picks by role, and a category-specific star rating with a public methodology. From PCMag, Wirecutter, NerdWallet and Canstar.
- **Build:**
  - **`VerdictBox` at the top of every /tools/* page:** label badge, an Afterkeep score of 1.0–5.0 (compared only within the category), "Best for", "Skip if", 3 pros / 3 cons and "Reviewed on · Facts last verified [date]".
  - **New /how-we-rate/ page:** the weighted rubric per category. For example, vaults: emergency access mechanism 35%, reliability/security track record 25%, cost of the legacy feature 20%, contact friction 10%, docs clarity 10%. The page also covers what we don't do (no hands-on testing claims unless done) and how sponsorship works ("sponsors can't buy a score"), and links from every score.
  - **Best-of pages:** role badges ("Best overall", "Best free", "Best for Apple families", "Best for crypto holders").
  - **Schema:** keep `Review`. Only add `reviewRating` once the rubric exists.
- **Why:** a verdict gives a decision shortcut, and a published method makes it credible. NerdWallet and Canstar make this explicit.

## P6. "Pick 2–3 to compare" tray (/tools/ and category pages)
- **Pattern:** persistent "Compare" checkboxes on cards and a sticky bottom tray showing selected items ("2 of 3"). From Baymard (B&H) and Healthcare.gov plan compare.
- **Build:**
  - The checkbox on each `ToolCard` adds the tool to a bottom tray. The "Compare" button goes to `/compare/?t=bitwarden,keeper,proton-pass`.
  - /compare/ renders the table from a single prebuilt static `/tools.json` (already similar to `search.json`). Only tools from the same category can be compared.
  - Hand-written /compare/a-vs-b/ pages stay as the SEO versions. If a pair has a curated page, link it from the tray.
  - State lives only in the URL query, so nothing is stored.
- **Why:** lets users build their own shortlist without a dozen hand-written vs pages. It stays static.
- **Effort:** medium. Do it after P1–P4.

## P7. Trust strip and disclosure placement
- **Pattern:**
  - Disclosure above the fold, next to the ranking: "How we make money", from NerdWallet, Finder and Canstar.
  - Visible sources: Healthcare.gov-style plain-language "official source" links.
- **Build:**
  - **One-line strip under the H1 on best-of, compare and tool pages:** "Independent · Sources linked for every fact · Sponsors can't change verdicts · Reviewed 15 Oct 2026". Link it to /about/#independence and /how-we-rate/.
  - **Featured listings:** a visible "Sponsored" pill on the card itself, never mixed into the ranked order unlabelled.
  - **Inline citations:** small superscript "source" links next to each key fact in tables, pointing to the vendor doc, not only a Sources list at the bottom.
  - **Change log per page:** "Updated: Dashlane removed Emergency Contact (date)".
- **Why:** this is a YMYL topic. Trust is what decides whether people act, and whether AI and search engines cite the site.

## P8. Decision helpers: "Start here" chooser + jump nav
- **Pattern:** a short guided chooser in the style of iSelect, Canstar and Trivago: no account, a few questions, then a result.
- **Build:**
  - **Static 3-question widget on the home page and /best/:**
    1. "What are you protecting?" (Passwords / Photos & email / Crypto / Will & documents)
    2. "Phone?" (iPhone / Android)
    3. "Budget?" (Free only / Happy to pay)
  - **Result:** links to a precomputed recommendation page or anchor, e.g. "iPhone + passwords + free → Apple Legacy Contact + Bitwarden Free... note Emergency Access needs Premium". That's a lookup table in JS with no data sent anywhere.
  - **On long best-of pages:** a sticky in-page nav (Quick picks · Comparison table · Reviews · FAQ) plus a "Quick picks" box above the fold with the top 3 and their roles.
- **Why:** many visitors are overwhelmed or grieving. A 15-second route to the right page lifts engagement and clicks out.

## P9 (light). Performance and consistency guardrails
- **Logos:** keep 40×40 WebP with width and height set and `loading=lazy` (already done). Sprite or inline SVG where possible.
- **JS:** a single `ak.js` under 5 KB, deferred, for filters, the differences toggle and the tray. No third-party scripts on decision pages.
- **Cells:** the same attribute names and the same tone of value text across all tables, generated from one data file so tables never disagree.
- **Accessibility:** use `<caption>` on tables and announce counts with `aria-live`.

## Suggested order
1. P1 + P2 (data model, then cards and tables).
2. P3.
3. P4.
4. P5 + P7.
5. P8.
6. P6.

P1–P3 are a single data-file plus template change that's needed for everything after it.

## Out of scope (by constraint)
User accounts, saved lists, vaults, uploads, reminders/check-ins, server-side search, and any storage of user input (including localStorage for shortlists, which the URL replaces).
