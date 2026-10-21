def get_nearest_charging_station(current_soc):
    stations = [
        {"name": "TotalEnergies Fast Charge - Ennasr", "distance_km": 4.2, "power_kw": 50},
        {"name": "Shell Recharge - Lac 2", "distance_km": 8.5, "power_kw": 120},
        {"name": "Agil EV Charging - Autoroute A1", "distance_km": 15.0, "power_kw": 22}
    ]
    return min(stations, key=lambda x: x["distance_km"])