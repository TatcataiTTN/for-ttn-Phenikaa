# -*- coding: utf-8 -*-
# Canonical question bank for QML Force Fields self-study.
# Each question: (group_num, group_name, stem, correct_answer_text, [distractor1, distractor2, distractor3])
# The correct answer is ALWAYS given directly here -- never tracked by letter position --
# so a generator script can shuffle options per-question and derive the answer key
# programmatically, eliminating manual transcription errors.

GROUPS_9_24 = []

def add(group, gname, stem, correct, distractors):
    assert len(distractors) == 3
    GROUPS_9_24.append({"group": group, "group_name": gname, "stem": stem,
                         "correct": correct, "distractors": distractors})

# ============ GROUP 9: Newton's equations & classical MD basics ============
G, GN = 9, "Classical MD basics (Newton's equations)"
add(G, GN, "Classical molecular dynamics integrates which fundamental equation?",
    "Newton's second law, $m_i\\ddot{\\vec r}_i = \\vec F_i$",
    ["The Schrodinger equation directly for nuclei", "Maxwell's equations", "The heat equation"])
add(G, GN, "In MD, the force on atom $i$ is obtained from the potential energy $U$ as:",
    "$\\vec F_i = -\\nabla_{\\vec r_i} U$",
    ["$\\vec F_i = \\nabla_{\\vec r_i} U$", "$\\vec F_i = U^2$", "$\\vec F_i$ is independent of $U$"])
add(G, GN, "What does the potential energy function $U(\\vec r_1,\\ldots,\\vec r_N)$ depend on?",
    "The positions of all atoms in the system",
    ["Only the temperature", "Only the total mass", "Only the simulation time step"])
add(G, GN, "Why is $U$ described as the central object that 'everything hinges on' in MD?",
    "Because both the energy and every force (via its gradient) come from a single function $U$",
    ["Because $U$ is measured directly by experiment", "Because $U$ has no effect on the trajectory", "Because $U$ is only used for visualization"])
add(G, GN, "Before quantum-chemical or machine-learned models existed, how was $U$ constructed?",
    "By hand, from simple physically-motivated analytic terms",
    ["By solving the Schrodinger equation exactly", "By training a neural network on lab data", "It was not possible to define $U$ at all"])
add(G, GN, "A trajectory produced by classical MD consists of:",
    "A sequence of atomic positions (and velocities) over time",
    ["A single static equilibrium geometry only", "A wavefunction evolving in Hilbert space", "A set of qubit measurement outcomes"])
add(G, GN, "Which quantity does MD NOT require in order to integrate the equations of motion?",
    "The electronic wavefunction, if using a classical force field",
    ["Atomic masses $m_i$", "Interatomic forces $\\vec F_i$", "Initial positions and velocities"])
add(G, GN, "The role of a 'force field' in MD, in the most general sense, is:",
    "Any model (empirical or learned) that supplies $U$ or $\\vec F$ given atomic positions",
    ["A literal physical field applied externally to the simulation box", "A synonym for temperature control", "A type of quantum circuit only"])
add(G, GN, "PaiNN, NequIP, MACE, and siVQLM are all, in this general sense, examples of:",
    "Force fields (models that predict energy/forces from atomic configuration)",
    ["Experimental spectroscopy techniques", "Crystallography refinement algorithms", "Classical thermostats"])
add(G, GN, "What ultimately connects Newton's second law to the topic of this whole self-study document?",
    "Every method studied here (classical FF, DFT, PaiNN, siVQLM) is a different way of computing $U$/$\\vec F$ for that same equation",
    ["Newton's law is unrelated to quantum chemistry", "Newton's law only applies to electrons, not nuclei", "Newton's law was replaced entirely by quantum mechanics for all purposes"])

# ============ GROUP 10: Lennard-Jones & empirical potentials ============
G, GN = 10, "Lennard-Jones potential and empirical terms"
add(G, GN, "The Lennard-Jones potential was proposed by John Lennard-Jones in:",
    "1924",
    ["1900", "1950", "1984"])
add(G, GN, "The Lennard-Jones formula is:",
    "$U_{LJ}(r) = 4\\varepsilon[(\\sigma/r)^{12} - (\\sigma/r)^{6}]$",
    ["$U_{LJ}(r) = \\varepsilon r^2$", "$U_{LJ}(r) = -q_1q_2/r$", "$U_{LJ}(r) = k(r-r_0)^2$"])
add(G, GN, "The $-r^{-6}$ term in the Lennard-Jones potential models:",
    "Van der Waals attraction, from induced-dipole interactions",
    ["Covalent bond stretching", "Coulomb repulsion between like charges", "Nuclear spin coupling"])
add(G, GN, "The $r^{-12}$ term in the Lennard-Jones potential models:",
    "Short-range Pauli repulsion, chosen crudely for computational convenience",
    ["An exact quantum-mechanical repulsion law", "Gravitational interaction", "Magnetic dipole interaction"])
add(G, GN, "Why is $r^{-12}$ (rather than a more physically exact repulsion form) used for the repulsive term?",
    "Because it is computationally convenient (it is just the square of the $r^{-6}$ term)",
    ["Because it was experimentally measured to be exact", "Because it is required by the Schrodinger equation", "Because it minimizes barren plateaus"])
add(G, GN, "Is the Lennard-Jones term still used in modern classical force fields (AMBER, CHARMM, OPLS)?",
    "Yes, it is still used as the van der Waals term",
    ["No, it was fully replaced by DFT", "No, it was replaced by machine learning in the 1990s", "It was never adopted by any force field"])
add(G, GN, "The Lennard-Jones potential can be considered:",
    "Arguably the first 'force field' term in the modern sense",
    ["A purely quantum-mechanical operator", "A dataset, not a potential", "A neural network architecture"])
