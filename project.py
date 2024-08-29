import sys
import random
import csv

UNMATCHED = []

def main():
    infile, outfile= parse_args(sys.argv)
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

    #tabulate the csv    
    if input("Do you want to output matched table in the terminal? Type 'Yes' or 'No': ").lower() == 'yes':
        format = check_format(input("Enter Table format: ").lower())
        table(outfile, format)

def parse_args(args):
    if not (len(args) == 3):
        sys.exit('Usage: python project.py input_file output_file')
    if ".csv" not in args[1] or ".csv" not in args[2]:
         sys.exit("Only .csv files are supported.")
    return args[1], args[2]

def match(candidates):
     ...

def table(outfile, format):
    return True
    

def check_format(format):
    formats = ["plain", "simple", "github", "grid", "simple_grid", "rounded_grid", "heavy_grid", "mixed_grid", "textile"
                "double_grid", "fancy_grid", "outline", "simple_outline", "rounded_outline", "heavy_outline", "mixed_outline"
                "double_outline", "fancy_outline", "pipe", "orgtbl", "asciidoc", "jira", "presto", "pretty", "psql", "tsv"
                "rst", "mediawiki", "moinmoin", "youtrack", "html", "unsafehtml", "latex", "latex_raw", "latex_booktabs", "latex_longtable"]
    while True:
        if format in formats:
            return format
        elif input("Table format is wrong. Do you want to Re-enter? Type 'Yes' or 'No': ").lower() != "yes":
            sys.exit("Program exited.")

if __name__ == "__main__":
    main()