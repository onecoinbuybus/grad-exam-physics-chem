import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

# Step potential for E < V0, showing wavefunction oscillation + exponential decay
# Choose k1 and alpha so figure is legible
k1 = 3.0     # wavenumber on left (E)
alpha = 1.2  # decay constant on right (V0 - E)

# Incident amplitude A = 1; compute B/A = (k1 - i*alpha)/(k1 + i*alpha)
# then C/A = 2 k1 / (k1 + i*alpha)
B_over_A = (k1 - 1j * alpha) / (k1 + 1j * alpha)
C_over_A = 2 * k1 / (k1 + 1j * alpha)

x_left = np.linspace(-4, 0, 800)
x_right = np.linspace(0, 3, 800)

psi_left = np.exp(1j * k1 * x_left) + B_over_A * np.exp(-1j * k1 * x_left)
psi_right = C_over_A * np.exp(-alpha * x_right)

fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True,
                          gridspec_kw={'height_ratios': [1, 2]})

# === Top panel: potential ===
ax0 = axes[0]
ax0.fill_between([0, 3], 0, 1.5, color='#D0D9E8', alpha=0.7, zorder=1)
ax0.plot([-4, 0, 0, 3], [0, 0, 1.5, 1.5], '-', color='#1565C0', lw=2.5, zorder=2)
ax0.axhline(0.9, color='#C62828', ls='--', lw=1.3, zorder=3)
ax0.text(-3.8, 1.55, r'$V_0$', fontsize=12, color='#1565C0', fontweight='bold')
ax0.text(-3.8, 0.95, r'$E\ (<V_0)$', fontsize=11, color='#C62828')
ax0.text(0, -0.2, r'$0$', ha='center', va='top', fontsize=11)
ax0.set_ylim(-0.1, 1.9)
ax0.set_ylabel(r'$V(x)$', fontsize=12)
ax0.set_yticks([])
ax0.spines['top'].set_visible(False)
ax0.spines['right'].set_visible(False)

# === Bottom panel: Re[psi(x)] ===
ax1 = axes[1]
ax1.axhline(0, color='#AAAAAA', lw=0.7)
ax1.axvline(0, color='#888888', lw=0.8, ls=':')
ax1.plot(x_left, psi_left.real, color='#1565C0', lw=2.2, label='Region I  (oscillation)')
ax1.plot(x_right, psi_right.real, color='#C62828', lw=2.2, label=r'Region II  $e^{-\alpha x}$')
# Envelope on right
ax1.plot(x_right, np.abs(C_over_A) * np.exp(-alpha * x_right),
         color='#C62828', lw=1, ls=':', alpha=0.7)
ax1.plot(x_right, -np.abs(C_over_A) * np.exp(-alpha * x_right),
         color='#C62828', lw=1, ls=':', alpha=0.7)

ax1.fill_between([0, 3], -2.5, 2.5, color='#D0D9E8', alpha=0.25)

ax1.text(-2.3, 2.2, 'incident + reflected\n(standing wave pattern)',
         fontsize=10, color='#1565C0', ha='center')
ax1.text(1.3, 1.5, r'$\psi_2 = C e^{-\alpha x}$' + '\n(exponential decay,\nnot zero!)',
         fontsize=10, color='#C62828', ha='left')

ax1.set_xlabel(r'$x$', fontsize=13)
ax1.set_ylabel(r'Re$[\psi(x)]$', fontsize=12)
ax1.set_xlim(-4, 3)
ax1.set_ylim(-2.4, 2.4)
ax1.legend(loc='lower right', fontsize=10, framealpha=0.95)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.tick_params(labelsize=10)

plt.suptitle(r'Step potential, $E < V_0$:  total reflection ($R=1$) with penetration',
             fontsize=13, y=0.995)
plt.tight_layout()
out = '/Users/yuan/grad-exam-physics-chem/物理化学7/figures/step_potential.png'
plt.savefig(out, dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print('Saved:', out)