add(G, GN, "Which parameter in $U_{LJ}$ sets the depth (strength) of the attractive well?",
    "$\\varepsilon$",
    ["$\\sigma$", "$r$", "$N$"])
add(G, GN, "Which parameter in $U_{LJ}$ sets the characteristic distance scale?",
    "$\\sigma$",
    ["$\\varepsilon$", "$k_b$", "$q_i$"])
add(G, GN, "The Lennard-Jones potential is an example of what broader category of model?",
    "An empirical, hand-built analytic potential, fit to reproduce known physics",
    ["A supervised deep-learning model", "A variational quantum circuit", "An exact solution of the Schrodinger equation"])

# ============ GROUP 11: Molecular mechanics force fields (AMBER/CHARMM/OPLS) ============
G, GN = 11, "Molecular mechanics force fields (AMBER/CHARMM/OPLS)"
add(G, GN, "AMBER, as a molecular mechanics force field, was developed by:",
    "Weiner and Kollman (1984)",
    ["Behler and Parrinello (2007)", "Schutt, Unke, and Gastegger (2021)", "Lennard-Jones (1924)"])
add(G, GN, "CHARMM was developed by:",
    "Brooks, Karplus, and colleagues (1983)",
    ["Jorgensen (1988)", "Kohn and Sham (1965)", "Peruzzo et al. (2014)"])
add(G, GN, "OPLS was developed by:",
    "Jorgensen (1988)",
    ["Weiner and Kollman (1984)", "Bartok et al. (2010)", "Kiss et al. (2022)"])
add(G, GN, "The AMBER/CHARMM/OPLS-style energy expression sums over which terms?",
    "Bonds, angles, dihedrals, van der Waals, and electrostatics",
    ["Only van der Waals terms", "Only the Schrodinger equation's kinetic term", "Only electrostatics"])
add(G, GN, "The bond-stretching term in a molecular mechanics force field typically has the form:",
    "$k_b(r-r_0)^2$, a harmonic term",
    ["$4\\varepsilon[(\\sigma/r)^{12}-(\\sigma/r)^6]$", "$\\exp(-i\\alpha\\vec x\\cdot\\vec\\sigma)$", "$k_\\phi[1+\\cos(n\\phi-\\delta)]$"])
add(G, GN, "The dihedral (torsion) term typically has the form:",
    "$k_\\phi[1+\\cos(n\\phi-\\delta)]$",
    ["$k_b(r-r_0)^2$", "$q_iq_j/(4\\pi\\epsilon_0 r_{ij})$", "$4\\varepsilon[(\\sigma/r)^{12}-(\\sigma/r)^6]$"])
add(G, GN, "How are the parameters ($k_b, r_0, k_\\theta,\\ldots$) of a molecular mechanics force field obtained?",
    "Fit once, offline, to experimental data and/or reference quantum-chemistry calculations",
    ["Learned online during every simulation via backpropagation", "Measured directly by a quantum computer", "They are universal physical constants, never fit"])
add(G, GN, "Once fit, how are these parameters used during a simulation?",
    "Reused unchanged for every simulation frame",
    ["Re-optimized at every single timestep", "Discarded after the first frame", "Replaced by DFT at every step"])
add(G, GN, "What is the main practical advantage of molecular mechanics force fields?",
    "They are extremely fast to evaluate and scale to systems with millions of atoms",
    ["They are more accurate than any quantum-chemical method", "They require no parameter fitting at all", "They can describe bond breaking natively"])
add(G, GN, "Why did molecular mechanics force fields dominate computational chemistry for three decades?",
    "Because their speed and scalability made large biomolecular/materials simulations (proteins, membranes) tractable",
    ["Because no alternative method existed at all", "Because they are more accurate than DFT", "Because they require quantum computers"])

# ============ GROUP 12: Limitations of classical force fields ============
G, GN = 12, "Limitations of classical force fields"
add(G, GN, "A classical molecular-mechanics force field assumes:",
    "A fixed bonding topology, decided before the simulation starts",
    ["A dynamically changing bonding topology at every step", "No atoms at all, only fields", "An exact solution of the electronic Schrodinger equation"])
add(G, GN, "Does a classical force field explicitly include electrons?",
    "No -- charge is a fixed point charge per atom, never redistributed",
    ["Yes, every electron is tracked individually", "Yes, but only core electrons", "Only for metals"])
add(G, GN, "What can a classical force field NOT describe, as a direct consequence of its fixed topology?",
    "A chemical reaction (a bond breaking or forming)",
    ["Any atomic motion whatsoever", "Temperature changes", "Van der Waals attraction"])
add(G, GN, "Besides reactions, what else does a classical force field fail to capture?",
    "Polarization and charge transfer",
    ["Atomic mass", "The existence of bonds", "Gravitational forces (irrelevant at this scale anyway)"])
add(G, GN, "How reliable is a classical force field outside its narrow fitting domain?",
    "Unreliable -- its accuracy for configurations unlike its training/fitting data is not guaranteed",
    ["Perfectly reliable everywhere by construction", "More reliable than DFT everywhere", "Irrelevant, since force fields have no domain restriction"])
add(G, GN, "What kind of process specifically requires going back to solving the underlying quantum mechanics?",
    "Any process where electronic structure actually changes (e.g. reactive chemistry, catalysis)",
    ["Any process at constant temperature", "Simulating a rigid crystal lattice", "Simulating an ideal gas"])
add(G, GN, "What was 'built to close' the gap left by classical force fields' limitations?",
    "Ab initio quantum-chemical methods, and later machine-learned potentials",
    ["Faster classical computers alone", "Larger simulation boxes", "Longer simulation times"])
