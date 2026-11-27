"""Fill L3 Capstone PPT — correct slide mapping."""

import re
import zipfile
from lxml import etree

SRC = "AI_Capstone_Template_L3.pptx"
DST = "AI_Capstone_L3_Case04_Raj_Lanjewar.pptx"

NSMAP = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}

# Visual order -> XML file mapping:
# 1  -> slide1  Title
# 2  -> slide2  How to Use (delete instructions)
# 3  -> slide3  Project Overview
# 4  -> slide4  AI Approach
# 5  -> slide5  Before/After
# 6  -> slide6  Impact Scorecard
# 7  -> slide7  Reusability
# 8  -> slide8  Right & Wrong
# 9  -> slide9  Evidence
# 10 -> slide10 Rubric (reference)
# 11 -> slide11 Self-Rating
# 12 -> slide12 Reflection
# 13 -> slide13 Validation (validator fills)


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


def replace_all(root, old, new):
    for para in root.findall('.//a:p', NSMAP):
        full = get_para_text(para)
        if old in full:
            set_para_text(para, full.replace(old, new))


# Read all files
with zipfile.ZipFile(SRC, 'r') as zin:
    contents = {n: zin.read(n) for n in zin.namelist()}

def process(slide_file, label, func):
    root = etree.fromstring(contents[slide_file])
    func(root)
    contents[slide_file] = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
    print(f"  {label}: filled")

# --- SLIDE 1: Title (slide1.xml) ---
def fill_title(r):
    replace(r, "Option 1 & Option 2", "Option 04 — Case Study Capstone")
    replace(r, "Option 1 — Customer Project Showcase", "Case 04 — Enterprise MCP Tool Gateway")
    replace(r, "Option 2 — Internal Platform Contribution", "")
    replace(r, "Keep the option you are submitting; delete the other.",
            "Kestrel Logistics — One governed MCP surface for four teams")
    replace(r, "______________________", "Raj Lanjewar")
    replace(r, "______________________", "")
    replace(r, "__________", "26 Nov 2026")
process('ppt/slides/slide1.xml', 'Slide 1 (Title)', fill_title)

# --- SLIDE 3: Project Overview (slide3.xml) ---
def fill_overview(r):
    replace(r, "[ … ]", "N/A (Platform Contribution)")
    replace(r, "[ … ]", "N/A")
    replace(r, "[ … ]", "N/A")
    replace(r, "[ … ]", "Kestrel Logistics AI Platform (synthetic 3PL, 11 warehouse sites)")
    replace(r, "[ … ]", "Enterprise MCP Tool Gateway — one governed surface where 4 teams access 4 internal systems through 11 curated MCP tools with 3-layer authorization, credential isolation, and composition-attack defence.")
    replace(r, "[ … ]", "Eliminated 16 separate integrations. Single audit surface. Credentials: 4 copies → 1. 158 automated tests. Composition attacks caught that manual review missed.")
process('ppt/slides/slide3.xml', 'Slide 3 (Overview)', fill_overview)

# --- SLIDE 4: AI Approach (slide4.xml) ---
def fill_approach(r):
    replace(r, '[ e.g., “Turn a legacy migration ticket into a reviewed, tested PR in one session.” ]',
            '“Expose 4 internal systems as governed MCP tools where authorization survives composition, credentials never reach the model, and every call is auditable.”')
    replace(r, "Step / Phase", "Design Auth Model")
    replace(r, "What happens here + which AI tool / prompt you used",
            "3-layer auth (tool ACL + row scope + composition guards). Claude generated policy matrix and identified 4 composition attack paths.")
    replace(r, "Step / Phase", "Build Controls")
    replace(r, "What happens here + which AI tool / prompt you used",
            "Credential isolation, sanitization, rate limiting, approval gates, kill switch. Claude built middleware pipeline and 158 paired tests.")
    replace(r, "Step / Phase", "Stub Systems")
    replace(r, "What happens here + which AI tool / prompt you used",
            "4 FastAPI stubs with faithful behavior: rate limits, auth, permissive search, seed data with different per-customer rates.")
    replace(r, "Step / Phase", "Write ADRs")
    replace(r, "What happens here + which AI tool / prompt you used",
            "ADR-001 (architecture), ADR-002 (authorization), ADR-003 (unattended operation: DENY). Each with negative consequences.")
    replace(r, "Step / Phase", "Deploy & Verify")
    replace(r, "What happens here + which AI tool / prompt you used",
            "Docker + Render free tier. MCP registration demonstrated. Agent selects tools at runtime. 158/158 tests passing.")
