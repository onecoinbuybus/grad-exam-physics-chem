import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from numpy.polynomial.hermite_e import hermeval
matplotlib.rcParams['mathtext.fontset'] = 'cm'

# Harmonic oscillator wavefunctions in dimensionless coordinate y = alpha*x
# psi_n(y) = N_n * H_n(y) * exp(-y^2/2), with "physicist" Hermite H_n
# Physicist's Hermite polynomials (explicit, low orders)
def H(n, y):
    if n == 0: return np.ones_like(y)
    if n == 1: return 2 * y
    if n == 2: return 4 * y**2 - 2
    if n == 3: return 8 * y**3 - 12 * y
    raise ValueError

def phi(n, y):
    from math import factorial, pi, sqrt
    N = 1.0 / np.sqrt(2**n * factorial(n) * np.sqrt(np.pi))
    return N * H(n, y) * np.exp(-y**2 / 2)

y = np.linspace(-4.5, 4.5, 800)
V = 0.5 * y**2  # parabolic potential in units where hbar*omega = 1 (so E_n = n + 1/2)

fig, ax = plt.subplots(figsize=(8, 6))

# Plot potential
ax.plot(y, V, '-', color='#555555', lw=2, zorder=2)
ax.fill_between(y, V, 12, color='#EEEEEE', alpha=0.5, zorder=1)

colors = ['#1565C0', '#2E7D32', '#E67E22', '#C62828']
scale = 0.8  # visual scale of wavefunction

for n in range(4):
    E = n + 0.5
    # Draw energy level across classical turning points y = +-sqrt(2E)
    tp = np.sqrt(2 * E)
    ax.hlines(E, -tp, tp, color=colors[n], lw=1.0, alpha=0.5, zorder=3)
    # Wavefunction offset by E_n
    psi = phi(n, y)
    ax.plot(y, E + scale * psi, color=colors[n], lw=2, zorder=5)
    # Fill under wavefunction to baseline E
    ax.fill_between(y, E, E + scale * psi, color=colors[n], alpha=0.15, zorder=4)
    # Label on the right
    x_label = 4.2
    ax.text(x_label, E + 0.05, rf'$n={n},\ E_{n}=\frac{{{2*n+1}}}{{2}}\hbar\omega$',
            color=colors[n], fontsize=11, va='bottom', ha='left', fontweight='bold')

# Annotate zero-point energy (upper-left area, away from wavefunction clusters)
ax.annotate(r'zero-point: $\frac{1}{2}\hbar\omega$',
            xy=(0.2, 0.5), xytext=(-4.2, 4.3),
            fontsize=11, color='#1565C0',
            arrowprops=dict(arrowstyle='->', color='#1565C0', lw=1.2,
                            connectionstyle='arc3,rad=-0.3'))

# Annotate equal spacing on far left (between n=2 and n=3 to avoid wavefunctions)
ax.annotate('', xy=(-3.8, 3.5), xytext=(-3.8, 2.5),
            arrowprops=dict(arrowstyle='<->', color='#C62828', lw=1.3))
ax.text(-4.0, 3.0, r'$\hbar\omega$', fontsize=12, color='#C62828',
        ha='right', va='center', fontweight='bold')

# Axes
ax.set_xlabel(r'$y = \alpha x$ (dimensionless displacement)', fontsize=13)
ax.set_ylabel(r'Energy  /  $\hbar\omega$', fontsize=13)
ax.set_title(r'Harmonic oscillator: $\Phi_n(y) = N_n H_n(y)\,e^{-y^2/2}$',
             fontsize=14, pad=10)
ax.set_xlim(-4.5, 6.8)
ax.set_ylim(-0.3, 5.0)
ax.set_yticks([0, 0.5, 1.5, 2.5, 3.5])
ax.tick_params(labelsize=11)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
out = '/Users/yuan/grad-exam-physics-chem/物理化学7/figures/harmonic_wavefunctions.png'
plt.savefig(out, dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print('Saved:', out)
