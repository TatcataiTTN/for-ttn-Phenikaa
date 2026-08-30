# -*- coding: utf-8 -*-
# 56 new practical/code-level questions (groups 25-26), based on REAL artifacts inspected/run
# this session: Source_Code/schnetpack config.yaml+split.npz (group 25), and a REAL training run
# of the siVQLM circuit this session (group 26) -- see Source_Code/practical_runs.md.
GROUPS_25_26 = []

def add(group, gname, stem, correct, distractors):
    assert len(distractors) == 3
    GROUPS_25_26.append({"group": group, "group_name": gname, "stem": stem,
                          "correct": correct, "distractors": distractors})

# ============ GROUP 25 (part A, 14) SchNetPack practical -- CLI/Hydra/config ============
G, GN = 25, "SchNetPack practical A -- CLI, Hydra config, real checkpoint"
add(G, GN, "The SchNetPack training CLI entry point is:",
    "spktrain (a thin wrapper calling schnetpack.cli.train)",
    ["schnetpack-run", "python train.py directly, no CLI wrapper exists", "spkfit"])
add(G, GN, "spktrain's train() function is decorated with:",
    "@hydra.main(config_path=\"configs\", config_name=\"train\")",
    ["@click.command()", "@pytest.fixture", "@torch.jit.script"])
add(G, GN, "To train PaiNN on rMD17 ethanol matching the real shipped checkpoint, the CLI override for the molecule is:",
    "data.molecule=ethanol",
    ["data.name=ethanol", "molecule=ethanol.db", "--molecule ethanol"])
add(G, GN, "The repo ships 5 pretrained PaiNN checkpoints on rMD17 ethanol named:",
    "painn_1 through painn_5 (an ensemble of 5 independent seeds)",
    ["painn_best only, a single checkpoint", "painn_v1 through painn_v10", "there are no pretrained checkpoints in the repo"])
add(G, GN, "Each checkpoint directory (e.g. painn_1/) contains:",
    "best_model, config.yaml, and split.npz",
    ["Only a .pt file, nothing else", "Only a README", "A Jupyter notebook only"])
add(G, GN, "Attempting torch.load() on best_model without the schnetpack package installed:",
    "Fails with ModuleNotFoundError: No module named 'schnetpack' (verified this session)",
    ["Succeeds immediately, no dependency needed", "Silently returns None", "Only works if PennyLane is installed instead"])
add(G, GN, "The real cutoff radius used in painn_1/config.yaml is:",
    "5.0 (Angstrom)",
    ["1.0", "10.0", "0.5"])
add(G, GN, "The real learning rate in painn_1/config.yaml is:",
    "0.001 (1e-3)",
    ["0.01", "1e-2 same as siVQLM", "0.1"])
add(G, GN, "The real n_atom_basis (embedding dimension C) used is:",
    "128",
    ["32", "8", "1024"])
add(G, GN, "The real n_interactions (number of PaiNN blocks) used is:",
    "3",
    ["1", "10", "100"])
add(G, GN, "shared_interactions and shared_filters in the real config are both set to:",
    "false (each interaction block has independent weights)",
    ["true (all blocks share the same weights)", "not present in the config at all", "true for interactions, false for filters"])
add(G, GN, "The real data.batch_size in painn_1/config.yaml is:",
    "10",
    ["256 (same as siVQLM)", "1", "1000"])
add(G, GN, "The default rmd17.yaml config (before any override) uses num_train/num_val of:",
    "950 / 50",
    ["900 / 100 (identical to the trained checkpoint, no override needed)", "9000 / 500", "100 / 10"])
add(G, GN, "The default molecule in configs/data/rmd17.yaml (before override) is:",
    "aspirin",
    ["ethanol", "malonaldehyde", "water"])

# ============ GROUP 25 (part B, 14) SchNetPack practical -- data split, loss, trainer ============
add(G, GN, "The real split.npz for painn_1 shows train_idx / val_idx / test_idx sizes of:",
    "900 / 100 / 99000",
    ["900 / 100 / 900", "80 / 20 / 0", "1000 / 1000 / 98000"])