process('ppt/slides/slide4.xml', 'Slide 4 (Approach)', fill_approach)

# --- SLIDE 5: Before/After (slide5.xml) ---
def fill_before_after(r):
    replace(r, "Step-by-step manual process",
            "Each team builds own integration (4×4=16 points). Credentials copied to each repo. No cross-team audit.")
    replace(r, "Time taken (hrs / min)", "2–3 days per integration × 16 = weeks")
    replace(r, "Pain points & error risks", "No composition analysis, credentials in 4 places, first incident unattributable")
    replace(r, "Quality issues that occurred", "Each request reviewed alone — nobody audited what teams reach by combining calls")
    replace(r, "Key AI steps / prompts used",
            "Claude designed 3-layer auth, generated 4 stubs, middleware pipeline, 158 tests, and 3 ADRs")
    replace(r, "How you refined the output (rounds)", "3 iterations: scaffold → MCP SDK v2 fix → deployment fixes")
    replace(r, "First-pass accuracy (e.g. ~90%)", "~85% — MCP SDK registration needed 2 fixes")
    replace(r, "Time taken with AI — compare", "~4 hours total (vs 20–25 hours manual)")
process('ppt/slides/slide5.xml', 'Slide 5 (Before/After)', fill_before_after)

# --- SLIDE 6: Impact Scorecard (slide6.xml) ---
def fill_scorecard(r):
    replace(r, "[Task 1 — time / run]", "Integration setup/team")
    replace(r, "[X hours]", "2–3 days")
    replace(r, "[X minutes]", "Config change")
    replace(r, "[% time saved]", "95% saved")
    replace(r, "[Task 2 — time / run]", "Composition analysis")
    replace_all(r, "[X hours]", "Not done")
    replace_all(r, "[X minutes]", "Automated")
    replace_all(r, "[% time saved]", "New capability")
    replace(r, "[old level]", "No cross-team audit")
    replace(r, "[new level]", "158 paired tests")
    replace(r, "[improvement]", "0 → 100% coverage")
    replace(r, "[how often]", "Per integration")
    replace(r, "[same / changed]", "Per deploy")
    replace(r, "[change]", "One gateway")
    replace(r, "N/A", "4 teams siloed")
    replace(r, "[# team members]", "4 teams unified")
    replace(r, "[hrs saved / month]", "~40 hrs/month")
    replace(r, "[ 1–2 sentences: overall time saved, quality gain, and team benefit — be specific with numbers. ]",
            "Gateway eliminates 16 integrations. 158 tests cover every access control. Credentials: 4→1. Composition attacks caught that manual review missed.")
process('ppt/slides/slide6.xml', 'Slide 6 (Scorecard)', fill_scorecard)

# --- SLIDE 7: Reusability (slide7.xml) ---
def fill_reusability(r):
    replace(r, "The asset others can pick up — a prompt library, skill, MCP server, template, or pattern.",
            "The entire MCP gateway: 3-layer auth engine, composition guard, rate limiter, audit logger, sanitizer. Containerised with 158 tests.")
    replace(r, "Which teams, accounts, or roles could use this as-is or with small changes?",
            "Any Perficient engagement with multiple teams needing governed AI agent access to internal APIs.")
    replace(r, "Docs, README, repo link, or demo that lets someone else run it.",
            "GitHub repo, Docker Compose, .vscode/mcp.json, 3 ADRs, live demo at https://kestrel-mcp-gateway-1.onrender.com/mcp")
    replace(r, "If adopted widely, what changes — hours saved, risk reduced, capability unlocked?",
            "Single pattern for governed AI-to-system access. Per engagement: weeks → hours. Unlocks: auditable agents, composition-safe auth, credential centralisation.")
