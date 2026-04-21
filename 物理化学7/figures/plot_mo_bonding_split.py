import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

# LCAO of two 1s orbitals along internuclear axis
R = 2.0
x = np.linspace(-5, 5, 1000)

def psi_1s(x, x0):
    r = np.abs(x - x0)
    return (1 / np.sqrt(np.pi)) * np.exp(-r)

psiA = psi_1s(x, -R / 2)
psiB = psi_1s(x, +R / 2)

S = 0.59
N_plus = 1 / np.sqrt(2 * (1 + S))
N_minus = 1 / np.sqrt(2 * (1 - S))

psi_plus = N_plus * (psiA + psiB)
psi_minus = N_minus * (psiA - psiB)


def make_panel(ax_top, ax_bot, psi, psi_sign, color, title, density_label,
               fill_alpha=0.2):
    # Top: wavefunction
    ax_top.axhline(0, color='#AAAAAA', lw=0.7)
    ax_top.plot(x, psiA, '--', color='#888888', lw=1.3, label=r'$\psi_A$')
    ax_top.plot(x, psi_sign * psiB, ':', color='#888888', lw=1.3,
                label=(r'$\psi_B$' if psi_sign > 0 else r'$-\psi_B$'))
    ax_top.plot(x, psi, color=color, lw=2.6, label=title)
    ax_top.fill_between(x, 0, psi, color=color, alpha=0.18)
    ax_top.axvline(-R / 2, color='#C62828', lw=0.8, ls=':')
    ax_top.axvline(+R / 2, color='#C62828', lw=0.8, ls=':')
    ax_top.set_ylabel(r'$\psi(x)$', fontsize=13)
    ax_top.set_ylim(-0.6, 0.8)
    ax_top.legend(loc='upper right', fontsize=10, framealpha=0.95)
    ax_top.tick_params(labelsize=10)
    ax_top.spines['top'].set_visible(False)
    ax_top.spines['right'].set_visible(False)

    # Bottom: density
    ax_bot.axhline(0, color='#AAAAAA', lw=0.7)
    ax_bot.plot(x, psiA**2 + psiB**2, '--', color='#888888', lw=1.4,
                label=r'$|\psi_A|^2+|\psi_B|^2$ (no overlap)')
    ax_bot.plot(x, psi**2, color=color, lw=2.6, label=density_label)
    ax_bot.fill_between(x, 0, psi**2, color=color, alpha=fill_alpha)
    ax_bot.axvline(-R / 2, color='#C62828', lw=0.8, ls=':')
    ax_bot.axvline(+R / 2, color='#C62828', lw=0.8, ls=':')
    ax_bot.set_xlabel(r'$x$ (internuclear axis)', fontsize=13)
    ax_bot.set_ylabel(r'density $|\psi|^2$', fontsize=13)
    ax_bot.set_ylim(0, 0.55)
    ax_bot.legend(loc='upper right', fontsize=10, framealpha=0.95)
    ax_bot.tick_params(labelsize=10)
    ax_bot.spines['top'].set_visible(False)
    ax_bot.spines['right'].set_visible(False)


# === Bonding only ===
fig, (ax_top, ax_bot) = plt.subplots(2, 1, figsize=(7.5, 6.2), sharex=True)
make_panel(ax_top, ax_bot, psi_plus, +1, '#1565C0',
           r'$\psi_+ = N_+(\psi_A+\psi_B)$',
           r'$|\psi_+|^2$')
ax_bot.annotate('electron density\npiled up between nuclei',
                xy=(0, psi_plus[len(x)//2]**2), xytext=(-4.5, 0.40),
                fontsize=11, color='#1565C0',
                arrowprops=dict(arrowstyle='->', color='#1565C0', lw=1.2,
                                connectionstyle='arc3,rad=-0.2'))
plt.suptitle(r'Bonding orbital  $\psi_+$  ($\sigma$)', fontsize=14,
             color='#1565C0', y=0.99, fontweight='bold')
plt.tight_layout()
out1 = '/Users/yuan/grad-exam-physics-chem/物理化学7/figures/mo_bonding_only.png'
plt.savefig(out1, dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print('Saved:', out1)


# === Antibonding only ===
fig, (ax_top, ax_bot) = plt.subplots(2, 1, figsize=(7.5, 6.2), sharex=True)
make_panel(ax_top, ax_bot, psi_minus, -1, '#C62828',
           r'$\psi_- = N_-(\psi_A-\psi_B)$',
           r'$|\psi_-|^2$')
# Nodal plane emphasis
ax_top.axvline(0, color='#C62828', lw=1.4, alpha=0.5)
ax_top.text(0, 0.7, 'node', ha='center', va='bottom', color='#C62828',
            fontsize=11, fontweight='bold')
ax_bot.axvline(0, color='#C62828', lw=1.4, alpha=0.5)
ax_bot.text(0, 0.46, 'nodal plane\n$|\\psi_-|^2 = 0$', ha='center',
            color='#C62828', fontsize=11, fontweight='bold')
plt.suptitle(r'Antibonding orbital  $\psi_-$  ($\sigma^*$)', fontsize=14,
             color='#C62828', y=0.99, fontweight='bold')
plt.tight_layout()
out2 = '/Users/yuan/grad-exam-physics-chem/物理化学7/figures/mo_antibonding_only.png'
plt.savefig(out2, dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print('Saved:', out2)
