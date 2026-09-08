from engine.display import show_intro, show_destination 
from engine.galaxy import create_galaxy
from engine.journey import travel
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

    # Set up the game loop to run for as many planets as there are in the galaxy
    for iteration in range(len(galaxy)):
        destination = galaxy[iteration]  # Terra Nova, Aqua Prime, Solaris Prime, etc.
        show_destination(destination, iteration, len(galaxy))  # Show destination

        # Player either stops or flies past; oxygen is consumed by default
        oxygen = oxygen - 10
        print("Current oxygen level:", oxygen)





if __name__ == "__main__":
    main()