process('ppt/slides/slide7.xml', 'Slide 7 (Reusability)', fill_reusability)

# --- SLIDE 8: Right & Wrong (slide8.xml) ---
def fill_right_wrong(r):
    replace(r, "Capability it handled well — cite a real example",
            "Generated 11×4 authorization matrix with 50 paired tests — correct positive/negative for every tool×team in one pass.")
    replace(r, "Another strength from your actual work",
            "Identified 4 composition attack paths (contract_search, ticket body leakage, rate card extraction, cross-site booking) not in the requirements.")
    replace(r, "A specific failure or limitation",
            "MCP SDK v2: Claude generated v1 code (Server.list_tools). SDK renamed FastMCP → MCPServer. Required 3 iterations to fix.")
    replace(r, "What triggered it — prompt, data, or tool limit?",
            "Training data cutoff — MCP Python SDK v2 released after model’s knowledge cutoff.")
    replace(r, "Where human judgement was required",
            "Deciding which operations NOT to expose (ticket_delete, contract_search) — judgment calls where “the team asked for it” is not sufficient reason.")
process('ppt/slides/slide8.xml', 'Slide 8 (Right/Wrong)', fill_right_wrong)

# --- SLIDE 9: Evidence (slide9.xml) ---
def fill_evidence(r):
    replace(r, "[ paste link ]", "https://github.com/rajlanjewar01/kestrel-mcp-gateway")
    replace(r, "[ paste link ]", "https://kestrel-mcp-gateway-1.onrender.com/mcp")
    replace(r, "[ paste link ]", "docs/agent-transcript.md (in repo)")
    replace(r, "[ paste link ]", "docs/pytest-output.txt | docs/audit-log-samples.json")
process('ppt/slides/slide9.xml', 'Slide 9 (Evidence)', fill_evidence)

# --- SLIDE 11: Self-Rating (slide11.xml) ---
def fill_rating(r):
    replace(r, "____ / 30", "15 / 30")   # LLM
    replace(r, "____ / 30", "22 / 30")   # Agentic
    replace(r, "____ / 30", "28 / 30")   # MCP
    replace(r, "____ / 30", "27 / 30")   # Governance
    replace(r, "____ / 30", "N/A")        # RAG
    replace(r, "____ / 150", "92 / 150")
    replace(r, "I demonstrated ____ of 5 topics",
            "I demonstrated 3 of 5 topics: MCP Design, AI Governance, Agentic Architecture")
process('ppt/slides/slide11.xml', 'Slide 11 (Self-Rating)', fill_rating)

# --- SLIDE 12: Reflection (slide12.xml) ---
def fill_reflection(r):
    replace(r, '“Before this program, I thought AI was …”',
            '“Before this program, I thought AI was a code-generation tool — useful for boilerplate, risky for anything architectural.”')
    replace(r, '“Now I know it is …”',
            '“Now I know it is an architectural component that needs the same governance rigour as any shared platform: access control, composition analysis, credential isolation, and audit.”')
    replace(r, '[ … ]',
            'The hardest part of building an AI gateway is composition. Each team’s access is individually reasonable; combined, they leak data nobody intended to grant.')
    replace(r, '__ /10', '6 /10')
    replace(r, '__ /10', '9 /10')
    replace(r, '[ … ]',
            'Draft your ADR before writing code. If you cannot state the decision and its consequences, you are not ready to build.')
process('ppt/slides/slide12.xml', 'Slide 12 (Reflection)', fill_reflection)

# Write output
with zipfile.ZipFile(DST, 'w', zipfile.ZIP_DEFLATED) as zout:
    for name, data in contents.items():
        zout.writestr(name, data)

print(f"\nSaved: {DST}")
print("Open in PowerPoint. Delete Slide 2 (How to Use). Slides 10 & 13 are for reference/validator.")