add(G, GN, "Which of the following is an example of a process a classical force field cannot model correctly?",
    "An enzyme catalyzing a bond-breaking reaction",
    ["A protein vibrating around its equilibrium structure", "A noble gas atom translating freely", "Two neutral atoms held together purely by van der Waals attraction"])
add(G, GN, "Machine-learned and quantum-mechanical potentials aim to fix this gap by:",
    "Learning or computing the true, geometry-dependent electronic energy surface instead of using a fixed functional form",
    ["Removing all atoms from the simulation", "Increasing the simulation box size only", "Using a larger integration timestep"])
add(G, GN, "In one sentence, why is this limitation 'the fundamental motivation for everything that follows' in this document?",
    "Because it is precisely the accuracy gap that ab initio methods and ML/QML force fields were developed to close",
    ["Because classical force fields are no longer used at all today", "Because it has no connection to the rest of the document", "Because it only matters for quantum computers"])

# ============ GROUP 13: Application domains ============
G, GN = 13, "Why atomistic simulation matters: application domains"
add(G, GN, "In drug design, atomistic simulation is used to predict:",
    "How a candidate molecule binds to a protein target (binding pose, binding free energy)",
    ["The color of the drug tablet", "The manufacturing cost only", "The patent filing date"])
add(G, GN, "In catalysis research, what is typically computed using atomistic simulation?",
    "Reaction barriers on metal surfaces or in zeolites",
    ["The price of the catalyst on the market", "The catalyst's brand name", "Its shipping weight"])
add(G, GN, "Give an example industrial catalytic process mentioned as motivation for accurate simulation.",
    "Ammonia synthesis or CO2 reduction",
    ["Manufacturing glass bottles", "Printing newspapers", "Baking bread"])
add(G, GN, "In battery/energy materials research, what does atomistic simulation help predict?",
    "Ion diffusion barriers in solid electrolytes and electrode degradation mechanisms",
    ["The battery's retail price", "The color of the battery casing", "Shipping regulations"])
add(G, GN, "In semiconductor/materials science, atomistic simulation helps compute:",
    "Defect formation energies and band-structure-relevant geometries",
    ["Marketing strategy", "Factory floor layout", "Employee schedules"])
add(G, GN, "Why does simulating a protein-ligand complex require higher accuracy than simulating a rigid crystal?",
    "Because binding involves subtle energy differences that determine whether binding is favorable at all",
    ["It does not -- both require identical accuracy", "Proteins have no atoms", "Ligands are always simulated classically with no need for accuracy"])
add(G, GN, "Atomistic simulation substitutes for, or guides, which real-world activity?",
    "Expensive physical experiments (synthesis, testing) across chemistry/materials/biology",
    ["Only theoretical mathematics with no experimental connection", "Manufacturing quality control exclusively", "Financial accounting"])
add(G, GN, "Which application domain involves zeolites as a specific example material?",
    "Catalysis",
    ["Drug design", "Battery materials", "Semiconductor defects"])
add(G, GN, "Which application domain is most directly connected to 'ion diffusion'?",
    "Battery and energy materials",
    ["Drug design", "Catalysis on metal surfaces", "Semiconductor band structure"])
add(G, GN, "Across all these domains, what is the common computational quantity being predicted?",
    "Energies and forces (or energy differences) as a function of atomic/molecular configuration",
    ["Stock market prices", "Weather forecasts", "Internet traffic patterns"])

# ============ GROUP 14: Why accuracy matters (Arrhenius, chemical accuracy) ============
G, GN = 14, "Why accuracy matters: Arrhenius law and chemical accuracy"
add(G, GN, "The Arrhenius law relates reaction rate to energy barrier as:",
    "$k = A\\exp(-E_a/RT)$",
    ["$k = A E_a T$", "$k = A/E_a$", "$k = A - E_a T$"])
add(G, GN, "Because of the exponential in the Arrhenius law, a small error in the computed barrier $E_a$ can:",
    "Change the predicted rate by an order of magnitude or more",
    ["Have no effect on the predicted rate at all", "Only affect the rate linearly, never exponentially", "Only matter at absolute zero temperature"])
add(G, GN, "An error of 1-2 kcal/mol in a computed reaction barrier is:",
    "Well within what a poorly-fit classical force field can be off by",
    ["Impossible for any force field to produce", "Only achievable by quantum computers", "Larger than any realistic computational error"])
add(G, GN, "'Chemical accuracy' is conventionally defined as errors below about:",
    "1 kcal/mol ($\\approx$43 meV)",
    ["1 eV", "100 kcal/mol", "1 J/mol"])
add(G, GN, "Do classical force fields typically reach chemical accuracy for chemistry involving bond rearrangement?",
    "Almost never",
    ["Always, by construction", "Only above 1000 K", "Only for noble gases"])
add(G, GN, "Can quantum-mechanical methods (DFT, CCSD(T)) reach chemical accuracy?",
    "Yes, but at a steep computational price",
    ["No, quantum methods are always less accurate than classical force fields", "Yes, and always for free", "Only for systems with a single atom"])
add(G, GN, "What is the entire motivation for building faster surrogate models (classical ML, and now QML)?",
    "To reproduce quantum-mechanical accuracy without the quantum-mechanical computational cost",
    ["To eliminate the need for any accuracy at all", "To replace Newton's laws", "To avoid using computers entirely"])
add(G, GN, "If a reaction barrier is underestimated by 1.4 kcal/mol at room temperature, the predicted rate is roughly:",
    "About one order of magnitude too fast (a rough rule of thumb from the exponential sensitivity)",
    ["Completely unaffected", "Exactly halved", "Reduced to zero"])
