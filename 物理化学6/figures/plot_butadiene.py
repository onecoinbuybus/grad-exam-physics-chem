import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

fig, ax = plt.subplots(figsize=(5, 7))

# Energy levels: n=1 -> 1, n=2 -> 4, n=3 -> 9, n=4 -> 16
levels = {1: 1, 2: 4, 3: 9, 4: 16}
x_left = 0.15
x_right = 0.85
line_lw = 3

for n, E in levels.items():
    ax.plot([x_left, x_right], [E, E], 'k-', lw=line_lw, solid_capstyle='butt')
    # n label on the left
    ax.text(x_left - 0.03, E, f'$n={n}$', ha='right', va='center', fontsize=13)
    # Energy label on the right
    if n == 1:
        label = r'$1E_1$'
    else:
        label = rf'${n**2}E_1$'
    ax.text(x_right + 0.03, E, label, ha='left', va='center', fontsize=13)

# Electrons: n=1 has 2 electrons, n=2 has 2 electrons
arrow_kwargs = dict(head_width=0.015, head_length=0.3, lw=1.5)
# n=1: up arrow and down arrow
ax.annotate('', xy=(0.42, 1.9), xytext=(0.42, 1.0),
            arrowprops=dict(arrowstyle='->', color='steelblue', lw=2))
ax.annotate('', xy=(0.58, 1.0), xytext=(0.58, 1.9),
            arrowprops=dict(arrowstyle='->', color='firebrick', lw=2))

# n=2: up arrow and down arrow
ax.annotate('', xy=(0.42, 4.9), xytext=(0.42, 4.0),
            arrowprops=dict(arrowstyle='->', color='steelblue', lw=2))
ax.annotate('', xy=(0.58, 4.0), xytext=(0.58, 4.9),
            arrowprops=dict(arrowstyle='->', color='firebrick', lw=2))

# HOMO label - below the n=2 level to avoid overlap
ax.text(x_right + 0.03, 4 - 0.8, 'HOMO', ha='left', va='center',
        fontsize=12, fontweight='bold', color='#2196F3')

# LUMO label - above the n=3 level to avoid overlap
ax.text(x_right + 0.03, 9 + 0.8, 'LUMO', ha='left', va='center',
        fontsize=12, fontweight='bold', color='#2196F3')

# Transition arrow (dashed, orange) from HOMO to LUMO
mid_x = 0.50
ax.annotate('', xy=(mid_x, 8.7), xytext=(mid_x, 4.3),
            arrowprops=dict(arrowstyle='->', color='#E67E22', lw=2.5,
                            linestyle='dashed'))
ax.text(mid_x + 0.08, 6.5, r'$\Delta E$', ha='left', va='bottom',
        fontsize=14, color='#E67E22', fontweight='bold')
ax.text(mid_x + 0.08, 5.8, r'$= h\nu$', ha='left', va='top',
        fontsize=13, color='#E67E22')

# Axes
ax.set_ylabel(r'Energy / $E_1$', fontsize=14)
ax.set_xlim(-0.05, 1.25)
ax.set_ylim(-0.5, 18)
ax.set_yticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
ax.set_xticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.tick_params(axis='y', labelsize=11)

ax.set_title(r'Butadiene (4 $\pi$ electrons)', fontsize=15, pad=12)

plt.tight_layout()
plt.savefig('/Users/yuan/grad-exam-physics-chem/物理化学6/figures/butadiene_levels.png',
            dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print("Done")
