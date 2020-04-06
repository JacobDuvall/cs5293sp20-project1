# cs5293sp20-project1
# Author: Jacob Duvall


# Description:
This program takes a text file and redacts sensitive information from the original file in a new redacted file. Some of this sensitive information can be things like names, dates, genders, and specific concepts. Doing these redactions by hand can be difficult and take time. This program automates that task.


# Process:
The process of the code is outlined and explained as follows:
A user passes in an argument into the terminal via the command:

python main.py --input demo_files/JimWalmsley.txt --output demo_files_redacted/ --names --genders --dates --concept state --stats stdout
OR
pipenv run python main.py --input demo_files/JimWalmsley.txt --output demo_files_redacted/ --names --genders --dates --concept state --stats stdout

WHERE the arguments are defined as:
--input: a glob of files to be redacted
--output: the directory where redactions will be made
--names: flag that takes no arguments to redact all names
--genders: flag that takes no arguments to redact all genders
--dates: flag that thakes no arguments to redact all dates
--concept: flag that can take a list of arguments with concepts to be redacted
--stats: flag that takes either "stderr", "stdout", or a file location to write stats file

With the command passed, the program cleans the files located in the input glob. 

Clean files manages the process by extracted all files from the glob and looping through each file. For each individual file, the process checks for the flags that are turned on. 

If the names flag is turned on, then all names are redacted using a stanford model for name entity recognition.
If the genders flag is turned on, then all genders are redacted by comparing the words of the document with gender words I found online.
If the dates flag is turned on, then all dates are redacted by searching the document for dates using the search_dates function from dateparser.
If the concepts flag is turned on, then all concepts related to the concept all redacted by using the synonym of all words specified.
If the stats flag is turned on, then the stats of the removed words are all formattted in a dictionary and they are shown via stderr, stdout, or written to a file for storage. 

# How To Run:
 From terminal, run via: python main.py --input <glob file> --output <directory> --names --genders --dates --concept <[list of concepts]> --stats <stdout,stderr,file_location/name>
  where names, genders, dates, concept, and stats are optional
 
 Some examples of this look like: 
 - python main.py --input demo_files/JimWalmsley.txt --output demo_files_redacted/ --names --genders --dates --concept state --stats stdout
- python main.py --input demo_files/JimWalmsley.txt --output demo_files_redacted/ --names
- python main.py --input demo_files/JimWalmsley.txt --output demo_files_redacted/ --names --stats stderr
 
 # Test File:
 My code has a test file called test_functions. 
 The test file tests that names, genders, dates, and concepts are all working at they should.
 
 To run the test file, execute command: pipenv run python -m pytest.
 
 ### Summary of all functions:
 #### main.py
 ##### main(arguments)
 - arguments from terminal
 * This function passes into project_1 and controls the workflow.
 
 #### project_1.py
 #### clean_files(arguments)
 - arguments from terminal
 * Takes arguments from terminal; Downloads nltk files; controls stats; collects all files using glob; cleans the files;
 
 #### download_nltk_stuff
 * These are nltk models necessary to run the program
