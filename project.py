import sys
import random
import csv

UNMATCHED = []

def main():
    infile, outfile = parse_args(sys.argv)
    males, females, bi = map(list, ([],)*3)
    
    #reading csv file
    try:
        with open(infile) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['preference'] == 'male/female':
                    bi.append(row)  
                elif row['gender'] == 'female':
                    females.append(row)
                else:
                    males.append(row)
    except FileNotFoundError:
         sys.exit("Couldn't read CSV file.")

    #writing output csv
    with open(outfile, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['match', 'match_email', 'matched', 'matched_email'])
        writer.writeheader()
        matches = match(bi)

        for female in females:
            if female['preference'] == 'male':
                match = random.choice([m for m in males if female['gender'] == m['preference']])
                males.remove(match)
        if female['preference'] == 'female':
            matches = match(females)
        writer.writerow({'match': female['name'], 'match_email': female['email'], 'matched': match['name'], 'matched_email': match['email']})

        for male in males:          
            matches = match(males)    

def parse_args(args):
    if not (1 < len(args) <= 3):
        sys.exit('Usage: python project.py input_file [output_file]')
    if ".csv" not in args[1] or ".csv" not in args[2]:
         sys.exit("Only .csv files are supported.")
    return args[1], args[2] if len(args) == 3 else "matches.csv"

def match(candidates):
     ...


if __name__ == "__main__":
    main()