add(G, GN, "rMD17 ethanol's total number of configurations (train+val+test) is:",
    "100,000",
    ["850 (same as the siVQLM H2O dataset)", "10,000", "1,000,000"])
add(G, GN, "In the real config, the energy loss_weight and force loss_weight are:",
    "0.01 (energy) and 0.99 (forces)",
    ["0.5 and 0.5, equal weighting", "0.99 (energy) and 0.01 (forces), reversed", "1.0 and 0.0, forces ignored entirely"])
add(G, GN, "The real optimizer class used is:",
    "torch.optim.AdamW",
    ["torch.optim.SGD", "jax.example_libraries.optimizers.adam (same as siVQLM)", "torch.optim.RMSprop"])
add(G, GN, "The real learning-rate scheduler is:",
    "schnetpack.train.ReduceLROnPlateau, factor=0.5, patience=75",
    ["A fixed learning rate, no scheduler used", "CosineAnnealingLR", "OneCycleLR"])
add(G, GN, "The real EarlyStopping patience (in epochs of no val_loss improvement) is:",
    "200",
    ["5", "1000 (same as max_epochs)", "0, disabled"])
add(G, GN, "The real trainer.max_epochs is:",
    "1000",
    ["10", "5000 (same as siVQLM num_batches)", "unlimited, no cap set"])
add(G, GN, "The ExponentialMovingAverage callback's decay parameter in the real config is:",
    "0.995",
    ["0.5", "1.0 (no averaging effect)", "0.001"])
add(G, GN, "The real data transforms are applied in this order:",
    "SubtractCenterOfMass -> RemoveOffsets(energy) -> MatScipyNeighborList(cutoff) -> CastTo32",
    ["CastTo32 first, then everything else", "Only CastTo32, no other transforms", "MatScipyNeighborList first, then SubtractCenterOfMass"])
add(G, GN, "The real postprocessors (applied after the model, at inference) include:",
    "CastTo64 and AddOffsets(energy, add_mean=True)",
    ["No postprocessors are defined", "Only a softmax layer", "RemoveOffsets, undoing the training-time offset removal"])
add(G, GN, "The real property units declared in the config are:",
    "energy: kcal/mol, forces: kcal/mol/Ang",
    ["energy: Hartree, forces: Hartree/Bohr (same units as siVQLM)", "energy: eV, forces: eV/Ang", "no units declared, dimensionless"])
add(G, GN, "The radial basis function used is:",
    "GaussianRBF with n_rbf=20",
    ["Bessel basis with n_rbf=8", "A single raw distance, no basis expansion", "Fourier basis with n_rbf=100"])
add(G, GN, "The cutoff function (smooth envelope) used is:",
    "CosineCutoff",
    ["A hard step function (no smoothing)", "PolynomialCutoff of degree 10", "No cutoff function is used"])
add(G, GN, "This session's environment limitation regarding SchNetPack, honestly documented, is:",
    "The full schnetpack package (with pytorch_lightning, hydra-core, ase, matscipy, torchmetrics) was NOT installed, to avoid heavy changes to the user's global Python environment -- so best_model was not re-evaluated for real MAE",
    ["schnetpack was fully installed and the model was fully re-evaluated with new MAE numbers", "SchNetPack cannot be installed on macOS at all", "The config.yaml and split.npz files could not be read either"])

# ============ GROUP 26 (part A, 14) siVQLM practical -- environment, data, real run ============
G, GN = 26, "siVQLM practical A -- environment fix, real data, official demo run"
add(G, GN, "Initially, `import pennylane` failed in this session's environment because:",
    "pennylane.qchem eagerly imports h5py, which was built against a different numpy ABI than the already-installed numpy",
    ["PennyLane was not installed at all and pip does not exist", "JAX and PennyLane cannot coexist in the same environment, ever", "The demo.py file itself had a syntax error"])
add(G, GN, "The fix applied this session for the pennylane import error was:",
    "pip install --upgrade h5py (only upgrading h5py)",
    ["Downgrading numpy to version 1.x", "Reinstalling the entire Python distribution", "Switching from pip to conda for every package"])
