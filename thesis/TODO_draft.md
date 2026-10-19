# Draft to-do list (first full draft 2026-10-16, revised 2026-10-17)

Revision 2026-10-17: the thesis is written as a standalone report. The figures in
`thesis/figures/` (teaser, detailed pipeline, thread model, simulation scenes, hardware
setup, test-object family, and the photos in `figures/photos/`) are the project's own
publication figures; the schematic `pipeline.tikz` was replaced by `mainpipeline.pdf`.

Revision 2026-10-18: the thesis no longer uses human-in-the-loop data. The method is
now "simulated data only + zero-shot transfer" (calibrated camera, metric point cloud,
visual DR, shared Cartesian action path; Sec. 3.4.4 "Zero-Shot Sim-to-Real Transfer").
Negative-result narratives were removed or recast (end-to-end RL subsection, libfranka-gain
teacher, pickup engagement 0 %, online-flow "no rollout", pretraining latent drift).
The former ablation (e) "simulated data only" is now the full method (e); the old (f) is gone.

### Results invalidated by the 2026-10-18 revision (previous runs used the real-world replay data)

| Location | What is needed |
| --- | --- |
| Ch. 4, Table 4.3 (a)–(d) | retrain single-cycle, ResNet, LSTM-regression, Transformer-regression students on the simulated-only ten-cycle M24 dataset; ten trials each |
| Ch. 4, Sec. 4.3 pose probe | rerun the probe on the encoders of the simulated-only students (e) and (b) |
| Ch. 4, Table 4.4 ResNet row | same as (b) above |
| Ch. 5, Table 5.1 | zero-shot hardware trials of (e), (a), (b) on M24. Note: the earlier zero-shot run of the simulated-only student reached only 2.1 ± 1.4 cycles (−10.05 ± 4.08°); the open P2 items below are what is expected to change that |
| Ch. 5, Table 5.2 | twelve-object zero-shot evaluation (M24/M30/M36 × four profiles) |
| Ch. 5, Sec. 5.5 | long-horizon stress trials with the zero-shot student |
| Ch. 3, Sec. 3.4.4 | fit sim camera randomization to measured D415 statistics (depth failures, exposure, blur, latency; forgeUltra `todo.md` P2); confirm which depth-noise model the retained DP3 pretraining used |
| Ch. 5, Sec. 5.2 | document deployment settings of the zero-shot trials |
| Abstract, Ch. 1 contributions, Ch. 6 Q1–Q4, Ch. 7 | fill in the hardware sentence / update interpretations once the above exist |
| Figures | `SimThreadTeaser.pdf` (Fig. 1.1) and `mainpipeline.pdf` (Fig. 3.1) are publication figures that may still draw the real-world replay / human-correction branch; edit them. The hardware photos in Fig. 5.2 were taken during the earlier trials; retake or confirm |

Every `\tbd` in the text and every `% TODO(...)` comment is listed here. Nothing in
this list was invented in the draft; where a number was unavailable the cell reads
`TBD`.

## 1. Missing results (`\tbd` placeholders, `% TODO(results)`)

