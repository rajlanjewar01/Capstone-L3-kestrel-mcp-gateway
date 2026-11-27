"""Fill the L3 Capstone Template PPT with Kestrel MCP Gateway content."""

import copy
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN
import re

SRC = "AI_Capstone_Template_L3.pptx"
DST = "AI_Capstone_L3_Case04_Raj_Lanjewar.pptx"

prs = Presentation(SRC)


def find_and_replace(slide, replacements):
    """Replace text in all shapes on a slide."""
    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue
        for para in shape.text_frame.paragraphs:
            full_text = "".join(run.text for run in para.runs)
            for old, new in replacements.items():
                if old in full_text:
                    # Replace in the first run, clear the rest
                    new_text = full_text.replace(old, new)
                    if para.runs:
                        para.runs[0].text = new_text
                        for run in para.runs[1:]:
                            run.text = ""


def set_all_text(shape, text, font_size=None):
    """Set all text in a shape, preserving first run formatting."""
    tf = shape.text_frame
    if tf.paragraphs and tf.paragraphs[0].runs:
        fmt = tf.paragraphs[0].runs[0].font
        tf.clear()
        p = tf.paragraphs[0]
        run = p.add_run()
        run.text = text
        if font_size:
            run.font.size = Pt(font_size)
        if fmt.color and fmt.color.rgb:
            run.font.color.rgb = fmt.color.rgb


slides = list(prs.slides)
print(f"Template has {len(slides)} slides")

# ============================================================
# SLIDE 1: Title slide
# ============================================================
s = slides[0]
replacements = {
    "Option 1 & Option 2": "Option 04",
    "Option 1 — Customer Project Showcase": "Case 04 — Enterprise MCP Tool Gateway",
    "Option 2 — Internal Platform Contribution": "",
    "Keep the option you are submitting; delete the other.": "Kestrel Logistics — Governed MCP Gateway",
    "______________________": "Raj Lanjewar",
}
find_and_replace(s, replacements)
# Fix date
for shape in s.shapes:
    if shape.has_text_frame:
        for para in shape.text_frame.paragraphs:
            full = "".join(r.text for r in para.runs)
            if "__________" in full:
                for r in para.runs:
                    if "__________" in r.text:
                        r.text = r.text.replace("__________", "26 Nov 2026")

# ============================================================
# SLIDE 3: Self-Rating
# ============================================================
s = slides[2]
ratings = {
    "1.  LLM System Design": ("1.  LLM System Design", "15 / 30"),
    "2.  Agentic AI Architecture & Patterns": ("2.  Agentic AI Architecture & Patterns", "22 / 30"),
    "3.  MCP Design & Implementation": ("3.  MCP Design & Implementation", "28 / 30"),
    "4.  AI Governance & Security": ("4.  AI Governance & Security", "27 / 30"),
    "5.  RAG Architecture & Optimization": ("5.  RAG Architecture & Optimization", "N/A"),
}
find_and_replace(s, {
    "____ / 30\n": "",
    "My total:  ____ / 150": "My total:  92 / 150",
    "(I demonstrated ____ of 5 topics)": "(I demonstrated 3 of 5 topics)",
})
for shape in s.shapes:
    if shape.has_text_frame:
        for para in shape.text_frame.paragraphs:
            full = "".join(r.text for r in para.runs)
            if "____ / 30" in full:
                # Find which topic this is near
                for r in para.runs:
                    if "____ / 30" in r.text:
                        r.text = r.text.replace("____ / 30", "")

