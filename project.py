import sys
import random
import csv

def main():
    infile, outfile = parse_args(sys.argv)
    males, females, bi = map(list, ([],)*3)
    with open(infile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['preference'] == 'male/female':
                bi.append(row)  
            elif row['gender'] == 'female':
                females.append(row)
            else:
                males.append(row)
    output_csv(outfile, females, males, bi)
    


def parse_args(args):
    if 1 < len(args) <= 3:
        outfile = args[2] if len(args) == 3 else 'match.csv'
        return args[1], outfile
    else:
        sys.exit('Usage: python project.py input_file [output_file]')

def output_csv(outfile, females, males, bi):
    with open(outfile, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['match', 'match_email', 'matched', 'matched_email'])
        writer.writeheader()
        for b in bi:
            bi.remove(b)
            match = random.choice([m for m in bi])
            writer.writerow({'match': b['name'], 'match_email': b['email'], 'matched': match['name'], 'matched_email': match['email']})
        for female in females:
            if female['preference'] == 'male':
                match = random.choice([m for m in males if female['gender'] == m['preference']])
                males.remove(match)
            if female['preference'] == 'female':
                females.remove(female)
                match = random.choice([f for f in females if female['gender'] == f['preference']])
                females.remove(match)
            writer.writerow({'match': female['name'], 'match_email': female['email'], 'matched': match['name'], 'matched_email': match['email']})
        for male in males:
            if male['preference'] == 'male':
                males.remove(male)
                match = random.choice(males)
            writer.writerow({'match': male['name'], 'match_email': female['email'], 'matched': match['name'], 'matched_email': match['email']})



if __name__ == "__main__":
    main()