add(G, GN, "After fixing h5py, which previously-working packages were verified to still import correctly?",
    "numpy, torch, jax, scikit-learn, and matplotlib (all re-checked)",
    ["None -- the fix broke everything else", "Only numpy was re-checked", "Only jax was re-checked"])
add(G, GN, "The real H2O dataset shipped with the official demo contains how many configurations?",
    "850",
    ["100,000 (same as rMD17 ethanol)", "5,000", "3"])
add(G, GN, "The real Energy.npy values fall in the range:",
    "approximately -76.319749 to -76.302945 (Hartree)",
    ["0 to 1 (already pre-scaled in the raw file)", "-627.5 to 0 (kcal/mol)", "1 to 100 (arbitrary units)"])
add(G, GN, "Positions.npy and Forces.npy both have shape:",
    "(850, 3, 3) -- 850 samples, 3 atoms, 3 Cartesian components",
    ["(850, 2, 3), only the 2 active atoms stored", "(3, 850, 3), atoms as the first axis", "(850,), a flat 1-D array"])
add(G, GN, "Does the real dataset need to be downloaded before running the demo?",
    "No -- Positions/Energy/Forces.npy already ship inside the repo's eqnn_force_field_data/ folder",
    ["Yes, a 50GB download is required first", "Yes, but only from a paid API", "No data exists; it must be generated synthetically"])
add(G, GN, "When the official demo.py was actually run this session (num_batches reduced 5000 to 300 to save time), the initial (step 0) train/test loss was approximately:",
    "train=0.18668, test=0.17282",
    ["train=0.00001, test=0.00001 (already converged at step 0)", "train=100.0, test=100.0", "train=NaN, test=NaN (it crashed immediately)"])
add(G, GN, "After 300 steps, the official demo.py's test loss reached approximately:",
    "0.00444 (down from 0.17282)",
    ["Still 0.17282, no improvement at all", "0.5, it got worse", "Exactly 0, perfect fit"])
add(G, GN, "Why was num_batches reduced from 5000 to 300 for the official-demo cross-check run?",
    "To save wall-clock time while still checking the loss converges in the right direction/order of magnitude",
    ["Because pennylane cannot run more than 300 steps", "Because the dataset only has 300 valid samples", "5000 steps caused a memory overflow"])
add(G, GN, "What was the purpose of running the official demo.py at all, given the raw-JAX reimplementation already existed?",
    "To cross-validate that the raw-JAX reimplementation's convergence behaviour is consistent with the original, catching potential bugs in the from-scratch rewrite",
    ["There was no purpose; it was run by accident", "To replace the raw-JAX version entirely, which was then deleted", "Because raw-JAX cannot compute gradients"])
add(G, GN, "The comparison between the two runs (official demo vs raw-JAX) showed:",
    "Both converge to a similar order-of-magnitude test loss within a few hundred steps, supporting that the raw-JAX rewrite has no logic bugs",
    ["The two runs produced completely contradictory, unrelated results", "The official demo failed to run at all", "The raw-JAX version diverged to infinity"])
add(G, GN, "eqnn_force_field_data/ is located under which path in this project?",
    "Source_Code/qml-force-fields/pennylane-qml/demonstrations_v2/tutorial_eqnn_force_field/",
    ["Literature_Review/papers/", "Reference Drawio Latex/", "Tự học /QML_Force_Fields/"])
add(G, GN, "Is the environment fix (h5py upgrade) documented anywhere in the project for future reproducibility?",
    "Yes, in Source_Code/practical_runs.md section 2.1",
    ["No, it was fixed silently with no record", "Only in a private note not saved to any file", "It is documented in the MCQ answer key only"])

# ============ GROUP 26 (part B, 14) siVQLM practical -- raw-JAX reimplementation, real results ============
add(G, GN, "The raw-JAX reimplementation (no PennyLane) is saved at:",
    "Source_Code/prototypes/raw_jax_sivqlm.py",
    ["It was not saved anywhere, only run interactively", "Source_Code/schnetpack/raw_jax.py", "Reference Drawio Latex/raw_jax_sivqlm.py"])