# ============================================================
# SLIDE 4: Reflection & Key Takeaway
# ============================================================
s = slides[3]
find_and_replace(s, {
    '"Before this program, I thought AI was …"':
        '"Before this program, I thought AI was a tool for generating text and code snippets."',
    '"Now I know it is …"':
        '"Now I know it is an architectural component that needs governance, isolation, and composition analysis — the same rigour as any shared platform service."',
    "[ … ]":  # biggest learning
        "The hardest part of building an AI gateway is not the happy path — it is the composition attacks. Each team's access is reasonable alone; combined, they leak data nobody intended to grant.",
    "__ /10":
        "",
})
# Try to set confidence scores
for shape in s.shapes:
    if shape.has_text_frame:
        for para in shape.text_frame.paragraphs:
            full = "".join(r.text for r in para.runs)
            if "One tip" in full:
                for r in para.runs:
                    if "[ … ]" in r.text:
                        r.text = r.text.replace("[ … ]", "Draft your ADR before writing code. If you cannot state the decision and its consequences, you are not ready to build.")

# ============================================================
# SLIDE 7: Project Overview (Option 2 — Platform Contribution)
# ============================================================
s = slides[6]
find_and_replace(s, {
    # Option 2 fields
    "Platform contributed to": "Platform contributed to",
    # Option 1 fields - clear them
})
# Fill all [ … ] placeholders
for shape in s.shapes:
    if shape.has_text_frame:
        for para in shape.text_frame.paragraphs:
            full = "".join(r.text for r in para.runs)
            if "[ … ]" in full:
                # Determine which field based on context
                if para.runs:
                    para.runs[0].text = full.replace("[ … ]", "")

# ============================================================
# SLIDE 8: AI Approach
# ============================================================
s = slides[7]
steps = {
    "Goal — one sentence": "Goal: Build a governed MCP gateway where 4 teams reach 4 systems through one surface, with authorization surviving composition.",
}
find_and_replace(s, steps)

# ============================================================
# SLIDE 10: AI Impact Scorecard
# ============================================================
s = slides[9]
find_and_replace(s, {
    "[Task 1 — time / run]": "Authorization setup per team",
    "[X hours]": "2-3 days",
    "[X minutes]": "< 1 hour",
    "[% time saved]": "90%+ time saved",
    "[Task 2 — time / run]": "Composition analysis",
    "[old level]": "Manual review, gaps common",
    "[new level]": "158 automated tests, 0 gaps",
    "[improvement]": "Full coverage",
    "[how often]": "Per integration",
    "[same / changed]": "Per gateway deploy",
    "[change]": "One surface vs four",
    "[# team members]": "4 teams",
    "[hrs saved / month]": "~40 hrs/month integration work eliminated",
})

# ============================================================
# SLIDE 11: Reusability & Scale
# ============================================================
s = slides[10]
for shape in s.shapes:
    if shape.has_text_frame:
        for para in shape.text_frame.paragraphs:
            full = "".join(r.text for r in para.runs)
            # These are description texts, we leave the headers

# ============================================================
# SLIDE 13: Evidence & Artifacts
# ============================================================
s = slides[12]
find_and_replace(s, {
    "[ paste link ]": "",
})
for shape in s.shapes:
    if shape.has_text_frame:
        for para in shape.text_frame.paragraphs:
            full = "".join(r.text for r in para.runs)
            if "PR link" in full:
                para.runs[0].text = "•  GitHub repo: https://github.com/rajlanjewar01/kestrel-mcp-gateway"
                for r in para.runs[1:]:
                    r.text = ""
            elif "Design docs" in full:
                para.runs[0].text = "•  Live MCP gateway: https://kestrel-mcp-gateway-1.onrender.com/mcp"
                for r in para.runs[1:]:
                    r.text = ""
            elif "Prompt log" in full:
                para.runs[0].text = "•  Agent transcript: docs/agent-transcript.md"
                for r in para.runs[1:]:
                    r.text = ""
            elif "Screenshots" in full:
                para.runs[0].text = "•  ADRs: docs/ADR-001, ADR-002, ADR-003 | pytest: docs/pytest-output.txt"
                for r in para.runs[1:]:
                    r.text = ""
            elif "____________________" in full and "Name" in full:
                para.runs[0].text = full.replace("____________________", "")
                for r in para.runs[1:]:
                    r.text = ""

prs.save(DST)
print(f"Saved: {DST}")
