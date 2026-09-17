import engine.display def check_defeat_Status(oxygen, hull, ship_name) ->None
if oxygen <=0:
            show_defeat(ship_name, "Oxygen depleted")
            return
        elif hull <=0:
            show_defeat(ship_name, "Hull destroyed")
            return None
cause = check_defeat_Status(oxygen =0, hull=15, "Dynamic")