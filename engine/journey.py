from engine.display import (
    show_destination,
    show_encounter,
    show_status,
    show_victory,
    show_defeat,
)
from engine.encounters import (
    apply_jump_cost,
    process_asteroid_field,
    process_raider,
    process_trader,
    process_empty,
    process_water_planet,
)


def process_encounter(destination, oxygen, hull):
    encounter = destination["encounter"]
    danger = destination["danger_level"]

    if encounter == "asteroid_field":
        oxygen, hull, narration = process_asteroid_field(oxygen, hull, danger)
    elif encounter == "raider":
        oxygen, hull, narration = process_raider(oxygen, hull, danger)
    elif encounter == "trader":
        oxygen, hull, narration = process_trader(oxygen, hull)
    else:
        oxygen, hull, narration = process_empty(oxygen, hull)

    return oxygen, hull, narration


def check_defeat(oxygen, hull):
    if hull <= 0:
        return "Hull destroyed"
    if oxygen <= 0:
        return "Oxygen depleted"
    return None


def travel(galaxy, oxygen, hull, ship_name, should_stop_fn=None):
    total = len(galaxy)

    for i in range(total):
        destination = galaxy[i]

        oxygen = apply_jump_cost(oxygen)
        show_destination(destination, i, total)

        if should_stop_fn is None or should_stop_fn():
            oxygen, hull, narration = process_encounter(destination, oxygen, hull)
            show_encounter(narration)

            if destination["has_water"]:
                oxygen, hull, water_narration = process_water_planet(oxygen, hull)
                show_encounter(water_narration)
        else:
            show_encounter("  You fly past without stopping.")

        show_status(oxygen, hull)

        cause = check_defeat(oxygen, hull)
        if cause:
            show_defeat(ship_name, cause)
            return "defeat"

    show_victory(ship_name)
    return "victory"
