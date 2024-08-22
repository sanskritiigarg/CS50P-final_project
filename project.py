import sys
import csv

def main():
    infile, outfile = parse_args(sys.argv)
    males, females = map(list, ([],)*2)
    with open(infile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            males.append(row) if row['gender'] == 'male' else females.append(row)
    
    print(males)
    print(females)

def parse_args(args):
    if 1 < len(args) <= 3:
        outfile = args[2] if len(args) == 3 else "match.csv"
        return args[1], outfile
    else:
        sys.exit("Usage: python final_project.py input_file [output_file]")

if __name__ == "__main__":
    main()