add(G, GN, "Chemical reaction rates depend on the energy barrier:",
    "Exponentially",
    ["Linearly", "Logarithmically", "Not at all"])
add(G, GN, "Why is 'accurate enough' described as 'a hard bar to clear'?",
    "Because the exponential sensitivity of rates to barrier height makes even small energy errors practically significant",
    ["Because no one has ever measured a reaction rate", "Because energy is not a well-defined physical quantity", "Because computers cannot represent real numbers"])

# ============ GROUP 15: Schrodinger equation & Born-Oppenheimer ============
G, GN = 15, "Schrodinger equation and Born-Oppenheimer approximation"
add(G, GN, "The time-independent Schrodinger equation is written as:",
    "$\\hat H \\Psi = E\\Psi$",
    ["$\\hat H + \\Psi = E$", "$\\hat H \\Psi = \\Psi$", "$E = mc^2$"])
add(G, GN, "The Schrodinger equation can be solved exactly, in closed form, for:",
    "The hydrogen atom",
    ["Any molecule with more than 2 atoms", "Only crystalline solids", "Only systems with more than 100 electrons"])
add(G, GN, "For systems larger than hydrogen, the Schrodinger equation is:",
    "Intractable to solve exactly in closed form",
    ["Trivially solvable by hand", "Not applicable at all", "Solvable using only Newton's laws"])
add(G, GN, "The Born-Oppenheimer approximation is justified because:",
    "Nuclei are about 1800 times heavier than electrons and move much more slowly",
    ["Electrons and nuclei have exactly equal mass", "Nuclei do not exist in quantum mechanics", "Electrons never move"])
add(G, GN, "Under the Born-Oppenheimer approximation, the electronic Schrodinger equation is solved:",
    "For fixed nuclear positions",
    ["Only after nuclei have finished moving forever", "By ignoring electrons entirely", "Using classical mechanics for electrons"])
add(G, GN, "The result of solving the electronic problem at fixed nuclear positions is:",
    "The electronic energy $E_{el}(\\{\\vec R_A\\})$, i.e. the potential energy surface (PES)",
    ["A random number with no physical meaning", "The nuclear mass", "The temperature of the system"])
add(G, GN, "Under Born-Oppenheimer, nuclear motion is governed by:",
    "$M_A\\ddot{\\vec R}_A = -\\nabla_{\\vec R_A} E_{el}(\\{\\vec R_A\\})$",
    ["$M_A\\ddot{\\vec R}_A = E_{el}$", "$M_A\\ddot{\\vec R}_A = 0$ always", "$M_A\\ddot{\\vec R}_A = \\hat H\\Psi$"])
add(G, GN, "According to this document, what 'is' the force field, defined rigorously rather than empirically?",
    "The potential energy surface $E_{el}(\\{\\vec R_A\\})$ itself",
    ["The Lennard-Jones parameter $\\sigma$", "The simulation timestep", "The number of qubits used"])
add(G, GN, "Which methods in this project are all ultimately trying to evaluate $E_{el}$ and its gradient?",
    "Classical MD force fields, PaiNN, and siVQLM",
    ["Only siVQLM", "Only classical MD", "None of them -- they compute unrelated quantities"])
add(G, GN, "The variable $\\Psi$ in the Schrodinger equation depends on:",
    "The positions of both electrons and nuclei, $\\{\\vec r_i\\}$ and $\\{\\vec R_A\\}$",
    ["Only the simulation software version", "Only the temperature", "Nothing -- it is a universal constant"])

# ============ GROUP 16: Hartree-Fock & post-HF methods ============
G, GN = 16, "Hartree-Fock and post-Hartree-Fock methods"
add(G, GN, "Hartree-Fock approximates the many-electron wavefunction as:",
    "A single Slater determinant of one-electron orbitals",
    ["A random matrix", "A classical point-charge model", "A single Gaussian function with no orbitals"])
add(G, GN, "How is the Hartree-Fock equation typically solved?",
    "Self-consistently (iteratively, until the orbitals converge)",
    ["In a single closed-form algebraic step", "By ignoring the nuclei entirely", "Using only classical mechanics"])
add(G, GN, "What does Hartree-Fock famously miss, limiting its accuracy?",
    "Electron correlation",
    ["The nuclear charge", "The number of electrons", "The existence of orbitals"])
add(G, GN, "Post-HF methods such as MP2 and CCSD(T) improve accuracy by:",
    "Adding electron correlation back into the calculation",
    ["Removing all electrons from the model", "Ignoring the nuclei", "Using a larger simulation timestep"])
add(G, GN, "CCSD(T) is often referred to as:",
    "The 'gold standard' of quantum chemistry",
    ["The fastest possible method", "A purely classical force field", "A dataset, not a method"])
add(G, GN, "How does CCSD(T) formally scale with system size $N$?",
    "$O(N^7)$",
    ["$O(N)$", "$O(\\log N)$", "$O(1)$, independent of size"])
add(G, GN, "Why is CCSD(T), despite being highly accurate, not used for every large simulation?",
    "Its steep computational cost (poor scaling with system size) makes it impractical for large systems",
    ["It is less accurate than Hartree-Fock", "It cannot be run on any computer", "It was never validated against experiment"])
add(G, GN, "Which of these is a 'post-Hartree-Fock' method mentioned in this document?",
    "MP2",
    ["DFT", "Lennard-Jones", "PaiNN"])
add(G, GN, "The accuracy ordering (loosely) among these methods, from lower to higher, is typically:",
    "Hartree-Fock < DFT (with a good functional) $\\lesssim$ MP2 < CCSD(T)",
    ["CCSD(T) < Hartree-Fock < DFT < MP2, always in that fixed order", "All these methods have identical accuracy always", "Accuracy is unrelated to method choice"])
