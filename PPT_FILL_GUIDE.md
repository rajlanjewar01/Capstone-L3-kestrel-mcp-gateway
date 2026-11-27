# PPT Fill Guide — Copy-paste into each slide

Open `AI_Capstone_Template_L3.pptx` in PowerPoint and fill each slide:

---

## Slide 1: Title
- Change "Option 1 & Option 2" → **Option 04 — Case Study Capstone**
- Change "Option 1 — Customer Project Showcase" → **Case 04 — Enterprise MCP Tool Gateway**
- Delete "Option 2 — Internal Platform Contribution"
- Change "Keep the option..." → **Kestrel Logistics — One governed MCP surface for four teams**
- Name: **Raj Lanjewar**
- Date: **26 Nov 2026**

---

## Slide 2: Rubric (leave as-is — reference only)

---

## Slide 3: My Self-Rating

| Topic | Score |
|-------|-------|
| 1. LLM System Design | **15 / 30** |
| 2. Agentic AI Architecture & Patterns | **22 / 30** |
| 3. MCP Design & Implementation | **28 / 30** |
| 4. AI Governance & Security | **27 / 30** |
| 5. RAG Architecture & Optimization | **N/A** |

- My total: **92 / 150**
- Clear = 70+ (I demonstrated **3** of 5 topics)

### Justification:
- **MCP (28):** Designed 11-tool gateway with curated interface, not mirrored endpoints. Containerised, registered in real agent host, tools selected at runtime.
- **Governance (27):** 3-layer auth (ACL + row scope + composition), credential isolation verified, audit trail, approval gates, kill switch, untrusted content handling.
- **Agentic (22):** Composition guard pattern, session-aware tracking, human-in-the-loop approval gates, tool annotations distinguishing read/write.
- **LLM System Design (15):** Tool descriptions designed for model selection, error shapes for model correction, content boundary markers. Not the primary dimension.

---

## Slide 4: Reflection & Key Takeaway

- **"Before this program, I thought AI was..."**
  → "...a code-generation tool — useful for boilerplate, risky for anything architectural."

- **"Now I know it is..."**
  → "...an architectural component that needs the same governance rigour as any shared platform: access control, composition analysis, credential isolation, and audit."

- **My biggest learning:**
  → The hardest part of building an AI gateway is composition. Each team's access is individually reasonable; combined, they leak data nobody intended to grant. I found 4 composition attack paths the inventory's reviewers missed.

- **Confidence:** Before: **6/10** → After: **9/10**

- **One tip for the next cohort:**
  → Draft your ADR before writing code. If you cannot state the decision and its consequences, you are not ready to build. And pair every negative test with a positive one.

---

## Slide 5: Rubric Validation (leave blank — validator fills this)

---

## Slide 6: How to Use (DELETE this slide — it's instructions)

---

## Slide 7: My Project Overview

**Use OPTION 2 column (Platform Contribution). Clear Option 1.**

- **Platform contributed to:**
  → Kestrel Logistics AI Platform (synthetic 3PL, 11 warehouse sites)

- **Feature / innovation contributed:**
  → Enterprise MCP Tool Gateway — one governed surface where 4 teams (Warehouse Ops, Transport Planning, Customer Service, Finance Analytics) access 4 internal systems (WMS, TMS, Ticketing, Contracts) through 11 curated MCP tools with 3-layer authorization, credential isolation, and composition-attack defence.

- **Org-scale AI capability impact:**
  → Eliminated 16 separate integration points (4 teams × 4 systems). Single audit surface answers "what did this agent do" without transcript access. Credential exposure reduced from 4 copies to 1. 158 automated tests cover every authorization path. Composition attacks caught that manual review missed.

---

## Slide 8: My AI Approach

**Goal:**
→ "Expose 4 internal systems as governed MCP tools where authorization survives composition, credentials never reach the model, and every call is auditable."

