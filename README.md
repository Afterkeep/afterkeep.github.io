Build: SITE_URL=https://<host> NEWSLETTER_ACTION=<form endpoint> python3 build.py -> dist/
Content lives in content.py; pages/SEO in build.py.

## Adding an affiliate link
1. Open `data/tools.json` and find the tool by slug.
2. Set `"affiliate_url": "https://..."` (leave `""` for no affiliate link).
3. Rebuild (`SITE_URL=https://afterkeep.github.io python3 build.py`) and push.
That tool's Official site buttons then use the affiliate URL with `rel="sponsored nofollow noopener"`, show an "Affiliate link" label linking to /affiliate-disclosure/, and its tool, best-of and compare pages get a one-line disclosure note near the top. Tools with an empty value stay unchanged.
