import numpy as np

hbar = 1.0546e-34
c = 2.998e8
k_B = 1.381e-23
hbar_c = hbar * c

A = np.pi**2 * hbar_c / 720.0
theta_tc = 1.17
T = 300.0
C = k_B * T * abs(theta_tc) / 2.0

L_cross = A / C
L_thresh = 2.0 * A / C

def rho_total(L):
    return -A/L**4 + C/L**3

def Trr_total(L):
    return -3*A/L**4 + 2*C/L**3

def ratio_total(L):
    return Trr_total(L) / rho_total(L)

print(f"L_crossover = {L_cross*1e9:.1f} nm")
print(f"L_threshold = {L_thresh*1e9:.1f} nm")
print(f"Sweet spot: {L_cross*1e9:.0f} - {L_thresh*1e9:.0f} nm")

for L_nm in [179, 200, 250, 300, 358]:
    L = L_nm * 1e-9
    r = rho_total(L)
    t = Trr_total(L)
    ratio = t/r if abs(r) > 1e-100 else float('inf')
    print(f"L={L_nm} nm: rho={r:.4e}, Trr={t:.4e}, ratio={ratio:.4f}")
