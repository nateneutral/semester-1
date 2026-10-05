# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music = {
        "Counting Crows": [("August And Everything After", 1993),("Recovering The Satellites",1996),("This Desert Life",1999)],
        "Sordid Humor": [("Tony Don't",1989),("Light Music For Dying People",1994)],
        "Geese": [("3D Country",2023),("Getting Killed",2025)],
        "The Rolling Stones":["Let it Bleed","Aftermath","Goat's Head Soup"]
}
# Pretty-print the data structu)re
pprint(music)
# Display details of one album recorded by a specific artist
print(music.get("Geese")[0])