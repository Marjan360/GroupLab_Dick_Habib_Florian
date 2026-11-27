"""
Group: 4
Name: Esther Dick, Maeve Florian, Marjan Habib
Date: 11/23/2026
Course: CSC-157
Lab: Group 
Program Description: 
"""

class Beverage:

    # When a beverage is created, store its details.
    def __init__(
            self, name, beverage_type, flavor, sweetness, 
            bitterness, caffeine, temperature
    ):
        self._name = name
        self._type = beverage_type
        self._flavor = flavor
        self._sweetness = sweetness
        self._bitterness = bitterness
        self._caffeine = caffeine
        self._temperature = temperature

    # When a beverage is printed, return its details as formatted text.
    def __str__(self):
        beverage_details = (
            f"Beverage name: {self._name}\n"
            f"Beverage type: {self._type}\n"
            f"Flavor profile: {self._flavor}\n"
            f"Sweetness level: {self._sweetness}\n"
            f"Bitterness level: {self._bitterness}\n"
            f"Caffeine level: {self._caffeine}\n"
            f"Serving temperature: {self._temperature}"
        )
        return beverage_details

    # Return the user's preferences that this beverage matches.
    def matching_preferences(self, preferences):
        matches = []

        for preference, beverage_detail in [
            ("flavor", self._flavor), 
            ("sweetness", self._sweetness),
            ("bitterness", self._bitterness),
            ("caffeine", self._caffeine),
            ("temperature", self._temperature)
        ]:

            if beverage_detail == preferences[preference]:
                matches.append(preference)

        return matches
    