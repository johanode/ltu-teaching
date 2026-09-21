from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# Inställningar
seed = 20260920
number_of_sides = 10
output_dir = Path("images")

output_dir.mkdir(exist_ok=True)
rng = np.random.default_rng(seed)


#%% Beräkna sannolikheter för 20 kast

p_failure = 1 / number_of_sides
n = 40

k = np.arange(0, n + 1)

# Funktionssäkerhet och kumulativ felsannolikhet
R = (1 - p_failure) ** k
F = 1 - R

# Sannolikhet att det första felet inträffar vid kast k
f = np.zeros(n + 1)
f[1:] = (
    p_failure
    * (1 - p_failure) ** (k[1:] - 1)
)


#%% Rita diagram

fig, ax = plt.subplots(
    3,
    1,
    figsize=(9, 8),
    sharex=True,
)

fig.suptitle(
    f"Geometrisk fördelning för en "
    f"{number_of_sides}-sidig tärning "
    f"($p=1/{number_of_sides}$)",
    fontsize=14,
)

# Funktionssäkerhet
ax[0].plot(
    k,
    R,
    color="seagreen",
    marker="o",
    markersize=4,
    linewidth=2,
)

ax[0].fill_between(
    k,
    R,
    color="seagreen",
    alpha=0.1,
)

ax[0].set_title("Funktionssäkerhet")
ax[0].set_ylabel("$R_K(k)$")
ax[0].set_ylim(0, 1.05)

# Kumulativ felsannolikhet
ax[1].plot(
    k,
    F,
    color="firebrick",
    marker="o",
    markersize=4,
    linewidth=2,
)

ax[1].fill_between(
    k,
    F,
    color="firebrick",
    alpha=0.1,
)

ax[1].set_title("Kumulativ felsannolikhet")
ax[1].set_ylabel("$F_K(k)$")
ax[1].set_ylim(0, 1.05)

# Sannolikhet för första fel vid kast k
ax[2].bar(
    k,
    f,
    color="steelblue",
    width=0.7,
)

ax[2].set_title("Sannolikhet att det första felet inträffar vid kast $k$")
ax[2].set_xlabel("Antal kast, $k$")
ax[2].set_ylabel("$P(K=k)$")
ax[2].set_ylim(0, f.max() * 1.15)
ax[2].set_xticks(k)

for axis in ax:
    axis.set_xlim(-0.5, n + 0.5)
    axis.grid(
        axis="y",
        alpha=0.3,
    )

fig.tight_layout()

#%% Geometriskt fördelad tid till första fel

p_failure = 1 / number_of_sides
population_size = 1_000
max_roll = 3 * number_of_sides

# Simulera antal kast fram till det första felet
simulated = rng.geometric(
    p_failure,
    size=population_size,
)

rolls = np.arange(1, max_roll + 1)

# Simulerad sannolikhet för fel vid respektive kast
observed = np.array([
    (simulated == roll).mean()
    for roll in rolls
])

# Teoretisk geometrisk fördelning
theoretical = (
    (1 - p_failure) ** (rolls - 1)
    * p_failure
)

fig, ax = plt.subplots(figsize=(9, 5))

ax.bar(
    rolls,
    observed,
    color="steelblue",
    alpha=0.7,
    label="Simulerad sannolikhet",
)

ax.plot(
    rolls,
    theoretical,
    color="firebrick",
    marker="o",
    markersize=4,
    label="Teoretisk sannolikhet",
)

ax.set_title(
    f"Tid till första fel med en {number_of_sides}-sidig tärning"
)
ax.set_xlabel("Kast då det första felet inträffar")
ax.set_ylabel("Sannolikhet")
ax.set_xlim(0, max_roll + 1)
ax.set_ylim(
    0,
    max(observed.max(), theoretical.max()) * 1.1,
)
ax.grid(alpha=0.3)
ax.legend()

fig.tight_layout()
# fig.savefig(
#     output_dir / "geometrisk-tid-till-fel.png",
#     dpi=180,
# )
plt.close(fig)


#%% Exponentialfördelad tid till första fel

failure_rate = 0.02
population_size = 5_000
max_time = 200

time = np.linspace(0, max_time, 401)

# Simulera livslängden för varje enhet
lifetimes = rng.exponential(
    scale=1 / failure_rate,
    size=population_size,
)

# Teoretisk funktionssäkerhet och felsannolikhet
reliability = np.exp(-failure_rate * time)
failure_probability = 1 - reliability

# Observerad andel fungerande enheter
observed_reliability = np.array([
    (lifetimes > value).mean()
    for value in time
])

fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(
    time,
    reliability,
    color="seagreen",
    linewidth=2,
    label="$R(t)$",
)

ax.plot(
    time,
    failure_probability,
    color="firebrick",
    linewidth=2,
    label="$F(t)$",
)

ax.plot(
    time[::10],
    observed_reliability[::10],
    linestyle="none",
    marker="o",
    markersize=4,
    color="steelblue",
    label="Simulerad andel fungerande",
)

ax.axvline(
    1 / failure_rate,
    color="gray",
    linestyle="--",
    label="$MTTF=1/\\lambda$",
)

ax.set_title("Exponentialfördelad tid till första fel")
ax.set_xlabel("Tid")
ax.set_ylabel("Sannolikhet")
ax.set_xlim(0, max_time)
ax.set_ylim(0, 1)
ax.grid(alpha=0.3)
ax.legend()

fig.tight_layout()
fig.savefig(
    output_dir / "exponentialfordelad-tid-till-fel.png",
    dpi=180,
)
plt.close(fig)


#%% Antal felade och fungerande enheter

failure_rate = 0.02
population_size = 1_000
max_time = 160

time = np.linspace(0, max_time, 321)

# Simulera livslängden för varje enhet
lifetimes = rng.exponential(
    scale=1 / failure_rate,
    size=population_size,
)

# Simulerat antal felade enheter
observed_failures = np.array([
    (lifetimes <= value).sum()
    for value in time
])

# Förväntat antal felade och fungerande enheter
expected_failures = (
    population_size
    * (1 - np.exp(-failure_rate * time))
)

expected_survivors = (
    population_size
    * np.exp(-failure_rate * time)
)

fig, ax = plt.subplots(figsize=(9, 5))

ax.step(
    time,
    observed_failures,
    where="post",
    color="firebrick",
    alpha=0.7,
    label="Simulerat antal felade",
)

ax.plot(
    time,
    expected_failures,
    color="darkred",
    linewidth=2,
    label="$mF(t)$",
)

ax.plot(
    time,
    expected_survivors,
    color="seagreen",
    linewidth=2,
    label="$mR(t)$",
)

ax.set_title("Population observerad fram till första fel")
ax.set_xlabel("Tid")
ax.set_ylabel("Antal enheter")
ax.set_xlim(0, max_time)
ax.set_ylim(0, population_size)
ax.grid(alpha=0.3)
ax.legend()

fig.tight_layout()
fig.savefig(
    output_dir / "population-tid-till-fel.png",
    dpi=180,
)
plt.close(fig)