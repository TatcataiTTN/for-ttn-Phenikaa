const LETTERS = ["A", "B", "C", "D"];
const STORAGE_PREFIX = "qmlff_quiz_v1_";

let QUESTIONS = [];

// ---------------- Tabs ----------------
function initTabs() {
  document.querySelectorAll(".tab-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
      document.querySelectorAll(".tab-panel").forEach(p => p.classList.remove("active"));
      btn.classList.add("active");
      document.getElementById("tab-" + btn.dataset.tab).classList.add("active");
    });
  });
}

// ---------------- Quiz ----------------
function loadProgress(groupId) {
  try {
    const raw = localStorage.getItem(STORAGE_PREFIX + "group" + groupId);
    return raw ? JSON.parse(raw) : null;
  } catch (e) { return null; }
}
function saveProgress(groupId, data) {
  try { localStorage.setItem(STORAGE_PREFIX + "group" + groupId, JSON.stringify(data)); }
  catch (e) { /* localStorage unavailable, silently skip persistence */ }
}

function groupBy(questions) {
  const map = new Map();
  questions.forEach(q => {
    if (!map.has(q.group)) map.set(q.group, { name: q.group_name, items: [] });
    map.get(q.group).items.push(q);
  });
  return map;
}

function renderQuiz() {
  const container = document.getElementById("quiz-groups");
  container.innerHTML = "";
  const groups = groupBy(QUESTIONS);

  groups.forEach((g, groupId) => {
    const saved = loadProgress(groupId);
    const card = document.createElement("div");
    card.className = "group-card";

    const head = document.createElement("div");
    head.className = "group-head";
    const scoreText = saved
      ? `${I18N[CURRENT_LANG].score_label}: ${saved.score}/10`
      : I18N[CURRENT_LANG].not_done;
    head.innerHTML = `<h3>Nhóm ${groupId} — ${g.name}</h3><span class="group-score">${scoreText}</span>`;
    card.appendChild(head);

    const body = document.createElement("div");
    body.className = "group-body";
    body.dataset.groupId = groupId;

    g.items.forEach(q => {
      const qDiv = document.createElement("div");
      qDiv.className = "question";
      qDiv.dataset.qid = q.id;
      const stemHtml = `<div class="q-stem">Q${q.id}. ${escapeHtml(q.stem)}</div>`;
      const optsHtml = q.options.map((opt, i) => `
        <label class="q-opt" data-idx="${i}">
          <input type="radio" name="q${q.id}" value="${i}">
          ${LETTERS[i]}. ${escapeHtml(opt)}
        </label>`).join("");
      qDiv.innerHTML = stemHtml + optsHtml;
      body.appendChild(qDiv);

      if (saved && saved.answers && saved.answers[q.id] !== undefined) {
        markAnswered(qDiv, q, saved.answers[q.id]);
      }
    });

    const actions = document.createElement("div");
    actions.style.marginTop = "12px";
    const submitBtn = document.createElement("button");
    submitBtn.className = "btn";
    submitBtn.textContent = I18N[CURRENT_LANG].submit_group;
    submitBtn.addEventListener("click", () => submitGroup(groupId, g.items, head));
    const resetBtn = document.createElement("button");
    resetBtn.className = "btn secondary";
    resetBtn.style.marginLeft = "8px";
    resetBtn.textContent = I18N[CURRENT_LANG].reset_group;
    resetBtn.addEventListener("click", () => resetGroup(groupId, body, head, g.items));
    actions.appendChild(submitBtn);
    actions.appendChild(resetBtn);
    body.appendChild(actions);

    head.addEventListener("click", () => body.classList.toggle("open"));
    card.appendChild(body);
    container.appendChild(card);
  });

  // open the first group by default
  const firstBody = container.querySelector(".group-body");
  if (firstBody) firstBody.classList.add("open");

  renderMathIn(container);
}

function renderMathIn(el) {
  if (window.renderMathInElement) {
    renderMathInElement(el, {
      delimiters: [{ left: "$", right: "$", display: false }],
      throwOnError: false,
    });
  }
}

function markAnswered(qDiv, q, chosenIdx) {
  qDiv.querySelectorAll(".q-opt").forEach((opt, i) => {
    opt.querySelector("input").checked = (i === chosenIdx);
    opt.querySelector("input").disabled = true;
    if (i === q.correct_index) opt.classList.add("correct");
    else if (i === chosenIdx) opt.classList.add("wrong");
  });
}

