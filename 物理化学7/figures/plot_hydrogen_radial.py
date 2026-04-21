import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

# Radial wavefunctions in units of Bohr radius a0 = 1
# R_10 = 2 * exp(-r)
# R_20 = (1/sqrt(2)) * (1 - r/2) * exp(-r/2)
# R_21 = (1/(2*sqrt(6))) * r * exp(-r/2)
# R_30 = (2/(81*sqrt(3))) * (27 - 18 r + 2 r^2) * exp(-r/3)
# R_31 = (8/(27*sqrt(6))) * (1 - r/6) * r * exp(-r/3)
# (Using standard hydrogenic form with Z=1, a0=1; normalization yields int |R|^2 r^2 dr = 1)
r = np.linspace(0, 25, 2000)

def R10(r): return 2 * np.exp(-r)
def R20(r): return (1 / np.sqrt(2)) * (1 - r / 2) * np.exp(-r / 2)
def R21(r): return (1 / (2 * np.sqrt(6))) * r * np.exp(-r / 2)
def R30(r): return (2 / (81 * np.sqrt(3))) * (27 - 18 * r + 2 * r**2) * np.exp(-r / 3)

# Radial probability density P(r) = |R|^2 r^2
funcs = [(R10, r'$1s$  ($n=1,l=0$)', '#1565C0'),
         (R20, r'$2s$  ($n=2,l=0$)', '#2E7D32'),
         (R21, r'$2p$  ($n=2,l=1$)', '#E67E22'),
         (R30, r'$3s$  ($n=3,l=0$)', '#C62828')]

fig, ax = plt.subplots(figsize=(8, 5))
# Stagger annotation offsets so nearby peaks don't collide
offsets = {r'$1s$  ($n=1,l=0$)': (0.6, 0.03),
           r'$2s$  ($n=2,l=0$)': (0.8, 0.06),
           r'$2p$  ($n=2,l=1$)': (-2.3, 0.05),
           r'$3s$  ($n=3,l=0$)': (0.8, 0.03)}
for R, label, color in funcs:
    P = (R(r)**2) * r**2
    ax.plot(r, P, lw=2.2, label=label, color=color)
    # Mark peak
    i_max = np.argmax(P)
    ax.plot(r[i_max], P[i_max], 'o', color=color, ms=6)
    dx, dy = offsets[label]
    ax.annotate(rf'$r^*={r[i_max]:.2f}\,a_0$',
                xy=(r[i_max], P[i_max]),
                xytext=(r[i_max] + dx, P[i_max] + dy),
                fontsize=9, color=color)

# Reference: a_0 = 1 line for 1s peak
ax.axvline(1, color='#888888', ls=':', lw=0.8)
ax.text(1.1, 0.56, r'$a_0$', fontsize=10, color='#555555')

ax.set_xlabel(r'$r / a_0$', fontsize=13)
ax.set_ylabel(r'Radial probability  $|R_{nl}(r)|^2\, r^2$', fontsize=12)
ax.set_title(r'Hydrogen radial probability distribution', fontsize=13, pad=8)
ax.set_xlim(0, 20)
ax.set_ylim(0, 0.62)
ax.legend(loc='upper right', fontsize=10, framealpha=0.95)
ax.tick_params(labelsize=11)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
out = '/Users/yuan/grad-exam-physics-chem/物理化学7/figures/hydrogen_radial.png'
plt.savefig(out, dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print('Saved:', out)
