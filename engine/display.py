def show_intro(ship_name, crew_description):
    print()
    print("=" * 50)
    print("  SPACE EXPLORER")
    print("=" * 50)
    print()
    print(f"  Ship: {ship_name}")
    print(f"  Crew: {crew_description}")
    print()
    print("  Your mission: reach the final destination")
    print("  where a great bounty awaits.")
    print("  Manage your resources wisely — the galaxy")
    print("  is full of danger.")
    print()
    print("-" * 50)


def show_destination(destination, current_index, total):
    print()
    print(f"  [{current_index + 1}/{total}] Arriving at: {destination['name']}")
    print(f"  {destination['description']}")


def show_status(oxygen, hull):
    print(f"  >> Oxygen: {oxygen}  |  Hull: {hull}")


def show_encounter(narration):
    print(narration)


def show_victory(ship_name):
    print()
    print("=" * 50)
    print(f"  {ship_name} has reached the final destination!")
    print("  The great bounty is yours. Well done, crew.")
    print("=" * 50)
    print()


def show_defeat(ship_name, cause):
    print()
    print("=" * 50)
    print(f"  {ship_name} has been lost to the void.")
    print(f"  Cause: {cause}")
    print("  The galaxy claims another crew...")
    print("=" * 50)
    print()
