import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

# === Parameters (decoupled for visualization) ===
Re = 1.4       # equilibrium distance
De = 5.0       # Morse dissociation energy
a_morse = 1.5  # Morse width (controls well shape, fixed independently)
# Harmonic force constant matched to Morse at bottom: k = 2*De*a^2
k = 2 * De * a_morse**2  # = 22.5
# omega for energy levels (artificial unit system, NOT from k)
# Want ~7-8 harmonic levels below display max (~7)
omega = 0.85

R = np.linspace(0.4, 4.5, 3000)

# Potentials
V_harm = 0.5 * k * (R - Re)**2
V_morse = De * (1 - np.exp(-a_morse * (R - Re)))**2

# === Figure ===
fig, ax = plt.subplots(figsize=(7.5, 5.5))

# Clip harmonic for display
ymax = 7.5
V_harm_clip = np.where(V_harm <= ymax, V_harm, np.nan)

# Plot potentials
ax.plot(R, V_harm_clip, '--', color='#1565C0', lw=2.5,
        label=r'Harmonic $V^H = \frac{1}{2}k(R-R_e)^2$', zorder=5)
ax.plot(R, V_morse, '-', color='#C62828', lw=2.5,
        label=r'Morse $V^M = D_e[1-e^{-a(R-R_e)}]^2$', zorder=5)

# De line
ax.axhline(De, color='#555555', ls=':', lw=1.2, zorder=1)
ax.text(4.4, De + 0.12, r'$D_e$', ha='left', va='bottom', fontsize=14,
        color='#555555', fontweight='bold')


def find_crossings(R_arr, V_arr, E_val):
    crossings = []
    for i in range(len(R_arr) - 1):
        if (V_arr[i] - E_val) * (V_arr[i+1] - E_val) < 0:
            rc = R_arr[i] + (E_val - V_arr[i]) / (V_arr[i+1] - V_arr[i]) * (R_arr[i+1] - R_arr[i])
            crossings.append(rc)
    return crossings


# === Harmonic energy levels ===
harm_levels = []
for n in range(20):
    E = (n + 0.5) * omega
    if E > ymax - 0.3:
        break
    harm_levels.append((n, E))

for n, E in harm_levels:
    cr = find_crossings(R, V_harm, E)
    if len(cr) >= 2:
        ax.plot([cr[0], cr[-1]], [E, E], '-', color='#90CAF9', lw=1.4, zorder=4)

# === Morse energy levels ===
morse_levels = []
for n in range(50):
    E = (n + 0.5) * omega - (n + 0.5)**2 * omega**2 / (4 * De)
    # Check if next level would be lower (past dissociation)
    E_next = (n + 1.5) * omega - (n + 1.5)**2 * omega**2 / (4 * De)
    if E >= De or E < 0:
        break
    morse_levels.append((n, E))
    if E_next <= E:
        break

for n, E in morse_levels:
    cr = find_crossings(R, V_morse, E)
    if len(cr) >= 2:
        ax.plot([cr[0], cr[-1]], [E, E], '-', color='#EF9A9A', lw=1.4, zorder=4)

# === Annotation: harmonic equal spacing ===
# Between n=2 and n=3 (middle of the well, clearly visible)
if len(harm_levels) >= 4:
    E2 = harm_levels[2][1]
    E3 = harm_levels[3][1]
    cr2 = find_crossings(R, V_harm, E2)
    if cr2 and len(cr2) >= 2:
        x_a = cr2[0] - 0.12
        ax.annotate('', xy=(x_a, E3), xytext=(x_a, E2),
                    arrowprops=dict(arrowstyle='<->', color='#1565C0', lw=1.5,
                                   shrinkA=2, shrinkB=2), zorder=6)
        ax.text(x_a - 0.08, (E2 + E3) / 2, r'$\hbar\omega$',
                ha='right', va='center', fontsize=13, color='#1565C0',
                fontweight='bold')

