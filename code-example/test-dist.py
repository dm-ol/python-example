# Тестова робота

def route_info(route):
    if ('distance' in route) and (type(route['distance']) == int):
        return f"Distance to your destination is {route['distance']} km"
    if ('speed' in route) and ('time' in route):
        return f"Distance to your destination is {route['speed'] * route['time']} km"
    return "No distance ifo si available"


info = {"speed": 50,
        "time": 2
        }

info_2 = {"distance": 250}

print(route_info(info))
print(route_info(info_2))

# or second example


def route_info_2(route):
    if ('distance' in route) and (type(route['distance']) == int):
        d_info = f"Distance to your destination is {route['distance']} km"
    elif ('speed' in route) and ('time' in route):
        d_info = f"Distance to your destination is {route['speed'] * route['time']} km"
    else:
        d_info = "No distance ifo si available"
    return d_info


info = {"speed": 50,
        "time": 2
        }

info_2 = {"distance": 250}

print(route_info_2(info))
print(route_info_2(info_2))
