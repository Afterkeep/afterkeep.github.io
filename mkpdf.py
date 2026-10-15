# Generates the printable executor checklist PDF (run locally; output is committed).
import growth, html, weasyprint
E=html.escape
rows="".join(f"<tr><td class=b>☐</td><td class=d>{E(d)}</td><td>{E(s)}</td></tr>" for d,s in growth.EXEC_STEPS)
src="".join(f"<li>{E(n)}: {E(u)}</li>" for n,u in growth.EXEC[5])
doc=f"""<html><head><style>@page{{size:A4;margin:16mm}}body{{font-family:'DejaVu Sans',sans-serif;color:#0e4c6b;font-size:10.5pt}}h1{{font-size:18pt;margin:0 0 4pt}}.k{{color:#0a8ea2;font-weight:bold;letter-spacing:1px;font-size:9pt}}table{{width:100%;border-collapse:collapse;margin-top:10pt}}td{{border-bottom:1px solid #d1eaee;padding:7pt 5pt;vertical-align:top;color:#1d2b30}}.b{{font-size:14pt;width:18pt}}.d{{width:70pt;font-weight:bold;color:#0e4c6b}}.n{{margin-top:8pt;font-size:9pt;color:#5b6467}}ul{{font-size:8pt;color:#5b6467;padding-left:14pt}}</style></head><body>
<img src="assets/brand/afterkeep-logo-full.png" style="height:28pt"><p class=k>EXECUTOR'S DIGITAL CHECKLIST</p><h1>What to do in the first 30 days</h1>
<p>{E(growth.EXEC[2].replace(' A printable PDF version is below.',''))}</p><table>{rows}</table>
<p class=n>Notes and reference numbers:</p><div style="border:1px solid #d1eaee;height:70pt"></div>
<p class=n>Official sources (checked 15 Oct 2026):</p><ul>{src}</ul>
<p class=n>Afterkeep is an independent guide directory. General information, not legal advice. afterkeep.github.io/guides/{growth.EXEC[0]}/</p></body></html>"""
weasyprint.HTML(string=doc,base_url=".").write_pdf("assets/afterkeep-executor-first-30-days-checklist.pdf")
