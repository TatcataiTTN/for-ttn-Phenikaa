// Content mirrors Reference Drawio Latex/qml_ff_04_train_eval_comparison.drawio and
// Section 4 of Study_Materials/QML_Force_Fields_Full_EN.tex / _VN.tex.
const COMPARE_ROWS = [
  {
    vi: "Hàm loss",
    en: "Loss function",
    painn: "Weighted MSE: năng lượng + lực, trọng số lực thường lớn hơn nhiều.",
    sivqlm: "Trong demo: chỉ năng lượng. F_target được truyền vào nhưng KHÔNG dùng trong cost().",
    painn_en: "Weighted MSE: energy + force, force weight usually much larger.",
    sivqlm_en: "In the demo: energy only. F_target is passed in but NOT used inside cost().",
  },
  {
    vi: "Optimizer",
    en: "Optimizer",
    painn: "Adam (torch), lr ~1e-3, thường có scheduler giảm dần.",
    sivqlm: "Adam (jax), lr=1e-2 cố định, num_batches=5000, batch_size=256.",
    painn_en: "Adam (torch), lr ~1e-3, usually with a decaying scheduler.",
    sivqlm_en: "Adam (jax), fixed lr=1e-2, num_batches=5000, batch_size=256.",
  },
  {
    vi: "Lấy lực (force)",
    en: "Force extraction",
    painn: "Autograd của torch: F = -dE/dR, một lượt backward, rất rẻ.",
    sivqlm: "Autodiff JAX (mô phỏng) hoặc parameter-shift rule (phần cứng thật) — 2 lần đánh giá mạch mỗi tham số mỗi thành phần lực, đắt hơn nhiều.",
    painn_en: "Torch autograd: F = -dE/dR, one backward pass, very cheap.",
    sivqlm_en: "JAX autodiff (simulation) or parameter-shift rule (real hardware) — 2 circuit evaluations per parameter per force component, much more expensive.",
  },
  {
    vi: "Khả năng mở rộng đã chứng minh",
    en: "Demonstrated scalability",
    painn: "MD17/rMD17 (9–21 nguyên tử); NequIP/MACE mở rộng tới vật liệu, hàng nghìn nguyên tử.",
    sivqlm: "LiH (2), H2O (3), dimer H2O (6 nguyên tử). Quantum Extreme Learning (khác kiến trúc) tới formamide (7).",
    painn_en: "MD17/rMD17 (9–21 atoms); NequIP/MACE extend to materials, thousands of atoms.",
    sivqlm_en: "LiH (2), H2O (3), water dimer (6 atoms). Quantum Extreme Learning (different architecture) reaches formamide (7).",
  },
  {
    vi: "Phần cứng chạy",
    en: "Runtime hardware",
    painn: "GPU/CPU cổ điển, không giới hạn cứng theo số nguyên tử ngoài bộ nhớ/thời gian.",
    sivqlm: "Mô phỏng statevector (default.qubit) hoặc IBM Quantum thật — số qubit giới hạn bởi NISQ hiện tại.",
    painn_en: "Classical GPU/CPU, no hard limit on atom count beyond memory/time.",
    sivqlm_en: "Statevector simulation (default.qubit) or real IBM Quantum hardware — qubit count limited by current NISQ devices.",
  },
  {
    vi: "Xử lý đối xứng",
    en: "Symmetry handling",
    painn: "Kênh vector đồng biến học được (μ), norm bất biến để mix an toàn.",
    sivqlm: "Thiết kế cổng theo lý thuyết nhóm tường minh (Twirling/Null space/Choi operator).",
    painn_en: "Learned equivariant vector channel (μ), invariant norm for safe mixing.",
    sivqlm_en: "Explicit group-theoretic gate design (Twirling/Null space/Choi operator methods).",
  },
];

function renderCompareTable() {
  const tbody = document.getElementById("compare-tbody");
  if (!tbody) return;
  const lang = CURRENT_LANG;
  tbody.innerHTML = COMPARE_ROWS.map(r => `
    <tr>
      <td><strong>${lang === "vi" ? r.vi : r.en}</strong></td>
      <td>${lang === "vi" ? r.painn : r.painn_en}</td>
      <td>${lang === "vi" ? r.sivqlm : r.sivqlm_en}</td>
    </tr>
  `).join("");
}
window.renderCompareTable = renderCompareTable;
