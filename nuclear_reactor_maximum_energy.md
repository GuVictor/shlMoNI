# Nuclear Reactor — Maximum Energy

## Problem Statement

Dr. Victor Frankenstein has quit the monster creation business. Nuclear energy now strikes his fantasy. He has created a fission reactor that takes radioactive materials in a liquid state.

The capacity of the reactor is `V` gallons. He has `N` vials of radioactive liquids, each with some mass and some volume. Some units of energy are produced when a liquid is poured into the reactor. Victor would like to maximize the energy output.

However, there is a catch. Upon studying the physics and history of atomic elements, he realizes that the combined mass of the radioactive liquids inside the reactor must not exceed a certain critical mass `M`; otherwise, the reaction would get out of control and cause a violent explosion.

Write an algorithm that will help Victor get the maximum energy from the reactor without losing his life.

## Input

1. The first line consists of an integer `reacCapacity`, representing the reactor capacity (`V`).
2. The second line consists of an integer `criticalMass`, representing the critical mass of the reactor (`M`).
3. The third line consists of an integer `numVolumes`, representing the number of liquid volumes (`X`).
4. The fourth line consists of `X` space-separated integers `vol[0], vol[1], ..., vol[X-1]`, representing the volumes of the `X` liquids in order.
5. The fifth line consists of an integer `numMasses`, representing the number of masses (`Y`).
6. The sixth line consists of `Y` space-separated integers `mass[0], mass[1], ..., mass[Y-1]`, representing the masses of the `Y` liquids in order.
7. The seventh line consists of an integer `numEnergy`, representing the number of energy values (`Z`).
8. The last line consists of `Z` space-separated integers `energy[0], energy[1], ..., energy[Z-1]`, representing the energy produced by the `Z` liquids in order.

## Output

Print an integer representing the maximum energy that can be generated from the reactor while satisfying the given constraints.

## Note

`numVolumes`, `numMasses`, and `numEnergy` are the same.

## Constraints

`1 ≤ numVolumes, numMasses, numEnergy ≤ 10^4`

## Example

### Input

```text
100
15
5
50 40 30 20 10
5
1 2 3 9 5
5
300 480 270 200 180
```

### Output

```text
960
```

### Explanation

By selecting liquids from vials number 1, 2, and 5, the energy produced is:

`300 + 480 + 180 = 960`.

This combination of liquids contributes a total volume of:

`50 + 40 + 10 = 100`,

which does not exceed the reactor capacity; and a total mass of:

`1 + 2 + 5 = 8`,

which does not exceed the critical mass.
