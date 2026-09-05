# ============================================================
# SPACE EXPLORER — Your Ship, Your Story
# ============================================================
# Change these values to make the game your own.
# Run the game after each change to see what happens!
# ============================================================

# --- Your ship ---
SHIP_NAME = "The Sr. Explorer"
CREW_DESCRIPTION = "A brave crew of space explorers"

# --- Starting resources ---
STARTING_OXYGEN = 100
STARTING_HULL = 100

# --- Galaxy ---
GALAXY_SIZE = 8
USE_CUSTOM_PLANETS = True
PLANETS = []
PLANETS.append("Terra nova")
PLANETS.append("aqua prime")
PLANETS.append("Solaris")
PLANETS.append("Destroyer")
PLANETS.append("Nebula")


print(len(PLANETS))
PLANETS[2] = "Solaris Prime"