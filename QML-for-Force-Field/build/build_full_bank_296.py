# -*- coding: utf-8 -*-
"""
Build the full 296-question bank (groups 1-26) from two sources:
  - Groups 1-24 (240 questions): parsed AS-IS from the already-built, already-shuffled
    QML_Force_Fields_MCQ_240.tex (preserves the exact option order/answer key already reviewed).
  - Groups 25-26 (56 new questions): from questions_practical.py, written directly as
    (correct answer + 3 distractors), shuffled here with a fresh deterministic seed.
Emits:
  1. QML_Force_Fields_MCQ_296.tex
  2. questions_296.json
"""
import re, json, random, collections, sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-tuannghiat-Downloads-Quantum-QML-Force-Fields/0d610756-17fc-4f06-8fc0-440b3f52d3fb/scratchpad")
from questions_practical import GROUPS_25_26

OLD_MCQ_TEX = "/Users/tuannghiat/Downloads/Quantum QML Force Fields/Tự học /QML_Force_Fields/Exam_Practice/QML_Force_Fields_MCQ_240.tex"
LETTERS = ["A", "B", "C", "D"]
OUT_DIR = "/private/tmp/claude-501/-Users-tuannghiat-Downloads-Quantum-QML-Force-Fields/0d610756-17fc-4f06-8fc0-440b3f52d3fb/scratchpad"

# ---------- Parse groups 1-24 AS-IS from the existing MCQ_240.tex ----------
text = open(OLD_MCQ_TEX, encoding="utf-8").read()
group_pattern = re.compile(r"\\section\*\{Nh\u00f3m (\d+) -- ([^}]*)\}", re.S)
groups = [(int(m.group(1)), m.group(2).strip(), m.start()) for m in group_pattern.finditer(text)]
groups.append((99, "END", text.find("Answer key")))

item_pattern = re.compile(
    r"\\item\s+(.*?)\n\s*\(A\)\s*(.*?)\s*\(B\)\s*(.*?)\s*\(C\)\s*(.*?)\s*\(D\)\s*(.*?)\n",
    re.S,
)
old_questions = []
for i in range(24):
    gnum, gname, gstart = groups[i]
    gend = groups[i + 1][2]
    chunk = text[gstart:gend]
    for m in item_pattern.finditer(chunk):
        stem = re.sub(r"\s+", " ", m.group(1)).strip()
        opts = [re.sub(r"\s+", " ", m.group(k)).strip() for k in range(2, 6)]
        old_questions.append({"group": gnum, "group_name": gname, "stem": stem, "options": opts})
assert len(old_questions) == 240, f"expected 240 old questions, got {len(old_questions)}"
for idx, q in enumerate(old_questions, start=1):
    q["id"] = idx

table_match = re.search(r"\\begin\{longtable\}\{\|c\|c\|\|c\|c\|\|c\|c\|\|c\|c\|\}(.*?)\\end\{longtable\}", text, re.S)
table_body = table_match.group(1)
row_pattern = re.compile(r"(\d+)&([A-D])&(\d+)&([A-D])&(\d+)&([A-D])&(\d+)&([A-D])")
answer_key = {}
for row in table_body.split("\\\\"):
    rm = row_pattern.search(row)
    if rm:
        for k in range(0, 8, 2):
            answer_key[int(rm.group(k + 1))] = rm.group(k + 2)
assert len(answer_key) == 240, f"expected 240 answers, got {len(answer_key)}"

out_old = []
for q in old_questions:
    letter = answer_key[q["id"]]
    out_old.append({
        "id": q["id"], "group": q["group"], "group_name": q["group_name"],
        "stem": q["stem"], "options": q["options"], "correct_index": LETTERS.index(letter),
    })

# ---------- Build + shuffle groups 25-26 (new) ----------
out_new = []
for i, q in enumerate(GROUPS_25_26, start=241):
    opts = [q["correct"]] + q["distractors"]
    rng = random.Random(250000 + i)  # base=25 in the offline balance search -> spread=2 (14/15/13/14)
    order = list(range(4))
    rng.shuffle(order)
    shuffled = [opts[k] for k in order]
    correct_index = shuffled.index(q["correct"])
    out_new.append({
        "id": i, "group": q["group"], "group_name": q["group_name"],
        "stem": q["stem"], "options": shuffled, "correct_index": correct_index,
    })

out_questions = out_old + out_new
assert len(out_questions) == 296, len(out_questions)

# audits
letter_counts_new = collections.Counter(LETTERS[q["correct_index"]] for q in out_new)
print("New-56 letter distribution:", dict(letter_counts_new))
groups_summary = collections.Counter(q["group"] for q in out_questions)
expected = {i: 10 for i in range(1, 25)}
expected[25] = 28
expected[26] = 28
assert groups_summary == expected, groups_summary

with open(f"{OUT_DIR}/questions_296.json", "w", encoding="utf-8") as f:
    json.dump(out_questions, f, ensure_ascii=False, indent=2)

