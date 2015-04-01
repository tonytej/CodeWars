import math



def wind_info(runway, wind_direction, wind_speed):
    cw = int(round((math.sin((wind_direction - int(runway[:2]+'0'))*0.0174532925)) * wind_speed))
    hw = int(round((math.cos((wind_direction - int(runway[:2]+'0'))*0.0174532925)) * wind_speed))
    return "{}wind {} knots. Crosswind {} knots from your {}.".format(
        "Head" if hw >= 0 else "Tail",
        abs(hw), abs(cw),
        "right" if cw >= 0 else "left")

print wind_info("18", 170, 15)
print wind_info("18", 210, 14)
print wind_info("22L", 160, 14)
print wind_info("18", 70, 15)

test_data = [
(("18", 170, 15),"Headwind 15 knots. Crosswind 3 knots from your left."),
(("18", 210, 14),"Headwind 12 knots. Crosswind 7 knots from your right."),
(("22L", 160, 14),"Headwind 7 knots. Crosswind 12 knots from your left."),
(("18", 70, 15),"Tailwind 5 knots. Crosswind 14 knots from your left." )
]



'''"%swind %s knots. Crosswind %s knots from your %s." % (
        "Head" if hw >= 0 else "Tail",
        abs(hw), abs(cw),
        "right" if cw >= 0 else "left")'''