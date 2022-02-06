A simple program to store Business Contacts

The application presented here, written in python, will allow the user to input, search and alphabetically sort basic business contact details (5 records). The application has the following fundamental features:

1. Presents a menu to the user and asks the user to select what they would like to do from 5 options.
2. Option 1 prompts the user to input 5 separate contact records, consisting of name, phone number and company and stores these in a list ([]contact1, []contact2 etc.) using the append method. 
3. Using the append method, these individual sublists are then stored into one 'master list' as a 2-dimensional array ('[]master_contact_list'). 
4. The individual contact records and the master contact list is printed to the console to confirm to the user that the records have been stored correctly.
5. Selecting option 2 will sort the records alphabetically by first name. The sorted contacts are printed to the console.
6. Selecting option 3 allows the user to search the contact list based on the name within a record. 
7. Selecting option 4 prints the master contact list and then allows the user to delete a record, based on it's number (1,2,3,4 or 5), which the user must input. It prints the list again without the selected record.

INSTRUCTIONS to execute the code:
On first execution of the code, the program will not function if the user does not select option 1 and enter 5 contact details, before the users can execute any of the further options 2, 3, 4, or 5. If the user wishes to stop the program, they must select option 5. For the search funtion, the user must input the name exactly as the contactdata is entered as strings and strings are case sensitive in Python.

TESTING STRATEGY (Manual Testing):
1. On selection of option 1 in the user menu, following data input, the tester should verify contacts are correctly allocated to the sublists ([]contact1, []contact2 etc.) and the []contact_master_list and are printed to the screen.
2. On selection of option 3, the tester should try entering a false search term (string), a partly false search term (i.e. mix of upper and lower case) and a number. Each of these should trigger a Boolean false result.
3. On selection of option 4, the tester should try a number greater than 5 or a letter. In these cases, the program should ask continue to ask the user for the index number of the record they would like to delete (1 = [0],2 = [1], 3 = [2], 4 = [3], 5 = [4]).


AMMENDMENTS/ IMPROVEMENTS required:
- Sorted lists favour uppercase over lower case, so if one record is written beginning with a lower case letter it will appear at the end of the list

Resources used:

    - For help on building menus:

    https://stackoverflow.com/questions/19964603/creating-a-menu-in-python

    https://gist.github.com/ericball1/81203cd5c56cd3ea9ad4

    - For help on building and structuring code in relation to creating the initial contacts and the contact master list:

    https://gist.github.com/ericball1/81203cd5c56cd3ea9ad4

    https://www.delftstack.com/howto/python/list-of-lists-in-python/

    https://colab.research.google.com/drive/1fW6-ztQFsfn6IxFTJdGjztnoxjCEvfnh?usp=sharing

    - For help with sorting lists within lists:

    https://www.delftstack.com/howto/python/sort-list-of-lists-in-python/
    
    - For help with if/elif/else statements:
    https://www.datacamp.com/community/tutorials/elif-statements-python?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=16084198552&utm_adgroupid=&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=x&utm_adpostion=&utm_creative=&utm_targetid=&utm_loc_interest_ms=&utm_loc_physical_ms=9062727&gclid=Cj0KCQiAgP6PBhDmARIsAPWMq6lrm1Es4g9BC47mn39lq1b7xBpSR6EpVOZk9ZA-EIftlLfjZ770xWoaAiBlEALw_wcB

    




