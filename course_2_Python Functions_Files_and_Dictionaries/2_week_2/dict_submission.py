"""The dictionary travel contains the number of countries within each continent that Jackie has traveled to
   . Find the total number of countries that Jackie has been to, and save this number to the variable name
  total. Do not hard code this!"""

travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
total=0
for coutries in travel:
    total+=travel[coutries]
