from app.models import Knight


def battle(knights_config: dict) -> dict[str, int]:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    lancelot_final_power = lancelot.power
    mordred_final_power = mordred.power

    lancelot.get_damage(mordred_final_power)
    mordred.get_damage(lancelot_final_power)

    arthur_final_power = arthur.power
    red_knight_final_power = red_knight.power

    arthur.get_damage(red_knight_final_power)
    red_knight.get_damage(arthur_final_power)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }
