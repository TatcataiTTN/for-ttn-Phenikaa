"""
Parse the verified QML_Force_Fields_MCQ_80.tex into data/questions.json.
- Extracts question stem + 4 options (A-D) per \\item, and the group each Q belongs to.
- Extracts the answer key table (Q -> correct letter) from the 'Bang dap an' table.
- Cross-checks: every question has an answer, exactly 80 questions, 8 groups of 10.
- Applies a deterministic per-question shuffle (seed = question id) to the 4 options to
  remove position bias (the un-shuffled source skews heavily toward letter B), then
  recomputes the correct index for the shuffled order. Semantic content is untouched --
  only display order + the stored correct-answer pointer change.
Never hand-types an answer: the correct option is always the same *text* as flagged in the
tex answer-key table, just relocated by the shuffle.
"""
import re, json, random, sys, collections

SRC = "/Users/tuannghiat/Downloads/Quantum QML Force Fields/Tự học /QML_Force_Fields/Exam_Practice/QML_Force_Fields_MCQ_80.tex"

text = open(SRC, encoding="utf-8").read()

# ---- 1. Groups & questions ----
group_pattern = re.compile(r"\\section\*\{Nhom (\d+) -- ([^}]*)\}", re.S)
groups = [(int(m.group(1)), m.group(2).strip(), m.start()) for m in group_pattern.finditer(text)]
groups.append((99, "END", len(text)))

item_pattern = re.compile(
    r"\\item\s+(.*?)\n\s*\(A\)\s*(.*?)\s*\(B\)\s*(.*?)\s*\(C\)\s*(.*?)\s*\(D\)\s*(.*?)\n",
    re.S,
)

questions = []
for i in range(len(groups) - 1):
    gnum, gname, gstart = groups[i]
    gend = groups[i + 1][2]
    chunk = text[gstart:gend]
    for m in item_pattern.finditer(chunk):
        stem = re.sub(r"\s+", " ", m.group(1)).strip()
        opts = [re.sub(r"\s+", " ", m.group(k)).strip() for k in range(2, 6)]
        questions.append({"group": gnum, "group_name": gname, "stem": stem, "options": opts})

assert len(questions) == 80, f"expected 80 questions, got {len(questions)}"

# assign sequential IDs 1..80 in source order (matches Q\arabic* numbering in the tex)
for idx, q in enumerate(questions, start=1):
    q["id"] = idx

# ---- 2. Answer key table ----
table_match = re.search(r"\\begin\{tabular\}\{\|c\|c\|\|c\|c\|\|c\|c\|\|c\|c\|\}(.*?)\\end\{tabular\}", text, re.S)
assert table_match, "answer key table not found"
table_body = table_match.group(1)
row_pattern = re.compile(r"(\d+)&([A-D])&(\d+)&([A-D])&(\d+)&([A-D])&(\d+)&([A-D])")
answer_key = {}
for row in table_body.split("\\\\"):
    rm = row_pattern.search(row)
    if rm:
        for k in range(0, 8, 2):
            qnum = int(rm.group(k + 1))
            letter = rm.group(k + 2)
            answer_key[qnum] = letter

assert len(answer_key) == 80, f"expected 80 answers, got {len(answer_key)}"
for q in questions:
    assert q["id"] in answer_key, f"missing answer for Q{q['id']}"

# ---- 3. Position-bias check on the source order ----
letter_counts = collections.Counter(answer_key.values())
print("Source (tex) correct-letter distribution:", dict(letter_counts))

# ---- 4. Deterministic per-question shuffle to remove position bias ----
LETTERS = ["A", "B", "C", "D"]
out_questions = []
for q in questions:
    correct_letter = answer_key[q["id"]]
    correct_idx_src = LETTERS.index(correct_letter)
    correct_text = q["options"][correct_idx_src]

    rng = random.Random(1000 + q["id"])  # deterministic, unique per question
    order = list(range(4))
    rng.shuffle(order)
    shuffled_options = [q["options"][k] for k in order]
    new_correct_idx = shuffled_options.index(correct_text)

    out_questions.append({
        "id": q["id"],
        "group": q["group"],
        "group_name": q["group_name"],
        "stem": q["stem"],
        "options": shuffled_options,
        "correct_index": new_correct_idx,
    })

# ---- 5. Post-shuffle bias audit ----
post_counts = collections.Counter(LETTERS[q["correct_index"]] for q in out_questions)
print("Post-shuffle correct-letter distribution:", dict(post_counts))
for letter, n in post_counts.items():
    assert 12 <= n <= 28, f"letter {letter} still skewed after shuffle: {n}/80"

groups_summary = collections.Counter(q["group"] for q in out_questions)
assert groups_summary == {i: 10 for i in range(1, 9)}, groups_summary

with open(
    "/private/tmp/claude-501/-Users-tuannghiat-Downloads-Quantum-QML-Force-Fields/0d610756-17fc-4f06-8fc0-440b3f52d3fb/scratchpad/qmlsite/data/questions.json",
    "w", encoding="utf-8"
) as f:
    json.dump(out_questions, f, ensure_ascii=False, indent=2)

print(f"OK: wrote {len(out_questions)} questions, 8 groups x 10.")
