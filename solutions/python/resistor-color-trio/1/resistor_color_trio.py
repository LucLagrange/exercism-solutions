def label(colors):
    colors_dict = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9,
    }

    color_integers_list = []

    for color in colors[:2]:
        color_integers_list.append(str(colors_dict[color]))

    color_integers_list.append(colors_dict[colors[2]] * '0')

    resistance_raw = int(''.join(color_integers_list))

    print(resistance_raw)

    if int(resistance_raw / 1000000000):
        print(str(int(resistance_raw / 1000000000)) + ' gigaohms')
        return str(int(resistance_raw / 1000000000)) + ' gigaohms'

    elif int(resistance_raw / 1000000):
        print(str(int(resistance_raw / 1000000)) + ' megaohms')
        return str(int(resistance_raw / 1000000)) + ' megaohms'

    elif int(resistance_raw / 1000):
        print(str(int(resistance_raw / 1000)) + ' kiloohms')
        return str(int(resistance_raw / 1000)) + ' kiloohms'
    else:
        print(str(resistance_raw) + ' ohms')
        return str(resistance_raw) + ' ohms'
