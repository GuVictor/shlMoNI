import sys


def max_reactor_energy(reac_capacity, critical_mass, volumes, masses, energies):
    """Return the maximum energy from a 0/1 knapsack with two capacity constraints.

    Each liquid is an item that can be selected at most once. The chosen items
    must fit within the reactor volume (reac_capacity) and the critical mass
    (critical_mass) simultaneously, while maximizing total energy.
    """
    width = critical_mass + 1
    # dp[cap * width + m] = max energy using volume <= cap and mass <= m.
    dp = [0] * ((reac_capacity + 1) * width)

    for volume, mass, energy in zip(volumes, masses, energies):
        # An item heavier or bulkier than a limit can never be selected.
        if volume > reac_capacity or mass > critical_mass:
            continue

        # Iterate backwards so each item is considered at most once.
        for cap in range(reac_capacity, volume - 1, -1):
            row = cap * width
            prev_row = (cap - volume) * width
            for current_mass in range(critical_mass, mass - 1, -1):
                idx = row + current_mass
                candidate = dp[prev_row + current_mass - mass] + energy
                if candidate > dp[idx]:
                    dp[idx] = candidate

    return dp[reac_capacity * width + critical_mass]


def main():
    data = sys.stdin.read().split()
    if not data:
        return

    it = iter(data)
    reac_capacity = int(next(it))
    critical_mass = int(next(it))
    num_volumes = int(next(it))
    volumes = [int(next(it)) for _ in range(num_volumes)]
    num_masses = int(next(it))
    masses = [int(next(it)) for _ in range(num_masses)]
    num_energy = int(next(it))
    energies = [int(next(it)) for _ in range(num_energy)]

    result = max_reactor_energy(reac_capacity, critical_mass, volumes, masses, energies)
    print(result)


if __name__ == "__main__":
    main()