add(G, GN, "What Hartree-Fock and CCSD(T) have in common, versus DFT, is that both work in terms of:",
    "The many-electron wavefunction (or determinants/excitations built from orbitals)",
    ["The electron density alone, never the wavefunction", "Only classical point charges", "Only qubit operators"])

# ============ GROUP 17: DFT and Kohn-Sham equations ============
G, GN = 17, "Density Functional Theory (DFT) and Kohn-Sham equations"
add(G, GN, "DFT reformulates the electronic structure problem in terms of:",
    "The electron density $n(\\vec r)$, rather than the many-body wavefunction",
    ["The nuclear charge only", "The simulation temperature", "The number of qubits available"])
add(G, GN, "The Kohn-Sham equations have the form:",
    "$[-\\tfrac12\\nabla^2 + v_{eff}[n](\\vec r)]\\phi_i(\\vec r) = \\epsilon_i\\phi_i(\\vec r)$",
    ["$\\hat H\\Psi = 0$ always", "$n(\\vec r) = \\text{const}$", "$m_i\\ddot{\\vec r}_i = \\vec F_i$"])
add(G, GN, "In Kohn-Sham DFT, the electron density is reconstructed from the orbitals as:",
    "$n(\\vec r) = \\sum_i |\\phi_i(\\vec r)|^2$",
    ["$n(\\vec r) = \\sum_i \\phi_i(\\vec r)$", "$n(\\vec r) = \\epsilon_i$", "$n(\\vec r)$ is unrelated to the orbitals"])
add(G, GN, "How does DFT typically scale with system size $N$, compared to CCSD(T)?",
    "Much more favourably, typically $O(N^3)$",
    ["Identically to CCSD(T), $O(N^7)$", "Worse than CCSD(T)", "DFT does not scale with $N$ at all"])
add(G, GN, "What makes DFT 'the dominant workhorse for generating training data for machine-learned potentials'?",
    "Its favourable balance of reasonable accuracy (with a good exchange-correlation functional) and manageable cost",
    ["It is the only method that has ever been implemented in software", "It requires no approximations whatsoever", "It is more accurate than CCSD(T) in all cases"])
add(G, GN, "What key ingredient of the Kohn-Sham equations is NOT exactly known and must be approximated?",
    "The exchange-correlation functional",
    ["The electron mass", "The number of atoms", "Newton's second law"])
add(G, GN, "Which named functional is mentioned in this document as a reference level for the QM9 dataset?",
    "B3LYP",
    ["PBE+vdW", "$\\omega$B97X", "CCSD(T)"])
add(G, GN, "Which reference level is mentioned for the MD17/rMD17 dataset?",
    "DFT (PBE+vdW)",
    ["CCSD(T) exclusively", "Experimental X-ray diffraction", "Hartree-Fock only"])
add(G, GN, "DFT and Hartree-Fock differ fundamentally in that DFT works with:",
    "The electron density, not the many-electron wavefunction directly",
    ["Exactly the same mathematical object as HF", "Only classical trajectories", "Qubit operators"])
add(G, GN, "Nearly every ML/QML force field dataset discussed in this document (QM9, MD17, ANI-1x, OC20) uses which family of reference method?",
    "DFT (with various functionals)",
    ["Experimental calorimetry exclusively", "Only Hartree-Fock", "Only classical force fields"])

# ============ GROUP 18: Experimental validation methods ============
G, GN = 18, "Experimental validation: diffraction, spectroscopy, NMR, calorimetry"
add(G, GN, "X-ray and neutron diffraction primarily give information about:",
    "Equilibrium molecular/crystal structures",
    ["Reaction rate constants directly", "The exchange-correlation functional", "Qubit coherence times"])
add(G, GN, "Infrared (IR) and Raman spectroscopy primarily give information about:",
    "Vibrational frequencies",
    ["Nuclear spin states only", "Electron correlation energy directly", "Reaction yield percentages"])
add(G, GN, "Vibrational frequencies from IR/Raman are sensitive to which property of the potential energy surface?",
    "Its curvature (second derivative) around the equilibrium geometry",
    ["Its value at infinite separation only", "Its first derivative (the force) only", "Nothing about the PES -- they are unrelated"])
add(G, GN, "NMR spectroscopy primarily gives information about:",
    "Local chemical environments",
    ["Bulk crystal density", "Reaction barrier heights directly", "Qubit gate fidelities"])
add(G, GN, "Calorimetry primarily gives information about:",
    "Reaction thermodynamics",
    ["Atomic positions to picometer precision", "Vibrational frequencies", "Electron density maps"])
add(G, GN, "What do these experimental techniques validate, according to this document?",
    "That DFT/CCSD(T), as methods, are trustworthy",
    ["That classical force fields never need experimental validation", "That quantum computers are faster than classical computers", "Nothing useful for computational chemistry"])
add(G, GN, "Why can't these experiments directly supply the training labels needed for supervised ML force fields?",
    "They measure bulk or ensemble-averaged properties, not atom-by-atom energy/force labels for arbitrary geometries",
    ["Because experiments are always less accurate than any calculation", "Because experiments cannot be performed on molecules", "Because ML models cannot use any experimental data ever"])
add(G, GN, "What is used instead of direct experimental measurement to generate per-atom force labels for datasets like MD17?",
    "Computed (not measured) DFT energies and forces for individual atomic configurations",
    ["Randomly generated numbers", "Direct laboratory force-sensor measurements on single atoms", "Guesses by the dataset authors"])