# ---------- Emit LaTeX MCQ file (296) ----------
tex_parts = []
tex_parts.append(
    "\\documentclass[11pt,a4paper]{article}\n"
    "\\usepackage{fontspec}\n\\setmainfont{Times New Roman}\n"
    "\\usepackage{amsmath,amssymb}\n\\usepackage{geometry}\n\\usepackage{booktabs}\n"
    "\\usepackage{array}\n\\usepackage{xcolor}\n\\usepackage{tcolorbox}\n\\usepackage{enumitem}\n"
    "\\usepackage{fancyhdr}\n\\usepackage{colortbl}\n\\usepackage{longtable}\n\\usepackage{hyperref}\n\n"
    "\\geometry{margin=2cm,headheight=14pt}\n\\pagestyle{fancy}\n\\fancyhf{}\n"
    "\\fancyhead[L]{QML Force Fields -- 296 MCQ (EN/VI)}\n\\fancyhead[R]{\\thepage}\n"
    "\\renewcommand{\\headrulewidth}{0.4pt}\n\n"
    "\\tcbuselibrary{theorems,skins,breakable}\n"
    "\\newtcolorbox{infobox}[1][]{colback=yellow!10,colframe=orange!50!black,title=#1,fonttitle=\\bfseries,breakable}\n\n"
)
tex_parts.append(
    "\\title{QML Force Fields --- 296 C\u00e2u H\u1ecfi Tr\u1eafc Nghi\u1ec7m\\\\ "
    "\\large Bilingual EN/VI self-test}\n"
    "\\author{Self-study document --- Tr\u01b0\u01a1ng Tu\u1ea5n Ngh\u0129a}\n"
    "\\date{\\today}\n\n"
    "\\begin{document}\n\\maketitle\n\n"
    "\\begin{infobox}[H\u01b0\u1edbng d\u1eabn / Instructions]\n"
    "26 nh\u00f3m x 10 c\u00e2u (nh\u00f3m 25--26: 28 c\u00e2u/nh\u00f3m) = 296 c\u00e2u. "
    "Nh\u00f3m 1--8: ki\u1ebfn tr\u00fac PaiNN/siVQLM. Nh\u00f3m 9--24: b\u1ed1i c\u1ea3nh l\u1ecbch "
    "s\u1eed/khoa h\u1ecdc. Nh\u00f3m 25--26 (\\textbf{m\u1edbi}): c\u00e2u h\u1ecfi th\u1ef1c h\u00e0nh "
    "b\u00e1m theo config/k\u1ebft qu\u1ea3 \\textbf{TH\u1eACT} \u0111\u00e3 ch\u1ea1y trong "
    "\\texttt{Source\\_Code/practical\\_runs.md} (kh\u00f4ng ph\u1ea3i s\u1ed1 li\u1ec7u gi\u1ea3 \u0111\u1ecbnh). "
    "C\u00e2u h\u1ecfi gi\u1eef nguy\u00ean ti\u1ebfng Anh g\u1ed1c \u0111\u1ec3 kh\u1edbp \u0111\u00fang "
    "\u0111\u00e1p \u00e1n. \u0110\u00e1p \u00e1n \u1edf b\u1ea3ng cu\u1ed1i t\u00e0i li\u1ec7u.\n"
    "\\end{infobox}\n\n"
)

q_by_group = collections.defaultdict(list)
for q in out_questions:
    q_by_group[q["group"]].append(q)

for gnum in range(1, 27):
    qs = q_by_group[gnum]
    gname = qs[0]["group_name"]
    tex_parts.append(f"%{'='*67}%\n\\section*{{Nh\u00f3m {gnum} -- {gname}}}\n")
    start = qs[0]["id"]
    label = r"\begin{enumerate}[label=\textbf{Q\arabic*.}" + (f", start={start}]" if gnum > 1 else "]")
    tex_parts.append(label + "\n")
    for q in qs:
        stem = q["stem"]
        options = q["options"]
        if q["group"] in (25, 26):
            # these two groups are plain-text/code-identifier questions with no $...$ math
            # anywhere, so underscores are always literal (e.g. n_atom_basis) and must be escaped
            stem = stem.replace("_", r"\_")
            options = [o.replace("_", r"\_") for o in options]
        opts = " ".join(f"({LETTERS[i]}) {o}" for i, o in enumerate(options))
        tex_parts.append(f"\\item {stem}\n  {opts}\n")
    tex_parts.append("\\end{enumerate}\n\n")
    if gnum in (8, 16, 24):
        tex_parts.append("\\newpage\n")

tex_parts.append("\\newpage\n\\section*{B\u1ea3ng \u0111\u00e1p \u00e1n / Answer key}\n\n")
tex_parts.append(r"\begin{center}\begin{longtable}{|c|c||c|c||c|c||c|c|}" + "\n\\hline\n")
header = "Q & \u0110\u00e1p \u00e1n & Q & \u0110\u00e1p \u00e1n & Q & \u0110\u00e1p \u00e1n & Q & \u0110\u00e1p \u00e1n \\\\\n\\hline\\hline\n"
tex_parts.append(header)
tex_parts.append(r"\endfirsthead" + "\n")
tex_parts.append(header)
tex_parts.append(r"\endhead" + "\n")

n = 296
block = 74  # 296 / 4
for r in range(block):
    cells = []
    for b in range(4):
        qid = b * block + r + 1
        letter = LETTERS[out_questions[qid - 1]["correct_index"]]
        cells.append(f"{qid}&{letter}")
    tex_parts.append("&".join(cells) + "\\\\\n")
    if (r + 1) % 10 == 0:
        tex_parts.append("\\hline\n")
tex_parts.append("\\end{longtable}\\end{center}\n\n")
tex_parts.append("\\end{document}\n")

with open(f"{OUT_DIR}/QML_Force_Fields_MCQ_296.tex", "w", encoding="utf-8") as f:
    f.write("".join(tex_parts))

print(f"Wrote {len(out_questions)} questions -> QML_Force_Fields_MCQ_296.tex and questions_296.json")
