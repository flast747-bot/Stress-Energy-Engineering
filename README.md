# Stress-Energy Engineering

## Achieving T_rr/ρ < 1 via Combined Quantum and Critical Casimir Effects

The quantum Casimir effect locks the stress-to-density ratio at T_rr/ρ = 3
due to tracelessness of the massless stress-energy tensor. This work proves
that combining the quantum and critical Casimir effects breaks this lock.

### Key Result

**At gap width 179-358 nm (T = 300K, θ = 1.17):**
- Ghosts are dead (ρ > 0)
- Lock is broken (T_rr/ρ < 1)
- ANEC satisfied above 238 nm
- Metric perturbation nearly isotropic (h_zz/h_tt ≈ 1)
- Residual reduced by 99.5%

### Mechanism

| Effect | Scaling | T_rr/ρ |
|--------|---------|--------|
| Quantum Casimir | L^-4 | 3 |
| Critical Casimir | L^-3 | 2 |
| Combined (sweet spot) | crossover | < 1 |

### Contents

- paper/ — Full LaTeX paper with all derivations
- solvers/ — Python verification code
- results/ — Numerical output

### Experimental Protocol

- Plates: Gold-coated, asymmetric wetting
- Fluid: Water + 3-methylpyridine (27.7 vol%)
- Temperature: T_c ± 100mK (~37.3°C)
- Gap: 250 nm
- Measurement: AFM force detection
