# Python-challenge
This set of four Python scripts are basic examples of the Data Analysis workflow:
1) Read data from input files (csv/txt)
2) Analyse data (looping through rows, computing and summarizing)
3) Write results into output files (csv/txt)
4) Print results to terminal

## 1. PyBank
This script reads financial records from a CSV file with the following structure:
| Date | Profit/Losses
| --- | --- 

Using a `for` loop, the script counts the number of months, computes the sum of Profit/Losses while, and computes the Profit/Losses change for each month (in relation to the last month) and stores it in a dictionary: *{month (key) : P/L change (value)}*.

To summarize the Profit/Losses change information, the script computes the *P/L average change* and gets the *Greatest increase in Profits* and the *Greatest increase in Profits* (or Greatest increase in Losses) over the entire period.

At the end, the script generates a report through a function and writes the report to an output file (txt) and print it to the terminal.

## 2. PyPoll
This script reads election data from a CSV file with the following structure:
| Voter ID | County | Candidate
| --- | --- | ---

Using a `for` loop, the script stores (and summarizes) the election data in a dictionary: *{candidate (key) : number of votes (value)}*. If a new candidate is detected, it adds the name as a key and counts the vote. If no new candidate is detected, it accumulates the vote for the existing one. After the loop is complete, the script computes the *Total number of votes* calling the `sum()` of votes (values) of all candidates.

The dictionary structure provides a simple way to generate the election results using *{key:value}* pairs to display the complete *List of candidates* who received votes, the *Percentage of votes* and the *Number of votes* each candidate won. The winner candidate is selected calling the `max()` and `get()` built-in functions.

At the end, the script generates a report through a function and writes the report to an output file (txt) and print it to the terminal.

## 3. PyBoss
This script reads employee data from a CSV file with the following structure: 
| Emp ID | Name | DOB | SSN | State
| --- | --- | --- | --- | ---

Using a `for` loop, the script converts and stores the data into lists according to a required format:
- The *Name* column is split into separate *First Name* and *Last Name* columns.
- The *DOB* data is re-written into *MM/DD/YYYY* format (converting from *YYYY-MM-DD*).
- The *SSN* data is re-written using asterisk (\*) character to hide the first five numbers from view.
- The *State* data is re-written two-letter abbreviations.

After setting a list for the formatted columns header, the script calls the `zip()` function to "lock" all lists together into tuples.
Finally, the script exports the formatted data to a CSV file using `csv.writer()` functions.

Note:
The *Python Dictionary for State Abbreviations* (https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5) is used for the *State* data conversion.

## 4. PyParagraph

RegEx










