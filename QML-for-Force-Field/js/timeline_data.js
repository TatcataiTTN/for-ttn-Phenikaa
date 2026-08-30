// Interactive timeline content, mirroring Section 1 of Study_Materials/QML_Force_Fields_Full_VN.tex
// (Bối cảnh Lịch sử và Khoa học). Each entry: year, short label, vi/en detail text.
const TIMELINE = [
  {
    year: "1924",
    label: { vi: "Thế năng Lennard-Jones", en: "Lennard-Jones potential" },
    detail: {
      vi: "John Lennard-Jones đề xuất $U_{LJ}(r) = 4\\varepsilon\\left[(\\sigma/r)^{12} - (\\sigma/r)^{6}\\right]$ để mô tả lực hút van der Waals và lực đẩy Pauli. Có thể coi là số hạng \"trường lực\" đầu tiên theo nghĩa hiện đại — vẫn dùng trong mọi trường lực cổ điển ngày nay.",
      en: "John Lennard-Jones proposes $U_{LJ}(r) = 4\\varepsilon\\left[(\\sigma/r)^{12} - (\\sigma/r)^{6}\\right]$ to model van der Waals attraction and Pauli repulsion. Arguably the first modern 'force field' term — still used in every classical force field today."
    }
  },
  {
    year: "1983–1988",
    label: { vi: "AMBER, CHARMM, OPLS", en: "AMBER, CHARMM, OPLS" },
    detail: {
      vi: "CHARMM (Brooks, Karplus, 1983), AMBER (Weiner & Kollman, 1984), OPLS (Jorgensen, 1988): trường lực cơ học phân tử đầy đủ, dạng hàm cố định (bonds/angles/dihedrals/van der Waals/electrostatics), tham số khớp offline. Nhanh, scale tới hàng triệu nguyên tử, nhưng không mô tả được phản ứng hoá học vì topology liên kết cố định.",
      en: "CHARMM (Brooks, Karplus, 1983), AMBER (Weiner & Kollman, 1984), OPLS (Jorgensen, 1988): full molecular-mechanics force fields with a fixed functional form, offline-fit parameters. Fast, scale to millions of atoms, but cannot describe chemical reactions since bonding topology is fixed."
    }
  },
  {
    year: "2007",
    label: { vi: "Behler–Parrinello NN potential", en: "Behler–Parrinello NN potential" },
    detail: {
      vi: "Thế năng mạng nơ-ron thực tế đầu tiên. Môi trường nguyên tử mã hoá thủ công thành \"hàm đối xứng tâm-nguyên-tử\" (ACSF) bất biến quay/hoán vị, rồi đưa vào mạng feed-forward theo từng nguyên tử.",
      en: "The first practical neural-network potential. Atomic environments hand-encoded into rotation/permutation-invariant 'atom-centered symmetry functions' (ACSF), fed into a per-atom feed-forward network."
    }
  },
  {
    year: "2010",
    label: { vi: "Gaussian Approximation Potentials", en: "Gaussian Approximation Potentials" },
    detail: {
      vi: "Bartók và cộng sự: hồi quy kernel (Gaussian process) trên đặc trưng bất biến (SOAP). Phổ biến cho vật liệu khi dữ liệu train khan hiếm.",
      en: "Bartók et al.: kernel-based (Gaussian process) regression on invariant SOAP descriptors. Popular for materials where training data is scarce."
    }
  },
  {
    year: "2014",
    label: { vi: "VQE — Variational Quantum Eigensolver", en: "VQE — Variational Quantum Eigensolver" },
    detail: {
      vi: "Peruzzo và cộng sự: giải trực tiếp bài toán cấu trúc electron trên máy tính lượng tử — mã hoá Hamiltonian electron thành toán tử qubit (Jordan-Wigner/Bravyi-Kitaev), thay thế Hartree-Fock/DFT/CCSD(T). Đây là 'Cánh cửa 1' — khác với hướng QML force field của dự án này.",
      en: "Peruzzo et al.: directly solves the electronic structure problem on a quantum computer — maps the electronic Hamiltonian to qubit operators (Jordan-Wigner/Bravyi-Kitaev), replacing Hartree-Fock/DFT/CCSD(T). This is 'Door 1' — distinct from this project's QML force field direction."
    }
  },
  {
    year: "2017",
    label: { vi: "SchNet", en: "SchNet" },
    detail: {
      vi: "Thế năng deep learning đầu tiên dùng rộng rãi — continuous-filter convolution trên khoảng cách liên nguyên tử, thuần bất biến. Tiền thân trực tiếp của PaiNN (đọc chi tiết ở tab So sánh).",
      en: "The first widely-used deep-learning potential — continuous-filter convolutions over interatomic distances, purely invariant. The direct predecessor of PaiNN (see the Compare tab for details)."
    }
  },
  {
    year: "2021",
    label: { vi: "PaiNN", en: "PaiNN" },
    detail: {
      vi: "Schütt, Unke, Gastegger: message passing đồng biến (equivariant), kênh vector song song kênh vô hướng. Paper hạt giống cổ điển của dự án này.",
      en: "Schütt, Unke, Gastegger: equivariant message passing, vector channel alongside the scalar channel. This project's classical seed paper."
    }
  },
  {
    year: "2022",
    label: { vi: "NequIP, MACE, Kiss et al. QNN", en: "NequIP, MACE, Kiss et al. QNN" },
    detail: {
      vi: "NequIP và MACE mở rộng equivariance lên tensor bậc cao, đạt SOTA cho MD17/vật liệu. Cùng năm, Kiss và cộng sự công bố VQLM tổng quát đầu tiên cho force field lượng tử — chưa ràng buộc đối xứng.",
      en: "NequIP and MACE extend equivariance to higher-order tensors, reaching SOTA on MD17/materials. The same year, Kiss et al. publish the first general VQLM for quantum force fields — not yet symmetry-constrained."
    }
  },
  {
    year: "2024",
    label: { vi: "Quantum Extreme Learning, lý thuyết EQNN", en: "Quantum Extreme Learning, EQNN theory" },
    detail: {
      vi: "Lo Monaco và cộng sự: Quantum Extreme Learning Machine — reservoir lượng tử cố định, né hoàn toàn barren plateau, chạm tới formamide (7 nguyên tử) kể cả trên phần cứng IBM thật. Nguyen và cộng sự công bố khung lý thuyết Equivariant QNN (Twirling/Null space/Choi operator) mà siVQLM dùng để xây lớp đồng biến.",
      en: "Lo Monaco et al.: Quantum Extreme Learning Machine — a fixed quantum reservoir, entirely avoiding barren plateaus, reaching formamide (7 atoms) even on real IBM hardware. Nguyen et al. publish the Equivariant QNN theory (Twirling/Null space/Choi operator) that siVQLM builds its equivariant layers from."
    }
  },
  {
    year: "2025",
    label: { vi: "siVQLM (paper hạt giống lượng tử)", en: "siVQLM (quantum seed paper)" },
    detail: {
      vi: "Le, Kiss, Schuhmacher, Tavernelli, Tacchino: VQLM bất biến đối xứng đầu tiên cho force field — LiH, H2O, dimer H2O. Vượt trội VQLM tổng quát về trainability, không thấy barren plateau ở độ sâu nông. Đây là 'Cánh cửa 2' — trọng tâm chính của dự án này.",
      en: "Le, Kiss, Schuhmacher, Tavernelli, Tacchino: the first symmetry-invariant VQLM for force fields — LiH, H2O, water dimer. Outperforms generic VQLMs on trainability, no barren plateau observed at shallow depth. This is 'Door 2' — this project's main focus."
    }
  },
  {
    year: "2026",
    label: { vi: "Kết quả thật từ dự án này", en: "Real results from this project" },
    detail: {
      vi: "Trong phiên làm việc thực hiện dự án này: đọc trực tiếp 5 checkpoint PaiNN đã train thật trên rMD17 ethanol (config.yaml + split.npz, xem Sơ đồ 5), và tự chạy lại toàn bộ pipeline siVQLM trên dữ liệu H$_2$O thật (850 mẫu) — cả bản PennyLane chính thức lẫn bản viết lại thuần JAX, đạt MAE $\\approx$ 0.166 kcal/mol, nằm trong ngưỡng \"chemical accuracy\" (xem Sơ đồ 6, và Nhóm 25–26 trong phần Trắc nghiệm).",
      en: "During this project's working session: directly read 5 real pretrained PaiNN checkpoints on rMD17 ethanol (config.yaml + split.npz, see Diagram 5), and actually re-ran the full siVQLM pipeline on real H$_2$O data (850 samples) — both the official PennyLane version and a from-scratch JAX rewrite, reaching MAE $\\approx$ 0.166 kcal/mol, within \"chemical accuracy\" (see Diagram 6, and Groups 25–26 in the Quiz tab)."
    }
  },
];

function renderTimeline() {
  const track = document.getElementById("timeline-track");
  const detail = document.getElementById("timeline-detail");
  if (!track || !detail) return;
  const lang = CURRENT_LANG;
  track.innerHTML = TIMELINE.map((t, i) => `
    <button class="timeline-dot" data-idx="${i}">
      <span class="timeline-year">${t.year}</span>
      <span class="timeline-label">${t.label[lang]}</span>
    </button>
  `).join("");
  track.querySelectorAll(".timeline-dot").forEach(btn => {
    btn.addEventListener("click", () => showTimelineDetail(parseInt(btn.dataset.idx, 10)));
  });
  showTimelineDetail(window._timelineActiveIdx || 0);
}

function showTimelineDetail(idx) {
  window._timelineActiveIdx = idx;
  const t = TIMELINE[idx];
  const lang = CURRENT_LANG;
  document.querySelectorAll(".timeline-dot").forEach((btn, i) => btn.classList.toggle("active", i === idx));
  const detail = document.getElementById("timeline-detail");
  detail.innerHTML = `<h2>${t.year} — ${t.label[lang]}</h2><p>${t.detail[lang]}</p>`;
  renderMathIn(detail);
}
window.renderTimeline = renderTimeline;
