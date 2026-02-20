# Core Combat Simulation Report

- Generated (UTC): `2026-02-20T05:24:18+00:00`
- Trials per simulation: **20000**
- Max rounds per encounter trial: **30**

## Assumptions
- round_seconds: `6`
- success_rule: `1d20 + modifiers > Difficulty Value`
- critical_success: `natural 20`
- critical_failure: `natural 1`

## Check Targets
| ID | Bonus | DV | Success Rate | Target Band | Status |
|---|---:|---:|---:|---|---|
| trained_vs_standard_dv | 6.0 | 15.0 | 55.0% | 55.0% - 75.0% | PASS |
| proficient_vs_hard_dv | 8.0 | 20.0 | 40.0% | 35.0% - 55.0% | PASS |
| expert_vs_very_hard_dv | 10.0 | 25.0 | 25.0% | 25.0% - 45.0% | PASS |

## Control Targets
| ID | Bonus | DV | Apply Rate | Target Band | Status |
|---|---:|---:|---:|---|---|
| repeatable_control_peer | 5.0 | 16.0 | 45.0% | 30.0% - 50.0% | PASS |
| hard_lockout_peer | 2.0 | 16.0 | 30.0% | 15.0% - 35.0% | PASS |

- `repeatable_control_peer`: Repeatable stun/immobilize should not be near-automatic against peers.
- `hard_lockout_peer`: Hard lockouts must stay rare unless setup/cost is high.

## Matchups
| ID | Style | Hit % | Crit % | DPR | Avg Dmg/Hit | Avg Rounds | P90 Rounds | Avg SP | Timeout % | Result |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| seq9_peer_melee | melee | 50.2% | 5.3% | 2.52 | 5.02 | 4.15 | 7.00 | 0.00 | 0.0% | PASS |
| seq9_peer_firearm | firearm | 75.4% | 5.2% | 2.65 | 3.51 | 3.67 | 6.00 | 0.00 | 0.0% | PASS |
| seq7_peer_melee | melee | 50.3% | 5.0% | 3.54 | 7.03 | 4.94 | 8.00 | 0.00 | 0.0% | PASS |
| seq7_peer_cast | cast | 55.6% | 5.0% | 3.93 | 7.06 | 4.48 | 7.00 | 4.48 | 0.0% | PASS |
| seq5_peer_melee | melee | 49.6% | 4.8% | 4.25 | 8.57 | 4.94 | 8.00 | 0.00 | 0.0% | PASS |
| seq5_firearm_vs_quick_dodge | firearm | 50.2% | 5.0% | 4.78 | 9.52 | 4.55 | 8.00 | 0.00 | 0.0% | PASS |
| seq5_vs_seq3_boss_melee | melee | 35.0% | 5.1% | 3.00 | 8.56 | 7.66 | 13.00 | 0.00 | 0.0% | PASS |
| seq5_vs_seq3_boss_cast | cast | 45.1% | 5.0% | 3.85 | 8.55 | 6.03 | 10.00 | 12.05 | 0.0% | PASS |

### Matchup Target Checks
| ID | Hit Target | Hit Status | Rounds Target | Rounds Status | SP Target | SP Status |
|---|---|---|---|---|---|---|
| seq9_peer_melee | 45.0% - 60.0% | PASS | 3.00 - 5.00 | PASS | - | N/A |
| seq9_peer_firearm | 70.0% - 90.0% | PASS | 2.00 - 4.00 | PASS | - | N/A |
| seq7_peer_melee | 45.0% - 60.0% | PASS | 3.00 - 5.00 | PASS | - | N/A |
| seq7_peer_cast | 45.0% - 65.0% | PASS | 3.00 - 5.00 | PASS | 3.00 - 8.00 | PASS |
| seq5_peer_melee | 45.0% - 60.0% | PASS | 3.00 - 5.00 | PASS | - | N/A |
| seq5_firearm_vs_quick_dodge | 45.0% - 65.0% | PASS | 3.00 - 5.00 | PASS | - | N/A |
| seq5_vs_seq3_boss_melee | 30.0% - 50.0% | PASS | 5.00 - 8.00 | PASS | - | N/A |
| seq5_vs_seq3_boss_cast | 30.0% - 50.0% | PASS | 5.00 - 9.00 | PASS | 8.00 - 20.00 | PASS |

## Firearm Gap Check
| Group | Melee Hit % | Firearm Hit % | Gap | Target Max | Status |
|---|---:|---:|---:|---:|---|
| seq9_peer | 50.2% | 75.4% | 25.2% | 30.0% | PASS |
| seq5_peer | 49.6% | 50.2% | 0.7% | 30.0% | PASS |

## Recommended Patch Set
| Priority | Knob | Recommendation | Rationale | Scope |
|---:|---|---|---|---|
| 1 | None | No automatic patch flags. Current simulation outputs are within configured targets. | No out-of-band metrics were detected. | global |

## Notes
- `Result=CHECK` means at least one configured target band was out of range.
- Timeout indicates trials where the defender was still standing after max rounds.
