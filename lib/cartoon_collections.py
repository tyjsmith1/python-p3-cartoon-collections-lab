def roll_call_dwarves(dwarves):
    num = 1
    for dwarf in dwarves:
        print(f"{num}. {dwarf}")
        num += 1

def summon_captain_planet(planeteer_calls):
    complete = [call.title() + "!" for call in planeteer_calls]
    return complete

def long_planeteer_calls(planeteer_calls):
    for call in planeteer_calls:
        if len(call) > 4:
            return True
    return False


def find_the_cheese(snacks):
    cheese = ["cheddar", "gouda", "camembert"]

    for snack in snacks:
        if snack in cheese:
            return snack
    return None
