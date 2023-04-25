one_gunpowder = {
    'sulfur': 2,
    'charcoal': 3,
}
one_explosive = {
    'gunpowder': 50,
    'sulfur': 10,
    'metall': 10,
    'fuel': 3,
}


def beancan_grenades(amount):
    """Рассчитывает количество ресурсов для Бобовых гранат"""
    # переменные с данными для крафта 1 гранаты
    gunpowder = 60
    metall = 20

    total_gunpowder = gunpowder * amount
    total_sulfur = total_gunpowder * one_gunpowder['sulfur']
    total_metall = metall * amount
    total_charcoal = total_gunpowder * one_gunpowder['charcoal']

    beancan_grenade_dict = {
        'total_gunpowder': total_gunpowder,
        'total_sulfur': total_sulfur,
        'total_metall': total_metall,
        'total_charcoal': total_charcoal,
    }

    return beancan_grenade_dict


def satchels(amount):
    """Рассчитывает количество ресурсов для Сачелей"""
    # переменные с данными для крафта 1 сачели
    grenades = 4
    stash = 1
    rope = 1

    total_grenades = grenades * amount
    total_gunpowder = beancan_grenades(total_grenades)
    total_charcoal = total_gunpowder['total_gunpowder'] * one_gunpowder[
        'charcoal']
    total_stash = stash * amount
    total_rope = rope * amount

    satchel_dict = {
        'total_grenades': total_grenades,
        'total_gunpowder': total_gunpowder,
        'total_stash': total_stash,
        'total_rope': total_rope,
        'total_charcoal': total_charcoal,
    }

    return satchel_dict


def explosive_ammos(amount):
    """Рассчитывает количество ресурсов для Разрывных патрон"""
    # переменные с данными для крафта 2 патрон
    gunpowder = 20
    sulfur = 10
    metall = 10

    sulfur_for_ammo = sulfur * amount
    total_gunpowder = gunpowder * amount
    total_sulfur = total_gunpowder * one_gunpowder['sulfur'] + sulfur_for_ammo
    total_metall = metall * amount
    total_charcoal = total_gunpowder * one_gunpowder['charcoal']

    explosive_ammo_dict = {
        'total_gunpowder': total_gunpowder,
        'total_sulfur': total_sulfur,
        'total_metall': total_metall,
        'total_charcoal': total_charcoal,
    }
    return explosive_ammo_dict


def rockets(amount):
    """Рассчитывает количество ресурсов для Ракет"""
    # переменные с данными для крафта 1 ракеты
    gunpowder = 150
    explosive = 10
    pipe = 2

    gunpowder_for_rocket = gunpowder * amount
    total_explosive = explosive * amount
    gunpowder_for_explosive = total_explosive * one_explosive['gunpowder']
    sulfur_for_explosive = total_explosive * one_explosive['sulfur']
    metal_for_explosive = total_explosive * one_explosive['metall']
    fuel_for_explosive = total_explosive * one_explosive['fuel']

    total_gunpowder = gunpowder_for_explosive + gunpowder_for_rocket
    total_sulfur = total_gunpowder * one_gunpowder[
        'sulfur'] + sulfur_for_explosive
    total_charcoal = total_gunpowder * one_gunpowder['charcoal']
    total_pipe = pipe * amount
    rocket_dict = {
        'total_explosive': total_explosive,
        'total_gunpowder': total_gunpowder,
        'gunpowder_for_rocket': gunpowder_for_rocket,
        'total_sulfur': total_sulfur,
        'total_charcoal': total_charcoal,
        'total_pipe': total_pipe,
        'total_metall': metal_for_explosive,
        'total_fuel': fuel_for_explosive,
    }
    return rocket_dict


def c4s(amount):
    """Рассчитывает количество ресурсов для C4"""
    # переменные с данными для крафта 1 С4
    explosive = 20
    cloth = 5
    tech_trash = 2

    total_explosive = explosive * amount
    gunpowder_for_explosive = total_explosive * one_explosive['gunpowder']
    sulfur_for_explosive = total_explosive * one_explosive['sulfur']
    metal_for_explosive = total_explosive * one_explosive['metall']
    fuel_for_explosive = total_explosive * one_explosive['fuel']

    total_sulfur = gunpowder_for_explosive * one_gunpowder[
        'sulfur'] + sulfur_for_explosive
    total_charcoal = gunpowder_for_explosive * one_gunpowder['charcoal']
    total_cloth = cloth * amount
    total_tech_trash = tech_trash * amount
    c4_dict = {
        'total_explosive': total_explosive,
        'total_gunpowder': gunpowder_for_explosive,
        'total_sulfur': total_sulfur,
        'total_charcoal': total_charcoal,
        'total_cloth': total_cloth,
        'total_tech_trash': total_tech_trash,
        'total_metall': metal_for_explosive,
        'total_fuel': fuel_for_explosive,
    }
    return c4_dict