| Location | What is missing | Run / artifact needed |
| --- | --- | --- |
| Ch. 3, Sec. 3.5.3 "Action chunking and execution" | student inference latency (image encoding + 16 Euler steps) | time `evaluate_flow.py` per policy tick on the deployment GPU; also per `N` for Table 4.6 |
| Ch. 4, Table 4.1 (teacher results) | final-epoch single-turn success and curriculum level of the retained FR3 M24 teacher and of the M24/M30/M36 multi-size teacher; hybrid-rollout count of the multi-size teacher | TensorBoard of the FR3 threading run promoted on 2026-09-10 (`last_ForgeTg2_ep_200_rew_17628.744.pth`) and of the `multi_nut_threading_z_randomized.yaml` run (`checkpoints/franka_threading_v2/multi_nut_z20mm`) |
| Ch. 4, Table 4.5 (vision encoders) | closed-loop ten-trial results for the Adapt3R-style, two-branch, and depth-only encoders | train `offline_flow_matching_adapt3r_agent.yaml`, `two_channel_rgbd_encoder.yaml`, `depth_aux.yaml` on the ten-cycle M24 dataset (`sequential-threading-dual-supervision-20260910-181107-771583`) with the DP3 recipe; `play_distillation --num_episodes 10` |
| Ch. 4, Table 4.6 (sweeps) | action horizon H ∈ {1,4,16}, Euler steps N ∈ {1,4,8,32}, ensemble decay ∈ {0,0.8}, `--hand-velocity-observation omitted`, privileged 3-D/6-D on the ten-cycle task | offline flow trainer/evaluator options; ten trials each |
| Ch. 4, Table 4.7 (robustness) | per-size simulation results M24/M30/M36; `--enable-domain-randomization` at evaluation; force observations (fingertip force, joint torque) in teacher and student | multi-size student from `collect_multinut_m24_dataset` extended to all sizes; force channels are implemented (`docs/distillation_observation_action_reference.md`) but not concatenated into any trained contract |
| Ch. 4, Sec. 4.5, Table 4.8 | online DAgger + flow matching result | `train_distillation --distillation-task online_dagger_flow_matching --training-environment cyclic_threading --student-observation nut_pose_6d`; no successful rollout exists |
| Ch. 5, Sec. 5.1 | physical controller gains, target filtering, hand command rate used in the hardware trials | libfranka tooling on `franka-chi` (`2e3a9eb`); the hardware trial configuration is not in the repository |
| Ch. 5, Sec. 5.5 | cycles-to-failure per nut size and profile in the long-horizon stress trials | the trial notes state only "15–22 cycles depending on nut size, geometry, and test conditions" |

## 2. Missing citations (keys cited in the text but absent from `library.bib`)

Do not guess metadata; add the entries to `library.bib` (then rerun the bib build) or
drop the claim.

| Key | Claim it supports |
| --- | --- |
| `Schulman2017` | PPO (clipped surrogate objective), Sec. 2.1.1 |
| `Pinto2017` | asymmetric actor–critic, Sec. 2.1.1 |
| `Hochreiter1997` | LSTM, Sec. 2.1.1 |
| `He2016` | ResNet-18, Sec. 2.1.4 |
| `Qi2017` | PointNet, Sec. 2.1.4 |
| `Tobin2017` | domain randomization, Sec. 2.1.4 and 2.2.3 |
| `Wilcox2025` | Adapt3R (CoRL 2025, PMLR 305), Sec. 2.1.4, 2.2.3, 3.5.3 |
| `Ze2024` exists; `Zhao2023` | ACT action chunking (RSS 2023), Sec. 2.2.4, 3.5.5 |
| `Siciliano2016` | Springer Handbook of Robotics, Sec. 2.2.1 |
| `Hsieh2026` | DexScrew (ICRA 2026, arXiv:2512.02011), Sec. 1.1, 2.2.1 |
| `Lum2026` | Play2Perfect (arXiv:2606.26428), Sec. 1.1, 2.2.1 |
| `Kirkpatrick2017` | catastrophic forgetting (PNAS 2017), Sec. 2.2.2 |
| `Lee2022` | adversarial skill chaining (CoRL 2021, PMLR 164), Sec. 2.2.2 |
| `Jiang2025transic` | TRANSIC (CoRL 2024, PMLR 270), Sec. 2.2.3 (note: `Jiang2025` in the library is a different paper) |
| `Chen2020` | Learning by Cheating (CoRL 2019, PMLR 100), Sec. 2.2.4 |
| `Wang2025` | UniGraspTransformer (CVPR 2025), Sec. 2.2.4 |

Look the metadata up on the publisher pages before adding the entries.

### Bibliography handling to confirm

- `literature.bib` is generated by `thesis/tools/build_literature_bib.py` from the
  cited keys (copy of the script is reproduced at the end of this file). Entries are
  copied unchanged from `library.bib`; `Mittal2023`/`Oertel2026` would come from
  `expose/source/library.bib` if cited (currently not cited).
- Three library keys are duplicated in `library.bib` (`Tang2023`, `Tang2024`,
  `Pitz2024`, `Kedia2026`). The draft cites the second occurrences under renamed keys
  `Tang2023industreal` (IndustReal) and `Tang2024screwdriving` (Tang & Jia 2024); the
  first occurrences keep their keys. Please deduplicate the library.
- `main.tex` nulls the `note`, `abstract`, and `annote` fields at the biber level
  (`\DeclareSourcemap`), because the library's reading notes contain raw HTML that
  breaks the generated `.bbl`. The `.bib` files are unchanged.
