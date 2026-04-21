import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

# Hydrogen energy levels E_n = -13.6 eV / n^2
# Lyman: n -> 1 (UV), Balmer: n -> 2 (visible), Paschen: n -> 3 (IR)
E = lambda n: -13.6 / n**2

fig, ax = plt.subplots(figsize=(8, 6.2))

n_max = 6
x_left = 0.15
x_right = 0.55

# Levels. For n >= 4 the spacing is tiny, so only label n=1..4 with energy on the right.
# n=5, 6 are shown but unlabeled to avoid overlap.
for n in range(1, n_max + 1):
    ax.hlines(E(n), x_left, x_right, color='#333333', lw=2)
    if n <= 4:
        ax.text(x_left - 0.02, E(n), f'$n={n}$', ha='right', va='center', fontsize=11)
        ax.text(x_right + 0.02, E(n), f'${E(n):.2f}$ eV', ha='left', va='center',
                fontsize=9, color='#555555')
# Bracket the n>=5 region with one label
ax.text(x_left - 0.02, E(5) + 0.15, r'$n\geq 5$', ha='right', va='center', fontsize=10,
        color='#555555')
ax.text(x_right + 0.02, E(5) + 0.15, r'$\to 0$ eV', ha='left', va='center', fontsize=9,
        color='#555555')

# Ionization line
ax.hlines(0, x_left, x_right, color='#888888', lw=1, ls='--')
ax.text(x_right + 0.02, 0, 'ionization (0 eV)', ha='left', va='center',
        fontsize=9, color='#888888')

# Transition arrows
def draw_series(m, color, label, x_offset):
    for n in range(m + 1, n_max + 1):
        x_arrow = x_right + x_offset + 0.035 * (n - m - 1)
        ax.annotate('', xy=(x_arrow, E(m)), xytext=(x_arrow, E(n)),
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.6, alpha=0.85))
    # Group label
    ax.text(x_right + x_offset + 0.035 * (n_max - m - 2) / 2, E(m) - 1.8,
            label, color=color, fontsize=11, fontweight='bold', ha='center')

draw_series(1, '#7B1FA2', 'Lyman\n(UV)', 0.25)
draw_series(2, '#1565C0', 'Balmer\n(visible)', 0.55)
draw_series(3, '#C62828', 'Paschen\n(IR)', 0.85)

# Title and axes
ax.set_ylabel(r'Energy  $E_n = -\dfrac{13.6\,\mathrm{eV}}{n^2}$', fontsize=12)
ax.set_title('Hydrogen Grotrian-style diagram: spectral series',
             fontsize=13, pad=10)
ax.set_xlim(-0.02, 1.55)
ax.set_ylim(-15, 1)
ax.set_xticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.tick_params(axis='y', labelsize=10)

plt.tight_layout()
out = '/Users/yuan/grad-exam-physics-chem/物理化学7/figures/hydrogen_spectrum.png'
plt.savefig(out, dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print('Saved:', out)
