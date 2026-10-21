import os


class EVSmartAgent:

    def __init__(self):
        pass

    def analyze_and_advise(
        self, soc, temp, speed, range_km, nearest_station
    ):
        optimal_speed = 90 if speed > 100 else speed

        advice = f"⚡ **Vitesse optimale:** {optimal_speed} km/h pour préserver la batterie.\n\n"

        if soc < 20:
            advice += f"🚨 **Attention Batterie Faible ({soc}%)!** Rendez-vous à la station la plus proche: **{nearest_station['name']}** ({nearest_station['distance_km']} km ).\n\n"
        else:
            advice += f"✅ **Niveau de charge correct.** Station la plus proche disponible: **{nearest_station['name']}** ({nearest_station['distance_km']} km).\n\n"

        if temp > 35 or temp < 5:
            advice += "🌡️ **Température extrême!** Utilisez le contrôle climatique Eco pour réduire la consommation de la batterie."

        return advice