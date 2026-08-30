// Minimal EN/VI toggle for static labels. Quiz question text stays in English
// (matching the verified source LaTeX) and is not machine-retranslated, to avoid
// introducing translation drift versus the checked answer key.
const I18N = {
  vi: {
    site_title: "Luyện tập: Quantum Machine Learning Force Fields",
    site_subtitle: "PaiNN & siVQLM — 296 câu hỏi, dòng thời gian tương tác, kết quả train thật",
    nav_slides: "📖 Học đầy đủ (Slides)",
    nav_history: "Lịch sử & Động lực",
    nav_quiz: "Trắc nghiệm (296 câu)",
    nav_exercises: "Bài tập tương tác",
    nav_compare: "So sánh PaiNN vs siVQLM",
    nav_about: "Giới thiệu",
    history_hint: "Dòng thời gian tương tác: bấm vào một mốc để xem chi tiết. Nội dung khớp Section 1 của tài liệu tự học (Study_Materials/QML_Force_Fields_Full_VN.tex).",
    quiz_hint: "296 câu hỏi trắc nghiệm chia làm 26 nhóm chủ đề (Phần 1: kiến trúc PaiNN/siVQLM — nhóm 1–8; Phần 2: bối cảnh lịch sử/khoa học — nhóm 9–24; Phần 3: thực hành code/kết quả train thật — nhóm 25–26), trích từ tài liệu tự học đã kiểm chứng (Exam_Practice/QML_Force_Fields_MCQ_296.tex). Chấm điểm ngay tại trình duyệt, tiến độ lưu ở localStorage của máy bạn (không gửi lên server nào). Câu hỏi giữ nguyên tiếng Anh gốc để khớp đúng với đáp án đã kiểm chứng.",
    practical_title: "Kết quả train THẬT (không phải số liệu giả định)",
    practical_p1: "Trong lúc xây dự án này, đã đọc trực tiếp 5 checkpoint PaiNN đã train thật trên rMD17 ethanol (config.yaml + split.npz, xem Sơ đồ 5), và tự chạy lại toàn bộ pipeline siVQLM trên dữ liệu H2O thật (850 mẫu) — cả bản PennyLane chính thức lẫn bản viết lại thuần JAX (xem Sơ đồ 6).",
    practical_result: "Kết quả: MAE ≈ 0.166 kcal/mol trên tập test — nằm trong ngưỡng \"chemical accuracy\" (<1 kcal/mol). Chi tiết đầy đủ ở Source_Code/practical_runs.md và Nhóm 25–26 trong phần Trắc nghiệm.",
    ex1_title: "Bài tập 1 — Kiểm tra tính đồng biến (equivariance check)",
    ex1_desc: "Xét quy tắc cập nhật vector cho nguyên tử i: μ_i' = Σ_j c_ij · r_ij, tổng theo các nguyên tử lân cận j. Hệ số vô hướng c_ij có thể phụ thuộc vào các đại lượng khác nhau. Chọn một lựa chọn cho c_ij rồi bấm Kiểm tra để xem quy tắc có đồng biến (equivariant) dưới phép quay hay không.",
    ex1_opt_dist: "c_ij chỉ phụ thuộc khoảng cách ‖r_ij‖ (đại lượng bất biến)",
    ex1_opt_component: "c_ij phụ thuộc trực tiếp 1 thành phần tọa độ, ví dụ x_ij (không bất biến)",
    ex1_opt_atomicnum: "c_ij chỉ phụ thuộc số hiệu nguyên tử Z_i, Z_j (đại lượng bất biến)",
    ex1_opt_random: "c_ij là một hằng số ngẫu nhiên cố định, không phụ thuộc gì vào hình học",
    btn_check: "Kiểm tra",
    btn_calc: "Tính",
    ex2_title: "Bài tập 2 — Tính số qubit của siVQLM",
    ex2_desc: "Theo demo PennyLane chính thức: num_qubits = active_atoms × rep. Nhập số \"active atom\" (nguyên tử không bị cố định làm gốc tọa độ) và hệ số lặp mã hoá rep để tính số qubit cần dùng.",
    ex2_lbl_active: "Số active atom:",
    ex2_lbl_rep: "Hệ số rep:",
    ex2_th_mol: "Hệ phân tử",
    ex2_th_qubits: "Số qubit (tham khảo, paper siVQLM)",
    compare_hint: "Tóm tắt từ Sơ đồ 4 (Reference Drawio Latex/qml_ff_04_train_eval_comparison.drawio) và Section 4 của tài liệu tự học.",
    cmp_th_aspect: "Khía cạnh",
    about_title: "Về trang này",
    about_p1: "Trang luyện tập tĩnh, chạy hoàn toàn trong trình duyệt, không có backend/server chấm bài. Nội dung bám sát pipeline nghiên cứu: 2 paper hạt giống (PaiNN — Schütt et al. 2021; siVQLM — Le et al. 2025), 8 paper mở rộng đã tải và xác minh, đọc source code gốc (SchNetPack + demo PennyLane chính thức), 4 sơ đồ kiến trúc TikZ/quantikz/chemfig, và tài liệu tự học song ngữ EN-VI (gồm chương Bối cảnh Lịch sử & Khoa học).",
    about_p2: "Đáp án trắc nghiệm được trích xuất tự động từ file LaTeX gốc đã kiểm chứng thủ công (không gõ tay lại), sau đó thứ tự 4 lựa chọn A/B/C/D được xáo trộn có kiểm soát (seed cố định theo từng câu) để loại bỏ thiên lệch vị trí đáp án đúng.",
    about_p3: "Tiến độ làm bài lưu trong localStorage của trình duyệt bạn đang dùng — sẽ mất nếu xoá dữ liệu trình duyệt hoặc dùng chế độ ẩn danh, và không đồng bộ giữa các thiết bị.",
    footer_text: "QML Force Fields — trang tự học tĩnh, không backend.",
    submit_group: "Nộp bài nhóm này",
    reset_group: "Làm lại",
    score_label: "Điểm",
    not_done: "chưa làm",
    ex1_good: "Đúng: hệ số này chỉ phụ thuộc đại lượng bất biến (khoảng cách hoặc số hiệu nguyên tử), nên quy tắc cập nhật vẫn đồng biến dưới phép quay — giống đúng cơ chế trong PaiNNInteraction.",
    ex1_bad: "Sai: hệ số này KHÔNG phải đại lượng bất biến quay (hoặc không phụ thuộc gì vào hình học), nên tổng Σ c_ij·r_ij không còn biến đổi đúng theo R khi quay hệ — phá vỡ tính đồng biến.",
  },
  en: {
    site_title: "Practice: Quantum Machine Learning Force Fields",
    site_subtitle: "PaiNN & siVQLM — 296 questions, interactive timeline, real training results",
    nav_slides: "📖 Full study (Slides)",
    nav_history: "History & Motivation",
    nav_quiz: "Quiz (296 questions)",
    nav_exercises: "Interactive exercises",
    nav_compare: "PaiNN vs siVQLM comparison",
    nav_about: "About",
    history_hint: "Interactive timeline: click a milestone to see details. Content mirrors Section 1 of the self-study document (Study_Materials/QML_Force_Fields_Full_EN.tex).",
    quiz_hint: "296 multiple-choice questions in 26 topic groups (Part 1: PaiNN/siVQLM architecture — groups 1–8; Part 2: historical/scientific context — groups 9–24; Part 3: practical code/real training results — groups 25–26), drawn from the verified self-study document (Exam_Practice/QML_Force_Fields_MCQ_296.tex). Graded instantly in the browser; progress is stored in your browser's localStorage only.",
    practical_title: "REAL training results (not placeholder numbers)",
    practical_p1: "While building this project, 5 really-trained PaiNN checkpoints on rMD17 ethanol were read directly (config.yaml + split.npz, see Diagram 5), and the full siVQLM pipeline was actually re-run on real H2O data (850 samples) — both the official PennyLane version and a from-scratch JAX rewrite (see Diagram 6).",
    practical_result: "Result: MAE ≈ 0.166 kcal/mol on the test set — within \"chemical accuracy\" (<1 kcal/mol). Full details in Source_Code/practical_runs.md and Groups 25–26 in the Quiz tab.",
    ex1_title: "Exercise 1 — Equivariance check",
    ex1_desc: "Consider the vector update rule for atom i: μ_i' = Σ_j c_ij · r_ij, summed over neighbours j. The scalar coefficient c_ij can depend on different quantities. Pick one option for c_ij and click Check to see whether the update rule is equivariant under rotation.",
    ex1_opt_dist: "c_ij depends only on the distance ‖r_ij‖ (an invariant quantity)",
    ex1_opt_component: "c_ij depends directly on one coordinate component, e.g. x_ij (not invariant)",
    ex1_opt_atomicnum: "c_ij depends only on atomic numbers Z_i, Z_j (an invariant quantity)",
    ex1_opt_random: "c_ij is a fixed random constant, independent of geometry",
    btn_check: "Check",
    btn_calc: "Compute",
    ex2_title: "Exercise 2 — Counting siVQLM qubits",
    ex2_desc: "Per the official PennyLane demo: num_qubits = active_atoms × rep. Enter the number of \"active atoms\" (atoms not fixed as the coordinate origin) and the encoding-repetition factor rep to compute the number of qubits required.",
    ex2_lbl_active: "Active atoms:",
    ex2_lbl_rep: "Rep factor:",
    ex2_th_mol: "Molecular system",
    ex2_th_qubits: "Qubits (reference, siVQLM paper)",
    compare_hint: "Summarised from Diagram 4 (Reference Drawio Latex/qml_ff_04_train_eval_comparison.drawio) and Section 4 of the self-study document.",
    cmp_th_aspect: "Aspect",
    about_title: "About this site",
    about_p1: "A static practice site, running entirely in the browser, with no backend/grading server. Content follows the research pipeline: two seed papers (PaiNN — Schütt et al. 2021; siVQLM — Le et al. 2025), 8 further papers downloaded and verified, source-code reading (SchNetPack + the official PennyLane demo), 4 TikZ/quantikz/chemfig architecture diagrams, and a bilingual EN-VI self-study document (including a Historical & Scientific Context chapter).",
    about_p2: "Quiz answers are extracted automatically from the manually-verified source LaTeX file (never re-typed by hand); the order of the four A/B/C/D options is then deterministically shuffled per question (fixed seed) to remove correct-answer position bias.",
    about_p3: "Progress is stored in your browser's localStorage — it is lost if you clear browser data or use a private window, and does not sync across devices.",
    footer_text: "QML Force Fields self-study — static site, no backend.",
    submit_group: "Submit this group",
    reset_group: "Reset",
    score_label: "Score",
    not_done: "not attempted",
    ex1_good: "Correct: this coefficient depends only on an invariant quantity (distance or atomic number), so the update rule remains equivariant under rotation — exactly the mechanism used in PaiNNInteraction.",
    ex1_bad: "Incorrect: this coefficient is NOT rotation-invariant (or does not depend on geometry at all), so the sum Σ c_ij·r_ij no longer transforms correctly under R when the system is rotated — equivariance is broken.",
  }
};

let CURRENT_LANG = "vi";

function applyI18n(lang) {
  CURRENT_LANG = lang;
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.getAttribute("data-i18n");
    if (I18N[lang][key]) el.textContent = I18N[lang][key];
  });
  document.getElementById("btn-vi").classList.toggle("active", lang === "vi");
  document.getElementById("btn-en").classList.toggle("active", lang === "en");
  if (window.renderCompareTable) window.renderCompareTable();
  if (window.rerenderDynamicLabels) window.rerenderDynamicLabels();
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("btn-vi").addEventListener("click", () => applyI18n("vi"));
  document.getElementById("btn-en").addEventListener("click", () => applyI18n("en"));
});
