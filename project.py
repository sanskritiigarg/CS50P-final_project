import sys
import random
import csv
from tabulate import tabulate

UNMATCHED = []

def main():
    infile, outfile= parse_args(sys.argv)
    sf, sm, bi, ga, lb = map(list, ([],)*5)
    
    #reading csv file
    try:
        with open(infile) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['preference'] == 'male/female':
                    bi.append(row)
                if row["preference"] == "male" and row["gender"] == "female":
                    sf.append(row)
                if row["preference"] == "female" and row["gender"] == "male":
                    sm.append(row)
                if row["preference"] == "male" and row["gender"] == "male":
                    ga.append(row)
                if row["preference"] == "female" and row["gender"] == "female":
                    lb.append(row)
    except FileNotFoundError:
         sys.exit("Couldn't read CSV file.")

    #writing output csv
    with open(outfile, 'w+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['match', 'match_email', 'matched', 'matched_email'])
        writer.writeheader()
        writer.writerows(match(bi))
        try:
            for f in sf:
                try:
                    matched = random.choice(sm)
                    writer.writerow({"match": f["name"], "match_email": f["email"], "matched": matched["name"], "matched_email": matched["email"]})
                except:
                    UNMATCHED.append(sm)
        except:
            UNMATCHED.append(f)
        writer.writerows(match(lb))
        writer.writerows(match(ga))

        readers = csv.DictReader(file)
        for row in readers:
            print(row)
        writer.writerows([unmatch for unmatch in UNMATCHED])
    


def parse_args(args):
    if not (len(args) == 3):
        sys.exit("Usage: python project.py input_file output_file")
    if ".csv" not in args[1] or ".csv" not in args[2]:
         sys.exit("Only .csv files are supported.")
    return args[1], args[2]

def match(candidates):
    random.shuffle(candidates)
    n = len(candidates)
    matched = []
    if n % 2 == 1:
        i = random.randint(0, n - 1)
        UNMATCHED.append(candidates[i]) 
        candidates.pop(i) 
    for i in range(0,n, 2):        
        matched.append(dict({"match": candidates[i]["name"], "match_email": candidates[i]["email"], "matched": candidates[i + 1]["name"], "matched_email": candidates[i + 1]["email"]}))
    return matched

def table(outfile, format):
    if input("Do you want to output matched table in the terminal? Type 'Yes' or 'No': ").lower() == "yes":
        while True:
            try:
                format = input("Enter Table format: ").lower()
                if check_format(format) == True:
                    return True
            except KeyboardInterrupt:
                sys.exit("\nProgram Exited")
    

def check_format(format):
    formats = ["plain", "simple", "github", "grid", "simple_grid", "rounded_grid", "heavy_grid", "mixed_grid", "textile"
                "double_grid", "fancy_grid", "outline", "simple_outline", "rounded_outline", "heavy_outline", "mixed_outline"
                "double_outline", "fancy_outline", "pipe", "orgtbl", "asciidoc", "jira", "presto", "pretty", "psql", "tsv"
                "rst", "mediawiki", "moinmoin", "youtrack", "html", "unsafehtml", "latex", "latex_raw", "latex_booktabs", "latex_longtable"]
    if format in formats:
        return True
    else:
        return False

if __name__ == "__main__":
    main()