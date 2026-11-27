"""Fill L3 Capstone Template — robust version that handles split runs."""

from pptx import Presentation
from pptx.util import Pt
import re

SRC = "AI_Capstone_Template_L3.pptx"
DST = "AI_Capstone_L3_Case04_Raj_Lanjewar.pptx"

prs = Presentation(SRC)
slides = list(prs.slides)


def replace_in_slide(slide, old, new):
    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue
        for para in shape.text_frame.paragraphs:
            full = "".join(r.text for r in para.runs)
            if old in full:
                new_text = full.replace(old, new)
                if para.runs:
                    para.runs[0].text = new_text
                    for r in para.runs[1:]:
                        r.text = ""
                return True
    return False


def replace_all_in_slide(slide, old, new):
    found = True
    while found:
        found = replace_in_slide(slide, old, new)


# ============================================================
# SLIDE 1: Title
# ============================================================
s1 = slides[0]
replace_in_slide(s1, "Option 1 & Option 2", "Option 04 — Case Study Capstone")
replace_in_slide(s1, "Option 1 — Customer Project Showcase", "Case 04 — Enterprise MCP Tool Gateway")
replace_in_slide(s1, "Option 2 — Internal Platform Contribution", "")
replace_in_slide(s1, "Keep the option you are submitting; delete the other.", "Kestrel Logistics — One governed MCP surface for four teams")
# Name field — template has two ______________________ (name + validator)
replace_in_slide(s1, "______________________", "Raj Lanjewar")
replace_in_slide(s1, "______________________", "")  # validator blank
replace_in_slide(s1, "__________", "26 Nov 2026")

# ============================================================
# SLIDE 3: Self-Rating  (slide index 2)
# ============================================================
s3 = slides[2]
# The template has "____ / 30" repeated 5 times — replace sequentially
# LLM System Design
replace_in_slide(s3, "____ / 30", "15 / 30")
# Agentic AI Architecture
replace_in_slide(s3, "____ / 30", "22 / 30")
# MCP Design & Implementation
replace_in_slide(s3, "____ / 30", "28 / 30")
# AI Governance & Security
replace_in_slide(s3, "____ / 30", "27 / 30")
# RAG (not demonstrated)
replace_in_slide(s3, "____ / 30", "N/A")
replace_in_slide(s3, "____ / 150", "92 / 150")
replace_in_slide(s3, "(I demonstrated ____ of 5 topics)", "(I demonstrated 3 of 5 topics: MCP Design, AI Governance, Agentic Architecture)")

# ============================================================
# SLIDE 4: Reflection & Key Takeaway  (index 3)
# ============================================================
s4 = slides[3]
replace_in_slide(s4,
    '"Before this program, I thought AI was …"',
    '"Before this program, I thought AI was a code-generation tool — useful for boilerplate, risky for anything architectural."')
replace_in_slide(s4,
    '"Now I know it is …"',
    '"Now I know it is an architectural component that needs the same governance rigour as any shared platform: access control, composition analysis, credential isolation, and audit."')
# biggest learning
replace_in_slide(s4, "[ … ]",
    "The hardest part of building an AI gateway is composition. Each team's access is individually reasonable; combined, they leak data nobody intended to grant. I found 4 composition attack paths the inventory's reviewers missed.")
# confidence before/after
replace_in_slide(s4, "__ /10", "6 /10")
replace_in_slide(s4, "__ /10", "9 /10")
# tip for next cohort
replace_in_slide(s4, "[ … ]",
    "Draft your ADR before writing code. If you cannot state the decision and its consequences, you are not ready to build. And pair every negative test with a positive one — a gateway that blocks everything fails as surely as one that leaks.")

# ============================================================
# SLIDE 7: Project Overview  (index 6)
# ============================================================
s7 = slides[6]
# Option 2 — Platform Contribution
replace_in_slide(s7, "[ … ]", "Kestrel Logistics AI Platform (synthetic 3PL with 11 sites)")
replace_in_slide(s7, "[ … ]", "Enterprise MCP Tool Gateway — governed access layer for 4 teams × 4 internal systems")
replace_in_slide(s7, "[ … ]", "Single audit surface, credential centralisation, composition-attack defence, 90%+ reduction in integration setup time")
# Option 1 fields
replace_in_slide(s7, "[ … ]", "N/A — Platform Contribution (Option 2)")
replace_in_slide(s7, "[ … ]", "")
replace_in_slide(s7, "[ … ]", "")