add(G, GN, "Why was a raw-JAX reimplementation written at all, once pennylane was working?",
    "It was already written as a fallback before the pennylane fix succeeded, and is pedagogically valuable since it makes every gate an explicit matrix (useful for teaching), including the ring-topology 'odd' layer the block diagram could not show",
    ["Because JAX is faster than PennyLane in every possible case, with no exceptions", "Because PennyLane cannot compute gradients", "Because the official demo.py contains a bug that had to be fixed"])
add(G, GN, "In the raw-JAX reimplementation, each gate is represented as:",
    "An explicit 16x16 unitary matrix (since the full system is 4 qubits, dimension 2 to the power 4 = 16), built via np.kron/jnp.kron",
    ["A PennyLane QNode, same as the original", "A random number with no matrix structure", "A classical neural network layer"])
add(G, GN, "Unlike Sơ đồ 3 (the quantikz block diagram), the raw-JAX script implements:",
    "The full 'odd' trainable layer including the (3,0) ring-topology wraparound pair, via an explicit permutation/kron construction",
    ["Fewer gates than the diagram, a simplified version", "Only the 'even' layer, identical in scope to the diagram", "A completely different, unrelated circuit architecture"])
add(G, GN, "In the raw-JAX run, the train/test split used was:",
    "80\%/20\% with numpy seed=42",
    ["50/50 with no fixed seed", "100\% train, no test set held out", "A fixed 10-sample test set only"])
add(G, GN, "The raw-JAX run used batch_size and number of training steps of:",
    "batch_size=128, 400 steps",
    ["batch_size=256, 5000 steps (identical to the official demo defaults)", "batch_size=1, 10 steps", "batch_size=10, matching SchNetPack's real batch_size"])
add(G, GN, "The optimizer and learning rate used in the raw-JAX run were:",
    "Adam, lr=1e-2 (via jax.example_libraries.optimizers.adam)",
    ["AdamW, lr=1e-3 (identical to the real SchNetPack config)", "Plain SGD, lr=1.0", "No optimizer; parameters were fixed at initialization"])
add(G, GN, "After 400 steps, the raw-JAX run's train/test loss reached approximately:",
    "train=0.00188, test=0.00125",
    ["train=0.4, test=0.4, no improvement", "train=0, test=0, exactly zero", "It diverged to NaN"])
add(G, GN, "The raw-JAX run's final test MAE in the model's native scaled units ([-1,1]) was:",
    "approximately 0.031525",
    ["approximately 3.15 (far outside the valid output range)", "exactly 1.0, the maximum possible error", "approximately 0.99999, essentially random"])
add(G, GN, "Converting that scaled MAE back to physical units (Hartree) using the same MinMaxScaler.scale_, the real result was:",
    "approximately 0.00026487 Hartree",
    ["approximately 76.3 Hartree (the full energy scale, not the error)", "exactly 0 Hartree, a perfect fit", "approximately 1000 Hartree"])
add(G, GN, "Converting that MAE to kcal/mol (1 Hartree = 627.5 kcal/mol), the real result is approximately:",
    "0.166 kcal/mol",
    ["166 kcal/mol", "1.66 x 10 to the power 6 kcal/mol", "0.00166 kcal/mol"])
add(G, GN, "Is 0.166 kcal/mol within the 'chemical accuracy' threshold (<1 kcal/mol) discussed in Section 1.2 of the self-study document?",
    "Yes, comfortably within it",
    ["No, it is about 6x too large", "Chemical accuracy does not apply to force-field energies, only to reaction barriers", "The units cannot be compared at all"])
add(G, GN, "The total real wall-clock time for the 400-step raw-JAX training run was approximately:",
    "19.7 seconds on CPU",
    ["19.7 hours, requiring an overnight run", "19.7 minutes on a quantum computer", "0.0197 seconds, i.e. instantaneous"])
add(G, GN, "What does the raw-JAX run's speed (under 20 seconds, CPU-only, no real quantum hardware) illustrate about siVQLM at this scale?",
    "At 4 qubits, exact statevector simulation is cheap enough that no quantum hardware or GPU is needed at all for this scale of problem",
    ["That siVQLM already requires a supercomputer even at 4 qubits", "That the demo secretly used a real IBM quantum computer", "That JAX cannot run on CPUs, only GPUs"])
