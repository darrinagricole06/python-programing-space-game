PLANET_POOL = [
    {
        "name": "Verdantis",
        "description": "A lush world covered in bioluminescent forests",
        "danger_level": 1,
        "has_water": True,
        "encounter": "empty",
    },
    {
        "name": "Kragnor",
        "description": "A barren rock surrounded by a dense asteroid belt",
        "danger_level": 3,
        "has_water": False,
        "encounter": "asteroid_field",
    },
    {
        "name": "Aquifera",
        "description": "An ocean world with floating trade platforms",
        "danger_level": 1,
        "has_water": True,
        "encounter": "trader",
    },
    {
        "name": "Nyx Station",
        "description": "An abandoned station on the edge of raider territory",
        "danger_level": 4,
        "has_water": False,
        "encounter": "raider",
    },
    {
        "name": "Heliosa",
        "description": "A scorched planet orbiting twin suns",
        "danger_level": 2,
        "has_water": False,
        "encounter": "asteroid_field",
    },
    {
        "name": "Thalassa",
        "description": "A frozen moon hiding liquid water beneath its crust",
        "danger_level": 2,
        "has_water": True,
        "encounter": "empty",
    },
    {
        "name": "The Drift",
        "description": "A lawless stretch of open space frequented by pirates",
        "danger_level": 5,
        "has_water": False,
        "encounter": "raider",
    },
    {
        "name": "Port Serenity",
        "description": "A peaceful trading hub at the crossroads of two trade routes",
        "danger_level": 1,
        "has_water": True,
        "encounter": "trader",
    },
    {
        "name": "Ashfall",
        "description": "A volcanic world spewing debris into its orbit",
        "danger_level": 4,
        "has_water": False,
        "encounter": "asteroid_field",
    },
    {
        "name": "Elysara",
        "description": "A tranquil garden world with crystal-clear lakes",
        "danger_level": 1,
        "has_water": True,
        "encounter": "empty",
    },
    {
        "name": "Vortex Outpost",
        "description": "A rickety station near a gravitational anomaly",
        "danger_level": 3,
        "has_water": False,
        "encounter": "raider",
    },
    {
        "name": "Meridia",
        "description": "A temperate world with a thriving merchant colony",
        "danger_level": 1,
        "has_water": True,
        "encounter": "trader",
    },
]


def create_galaxy(size):
    pool = PLANET_POOL
    if size <= len(pool):
        return pool[:size]
    # If the galaxy is larger than our pool, cycle through planets again
    galaxy = []
    for i in range(size):
        galaxy.append(pool[i % len(pool)])
    return galaxy
