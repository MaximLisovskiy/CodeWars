def get_drink_by_profession(param):
    d = {
        "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal",
    }
    for key, value in d.items():
        if param.lower() in key:
            return value
    return "Beer"


print(get_drink_by_profession("jabroni"))