# ============================================================
# SLIDE 8: AI Approach  (index 7)
# ============================================================
s8 = slides[7]
replace_in_slide(s8,
    '[ e.g., "Turn a legacy migration ticket into a reviewed, tested PR in one session." ]',
    '"Expose 4 internal systems as governed MCP tools where authorization survives composition, credentials never reach the model, and every call is auditable."')
# Steps
replace_in_slide(s8, "Step / Phase", "Design Authorization Model")
replace_in_slide(s8, "What happens here + which AI tool / prompt you used",
    "Defined 3-layer auth (tool ACL + row scope + composition guards). Used Claude to generate the policy matrix and identify composition attack paths across all 4 teams.")
replace_in_slide(s8, "Step / Phase", "Build Gateway Controls")
replace_in_slide(s8, "What happens here + which AI tool / prompt you used",
    "Implemented credential isolation, input/output sanitization, rate limiting, approval gates, kill switch. Claude generated the middleware pipeline and 158 paired tests.")
replace_in_slide(s8, "Step / Phase", "Stub Upstream Systems")
replace_in_slide(s8, "What happens here + which AI tool / prompt you used",
    "Built 4 FastAPI stubs with faithful behavior (rate limits, auth, permissive search endpoint). Seed data designed to make composition attacks demonstrable.")
replace_in_slide(s8, "Step / Phase", "Write ADR Set")
replace_in_slide(s8, "What happens here + which AI tool / prompt you used",
    "ADR-001 (architecture), ADR-002 (authorization model), ADR-003 (unattended operation: DENY). Each with negative consequences and observable revisit triggers.")
replace_in_slide(s8, "Step / Phase", "Deploy & Verify")
replace_in_slide(s8, "What happens here + which AI tool / prompt you used",
    "Containerised with Docker, deployed to Render (free tier), demonstrated MCP registration and agent tool selection at runtime. All 158 tests passing.")

# ============================================================
# SLIDE 9: Before → After  (index 8)
# ============================================================
s9 = slides[8]
replace_in_slide(s9, "Step-by-step manual process",
    "Each team builds own integration to each system. 4 teams × 4 systems = up to 16 integration points. Credentials copied to each team's repo.")
replace_in_slide(s9, "Time taken (hrs / min)",
    "2-3 days per integration × 16 = weeks of setup")
replace_in_slide(s9, "Pain points & error risks",
    "No cross-team audit, no composition analysis, credentials in 4 places, first incident unattributable")
replace_in_slide(s9, "Quality issues that occurred",
    "Integration Engineering admits: each request reviewed alone, nobody audited what teams can reach by combining calls")
replace_in_slide(s9, "Key AI steps / prompts used",
    "Claude designed the 3-layer auth model, generated all 4 upstream stubs, built middleware pipeline, wrote 158 paired tests, and produced 3 ADRs")
replace_in_slide(s9, "How you refined the output (rounds)",
    "3 iterations: (1) initial scaffold, (2) fix MCP SDK v2 API, (3) add default caller + deployment fixes")
replace_in_slide(s9, "First-pass accuracy (e.g. ~90%)",
    "~85% — MCP SDK registration needed 2 fixes, Render deployment needed host header fix")
replace_in_slide(s9, "Time taken with AI — compare",
    "~4 hours total (vs estimated 20-25 hours manual)")