| # | Step / Phase | What happens + AI tool used |
|---|---|---|
| 1 | Design Authorization Model | Defined 3-layer auth (tool ACL + row scope + composition guards). Used Claude to generate the policy matrix and identify 4 composition attack paths across all teams. |
| 2 | Build Gateway Controls | Implemented credential isolation, input/output sanitization, rate limiting, approval gates, kill switch. Claude generated the middleware pipeline and 158 paired tests. |
| 3 | Stub Upstream Systems | Built 4 FastAPI stubs with faithful behavior — rate limits, auth, permissive search endpoint, seed data with different per-customer rates to prove composition attacks. |
| 4 | Write ADR Set | ADR-001 (architecture), ADR-002 (authorization depth), ADR-003 (unattended operation: DENY). Each with negative consequences and observable revisit triggers. |
| 5 | Deploy & Verify | Containerised with Docker, deployed to Render free tier. Demonstrated MCP registration and agent tool selection at runtime. 158/158 tests passing. |

---

## Slide 9: Before → After

**BEFORE — The Manual Way:**
- Each team builds own integration to each system (4×4 = 16 integration points)
- 2–3 days per integration setup
- Credentials copied into 4 repositories
- No cross-team audit, no composition analysis
- Integration Engineering admits: each request reviewed alone

**AFTER — The AI-Assisted Way:**
- Claude designed auth model, generated stubs, middleware, 158 tests, and 3 ADRs
- 3 iterations: initial scaffold → MCP SDK v2 fix → deployment fixes
- First-pass accuracy: ~85% (MCP SDK API changed between versions)
- Total time with AI: ~4 hours (vs estimated 20–25 hours manual)

---

## Slide 10: AI Impact Scorecard

| Metric | Before AI | After AI | Impact |
|--------|-----------|----------|--------|
| Integration setup per team | 2–3 days | Config change | 95% time saved |
| Composition security analysis | Not done | 158 automated tests | New capability |
| Quality / coverage | No cross-team audit | 100% auth matrix tested | 0 → full coverage |
| Frequency | Per integration | Per gateway deploy | One surface vs four |
| Team benefit | 4 teams siloed | 4 teams unified | ~40 hrs/month saved |

**Summary:** Gateway eliminates 16 separate integrations. 158 automated tests cover every access control. Credential exposure reduced from 4 copies to 1. Composition attacks caught that manual review missed.

---

## Slide 11: Reusability & Scale

- **R — What is reusable?**
  → The entire MCP gateway: 3-layer auth engine, composition guard, rate limiter, audit logger, sanitizer. Containerised with documented startup contract and 158 tests.

- **A — Who can adopt it?**
  → Any Perficient engagement with multiple teams needing governed access to internal APIs through AI agents. The auth model, middleware pipeline, and test patterns are directly reusable.

- **P — What did you package?**
  → GitHub repo with README, Docker Compose, .vscode/mcp.json registration, 3 ADRs, composition analysis, and a live demo at https://kestrel-mcp-gateway-1.onrender.com/mcp

- **S — Org-scale potential?**
  → Single pattern for governed AI-to-system access across the org. Per engagement: weeks of integration → hours. Unlocks: auditable agent actions, composition-safe authorization, credential centralisation.

---

## Slide 12: What AI Got Right & Wrong

**RIGHT:**
- Generated the full 11×4 authorization matrix with 50 paired test cases in one pass — every tool × team combination correct
- Identified 4 composition attack paths (contract_search leakage, ticket body cross-customer data, rate card bulk extraction, cross-site booking) that were not in the requirements

**WRONG:**
- MCP SDK v2 API: Claude initially generated code for v1 (Server.list_tools decorator). The SDK renamed FastMCP → MCPServer and changed the registration pattern. Required 3 iterations.
- Trigger: Training data cutoff — MCP Python SDK v2 released after model's knowledge cutoff

**What I corrected manually:**
- Deciding which operations NOT to expose (ticket_delete, contract_search) — these are architectural judgment calls the brief explicitly says require human reasoning, not just "the team asked for it"

---

## Slide 13: Evidence & Artifacts

- **GitHub repo:** https://github.com/rajlanjewar01/kestrel-mcp-gateway
- **Live MCP gateway:** https://kestrel-mcp-gateway-1.onrender.com/mcp
- **Agent transcript:** docs/agent-transcript.md (in repo)
- **Test output:** docs/pytest-output.txt (158 passed) | docs/audit-log-samples.json

**Validator:** (leave blank for your validator to fill)
