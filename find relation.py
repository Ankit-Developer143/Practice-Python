dict = {
    "Darth Vader":"father",
    "Leia":"sister",
    "Han":"brother in law",
    "R2D2":"droid"


}

def relation_to_luke(name):
    name = dict.get(name)
    return("Luke, I am your {}." .format(name))

print(relation_to_luke("Leia"))

#op:-Luke i am your sister


#other Solutions
def relation_to_luke(name):
  return "Luke, I am your "+ {"Darth Vader":"father.","Leia":"sister.","Han":"brother in law.","R2D2":"droid."}[name]