- The Unicode `π` in the `Black2026` title is mapped with `\DeclareUnicodeCharacter`.

## 3. Figures (`% TODO(figure)`)

| Location | Figure |
| --- | --- |
| Ch. 1, Fig. 1.1 | `SimThreadTeaser.pdf` is included with the same trim as in its source layout; check the margins visually |
| Ch. 3, Fig. 3.1 | `mainpipeline.pdf` labels the fused condition "c_t (256D)" and the visual feature "v_t (64D)"; the caption follows the code (64 + 128 projected to 256) |
| Ch. 5 | `figures/photos/`: `real_approach/grasp/rotate/goal/release.png` are side views of one cycle, `dial_*.png` the top-down scale views, `real_rgb/depth.png` the student's real observation, `sim_rgbd_strip.png` the simulated RGB/depth strip; all were cut from the project's own teaser and pipeline figures and their captions were checked against the images |
| TikZ figures | `student.tikz`, `datacollection.tikz`, `ladder.tikz` are schematic drafts; check them visually |

## 4. Statements to verify (`% TODO(unsure)`)

- Title (German and English) and submission date on the title page (`main.tex`); the
  draft uses the project's working title and 15 Nov 2026.
- Acknowledgments: attribution of jointly developed components (hybrid teacher,
  distillation stack, hardware experiments were largely developed/run by the advisor's
  commits).
- Isaac Lab version: the experiment notes say 2.2.1, the repository README v2.3.2 (Ch. 3, Sec. 3.2.1).
- Phase encoding: an earlier method description lists a one-hot over all six phases of
  eq. (1); the code uses a three-way one-hot (policy / release waypoints / return). Text
  follows the code (Sec. 3.5.3). `mainpipeline.pdf` labels a 256-D state feature next to
  the 64-D visual feature; the code projects the 64+128 concatenation to a 256-D condition.
- Proprioception standardization: the offline flow trainer appears not to standardize
  the 29-D input (only the auxiliary nut position is standardized). Sec. 3.5.3.
- Camera calibration used for hardware trials: the repository artifact is "measured"
  (27.46 mm / 3.50° fit RMSE), not deployment-validated (Sec. 5.1).
- Teacher actor width: the observation reference lists 39-D including two fingertip
  force channels, but the retained task YAML disables `fingertip_force` for the actor
  (Appendix Table A.1).
- Ch. 4, Table 4.1: the 83.6 % / 90.0 % threading-expert success is from the Tiangong 2
  line (`todo.md`, 2026-08-23); no FR3 success rate is recorded in the docs.
- Ch. 5, Sec. 5.1: hand control interface ("serial interface") and 1 kHz libfranka rate
  are stated from general knowledge of the hardware, not from repository docs.
- Ch. 6: the axial-coverage argument for Q1 and the orientation argument for Q2 are
  mechanistic interpretations that the retrained ablations (a), (b) must confirm; the
  claim that random point sampling acts as augmentation is a hypothesis.
- The experiment notes report 512 environments for the retained FR3 teacher; the README
  quickstart uses 384 for pickup. Text uses 512.

## 5. Open questions for Carsten

1. Should the thesis keep the Tiangong 2 / KUKA history as design-decision findings only
   (current draft), or add a short "platform history" subsection?
2. Should the online DAgger + flow matching experiment be run for the thesis? The draft
   now mentions it only as implemented and pending (Ch. 4 TODO, Ch. 7 future work).
3. Do you want the page count raised toward 60 body pages (currently ≈49 + appendix)?
   Natural extensions with available material: a subsection on the pickup expert's
   reward and its handoff failure modes (exp_09/exp_10 logs), a figure of a recorded
   student trajectory (joint/TCP/nut-turn plots exist in the evaluation artifacts), and
   the multi-size threading V2 teacher recipe.
4. The `expose/` title is "SimThreadReal …"; the draft uses a different working title. Confirm.

## Appendix: bibliography build script

Run from the repository root after editing citations:

```
python3 thesis/tools/build_literature_bib.py
```

(The script collects `\cite{...}` keys from `thesis/source/*.tex`, copies the matching
entries verbatim from `thesis/source/library.bib` (first occurrence), falls back to
`expose/source/library.bib`, applies the two key renames above, and prints the missing
keys.)
