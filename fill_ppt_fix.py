"""Fix remaining unfilled slides: 4, 9, 12."""

import zipfile
from lxml import etree

SRC = "AI_Capstone_L3_Case04_Raj_Lanjewar.pptx"
DST = "AI_Capstone_L3_Case04_Raj_Lanjewar.pptx"

NSMAP = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}


def get_para_text(para):
    return ''.join((t.text or '') for t in para.findall('.//a:r/a:t', NSMAP))


def set_para_text(para, new_text):
    runs = para.findall('.//a:r', NSMAP)
    if not runs:
        return
    runs[0].find('a:t', NSMAP).text = new_text
    for r in runs[1:]:
        r.find('a:t', NSMAP).text = ''


def replace(root, old, new, count=1):
    n = 0
    for para in root.findall('.//a:p', NSMAP):
        if n >= count:
            break
        full = get_para_text(para)
        if old in full:
            set_para_text(para, full.replace(old, new))
            n += 1
    return n


with zipfile.ZipFile(SRC, 'r') as zin:
    contents = {n: zin.read(n) for n in zin.namelist()}

# --- SLIDE 4: AI Approach (uses ASCII straight quotes) ---
root = etree.fromstring(contents['ppt/slides/slide4.xml'])
replace(root, '[ e.g., "Turn a legacy migration ticket into a reviewed, tested PR in one session." ]',
        '"Expose 4 internal systems as governed MCP tools where authorization survives composition, credentials never reach the model, and every call is auditable."')
replace(root, "Step / Phase", "Design Auth Model")
replace(root, "What happens here + which AI tool / prompt you used",
        "3-layer auth (tool ACL + row scope + composition guards). Claude generated policy matrix and identified 4 composition attack paths.")
replace(root, "Step / Phase", "Build Controls")
replace(root, "What happens here + which AI tool / prompt you used",
        "Credential isolation, sanitization, rate limiting, approval gates, kill switch. Claude built middleware and 158 paired tests.")
replace(root, "Step / Phase", "Stub Systems")
replace(root, "What happens here + which AI tool / prompt you used",
        "4 FastAPI stubs with rate limits, auth, permissive search, seed data with different per-customer rates.")
replace(root, "Step / Phase", "Write ADRs")
replace(root, "What happens here + which AI tool / prompt you used",
        "ADR-001 (architecture), ADR-002 (authorization), ADR-003 (unattended operation: DENY). Each with negative consequences.")
replace(root, "Step / Phase", "Deploy & Verify")
replace(root, "What happens here + which AI tool / prompt you used",
        "Docker + Render. MCP registration demonstrated. Agent selects tools at runtime. 158/158 tests passing.")
contents['ppt/slides/slide4.xml'] = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
print("  Slide 4 (Approach): fixed")

# --- SLIDE 9: Evidence (uses ASCII [ paste link ]) ---
root = etree.fromstring(contents['ppt/slides/slide9.xml'])
replace(root, "[ paste link ]", "https://github.com/rajlanjewar01/kestrel-mcp-gateway")
replace(root, "[ paste link ]", "https://kestrel-mcp-gateway-1.onrender.com/mcp")
replace(root, "[ paste link ]", "docs/agent-transcript.md (in repo)")
replace(root, "[ paste link ]", "docs/pytest-output.txt | docs/audit-log-samples.json")
contents['ppt/slides/slide9.xml'] = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
print("  Slide 9 (Evidence): fixed")

# --- SLIDE 12: Reflection (straight quotes, combined before/after line) ---
root = etree.fromstring(contents['ppt/slides/slide12.xml'])
replace(root, '"Before this program, I thought AI was …"',
        '"Before this program, I thought AI was a code-generation tool — useful for boilerplate, risky for anything architectural."')
replace(root, '"Now I know it is …"',
        '"Now I know it is an architectural component that needs the same governance as any shared platform: access control, composition analysis, credential isolation, and audit."')
replace(root, '[ … ]',
        'The hardest part is composition. Each team’s access is reasonable alone; combined, they leak data nobody intended to grant.')
# The before/after confidence is one paragraph: "Before: __ /10        After: __ /10"
replace(root, 'Before: __ /10        After: __ /10',
        'Before: 6 /10        After: 9 /10')
replace(root, '[ … ]',
        'Draft your ADR before writing code. If you cannot state the decision, you are not ready to build.')
contents['ppt/slides/slide12.xml'] = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
print("  Slide 12 (Reflection): fixed")

# --- SLIDE 11: Self-Rating (check if still has ____) ---
root = etree.fromstring(contents['ppt/slides/slide11.xml'])
# Check
for para in root.findall('.//a:p', NSMAP):
    full = get_para_text(para)
    if '____' in full:
        print(f"  Slide 11 still has placeholder: {repr(full[:80])}")
# The ____ / 30 may be in a combined paragraph
replace(root, '____ / 30', '15 / 30')
replace(root, '____ / 30', '22 / 30')
replace(root, '____ / 30', '28 / 30')
replace(root, '____ / 30', '27 / 30')
replace(root, '____ / 30', 'N/A')
replace(root, '____ / 150', '92 / 150')
replace(root, 'I demonstrated ____ of 5 topics',
        'I demonstrated 3 of 5 topics: MCP Design, AI Governance, Agentic Architecture')
contents['ppt/slides/slide11.xml'] = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
print("  Slide 11 (Self-Rating): re-checked")

with zipfile.ZipFile(DST, 'w', zipfile.ZIP_DEFLATED) as zout:
    for name, data in contents.items():
        zout.writestr(name, data)

print(f"\nSaved: {DST}")
