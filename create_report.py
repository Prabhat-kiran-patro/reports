import json
import csv

class Files_Operator:

    @staticmethod
    def fetch_json(file_name):
        with open(file_name) as file:
            return json.load(file)
    
    @staticmethod
    def write_to_csv(file_name, data):
        with open(file_name, "w") as file:
            writer = csv.writer(file)
            writer.writerows(data)

class Formatter:

    @staticmethod
    def set_header(arr, *args):
        arr.append(list(args))
    
    @staticmethod
    def get_scores(val):
        total = val["math"] + val["phy"] + val["cs"]
        return [val["math"], val["phy"], val["cs"], total]

    @staticmethod
    def to_rows(names, scores, present, absent):
        for id, name in names.items():
            row = [id, name]
            if id not in scores:
                absent.append(row)
            else:
                row.extend(Formatter.get_scores(scores[id]))
                present.append(row)

def main():
    # Load data
    names = Files_Operator.fetch_json("names.json")
    scores = Files_Operator.fetch_json("scores.json")
    # Format data
    present = []
    absent = []
    Formatter.set_header(present, "ID", "NAME", "MATH", "PHYSICS", "CS", "TOTAL")
    Formatter.set_header(absent, "ID", "NAME")
    Formatter.to_rows(names, scores, present, absent)
    # Generate reports
    Files_Operator.write_to_csv("report1.csv", present)
    Files_Operator.write_to_csv("report2.csv", absent)

    print("Reports generated successfully!")

if __name__ == "__main__":
    main()
