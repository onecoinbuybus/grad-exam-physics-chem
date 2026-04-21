import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

B = 1.0  # rotational constant (arbitrary units, B)
J_max = 5

# Two panels: (top) levels E_J = BJ(J+1), (bottom) absorption lines at 2B(J+1)
fig, (ax_levels, ax_spec) = plt.subplots(2, 1, figsize=(8.5, 5.5),
                                          gridspec_kw={'height_ratios': [2, 1]},
                                          sharex=False)

# === Levels ===
levels = [(J, B * J * (J + 1)) for J in range(J_max + 1)]
for J, E in levels:
    ax_levels.hlines(E, 0.1, 0.9, color='#1565C0', lw=2.5)
    ax_levels.text(0.05, E, f'$J={J}$', ha='right', va='center', fontsize=11,
                   color='#1565C0')
    ax_levels.text(0.95, E, rf'$E_{J}={J}({J+1})B={J*(J+1)}B$',
                   ha='left', va='center', fontsize=10)

# Transition arrows J -> J+1
for J in range(J_max):
    x_arrow = 0.5 + 0.04 * J
    E_low = B * J * (J + 1)
    E_high = B * (J + 1) * (J + 2)
    ax_levels.annotate('', xy=(x_arrow, E_high), xytext=(x_arrow, E_low),
                       arrowprops=dict(arrowstyle='->', color='#C62828', lw=1.4))

ax_levels.set_ylabel(r'$E_J / B$', fontsize=12)
ax_levels.set_title(r'Rotational levels $E_J = BJ(J+1)$ and $\Delta J = +1$ transitions',
                    fontsize=12, pad=8)
ax_levels.set_xlim(-0.2, 2.2)
ax_levels.set_ylim(-2, B * (J_max + 1) * (J_max + 2) + 3)
ax_levels.set_xticks([])
ax_levels.spines['top'].set_visible(False)
ax_levels.spines['right'].set_visible(False)
ax_levels.spines['bottom'].set_visible(False)
ax_levels.tick_params(axis='y', labelsize=10)

# === Absorption spectrum ===
for J in range(J_max):
    freq = 2 * B * (J + 1)  # transition J -> J+1
    ax_spec.vlines(freq, 0, 1, color='#C62828', lw=3)
    ax_spec.text(freq, 1.05, rf'${2*(J+1)}B$', ha='center', va='bottom',
                 fontsize=10, color='#C62828')
    ax_spec.text(freq, -0.15, f'$J={J}\\to{J+1}$', ha='center', va='top',
                 fontsize=9, color='#333333')

# Spacing annotation
ax_spec.annotate('', xy=(4 * B, 0.55), xytext=(2 * B, 0.55),
                 arrowprops=dict(arrowstyle='<->', color='#1565C0', lw=1.3))
ax_spec.text(3 * B, 0.65, r'spacing $=2B$', ha='center', va='bottom',
             fontsize=11, color='#1565C0', fontweight='bold')

ax_spec.set_xlabel(r'Absorption frequency  /  $B$', fontsize=12)
ax_spec.set_xlim(0, 2 * B * (J_max + 1) + 1)
ax_spec.set_ylim(-0.5, 1.6)
ax_spec.set_yticks([])
ax_spec.spines['top'].set_visible(False)
ax_spec.spines['right'].set_visible(False)
ax_spec.spines['left'].set_visible(False)
ax_spec.tick_params(labelsize=10)

plt.tight_layout()
out = '/Users/yuan/grad-exam-physics-chem/物理化学7/figures/rotational_spectrum.png'
plt.savefig(out, dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print('Saved:', out)
