A simple program to store Business Contacts

The application presented here, written in python, will allow the user to input, search and alphabetically sort basic business contact details (5 records). The application has the following fundamental features:

1. Presents a menu to the user and asks the user to select what they would like to do from 5 options.
2. Option 1 prompts the user to input 5 separate contact records, consisting of name, phone number and company and stores these in a list ([]contact1, []contact2 etc.) using the append method. 
3. Using the append method, these individual sublists are then stored into one 'master list' as a 2-dimensional array ('[]master_contact_list'). 
4. The individual contact records and the master contact list are printed to the console to confirm to the user that the records have been stored correctly.
5. Selecting option 2 will sort the records alphabetically by first name. The sorted contacts are printed to the console.
6. Selecting option 3 allows the user to search the contact list based on the name within a record and confirms if that record is present. 
7. Selecting option 4 prints the master contact list and then allows the user to delete a record, based on it's number (1,2,3,4 or 5), which the user must input. It prints the list again without the selected record.

INSTRUCTIONS to execute the code:
On first execution of the code, the program will not function if the user does not select option 1 and enter 5 contact details, before the users can execute any of the further options 2, 3, 4, or 5. If the user wishes to stop the program, they must select option 5. For the search funtion, the user must input the name exactly as the contact data is entered as strings and strings are case sensitive in Python.

TESTING STRATEGY (Manual Testing):
1. On selection of option 1 in the user menu, following data input, the tester should verify contacts are correctly allocated to the sublists ([]contact1, []contact2 etc.) and the []contact_master_list and are printed to the screen.
2. On selection of option 3, the tester should try entering a false search term (string), a partly false search term (i.e. mix of upper and lower case) and a number. Each of these should trigger a Boolean false result.
3. On selection of option 4, the tester should try a number greater than 5 or a letter. In these cases, the program should continue to ask the user for the number of the record they would like to delete (1 = [0],2 = [1], 3 = [2], 4 = [3], 5 = [4]).

THE APPROACH to writing this program.

I began by implementing a user menu using while-if-elif loop, as modelled by Ball, E (2015). This approach allowed me to write the program code nested within this loop structure, whilst always returning to the main menu on completion of each function. The next stage was to build the contact book based on user input which involved a 2 stage approach: Using the .append function in python allows the program to build each individual contact as a list and then append these as sublists to a master list (Anon, DelftStack, 19 Nov. 2021). Following this I could begin to write code which would allow the user to manipulate the inputted records. I found that using a simple alphabetic sort function would be ideal for this exercise (Anon, DelftStack, 2 June 2021), as I wanted to sort the records by name only. In order to build the search funtion, I configured the program to initially set the found variable to False and then, using a for-if loop, to iterate over the sub-list items which I wanted to match with the user input as the condition for triggering the found variable to be True (Sotiriadis, 2022). Finally the delete function was written as a nested if-elif statement using the .pop function to delete records selected by the user according to their list index (Anon - W3schools).


AMMENDMENTS/ IMPROVEMENTS required:
- Sorted lists favour uppercase over lower case, so if one record is written beginning with a lower case letter it will appear at the end of the list. This should be addressed as an improvement.
- Better formatting of the printed 'master list' - i.e. print each contact labelled correctly and on separate lines
- The search function could trigger subsequent options, after finding the entry (e.g. ask for modifications or deletion).
- The search funtion could be possible by company name, phone number, or partial entries of any data record.


Resources used for writing code:


Ball, E. (2015). ericball1/Phonebook.py. 11 November. Github Gist. [online]. [Accessed: 04.02.22]. Available from: https://gist.github.com/ericball1/81203cd5c56cd3ea9ad4

Anon (2021). Create List of Lists in Python. 19 February. DelftStack. [online]. [Accessed: 04.02.22]. Available from: https://www.delftstack.com/howto/python/list-of-lists-in-python/

Anon (2021). Sort a List of Lists in Python. 2 June. DelftStack. [online]. [Accessed: 06.02.22]. Available from: https://www.delftstack.com/howto/python/sort-list-of-lists-in-python/

Sotiriadis, S. (2022). LCS Seminar 6.ipynb. [online - google drive shared document]. Available from: https://colab.research.google.com/drive/1fW6-ztQFsfn6IxFTJdGjztnoxjCEvfnh?usp=sharing

Anon (unknown). Python - Remove List Items. w3schools. [online]. [Accessed: 06.02.22]. Available from: https://www.w3schools.com/python/python_lists_remove.asp

DataCamp Team (2020). if…elif…else in Python. 25 June. [online]. [Accessed: 07.02.22]. Available from:https://www.datacamp.com/community/tutorials/elif-statements-python?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=16084198552&utm_adgroupid=&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=x&utm_adpostion=&utm_creative=&utm_targetid=&utm_loc_interest_ms=&utm_loc_physical_ms=9062727&gclid=Cj0KCQiAgP6PBhDmARIsAPWMq6lrm1Es4g9BC47mn39lq1b7xBpSR6EpVOZk9ZA-EIftlLfjZ770xWoaAiBlEALw_wcB

    




