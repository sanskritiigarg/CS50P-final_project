import sys
import random
import csv
from tabulate import tabulate

UNMATCHED = []

def main():
    infile, outfile= parse_args(sys.argv)
    sf, sm, bi, ga, lb = map(list, ([],)*5)
    
    # reading csv file
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

    # writing output csv
    with open(outfile, 'w+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['match', 'match_email', 'matched', 'matched_email'])
        writer.writeheader()
        writer.writerows(match(bi))
        for f in sf:
            try:
                matched = random.choice(sm)
                writer.writerow({"match": f["name"], "match_email": f["email"], "matched": matched["name"], "matched_email": matched["email"]})
                sm.remove(matched)
            except:
                UNMATCHED.append(f)
        if sm != []:
            for m in sm:
                UNMATCHED.append([m])
        writer.writerows(match(lb))
        writer.writerows(match(ga))

    # create a table
    format = ""
    if input("Do you want to output matched table in the terminal? Type 'Y' or 'N': ").lower() == "y":
        while True:
            try:
                format = input("Enter Table format: ").lower()
                if check_format(format) == True:
                    with open(outfile) as file:
                        file.seek(0)
                        reader = csv.reader(file)
                        tables = [row for row in reader]
                    table(tables, format)
                    break
            except KeyboardInterrupt:
                    break
    
    if UNMATCHED != []:
        header = UNMATCHED[0].keys() 
        rows = [x.values() for x in UNMATCHED]
        print("\nUnmatched candidates:\n")
        print(tabulate(rows, headers=header, tablefmt=format if format != "" else "grid"))
    else:
        print("\nNo unmatched candidates. All matched!")


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
        n -= 1
        i = random.randint(0, n)
        UNMATCHED.append(candidates[i]) 
        candidates.pop(i)
    # base case if only two candidates left
    if n == 2:
        matched.append(dict({"match": candidates[0]["name"], "match_email": candidates[0]["email"], "matched": candidates[1]["name"], "matched_email": candidates[1]["email"]}))
    else:
        for i in range(0,n, 2):        
            matched.append(dict({"match": candidates[i]["name"], "match_email": candidates[i]["email"], "matched": candidates[i + 1]["name"], "matched_email": candidates[i + 1]["email"]}))
    return matched

def table(tables, format):
    print("\n", tabulate(tables[1:], headers=["name", "gender", "email", "preference"], tablefmt=format))
    return True
        
    
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