add(G, GN, "This document calls the process of running DFT to generate dataset labels:",
    "Computational 'measurement' (i.e. labelling)",
    ["Experimental validation", "Quantum error correction", "Barren plateau mitigation"])
add(G, GN, "The overall two-step logic connecting theory to datasets is:",
    "Validate the QM method against experiment first, then use that trusted method to compute labels for many configurations",
    ["Skip experimental validation entirely and trust any QM method blindly", "Use experiments directly as force labels with no computation involved", "There is no connection between experiment and datasets"])

# ============ GROUP 19: Computational "measurement" recap + broader synthesis ============
G, GN = 19, "From equations to datasets: synthesis"
add(G, GN, "Two activities are 'often conflated' under the question 'how do we know the energy/forces are right'. What are they?",
    "Experimental validation of the method, and computational labelling (running the method to generate data)",
    ["Only running simulations twice", "Buying more expensive hardware and nothing else", "There is only one such activity, not two"])
add(G, GN, "If a new exchange-correlation functional were never checked against any spectroscopy or diffraction data, what would be missing?",
    "Experimental validation that the method itself is trustworthy",
    ["Nothing -- validation is unnecessary for DFT", "The functional would automatically be exact", "The dataset labels would still be reliable regardless"])
add(G, GN, "Why does this document emphasize the distinction between 'validation' and 'labelling'?",
    "Because ML force fields are trained on computed (labelling) data, which is only trustworthy because the underlying method was separately validated experimentally",
    ["Because the two concepts are identical and the distinction is meaningless", "Because only labelling matters and validation is irrelevant", "Because only validation matters and labelling is irrelevant"])
add(G, GN, "Which of the following best restates the logical chain from Section 1 of this document?",
    "Newton's laws need a potential $\\to$ empirical potentials were limited $\\to$ quantum mechanics gives a rigorous potential $\\to$ DFT makes it computable $\\to$ DFT is validated experimentally $\\to$ DFT then labels datasets $\\to$ ML/QML learn from those datasets",
    ["Datasets come first, then Newton's laws are derived from them", "Quantum computers were used to generate every historical dataset since 1924", "None of these steps are actually connected"])
add(G, GN, "A vibrational frequency computed from DFT can be checked against which experimental technique?",
    "IR or Raman spectroscopy",
    ["Only NMR", "Only X-ray diffraction", "Only calorimetry"])
add(G, GN, "An equilibrium bond length computed from DFT can be checked against which experimental technique?",
    "X-ray or neutron diffraction",
    ["Only calorimetry", "Only IR spectroscopy", "Only NMR"])
add(G, GN, "Why is chemical accuracy (Group 14) relevant to the choice of reference method (Groups 16-17) for a dataset?",
    "Because the dataset's usefulness for training an accurate force field depends on its labels meeting chemical accuracy versus experiment",
    ["It is not relevant at all", "Because chemical accuracy only applies to classical force fields", "Because reference methods are chosen randomly regardless of accuracy"])
add(G, GN, "If a force field is trained on DFT labels with a poor exchange-correlation functional, what is the likely consequence?",
    "The trained force field inherits and cannot exceed the errors of the underlying DFT functional",
    ["The force field will automatically be more accurate than the DFT it was trained on", "There will be no consequence at all", "The force field will instead learn the exact Schrodinger equation"])
add(G, GN, "Is CCSD(T) or DFT more commonly used to label large-scale ML datasets like OC20 (millions of configurations)?",
    "DFT, because of its far better computational scaling",
    ["CCSD(T), because it is cheaper", "Neither -- OC20 uses experimental data only", "Hartree-Fock exclusively"])
add(G, GN, "What is the ultimate practical payoff of training an ML force field on DFT-labelled data?",
    "Approaching DFT-level accuracy at a small fraction of DFT's computational cost, at inference time",
    ["Achieving CCSD(T) accuracy for free with no computation", "Eliminating the need for the Born-Oppenheimer approximation", "Making the classical force field parameters irrelevant to memory"])

# ============ GROUP 20: Datasets I - QM9, MD17/rMD17 ============
G, GN = 20, "Datasets I -- QM9 and MD17/rMD17"
add(G, GN, "QM9 contains approximately how many small organic molecules?",
    "$\\sim$134,000",
    ["134", "1.34 million", "13"])
add(G, GN, "QM9 molecules are limited to up to how many heavy (non-hydrogen) atoms?",
    "9",
    ["2", "50", "900"])
add(G, GN, "QM9's reference level of theory is:",
    "DFT (B3LYP)",
    ["CCSD(T)", "Experimental calorimetry", "Hartree-Fock only"])
add(G, GN, "QM9 is primarily used for:",
    "Property prediction and pretraining",
    ["Real-time weather forecasting", "Battery manufacturing schedules", "Protein folding exclusively"])
add(G, GN, "MD17/rMD17 contains what kind of data?",
    "MD trajectories of single small organic molecules, with energies and forces",
    ["Only equilibrium crystal structures", "Only reaction rate constants", "Only NMR spectra"])
add(G, GN, "The molecule size range in MD17 is:",
    "9 to 21 atoms",
    ["1 to 3 atoms", "1000 to 5000 atoms", "Exactly 100 atoms always"])
add(G, GN, "MD17's reference level of theory is:",
    "DFT (PBE+vdW)",
    ["B3LYP only", "CCSD(T) exclusively", "No quantum-chemical reference at all"])
add(G, GN, "Which models mentioned in this document all target the MD17/rMD17 benchmark family?",
    "PaiNN, NequIP, MACE, and siVQLM",
    ["Only AMBER and CHARMM", "Only Lennard-Jones-based models", "Only experimental spectroscopy techniques"])
