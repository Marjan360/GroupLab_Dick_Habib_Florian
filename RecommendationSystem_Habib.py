"""
Name: Marjan Habib
Date: 11/27/2026
Course: CSC-157
Lab: Group (My Part)
Program Description: Build the recommendation system for the program.
"""  

#checklist:
#1. loop through the beverage list
#2. check for the type the user chose
#3. rank the matches by score 
#4. handle input validation 

VALID_CHOICES = {
    "type": ["coffee", "tea"],
    "taste":["sweet", "bitter", "mild"],
    "temperature":["hot", "iced"],
    "caffeine":["high", "moderate", "low"],
    "flavor":["vanilla","chocolate", "caramel", "fruit", "spice"],
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





def score_beverages(beverages, answers): #this'll score every beverage of the type the user chooses
    scored = []
    for beverage in beverages:
        if beverage.beverage_type == answers["type"]:
            matches = beverage.get_matches(answers)
            scored.append((beverage, matches, len(matches)))
    return scored   #this returns a list of (beverage, matches, score) tuples; we'll skip drink of other types entirely 


def rank_beverages(scored):  #this'll sort best score first; the ties are broken alphabetically
    return sorted(scored, key=lambda item: (-item[2], item[0].name))


def get_top_matches(beverages, answers):  #this'll return every beverage tied for the highest score (may be none, may be 2, so on and so forth)
    ranked = rank_beverages(score_beverages(beverages, answers))
    if not ranked:
        return[]

    best_score = ranked[0][2]
    top = []
    for item in ranked:
        if item[2] == best_score:
            top.append(item)
    return top


def get_more_matches(beverages, answers, how_many=3): #this is an EXPLORE MORE option where the next-best drinks that still match at least one preference are displayed
    ranked = rank_beverages(score_beverages(beverages, answers))
    if not ranked:
        return[]

    best_score = ranked[0][2]
    others = []
    for item in ranked:
        if item[2] < best_score and item[2] > 0:
            others.append(item)
    return others[:how_many]


def build_reason(matches): #this'll turn a list of matches preferences into a short sentence for display
    if not matches:
        return "It doesn't match your preference closely..."
    if len(matches) == 1:
        return "It matches your preference for " + matches[0] + "."
    return ("It matches your preference for "
            + ", ".join(matches[:-1]) + " and " +  matches[-1] + ".")




#self-testing
if __name__ ==  "__main__":


    class StubBeverage:
        def __init__(self, name, btype, taste, temp, caffeine, flavor):
            self.name = name
            self.beverage_type = btype
            self.taste, self.temp = taste, temp
            self.caffeine, self.flavor = caffeine, flavor


        def get_matches(self, answers):
            matches = []
            if self.taste == answers["taste"]:
                matches.append(self.taste)
            if self.temp == answers["temperature"]:
                matches.append(self.temp)
            if self.caffeine == answers["caffeine"]:
                matches.append(self.caffeine + " caffeine")
            if self.flavor == answers ["flavor"]:
                matches.append(self.flavor)
            return matches


    
    drinks = [
        StubBeverage("Hot Chamomile", "tea", "mild", "hot", "low", "fruit"),
        StubBeverage("Iced Black Tea", "tea", "bitter", "iced", "high", "fruit"),
        StubBeverage("Hot Vanilla Rooibos", "tea", "mild", "hot", "low", "vanilla"),
        StubBeverage("Mocha", "coffee", "sweet", "hot", "high", "chocolate"),
        StubBeverage("Espresso", "coffee", "bitter", "hot", "high", "spice"),
    ]
    answers = {"type": "tea", "taste": "mild", "temperature": "hot",
               "caffeine": "low", "flavor": "fruit"}



    #coffee is excluded when the user picks tea
    scored = score_beverages(drinks, answers)
    assert all(b.beverage_type == "tea" for b, _, _ in scored)

    #scores are all calc. correctly
    scores = {b.name: s for b, _, s in scored}
    assert scores["Hot Chamomile"] == 4
    assert scores["Hot Vanilla Rooibos"] == 3
    assert scores["Iced Black Tea"] == 1


    #hot, low-caff. tea needs to rank above iced, high-caff. tea
    names = [b.name for b, _, _ in rank_beverages(scored)]
    assert names.index("Hot Chamomile") < names.index("Iced Black Tea")


    #the ties produce multiple top matches
    answers_tie = dict(answers, flavor="chocolate")
    top = get_top_matches(drinks, answers_tie)
    assert{b.name for b, _, _ in top} == {"Hot Chamomile", "Hot Vanilla Rooibos"}

    #both types CAN BE recommended
    coffee_top = get_top_matches(drinks, dict(answers, type="coffee"))
    assert coffee_top and coffee_top[0][0].beverage_type == "coffee"


    #the EXPLORE MORE function should exclude top matches
    more = get_more_matches(drinks, answers)
    assert "Hot Chamomile" not in [b.name for b, _, _ in more]



    #ALAS!
    print("All recommender tests passed.")
    for b, m, s in get_top_matches(drinks, answers):
        print(f"Top match: {b.name} (score {s}) - {build_reason(m)}")


