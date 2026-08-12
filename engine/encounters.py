OXYGEN_COST_PER_JUMP = 8
ASTEROID_HULL_DAMAGE_BASE = 10
RAIDER_HULL_DAMAGE_BASE = 12
RAIDER_OXYGEN_COST = 5
TRADER_OXYGEN_REFILL = 15
TRADER_HULL_REPAIR = 10
WATER_PLANET_OXYGEN_REFILL = 20


def process_asteroid_field(oxygen, hull, danger_level):
    damage = ASTEROID_HULL_DAMAGE_BASE + (danger_level * 2)
    new_hull = hull - damage
    narration = (
        f"  Asteroid debris slams into the hull! "
        f"Hull takes {damage} damage."
    )
    return oxygen, new_hull, narration


def process_raider(oxygen, hull, danger_level):
    damage = RAIDER_HULL_DAMAGE_BASE + (danger_level * 2)
    new_hull = hull - damage
    new_oxygen = oxygen - RAIDER_OXYGEN_COST
    narration = (
        f"  Raiders attack! The crew fights them off but takes "
        f"{damage} hull damage and uses {RAIDER_OXYGEN_COST} extra oxygen in the struggle."
    )
    return new_oxygen, new_hull, narration


def process_trader(oxygen, hull):
    new_oxygen = oxygen + TRADER_OXYGEN_REFILL
    new_hull = hull + TRADER_HULL_REPAIR
    narration = (
        f"  A friendly trader offers supplies. "
        f"Oxygen restored by {TRADER_OXYGEN_REFILL}, hull repaired by {TRADER_HULL_REPAIR}."
    )
    return new_oxygen, new_hull, narration


def process_empty(oxygen, hull):
    narration = "  All is calm. The crew rests and takes in the view."
    return oxygen, hull, narration


def process_water_planet(oxygen, hull):
    new_oxygen = oxygen + WATER_PLANET_OXYGEN_REFILL
    narration = (
        f"  The crew extracts oxygen from the planet's water. "
        f"Oxygen restored by {WATER_PLANET_OXYGEN_REFILL}."
    )
    return new_oxygen, hull, narration


def apply_jump_cost(oxygen):
    return oxygen - OXYGEN_COST_PER_JUMP
