import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

# LCAO of two 1s orbitals along internuclear axis
# Atoms at x = -R/2 and x = +R/2
R = 2.0  # internuclear distance in units of a0
x = np.linspace(-5, 5, 1000)

# 1s atomic orbital in atomic units: psi_1s(r) = (1/sqrt(pi)) exp(-r)
def psi_1s(x, x0):
    r = np.abs(x - x0)
    return (1 / np.sqrt(np.pi)) * np.exp(-r)

psiA = psi_1s(x, -R / 2)
psiB = psi_1s(x, +R / 2)

# Approximate overlap (at R=2 for 1s-1s, S ~ 0.59 analytically)
S = 0.59
N_plus = 1 / np.sqrt(2 * (1 + S))
N_minus = 1 / np.sqrt(2 * (1 - S))

psi_plus = N_plus * (psiA + psiB)
psi_minus = N_minus * (psiA - psiB)

fig, axes = plt.subplots(2, 2, figsize=(10, 6.5), sharex=True)

# Top row: wavefunctions
ax = axes[0, 0]
ax.axhline(0, color='#AAAAAA', lw=0.7)
ax.plot(x, psiA, '--', color='#888888', lw=1.3, label=r'$\psi_A$')
ax.plot(x, psiB, ':', color='#888888', lw=1.3, label=r'$\psi_B$')
ax.plot(x, psi_plus, color='#1565C0', lw=2.4, label=r'$\psi_+ = N_+(\psi_A+\psi_B)$')
ax.fill_between(x, 0, psi_plus, color='#1565C0', alpha=0.15)
ax.axvline(-R / 2, color='#C62828', lw=0.8, ls=':')
ax.axvline(+R / 2, color='#C62828', lw=0.8, ls=':')
ax.set_ylabel(r'$\psi$', fontsize=12)
ax.set_title('Bonding (σ)', fontsize=12, color='#1565C0', fontweight='bold')
ax.legend(loc='upper right', fontsize=9)
ax.tick_params(labelsize=10)
ax.set_ylim(-0.6, 0.8)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

ax = axes[0, 1]
ax.axhline(0, color='#AAAAAA', lw=0.7)
ax.plot(x, psiA, '--', color='#888888', lw=1.3, label=r'$\psi_A$')
ax.plot(x, -psiB, ':', color='#888888', lw=1.3, label=r'$-\psi_B$')
ax.plot(x, psi_minus, color='#C62828', lw=2.4, label=r'$\psi_- = N_-(\psi_A-\psi_B)$')
ax.fill_between(x, 0, psi_minus, color='#C62828', alpha=0.15)
ax.axvline(-R / 2, color='#C62828', lw=0.8, ls=':')
ax.axvline(+R / 2, color='#C62828', lw=0.8, ls=':')
ax.set_title('Antibonding (σ*)', fontsize=12, color='#C62828', fontweight='bold')
ax.legend(loc='upper right', fontsize=9)
ax.tick_params(labelsize=10)
ax.set_ylim(-0.6, 0.8)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

# Bottom row: densities
ax = axes[1, 0]
ax.axhline(0, color='#AAAAAA', lw=0.7)
ax.plot(x, psiA**2 + psiB**2, '--', color='#888888', lw=1.3,
        label=r'$|\psi_A|^2+|\psi_B|^2$ (no overlap)')
ax.plot(x, psi_plus**2, color='#1565C0', lw=2.4, label=r'$|\psi_+|^2$')
ax.fill_between(x, 0, psi_plus**2, color='#1565C0', alpha=0.2)
ax.axvline(-R / 2, color='#C62828', lw=0.8, ls=':')
ax.axvline(+R / 2, color='#C62828', lw=0.8, ls=':')
ax.set_xlabel(r'$x$ (internuclear axis)', fontsize=12)
ax.set_ylabel(r'density $|\psi|^2$', fontsize=12)
ax.annotate('electron density piled up\nbetween nuclei',
            xy=(0, psi_plus[len(x)//2]**2), xytext=(-4.5, 0.35),
            fontsize=10, color='#1565C0',
            arrowprops=dict(arrowstyle='->', color='#1565C0', lw=1.2,
                            connectionstyle='arc3,rad=-0.2'))
ax.legend(loc='upper right', fontsize=9)
ax.tick_params(labelsize=10)
ax.set_ylim(0, 0.55)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

ax = axes[1, 1]
ax.axhline(0, color='#AAAAAA', lw=0.7)
ax.plot(x, psiA**2 + psiB**2, '--', color='#888888', lw=1.3,
        label=r'$|\psi_A|^2+|\psi_B|^2$ (no overlap)')
ax.plot(x, psi_minus**2, color='#C62828', lw=2.4, label=r'$|\psi_-|^2$')
ax.fill_between(x, 0, psi_minus**2, color='#C62828', alpha=0.2)
ax.axvline(-R / 2, color='#C62828', lw=0.8, ls=':')
ax.axvline(+R / 2, color='#C62828', lw=0.8, ls=':')
ax.set_xlabel(r'$x$ (internuclear axis)', fontsize=12)
# Nodal plane
ax.axvline(0, color='#C62828', lw=1.5, alpha=0.5)
ax.text(0, 0.42, 'nodal\nplane', ha='center', color='#C62828', fontsize=10)
ax.legend(loc='upper right', fontsize=9)
ax.tick_params(labelsize=10)
ax.set_ylim(0, 0.55)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

plt.suptitle(r'LCAO $\mathrm{H}_2$:  $\psi_\pm = N_\pm (\psi_A \pm \psi_B)$',
             fontsize=13, y=0.995)
plt.tight_layout()
out = '/Users/yuan/grad-exam-physics-chem/物理化学7/figures/mo_bonding.png'
plt.savefig(out, dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print('Saved:', out)
