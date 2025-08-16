import report_package.file_utilities as futils

def total(scores):
    sum = 0
    for val in scores.values():
        sum += val
    return sum
    
def avg(scores):
    return round(total(scores) / len(scores), 2)

def format(header):
    names = futils.fetch_json("data/names.json")
    scores = futils.fetch_json("data/scores.json")
    data = [header]
    for key in names:
        row = []
        for col in header:
            if col == "id":
                row.append(key)
            elif col == "name":
                row.append(names[key])
            elif scores.get(key):
                if col == "total":
                    row.append(total(scores.get(key)))
                elif col == "avg":
                    row.append(avg(scores.get(key)))
                else:
                    row.append(scores.get(key).get(col))
            else:
                row.append("-")
            
        data.append(row)
    return data