add(G, GN, "What distinguishes MD17 from QM9 in terms of scope?",
    "MD17 focuses on force-field-relevant trajectories of single molecules; QM9 is a broad, static equilibrium-geometry property dataset",
    ["They are identical datasets with different names", "QM9 has forces and MD17 does not", "MD17 contains inorganic crystals, QM9 does not"])
add(G, GN, "Does MD17 provide per-atom forces, not just energies?",
    "Yes -- forces are a core part of the dataset, essential for force-field training",
    ["No, only energies are provided", "No, only equilibrium structures are provided", "Forces are provided but never used for training"])

# ============ GROUP 21: Datasets II - ANI-1x, OC20/22, Materials Project, SPICE ============
G, GN = 21, "Datasets II -- ANI-1x, Open Catalyst, Materials Project, SPICE"
add(G, GN, "ANI-1/ANI-1x contain:",
    "Millions of off-equilibrium conformations across a broad chemical space",
    ["Only 10 molecules total", "Only equilibrium geometries", "Only inorganic crystals"])
add(G, GN, "ANI-1x's reference level of theory is:",
    "DFT ($\\omega$B97X)",
    ["Experimental NMR only", "CCSD(T) exclusively", "No DFT functional at all"])
add(G, GN, "ANI-1x-style datasets are primarily used for:",
    "Transferable, general-purpose potentials",
    ["Single-molecule spectroscopy only", "Weather prediction", "Only battery materials"])
add(G, GN, "The Open Catalyst (OC20/OC22) dataset contains:",
    "Millions of adsorbate-catalyst-surface configurations",
    ["Only small organic molecules with no surfaces", "Only protein structures", "Only NMR spectra"])
add(G, GN, "OC20/OC22 is primarily relevant for:",
    "Catalysis-relevant surface force fields",
    ["Drug binding affinity exclusively", "Battery electrolyte diffusion exclusively", "Astronomical simulations"])
add(G, GN, "The Materials Project dataset contains:",
    ">100k inorganic crystal structures with formation energies",
    ["Only organic drug-like molecules", "Only protein-ligand complexes", "Only vibrational spectra"])
add(G, GN, "Materials Project is primarily used for:",
    "Materials discovery and screening",
    ["Protein folding prediction exclusively", "Drug binding affinity exclusively", "Weather forecasting"])
add(G, GN, "The SPICE dataset focuses on:",
    "Drug-like molecules, with a DFT/coupled-cluster mix of reference levels",
    ["Only inorganic crystals", "Only catalytic surfaces", "Only vibrational spectra with no energies"])
add(G, GN, "SPICE is primarily used for:",
    "Force fields for biomolecular simulation",
    ["Materials discovery in inorganic crystals", "Weather prediction", "Catalytic surface reactions exclusively"])
add(G, GN, "Which dataset among ANI-1x, OC20, Materials Project, and SPICE is most directly relevant to catalysis?",
    "Open Catalyst (OC20/OC22)",
    ["ANI-1x", "Materials Project", "SPICE"])

# ============ GROUP 22: ML era I - Behler-Parrinello, GAP ============
G, GN = 22, "The ML era I -- Behler-Parrinello and GAP"
add(G, GN, "The Behler-Parrinello neural-network potential was introduced in:",
    "2007",
    ["1924", "1984", "2021"])
add(G, GN, "Behler-Parrinello potentials encode atomic environments using:",
    "Hand-encoded, rotation/permutation-invariant 'atom-centered symmetry functions' (ACSFs)",
    ["A raw list of Cartesian coordinates fed directly to the network with no preprocessing", "A quantum circuit", "Only the total molecular mass"])
add(G, GN, "In Behler-Parrinello potentials, who designs the descriptor (ACSF)?",
    "The researcher -- it is engineered by hand, not learned",
    ["The neural network learns it end-to-end automatically", "A quantum computer generates it", "It is derived directly from experimental spectra"])
add(G, GN, "After computing ACSFs, what processes them in a Behler-Parrinello model?",
    "A per-atom feed-forward neural network",
    ["A classical Lennard-Jones formula only", "A convolutional filter over images", "A parameter-shift quantum circuit"])
add(G, GN, "Gaussian Approximation Potentials (GAP) were introduced by Bartok et al. in:",
    "2010",
    ["1924", "2007", "2022"])
add(G, GN, "GAP is based on which machine-learning technique?",
    "Kernel-based (Gaussian process) regression",
    ["Deep convolutional neural networks", "Variational quantum circuits", "Random forests"])
add(G, GN, "GAP typically operates on which kind of descriptor?",
    "Invariant descriptors such as SOAP",
    ["Raw unprocessed pixel images", "Qubit measurement statistics", "Stock price time series"])
add(G, GN, "GAP is described as particularly popular for materials where:",
    "Training data is scarce",
    ["Training data is infinite", "No quantum-chemical reference exists", "Only experimental data is available"])
add(G, GN, "What do Behler-Parrinello and GAP have in common, contrasted with later deep-learning potentials?",
    "Both rely on hand-crafted (not learned) descriptors of the atomic environment",
    ["Both use exactly the same neural network architecture", "Both were introduced after SchNet", "Neither has ever been used for real materials"])
add(G, GN, "In the historical timeline of this document, Behler-Parrinello (2007) and GAP (2010) both precede:",
    "SchNet (2017) and the equivariant wave (2021-2022)",
    ["The Lennard-Jones potential (1924)", "AMBER (1984)", "The Schrodinger equation itself"])

# ============ GROUP 23: ML era II - SchNet to equivariant wave ============
G, GN = 23, "The ML era II -- SchNet to the equivariant wave"
add(G, GN, "SchNet, introduced in 2017, was significant as:",
    "The first widely-used deep-learning potential in this project's direct baseline lineage",
    ["The first molecular dynamics simulation ever performed", "A purely classical force field with no learning", "A quantum circuit-based model"])
