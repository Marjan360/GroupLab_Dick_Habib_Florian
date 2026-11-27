"""
Group: 4
Name: Esther Dick, Maeve Florian, Marjan Habib
Date: 11/23/2026
Course: CSC-157
Lab: Group 
Program Description: A personalized coffee and tea recommendation program for the terminal. The user answers questions about their beverage preferences, and the program recommends coffee or tea selections based on their answers.
"""

#============================================================================================================================================
#ESTHER: Classes & Data
#============================================================================================================================================

from beverage_menu import beverage_menu

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

# Build a list of Beverage objects from the menu entries.
beverages = []
for entry in beverage_menu:
    beverage = Beverage(
        entry["name"],
        entry["beverage_type"],
        entry["flavor"],
        entry["sweetness"],
        entry["bitterness"],
        entry["caffeine"],
        entry["temperature"],
    )
    beverages.append(beverage)




#============================================================================================================================================
#MARJAN: Recommendation Logic System (Decisions & Loops)
#============================================================================================================================================

 LEVELS = ["low", "moderate", "high"]

VALID_CHOICES = {
    "type": ["coffee", "tea"],
    "temperature":["hot", "iced"],
    "caffeine": LEVELS,
    "sweetness": LEVELS,
    "bitterness": LEVELS,
    "flavor":["vanilla","chocolate", "caramel", "fruity", "spiced", "roasted", "creamy", "malty", "nutty", "citrus", "floral", "grassy", "mint", "tart"],
}


def get_valid_input(prompt, valid_options): #this'll be used to keep asking the user until they provide us with a valid option 
    while True:
        answer = input(prompt).strip().lower()
        if answer in valid_options:
            return answer
        print("INVALID CHOICE! Please enter one of: " + ", ".join(valid_options))


def get_valid_yes_no(prompt): #this'll be used to ask a yes/no question until the user provides a valid answer (Return True/Flase)
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please Enter 'y' or 'n'")



















