function submitGroup(groupId, items, head) {
  const answers = {};
  let score = 0;
  let allAnswered = true;
  items.forEach(q => {
    const checked = document.querySelector(`input[name="q${q.id}"]:checked`);
    if (!checked) { allAnswered = false; return; }
    const idx = parseInt(checked.value, 10);
    answers[q.id] = idx;
    if (idx === q.correct_index) score++;
  });
  if (!allAnswered) {
    alert(CURRENT_LANG === "vi"
      ? "Vui lòng trả lời hết 10 câu trong nhóm trước khi nộp."
      : "Please answer all 10 questions in this group before submitting.");
    return;
  }
  items.forEach(q => {
    const qDiv = document.querySelector(`.question[data-qid="${q.id}"]`);
    markAnswered(qDiv, q, answers[q.id]);
  });
  saveProgress(groupId, { score, answers });
  head.querySelector(".group-score").textContent = `${I18N[CURRENT_LANG].score_label}: ${score}/10`;
}

function resetGroup(groupId, body, head, items) {
  localStorage.removeItem(STORAGE_PREFIX + "group" + groupId);
  items.forEach(q => {
    const qDiv = body.querySelector(`.question[data-qid="${q.id}"]`);
    qDiv.querySelectorAll(".q-opt").forEach(opt => {
      opt.classList.remove("correct", "wrong");
      const input = opt.querySelector("input");
      input.checked = false;
      input.disabled = false;
    });
  });
  head.querySelector(".group-score").textContent = I18N[CURRENT_LANG].not_done;
}

function escapeHtml(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

// ---------------- Exercise 1: equivariance check ----------------
function initExercise1() {
  document.getElementById("btn-check-ex1").addEventListener("click", () => {
    const choice = document.querySelector('input[name="cij"]:checked').value;
    const box = document.getElementById("ex1-result");
    const isEquivariant = (choice === "dist" || choice === "atomicnum");
    box.className = "result-box show " + (isEquivariant ? "good" : "bad");
    box.textContent = isEquivariant ? I18N[CURRENT_LANG].ex1_good : I18N[CURRENT_LANG].ex1_bad;
  });
}

// ---------------- Exercise 2: qubit calculator ----------------
function initExercise2() {
  document.getElementById("btn-check-ex2").addEventListener("click", () => {
    const active = parseInt(document.getElementById("ex2-active").value, 10);
    const rep = parseInt(document.getElementById("ex2-rep").value, 10);
    const box = document.getElementById("ex2-result");
    box.className = "result-box show good";
    if (!Number.isFinite(active) || !Number.isFinite(rep) || active < 1 || rep < 1) {
      box.className = "result-box show bad";
      box.textContent = CURRENT_LANG === "vi"
        ? "Nhập số nguyên dương cho cả hai trường."
        : "Please enter positive integers for both fields.";
      return;
    }
    const qubits = active * rep;
    box.textContent = (CURRENT_LANG === "vi"
      ? `num_qubits = active_atoms × rep = ${active} × ${rep} = ${qubits} qubit.`
      : `num_qubits = active_atoms × rep = ${active} × ${rep} = ${qubits} qubits.`);
  });
}

window.rerenderDynamicLabels = function () {
  // re-render quiz score labels + compare table text on language switch
  document.querySelectorAll(".group-head").forEach(head => {
    const scoreEl = head.querySelector(".group-score");
    if (scoreEl && scoreEl.textContent.indexOf("/10") === -1) {
      scoreEl.textContent = I18N[CURRENT_LANG].not_done;
    }
  });
};

// ---------------- Boot ----------------
document.addEventListener("DOMContentLoaded", async () => {
  initTabs();
  initExercise1();
  initExercise2();
  try {
    const resp = await fetch("data/questions.json");
    if (!resp.ok) throw new Error("HTTP " + resp.status);
    QUESTIONS = await resp.json();
    renderQuiz();
  } catch (err) {
    document.getElementById("quiz-groups").innerHTML =
      `<div class="result-box show bad">Không tải được ngân hàng câu hỏi (data/questions.json): ${err.message}</div>`;
  }
  renderCompareTable();
});