add(G, GN, "SchNet's core architectural mechanism is:",
    "Continuous-filter convolutions over interatomic distances",
    ["Attention over qubit measurement outcomes", "Fixed Lennard-Jones parameters only", "Hand-crafted ACSF descriptors with no convolution"])
add(G, GN, "Is SchNet invariant or equivariant?",
    "Purely invariant",
    ["Purely equivariant, carrying explicit vector channels", "Neither -- it has no symmetry properties at all", "Equivariant only under permutation, never rotation"])
add(G, GN, "Which model is described as SchNet's 'direct successor', covered in full architectural detail elsewhere in this document?",
    "PaiNN",
    ["siVQLM", "GAP", "Behler-Parrinello"])
add(G, GN, "The 'equivariant wave' of models (2021-2022) includes:",
    "PaiNN, NequIP, Allegro, and MACE",
    ["Only Lennard-Jones and AMBER", "Only Behler-Parrinello and GAP", "Only siVQLM and Kiss et al. 2022"])
add(G, GN, "What did the equivariant wave replace, compared to earlier invariant-only models?",
    "Hand-crafted invariant descriptors, replaced with learned, geometry-respecting vector/tensor features",
    ["All neural networks, replaced with kernel methods", "DFT itself, replaced with experiments", "Newton's laws, replaced with quantum mechanics"])
add(G, GN, "What is claimed as the practical benefit of the equivariant wave models?",
    "Closing most of the accuracy gap to DFT at a fraction of the computational cost",
    ["Making DFT completely obsolete and unnecessary", "Eliminating the need for any training data", "Removing the need for the Born-Oppenheimer approximation"])
add(G, GN, "According to this document's stated 'throughline', what does each ML generation remove?",
    "One more hand-engineered assumption (functional form of $U$, then the descriptor, then the invariant-only restriction)",
    ["All physical laws, replaced entirely by data", "The need for any atoms in the simulation", "The requirement of using a computer at all"])
add(G, GN, "Where in this document is the equivariant wave (PaiNN, NequIP, MACE) compared in detail?",
    "Section 3 (PaiNN architecture) and the project's Literature Review",
    ["Nowhere -- they are only mentioned in Section 1", "Only in the MCQ exam file", "Only in the siVQLM circuit diagram"])
add(G, GN, "Today's classical state-of-the-art machine-learned force fields, per this document, are:",
    "The equivariant-wave models (PaiNN, NequIP, Allegro, MACE)",
    ["Behler-Parrinello potentials", "AMBER and CHARMM", "Lennard-Jones-only models"])

# ============ GROUP 24: Quantum computing frontier - VQE vs QML FF, encoding ============
G, GN = 24, "The quantum-computing frontier: VQE vs QML force fields, encoding"
add(G, GN, "Quantum computing enters computational chemistry through how many conceptually different 'doors', per this document?",
    "Two",
    ["Zero", "One", "Five"])
add(G, GN, "VQE (Variational Quantum Eigensolver) was introduced by Peruzzo et al. in:",
    "2014",
    ["1924", "2007", "2022"])
add(G, GN, "VQE targets which problem directly?",
    "The electronic structure problem itself",
    ["Classical molecular dynamics integration", "Weather forecasting", "Protein sequence alignment"])
add(G, GN, "In VQE, the molecular electronic Hamiltonian is mapped from fermionic operators to qubit operators via:",
    "The Jordan-Wigner or Bravyi-Kitaev transformation",
    ["The Fourier transform only", "A classical force field parametrization", "The Born-Oppenheimer approximation"])
add(G, GN, "In VQE, what does the parametrized quantum circuit do?",
    "Prepares a trial wavefunction whose energy is variationally minimized",
    ["Directly simulates Newton's equations of motion", "Stores classical MD trajectories only", "Replaces the need for any Hamiltonian"])
add(G, GN, "VQE is described as directly replacing which classical methods, as the electronic-structure solver?",
    "Hartree-Fock/DFT/CCSD(T)",
    ["Only Newtonian mechanics", "Only classical force fields like AMBER", "Only experimental spectroscopy"])
add(G, GN, "What is VQE's long-term motivating hope?",
    "That a fault-tolerant quantum computer could reach CCSD(T)-or-better accuracy at polynomial rather than exponential cost for strongly-correlated systems",
    ["That VQE will replace Newton's second law for all classical MD", "That VQE eliminates the need for any qubits", "That VQE only works for the hydrogen atom"])
add(G, GN, "In contrast to VQE, what do QML force fields (Kiss et al. 2022, siVQLM) attempt to do?",
    "They do NOT attempt to solve the electronic structure problem on the quantum computer at all",
    ["They solve the exact many-electron Schrodinger equation on a quantum computer", "They are identical to VQE in every respect", "They replace DFT as the electronic-structure solver"])
add(G, GN, "In QML force fields, what role does the variational quantum circuit play?",
    "A flexible, trainable function approximator $f_\\Theta: \\mathcal X \\to \\mathbb R$ mapping nuclear coordinates to predicted energy",
    ["An electronic-structure solver replacing CCSD(T)", "A random number generator with no training", "A classical force field with fixed parameters"])
add(G, GN, "What is 'encoded' into the quantum circuit in a QML force field (siVQLM), as clarified in this document?",
    "Classical geometric/nuclear coordinate data, not the electronic wavefunction",
    ["The full electronic wavefunction, exactly as in VQE", "Experimental spectroscopy data directly", "Nothing -- QML force fields require no encoding"])
