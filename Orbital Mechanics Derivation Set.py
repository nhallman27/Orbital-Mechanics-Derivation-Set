import math
import urllib.request
import csv
import io

from collections import defaultdict

G = 6.67430e-11

SOLAR_SYSTEM = {
    "mercury": {"mass": 3.301e23,  "radius": 2.4397e6},
    "venus":   {"mass": 4.867e24,  "radius": 6.0518e6},
    "earth":   {"mass": 5.972e24,  "radius": 6.3710e6},
    "mars":    {"mass": 6.417e23,  "radius": 3.3895e6},
    "jupiter": {"mass": 1.898e27,  "radius": 7.1492e7},
    "saturn":  {"mass": 5.683e26,  "radius": 6.0268e7},
    "uranus":  {"mass": 8.681e25,  "radius": 2.5559e7},
    "neptune": {"mass": 1.024e26,  "radius": 2.4764e7},
}

def calculate_orbital_velocity(mass, radius):
    return math.sqrt(G * mass / radius)

def calculate_escape_velocity(mass, radius):
    return math.sqrt(2 * G * mass / radius)

def load_planets():
    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,pl_masse,pl_massj,pl_rade+from+pscomppars+where+pl_rade+is+not+null&format=csv"
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')

    raw = defaultdict(list)
    reader = csv.DictReader(io.StringIO(content))
    for row in reader:
        massj = row['pl_massj']
        masse = row['pl_masse']
        rade = row['pl_rade']

        if not rade:
            continue
        if massj:
            mass = float(massj) * 1.898e27
        elif masse:
            mass = float(masse) * 5.972e24
        else:
            continue

        raw[row['pl_name'].lower()].append({
            "mass": mass,
            "radius": float(rade) * 6.371e6
        })

    planets = {}
    for name, entries in raw.items():
        planets[name] = {
            "mass": sum(e["mass"] for e in entries) / len(entries),
            "radius": sum(e["radius"] for e in entries) / len(entries)
        }
    return planets

# tool selection
while True:
    try:
        tool = int(input("Choose a tool:\n1. Orbital Velocity\n2. Escape Velocity\n3. Both\n\n"))
        if tool in [1, 2, 3]:
            break
        print("Invalid choice. Please select 1, 2, or 3.")
    except ValueError:
        print("Invalid choice. Please select 1, 2, or 3.")

# input method selection
while True:
    try:
        mode = int(input("\nInput method:\n1. Enter mass and radius manually\n2. Use planetary data\n\n"))
        if mode in [1, 2]:
            break
        print("Invalid choice. Please select 1 or 2.")
    except ValueError:
        print("Invalid choice. Please select 1 or 2.")

if mode == 1:
    mass = float(input("Mass (kg): "))
    radius = float(input("Radius (m): "))
else:
    try:
        print("\nFetching latest planetary data...")
        planets = load_planets()
        planets.update(SOLAR_SYSTEM)
        print(f"Loaded {len(planets)} planets.\n")
    except Exception as e:
        print(f"Could not fetch data: {e}")
        exit()

    while True:
        name = input("Enter planet name: ").strip().lower()
        if name in planets:
            mass = planets[name]["mass"]
            radius = planets[name]["radius"]
            break
        print(f"Planet '{name}' not found. Try again.")

# gives surface values
if tool in [1, 3]:
    print(f"\nOrbital velocity: {calculate_orbital_velocity(mass, radius)/1000:.4f} km/s")
if tool in [2, 3]:
    print(f"Escape velocity:  {calculate_escape_velocity(mass, radius)/1000:.4f} km/s")