import json
import csv

with open("names.json") as file:
    names = json.load(file)

with open("scores.json") as file:
    scores = json.load(file)

absent = [["students with attendance shortage", "", "", "", "", ""]]
present_scores = [["ID", "NAME", "MATH", "PHY", "CS", "TOTAL"]]

for key in names:
    row = [key, names[key]]
    if key in scores:
        row.extend([scores[key]["math"], scores[key]["phy"], scores[key]["cs"], scores[key]["math"]+scores[key]["phy"]+scores[key]["cs"]])
        present_scores.append(row)
    else:
        row.extend(["" for i in range(len(present_scores[0]) - len(row))])
        absent.append(row)

with open("report.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(present_scores)
    writer.writerows(absent)