# === Annotation: Morse spacing narrows ===
if len(morse_levels) >= 4:
    # Low pair: n=0 and n=1
    Em0 = morse_levels[0][1]
    Em1 = morse_levels[1][1]
    cr_m1 = find_crossings(R, V_morse, Em1)

    # High pair: second-to-last and last
    n_top = len(morse_levels) - 1
    Em_top1 = morse_levels[n_top - 1][1]
    Em_top = morse_levels[n_top][1]
    cr_mtop = find_crossings(R, V_morse, Em_top)

    if cr_m1 and len(cr_m1) >= 2:
        x_lo = cr_m1[-1] + 0.12
        ax.annotate('', xy=(x_lo, Em1), xytext=(x_lo, Em0),
                    arrowprops=dict(arrowstyle='<->', color='#C62828', lw=1.3,
                                   shrinkA=2, shrinkB=2), zorder=6)
        ax.text(x_lo + 0.08, (Em0 + Em1) / 2, 'wide',
                ha='left', va='center', fontsize=9.5, color='#C62828',
                style='italic')

    if cr_mtop and len(cr_mtop) >= 2:
        x_hi = cr_mtop[-1] + 0.12
        ax.annotate('', xy=(x_hi, Em_top), xytext=(x_hi, Em_top1),
                    arrowprops=dict(arrowstyle='<->', color='#C62828', lw=1.3,
                                   shrinkA=2, shrinkB=2), zorder=6)
        ax.text(x_hi + 0.08, (Em_top1 + Em_top) / 2, 'narrow',
                ha='left', va='center', fontsize=9.5, color='#C62828',
                style='italic')

# === Zero-point energy ===
E0 = morse_levels[0][1]
cr0 = find_crossings(R, V_morse, E0)
if cr0 and len(cr0) >= 2:
    mid_r = (cr0[0] + cr0[-1]) / 2
    ax.annotate('Zero-point\nenergy',
                xy=(mid_r, E0),
                xytext=(3.2, 1.5),
                fontsize=10, color='#C62828', ha='center',
                arrowprops=dict(arrowstyle='->', color='#C62828', lw=1.2,
                               connectionstyle='arc3,rad=-0.2'))

# === n labels ===
if harm_levels:
    cr_h0 = find_crossings(R, V_harm, harm_levels[0][1])
    if cr_h0:
        ax.text(cr_h0[0] - 0.04, harm_levels[0][1], r'$n\!=\!0$',
                ha='right', va='center', fontsize=9, color='#1565C0')

if morse_levels:
    n_last_m = morse_levels[-1][0]
    E_last_m = morse_levels[-1][1]
    cr_lm = find_crossings(R, V_morse, E_last_m)
    if cr_lm and len(cr_lm) >= 2:
        ax.text(cr_lm[-1] + 0.04, E_last_m, f'$n\\!=\\!{n_last_m}$',
                ha='left', va='center', fontsize=9, color='#C62828')

# R_e
ax.plot(Re, 0, 'k.', ms=5, zorder=6)
ax.text(Re, -0.4, r'$R_e$', ha='center', va='top', fontsize=13)

# Axes
ax.set_xlabel(r'$R$ (internuclear distance)', fontsize=13)
ax.set_ylabel(r'$V(R)$', fontsize=13)
ax.set_title('Harmonic vs Morse Potential', fontsize=14, pad=10)
ax.set_xlim(0.5, 4.5)
ax.set_ylim(-0.7, ymax)
ax.legend(loc='upper right', fontsize=10.5, framealpha=0.95)
ax.tick_params(labelsize=11)

plt.tight_layout()
out = '/Users/yuan/grad-exam-physics-chem/物理化学6/figures/morse_vs_harmonic.png'
plt.savefig(out, dpi=200, bbox_inches='tight', facecolor='white')
plt.close()

# Print diagnostics
print(f"Parameters: Re={Re}, De={De}, a={a_morse}, k={k}, omega={omega}")
print(f"Harmonic levels ({len(harm_levels)}):")
for n, E in harm_levels:
    cr = find_crossings(R, V_harm, E)
    print(f"  n={n}: E={E:.3f}, crossings={[f'{c:.2f}' for c in cr]}")
print(f"Morse levels ({len(morse_levels)}):")
for n, E in morse_levels:
    cr = find_crossings(R, V_morse, E)
    print(f"  n={n}: E={E:.3f}, crossings={[f'{c:.2f}' for c in cr]}")
print(f"\nSaved to {out}")