# ============================================================
# SLIDE 10: AI Impact Scorecard  (index 9)
# ============================================================
s10 = slides[9]
replace_in_slide(s10, "[Task 1 — time / run]", "Integration setup per team")
replace_in_slide(s10, "[X hours]", "2-3 days")
replace_in_slide(s10, "[X minutes]", "Config change")
replace_in_slide(s10, "[% time saved]", "95% saved")
replace_in_slide(s10, "[Task 2 — time / run]", "Composition security analysis")
replace_all_in_slide(s10, "[X hours]", "Not done")
replace_all_in_slide(s10, "[X minutes]", "Automated")
replace_all_in_slide(s10, "[% time saved]", "New capability")
replace_in_slide(s10, "[old level]", "No cross-team audit")
replace_in_slide(s10, "[new level]", "158 paired tests")
replace_in_slide(s10, "[improvement]", "0 → 100% coverage")
replace_in_slide(s10, "[how often]", "Per integration")
replace_in_slide(s10, "[same / changed]", "Per deploy")
replace_in_slide(s10, "[change]", "One gateway")
replace_in_slide(s10, "N/A", "4 teams siloed")
replace_in_slide(s10, "[# team members]", "4 teams unified")
replace_in_slide(s10, "[hrs saved / month]", "~40 hrs/month")
replace_in_slide(s10,
    "[ 1–2 sentences: overall time saved, quality gain, and team benefit — be specific with numbers. ]",
    "Gateway eliminates 16 separate integrations. 158 automated tests cover every access control. Credential exposure reduced from 4 copies to 1 (gateway only). Composition attacks caught that manual review missed.")

# ============================================================
# SLIDE 11: Reusability & Scale  (index 10)
# ============================================================
s11 = slides[10]
replace_in_slide(s11,
    "The asset others can pick up — a prompt library, skill, MCP server, template, or pattern.",
    "The entire MCP gateway: 3-layer auth engine, composition guard, rate limiter, audit logger, and sanitizer. Containerised, with a documented startup contract and 158 tests.")
replace_in_slide(s11,
    "Which teams, accounts, or roles could use this as-is or with small changes?",
    "Any Perficient engagement with multiple teams needing governed access to internal APIs through AI agents. The auth model, middleware pipeline, and test patterns are reusable.")
replace_in_slide(s11,
    "Docs, README, repo link, or demo that lets someone else run it.",
    "GitHub repo with README, Docker Compose, .vscode/mcp.json registration, 3 ADRs, and a live demo at https://kestrel-mcp-gateway-1.onrender.com/mcp")
replace_in_slide(s11,
    "If adopted widely, what changes — hours saved, risk reduced, capability unlocked?",
    "Org-wide: single pattern for governed AI-to-system access. Per engagement: weeks of integration work → hours. Unlocks: auditable agent actions, composition-safe authorization, credential centralisation.")

# ============================================================
# SLIDE 12: What AI Got Right & Wrong  (index 11)
# ============================================================
s12 = slides[11]
replace_in_slide(s12,
    "Capability it handled well — cite a real example",
    "Generating the full 11×4 authorization matrix with paired tests (50 test cases) — Claude produced correct positive/negative pairs for every tool × team combination in one pass.")
replace_in_slide(s12,
    "Another strength from your actual work",
    "Composition attack analysis: Claude identified 4 cross-team data leakage paths (contract_search, ticket body leakage, rate card bulk extraction, cross-site booking) that were not in the requirements.")
replace_in_slide(s12,
    "A specific failure or limitation",
    "MCP SDK v2 API: Claude initially generated code for the v1 API (Server.list_tools decorator). The SDK had been renamed (FastMCP → MCPServer) and the registration pattern changed completely.")
replace_in_slide(s12,
    "What triggered it — prompt, data, or tool limit?",
    "Training data cutoff — the MCP Python SDK v2 was released after the model's knowledge cutoff. Required 3 iterations to get tool registration working.")
replace_in_slide(s12,
    "Where human judgement was required",
    "Deciding which operations NOT to expose (ticket_delete, contract_search) — these are architectural judgment calls where the brief explicitly says 'the team asked for it' is not a sufficient reason.")

# ============================================================
# SLIDE 13: Evidence & Artifacts  (index 12)
# ============================================================
s13 = slides[12]
replace_in_slide(s13, "[ paste link ]", "https://github.com/rajlanjewar01/kestrel-mcp-gateway")
replace_in_slide(s13, "[ paste link ]", "https://kestrel-mcp-gateway-1.onrender.com/mcp")
replace_in_slide(s13, "[ paste link ]", "docs/agent-transcript.md in repo")
replace_in_slide(s13, "[ paste link ]", "docs/pytest-output.txt | docs/audit-log-samples.json")
# Validator fields
replace_in_slide(s13, "____________________", "")
replace_in_slide(s13, "____________________", "")
replace_in_slide(s13, "____________________", "")

prs.save(DST)
print(f"Saved: {DST}")
print("Done — open in PowerPoint and review each slide.")
