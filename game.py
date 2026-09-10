from engine.display import (
    show_intro,
    show_destination,
    show_encounter,
    show_defeat
)
from engine.galaxy import create_galaxy
from engine.encounters import process_water_planet
from engine.journey import process_encounter
import constants

def should_stop_fn() -> bool:
    answer = input("Do you want to continue your journey? (y/n): ")

    if answer == "y":
        return True
    else:
        return False
        
def main() -> None:
    
    show_intro(constants.SHIP_NAME, constants.CREW_DESCRIPTION)
    galaxy = create_galaxy(constants.GALAXY_SIZE)

    oxygen = constants.STARTING_OXYGEN
    hull = constants.STARTING_HULL
    ship_name = constants.SHIP_NAME
    crew_description = constants.CREW_DESCRIPTION
    galaxy_size = constants.GALAXY_SIZE

    # Set up the game loop to run for as many planets as there are in the galaxy
    for iteration in range(len(galaxy)):
        destination = galaxy[iteration]  # Terra Nova, Aqua Prime, Solaris Prime, etc.
        show_destination(destination, iteration, len(galaxy))  # Show destination

        # Player either stops or flies past; oxygen is consumed by default
        oxygen = oxygen - 10
        print("Current oxygen level:", oxygen)

        if  should_stop_fn():
            oxygen, hull, narration = process_encounter(destination, oxygen, hull)
            show_encounter(narration)
            if destination["has_water"]:
                oxygen, hull, water_narration = process_water_planet( oxygen, hull)
                show_encounter(water_narration)

        else:
            show_encounter("You fly past the planet without stopping.")
        
        print (f" Oxygen levels: {oxygen}, Hull integrity: {hull}")
        if oxygen <=0:
            show_defeat(ship_name, "Oxygen depleted")
            return
        elif hull <=0:
            show_defeat(ship_name, "Hull destroyed")
            return



if __name__ == "__main__":
    main()
