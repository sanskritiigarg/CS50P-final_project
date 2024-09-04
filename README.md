# Match a Date
#### Video Demo: <https://youtu.be/UUVqpSF9A2Y>

## Description:
This program takes a command line argument of an input and a output csv file. 
The input CSV file should have 4 attributes - Name, Gender, Email, Preference(gender). 
The output CSV will contain a randomized match of each candidate given in the input with other candidates, based only on their gender and gender preference. It will have 4 attributes, ie, names and emails of both entries.
If there are no matches of a candidate, they will be printed in a table.
The program will also prompt the user if they want a matched table printed. The user can reply as per instructions and then, input a valid table format.

## Libraries:
**sys**: To take command line arguments.

**csv**: To read and write files.

**random**: To choose a random match for each candidate.

**tabulate**: To create table for matched and unmatched candidates.

**pytest**: to test the functions made inside the project.
## Note:
This program only supports the following gender:

'male',
'female'

This program only supports the following gender preferences:

'male',
'female',
'male/female'

