mainMenu = True

while mainMenu:

    print('To add contacts, select 1')
    print('To sort alphabetically by name, select 2')
    print('To search for a contact by name, select 3')
    print('To delete a contact record, select 4')
    print('To end the program, select 5')

    select_function = input("Select a function: ")

    if select_function == '1':

        # Function 1: get user input to build phone book
        # enter first contact
        print('Enter your first contact')
        full_name1 = input("Full Name: ")
        company1 = input("Company: ")
        mobile_number1 = input("Mobile Number: ")
        print('Thank you for entering your first contact')

        # create the first contact as a list
        contact1 = []

        contact1.append(full_name1)
        contact1.append(company1)
        contact1.append(mobile_number1)

        # enter contact 2
        print('Enter your second contact')
        full_name2 = input("Full Name: ")
        company2 = input("Company: ")
        mobile_number2 = input("Mobile Number: ")
        print('Thank you for entering your second contact')

        # assign contact 2 to a list
        contact2 = []

        contact2.append(full_name2)
        contact2.append(company2)
        contact2.append(mobile_number2)

        # enter contact 3
        print('Enter your third contact')
        full_name3 = input("Full Name: ")
        company3 = input("Company: ")
        mobile_number3 = input("Mobile Number: ")
        print('Thank you for entering your third contact')

        # assign contact 3 to a list
        contact3 = []

        contact3.append(full_name3)
        contact3.append(company3)
        contact3.append(mobile_number3)

        # enter contact 4
        print('Enter your fourth contact')
        full_name4 = input("Full Name: ")
        company4 = input("Company: ")
        mobile_number4 = input("Mobile Number: ")
        print('Thank you for entering your fourth contact')

        # assign contact 4 to a list
        contact4 = []

        contact4.append(full_name4)
        contact4.append(company4)
        contact4.append(mobile_number4)

        # enter contact 5
        print('Enter your fifth contact')
        full_name5 = input("Full Name: ")
        company5 = input("Company: ")
        mobile_number5 = input("Mobile Number: ")
        print('Thank you for entering your fourth contact')

        # assign contact 5 to a list
        contact5 = []

        contact5.append(full_name5)
        contact5.append(company5)
        contact5.append(mobile_number5)

        # TEST 1: demonstrates that contacts have been entered correctly by printing each original list
        print('Contact 1 is: ' + str(contact1))
        print('Contact 2 is: ' + str(contact2))
        print('Contact 3 is: ' + str(contact3))
        print('Contact 4 is: ' + str(contact4))
        print('Contact 5 is: ' + str(contact5))

        # using the append function, add each list to a master list
        master_contact_list = []

        master_contact_list.append(contact1)
        master_contact_list.append(contact2)
        master_contact_list.append(contact3)
        master_contact_list.append(contact4)
        master_contact_list.append(contact5)

        # TEST 2: print the master contact list
        print('Your full list of contacts is:')
        print(master_contact_list)

    elif select_function == '2':
        # FUNCTION 2: Sort the master list by name of each record
        master_contact_list.sort()
        print("Your contacts have been sorted alphabetically by name: % s" %
              (master_contact_list))

    elif select_function == '3':
        # FUNCTION3: Search for a contact by name
        search_name = input('Enter name to search: ')
        for search_name in master_contact_list:
            found = False
            for search_name in master_contact_list:
                if full_name1[0] or full_name2[0] or full_name3[0] or full_name4[0] or full_name5[0] == search_name:
                    found = True

        print(search_name, found)

    # FUNCTION 4: Delete record and print the list
    elif select_function == '4':
        print(master_contact_list)

        delete_contact = input(
            'Would you like to deleted contact 1, 2, 3, 4 or 5? Type the number to delete: ')
        if delete_contact == '1':
            master_contact_list.pop(0)

        elif delete_contact == '2':
            master_contact_list.pop(1)

        elif delete_contact == '3':
            master_contact_list.pop(2)

        elif delete_contact == '4':
            master_contact_list.pop(3)

        elif delete_contact == '5':
            master_contact_list.pop(4)

        print(master_contact_list)

    elif select_function == '5':
        break
