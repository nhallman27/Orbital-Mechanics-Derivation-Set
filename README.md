# Orbital Mechanics Derivation Set

A Python tool for calculating orbital and escape velocities for planets, using either manually entered values or real astronomical data pulled from NASA's Exoplanet Archive.

## What it does

This script calculates:
- **Orbital velocity** — the speed needed to maintain a stable orbit around a body
- **Escape velocity** — the speed needed to break free of a body's gravity entirely

You can calculate these for:
- Any custom object, by manually entering mass and radius
- Any planet in our solar system (built-in data)
- Thousands of confirmed exoplanets, pulled live from NASA's Exoplanet Archive API

## How it works

The script uses the standard gravitational formulas:

- Orbital velocity: `v = √(GM / r)`
- Escape velocity: `v = √(2GM / r)`

Where `G` is the gravitational constant, `M` is the mass of the body, and `r` is its radius.

For exoplanet data, the script queries NASA's Exoplanet Archive, converts reported mass and radius values into standard SI units (kilograms and meters), and averages any duplicate entries for the same planet.

## Usage

Run the script:

```
python orbital-mechanics-derivation-set.py
```

You'll be prompted to:
1. Choose which calculation(s) to run (orbital velocity, escape velocity, or both)
2. Choose your input method — enter mass/radius manually, or look up a planet by name
3. If looking up a planet, the script fetches the latest data and lets you search by name

## Example

```
Choose a tool:

1. Orbital Velocity
2. Escape Velocity
3. Both

> 3

Input method:

1. Enter mass and radius manually
2. Use planetary data

> 2

Enter planet name: earth

Orbital velocity: 7.9097 km/s
Escape velocity:  11.1859 km/s
```

## Requirements

- Python 3
- Internet connection (only required when using live exoplanet data)

## Notes

Solar system planet data is stored locally for speed and reliability. Exoplanet data is fetched live on each run, so values may update as NASA's archive is updated.