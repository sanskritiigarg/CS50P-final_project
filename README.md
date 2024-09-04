# Match a Date
#### Video Demo: <https://youtu.be/UUVqpSF9A2Y>

## Description:
 It is a program that takes a .csv file of candidates and outputs randomly matched .csv file, based on their gender and gender preference.
This program takes a command line argument of an input and a output csv file. 
The input CSV file should have 4 attributes - Name, Gender, Email, Preference(gender). 
The output CSV will contain a randomized match of each candidate given in the input with other candidates. It will have 4 attributes, ie, names and emails of both entries.
If there are no matches of a candidate, they will be printed in a table.
The program will also prompt the user if they want a matched table printed. The user can reply as per instructions and then, input a valid table format.

## Libraries:
**sys**: To take command line arguments.

**csv**: To read and write files.

**random**: To choose a random match for each candidate.

**tabulate**: To create table for matched and unmatched candidates.

**pytest**: to test the functions made inside the project.

## Usage:
**Command-line arguments** - Only 2 arguments are to be given on command line - input_CSV, output_CSV

**Parsing the arguments** - The arguments are parsed in parse_args() function. If there are less or more than 2 arguments, the following usage message is printed

    Usage: python project.py input_file output_file
    
  If either of the arguments do not have .csv extension, the following message is printed
  
    Only .csv files are supported.

**Display matched table** - The user is asked if they want a table of matched candidates. The answer is asked as 'Y' or 'N'. It is case insensitive.

    Do you want to output matched table in the terminal? Type 'Y' or 'N': 

  *If yes* - Table format is asked, which is further checked by check_format().

    Enter Table format: 

  If the table format is valid, then the table() function will be called. Otherwise, the table format will be asked repeatedly until you interrupt it with Ctrl+C.

**Testing the project** - Run the following command in the terminal.

    pytest project.py

## How the program works?
The program reads the input file. It divides the candidates in the file into 5 different lists as per their gender and preference.

The output file is overwritten or a new file is created. The matched candidates are written in the file as per the following attributes: 
  match, match_email, matched, matched_email

The matches between candidates are made randomly using random library. Matches between two different was made within the main function. Matches among candidates in same list were made using the reusable function match(). 

Candidates who could not be matched with a suitable candidate are added to Unmatched list. This list is printed as a table in the end. The table format, by default, is 'grid' unless a format is specified.

If the user wants a table and has input a correct table format, then a table of the matched candidates is displayed in the terminal. It is of the specified format. If there are any unmatched candidates, they will be displayed in a table even if the user does not want a table of matched candidates.

## TODO:
#### Download
Download the Repository through Clone Repository or Download Zip
```
git clone (https://github.com/sanskritiigarg/CS50P-final_project.git)
```
#### Installation
After download, go to `cmd` and navigate to the project folder directory.
```
cd CS50P-final_project
``` 
Use [pip](https://pip.pypa.io/en/stable/) to install needed libraries.
```
$ pip install -r requirements.txt
```

## Note:
This program only supports the following gender:

'male',
'female'

This program only supports the following gender preferences:

'male',
'female',
'male/female'

All the names used in the program are fictional. I own no rights to them.
