
# Object Class --- Book

class Book:
    
    # Book Class Constructor Initialization
    def __init__(self, title, auth_name, genre, isbn_num, is_avail=True): 
        
        self.title = title          # Book's Title (String)
        self.auth_name = auth_name  # Author's Name (String)
        self.genre = genre          # Book's Genre (String)
        self.isbn_num = isbn_num    # Book's ISBN (string)
        self.is_avail = is_avail    # Book's Availability (bool)
    
    """ No Methods Required For This Class. """

      
    
# Object Class --- System User

class SystemUser:
    
    # System User Class Constructor Initialization
    def __init__(self, usr_name, usr_pass, isLogon=True, isAdmin=False):
        
        self.usr_name = usr_name  # User Name (string)
        self.usr_pass = usr_pass  # User's Oassword (string)
        self.islogon = isLogon    # Is User Currently Logged On? (bool)
        self.isAdmin = isAdmin    # Is User an Admin? (bool)
        
        self.details = {'Borrowed': [],
                        'Fines': 0,
                        'Overdue': [],
                        'Reserve': [],
                        'Wait': []}     # Dictionary Containing User's Account Details
        
    
    # System User Class Method --- Change Password
    def change_pass():
        
        pass_chk = input("Please Enter Your Current Password: ") # Security Check for User's Current Password
        
        while pass_chk != self.usr_pass:
            pass_chk = input("Incorrect Password. Please Enter Your Current Password: ") # Error-Catching for Invalid Password
        
        else:
            
            new_pass = input("Please Enter Your New Password: ") # User Enters New Password Upon Security Check
            self.usr_pass = new_pass                             # New Password is Applied to User
    
    # System User Class Method --- User Log Off
    def log_off():
        
        self.usr_islogon = False # Bool Switches for Break Condition
        
    





# Object Class --- Library Management System

class LibraryManagementSystem:
    
    def __init__(self):         # LMS Class Object Constructor Initialization
        
        self.usr_accounts = []  # List Containing All Known Registered Accounts
        self.logged_on = []     # List Containing All Currently Active Users
        
        
        self.lib_db = []       # List Simulating Library's Book Database
        
      
      
      
    
    def add_book(self):        # LMS Class Object Method --- Add Book to Database
        
        print()                
        title = input("Enter the Book's Title: ")       # User Input - Enter Book's Title (string)
        auth_name = input("Enter the Book's Author: ")  # User Input - Enter Book's Author (string)
        genre = input("Enter the Book's Genre: ")       # User Input - Enter Book's Genre (string)
        isbn_num = input("Enter the Book's ISBN #: ")   # User Input - Enter Book's ISBN (string)
        
        added_book = Book(title, auth_name, genre, isbn_num, is_avail=True) # New Book Object Created with User Input Data
        lms.lib_db.append(added_book)                                       # New Book Object Appended to Library's Book Database
    
    
    
    
    
    
    def del_book(self):       # LMS Class Object Method --- Delete Book from Database
        
        menu_counter = 1      # Menu Counter Initialized for Navigation/Selection
        
        print("------ LIBRARY BOOK LIST ------")   # Library Book List Header
        
        for book in lms.lib_db:                                # For-Loop Initialized: Iterating through Books in Database
            print(menu_counter, ".) ", book.title, sep = '')   # Each Book in Database Listed to User
            menu_counter += 1                                  # Menu Counter Incremented per Book Iteration
        
        book_sel = int(input("\nPlease Select the Book to Delete from Library: ")) # User Input - Integer for Menu Option Selection (Used for Index)
        book_sel -= 1                                                              # Selected Index is Adjusted for List Index Access
        
        del lms.lib_db[book_sel]                                                   # Index is used to Select Book for Deletion. Book is Deleted
        
        print("Book Deleted Successfully!")                                        # Confirmation Message Displayed to User
        
        
        
        
    
    def take_book(self):                                         # LMS Class Object Method --- User Taking Out Book to Borrow
        
        print("\n ------ LIBRARY'S AVAILABLE BOOKLIST ------ ")  # Library's Available Booklist Header
        
        menu_counter = 1                                         # Menu Counter Initialized for Navigation/Selection (Used for Index)
        
        for book in lms.lib_db:                                  # For-Loop Initialized: Iterating through Every Book in Library's Catalogue/Database
            
            if book.is_avail:                                                                                                 # If-Condition: If the Book is Available
                print(menu_counter, ".) ", book.title, ", Written By: ", book.auth_name, "| Genre: ", book.genre, sep = '')   # If Available: Book is Printed to User
            
            else:                                                                                                                                       # Else-Condition: If Book is NOT Available
                print(menu_counter, ".) ", book.title, ", Written By: ", book.auth_name, "| Genre: ", book.genre, " | ---NOT AVAILABLE--- ", sep = '')  # If Not: Book is Printed to User with Notice
            
            menu_counter += 1                                                         # Menu Counter increments by one every book.
            
        book_sel = int(input("\nWhich Book Would You Like to Take?: "))               # User Input - Integer for Menu Selection/Navigation
        
        while book_sel not in range(1, menu_counter):                                 # User Input Error-Catch: Ensuring User Inputs Integers in Range of Menu Selections
            book_sel = int(input("Invalid Selection. Please Select from the Menu."))  # User Input Error-Catch: Second Pass at Input
        
        book_sel -= 1                                                                 # Succesful Input: User's Input is adjusted for Index Positioning
        
        if lms.lib_db[book_sel].is_avail:                                             # If-Condition: If Selected Book is Available
        
            print("You Have Selected: ", lms.lib_db[book_sel].title, ", Written By: ", lms.lib_db[book_sel].auth_name, sep = '')  # Verifying Selected Book to User
            sel_chk = input("\nProceed to Take Out? (Y/N): ").upper()                                                             # User Verifies with Input (Y/N) = Yes or No
        
            if sel_chk == 'Y':                                                     # If-Condition: If User Verifies (Yes/Y)
            
                user_basic.details['Borrowed'].append(lms.lib_db[book_sel])        # User's Detail Dictionary at 'Borrowed' Key is Updated with User's Selected Book
                lms.lib_db[book_sel].is_avail = False                              # Book's Availability is Updated to LMS Book Database
        
            elif sel_chk == 'N':                                                   # If-Condition: If User NOT Verifies (No/N)
                print()                                                            # New Line Pass
        
            else:                                                                  # Else-Condition: Neither Yes or No
                print("Invalid Input")                                             # Causes 'Invalid Input' message to user.
        
        else:                                                                      # Else-Condition: If Selected Book Is NOT Available
            print("Sorry, the book you have chosen is currently out of stock.")    # User Notified of Book being Out of Stock
        
        
        
        
        
        
    def return_book(self):        # LMS Class Object Method --- Returning Book to Library Database
        
        menu_counter = 1          # Menu Counter Initialized for Navigation/Selection (Used for Index)
        
        print("\n ------ Your Borrowed Books List ------ ")          # Borrowed Book List of User Header
        print()                                                      # New Line Space Created
        
        for book_lent in user_basic.details['Borrowed']:             # For-Loop Initialized: Iterating Through User's Loaned Books
            
            print(menu_counter, ".) ", book_lent.title, sep = '')    # Book Taken Out by User Listed for Selection to User
            menu_counter += 1                                        # Menu Counter Increments per Book
            
        book_sel = int(input("Which Book to Return?: "))             # User Input - Integer Input for Menu Selection (Returning Book)
        
        while book_sel not in range(1, menu_counter):                                     # User Input Error-Catch: Ensuring User Inputs Integer in Range of Menu Selection
            book_sel = int(input("Invalid Selection. Please Choose a Book to Return: "))  # User Input Second Pass
        
        book_sel -= 1                                                                     # User Integer Index ReAdjusted
        
        print("\nYou Have Selected: ", user_basic.details['Borrowed'][book_sel].title)    # Displaying Book Selection to User for Confirmation
        
        sel_chk = input("Would You Like to Return This Book? (Y/N): ").upper()            # User Input - Confirming Book Selection for Return (Y/N) = Yes or No
        
        if sel_chk == 'Y':                                               # If-Condition: If Yes/Y
            
            user_basic.details['Borrowed'][book_sel].is_avail = True     # Book's Availability Status Switches to True for LMS Database
            del user_basic.details['Borrowed'][book_sel]                 # Book is Deleted from User's Borrowed List.
        
    
    
    
    
    
    def chk_inv(self):                                     # LMS Class Object Method --- Checking Entire Library Database/Catalogue
        
        print("\n-------- LIBRARY BOOK LIST --------")     # Library Catalogue/Database Header
        print()                                            # New Line Space
        
        for item in lms.lib_db:                            # For-Loop Initialized: Iterating Through Library's Catalogue
            
            if item.is_avail:                                                                                                 # If Book is Available
                print(item.title, ", Written By: ", item.auth_name, " | Genre: ", item.genre, sep = '')                       # List Book to User
            
            else:                                                                                                             # If Book is NOT Available
                print(item.title, ", Written By: ", item.auth_name, " | Genre: ", item.genre, " -NOT AVAILABLE- ", sep = '')  # List Book to User with "NOT AVAILABLE" Tag
            
        input_break = input("\nPress Any Key to Continue...")                                                         # User Input - Break the Pause
            
        
        
        
        
    
    def chk_borrows(self):                                             # LMS Class Object Method --- Check Borrowed Books from Library Database/Catalogue
        
        print("\n------ Library Members with Borrowed Books ------ ")  # Library Database Borrowed Books Header
        print()                                                        # New Line Space
        
        for known_user in lms.usr_accounts:                            # For-Loop Initialized: Iterating Through Every Registered User in the LMS
            
            if len(known_user.details['Borrowed']) != 0:               # If-Condition: If User's Borrowed Books List is not Empty
                
                print("--- Member:", known_user.usr_name, "---")       # Display User with Borrowed Books to Admin
                
                for book_lent in known_user.details['Borrowed']:       # Iterate Through Every Book in User's Borrowed List
                    print("Borrowed:", book_lent.title)                # Displayed User's Borrowed Books to Admin
                
                print()                                                # New Line Space
    
    
    
    
    def chk_overdue(self):                                            # LMS Class Object Method --- Check for Overdue Books in Library Database/Catalogue
        
        print("\n------ Library Members with Overdue Books ------ ")  # Library Overdue Books Header
        print()                                                       # New Line Space
        
        for known_user in lms.usr_accounts:                           # For-Loop Initialized: Iterating Through Every Known User Account in LMS 
            
            if len(known_user.details['Overdue']) != 0:               # If-Condition: If User's Overdue List is not Empty
                
                print("--- Member:", known_user.usr_name, "---")      # Display User with Overdue Books
                
                for book_due in known_user.details['Overdue']:        # Iterate Through every Overdue Book of User
                    print("Overdue:", book_due.title)                 # Display all Overdue Books of User to Admin
                
                print()                                               # New Line Space
            
            
            
    
    def chk_fines(self):                                                                  # LMS Class Object Method --- Check Fines of Users in LMS Database
        
        print("\n------ Library Members with Outstanding Fines ------")                   # LMS Database Fines Header
        print()                                                                           # New Line Space
        
        for known_user in lms.usr_accounts:                                               # For-Loop Initialized: Iterating Through Every Known User in LMS Database
            
            if known_user.details['Fines'] != 0:                                          # If-Condition: If Fine in User's Details is not Zero
                
                print("--- Member:", known_user.usr_name, "---")                          # Display User with Fines to Admin
                print("Outstanding Fines: ", "$", known_user.details['Fines'], sep = '')  # Display Outstanding Fines of User to Admin
                print()                                                                   # New Line Space
            
            
    
    
    
    def chk_wlist(self):                                           # LMS Class Object Method --- Check Waiting Lists in LMS Database/Catalogue
        
        print("\n------ Library Members on Wait Lists ------")     # LMS Waiting List Header
        print()                                                    # New Line Space
        
        for known_user in lms.usr_accounts:                        # For-Loop Initialized: Iterating Through Every Known User in LMS Database
            
            if len(known_user.details['Wait']) != 0:               # If-Condition: If User's Wait List is not empty
                
                print("--- Member:", known_user.usr_name, "---")   # Display User with Wait list to Admin
                
                for book_wait in known_user.details['Wait']:       # Iterate Through Every Book in User's Wait List
                    
                    print("Wait List For:", book_wait.title)       # Display Book on User's Wait List to Admin
                
                print()                                            # New Line Space
    
    
    
    
    
    
    def chk_reserves(self):                                          # LMS Class Object Method --- Checking Reservations in LMS Database
        
        print("\n------ Library Members with Reservations -------")  # LMS Database Reservations Page Header
        print()                                                      # New Line Space
        
        for known_user in lms.usr_accounts:                          # Iterating Through Ever Known User in LMS Database
            
            if len(known_user.details['Reserve']) != 0:              # If-Condition: If User's Reservation List is not Empty/Zero
                
                print("--- Members:", known_user.usr_name, "---")    # Display Users with Reservations to Admin
                
                for book_res in known_user.details['Reserve']:       # Iterate Through Every Reserved Book in User's Reservations List
                    
                    print("Reserved:", book_res.title)               # Display User's Book Reservations to Admin
                
                print()                                              # New Line Space
            
            
    
    
    
    def chk_users(self):                                                      # LMS Class Object Method --- Checking All Current Users Online in LMS 
        
        print("\n------- All Active Current Users on the LMS ------")         # Current Active Users in LMS Page Header
        print()                                                               # New Line Space
        
        for online_user in lms.logged_on:                                     # Iterating Through Every Online User Currently on the LMS
            
            if online_user.isAdmin:                                           # If Online User is Administrator
                acc_lev = "Administrator"                                     # Apply 'Administrator' Tag for Display purposes
            
            else:                                                             # If Online User is NOT Administrator
                acc_lev = "Basic"                                             # Apply 'Basic' Tag for Display Purposes
            
            print("User:", online_user.usr_name, "| Access Level:", acc_lev)  # Current Active User is Displayed to Admin with Indication Tag (Admin or Basic User)
            print()                                                           # New Line Space
            
            
            
            
    
    def search_inv(self):                                                        # LMS Class Object Method --- Library Database/Catalogue Search
        
        result_output = []                                                       # Container Created for Final Result Output to User/Admin
        
        print("\n------ Library Collections Search -------")                     # Library Search Page Menu Header
        print()                                                                  # New Line Space
        print("1.) Search by Available Title")                                   # Menu Option 1 for User - Search Library Catalogue by Book Title in Database
        print("2.) Search by Available Author")                                  # Menu Option 2 for User - Search Library Catalogue by Author in Database
        print("3.) Search by Available Genre")                                   # Menu Option 3 for User - Search Library Catalogue by Genre in Database
        
        menu_sel = int(input("Please Make a Selection: "))                       # User Input - Integer Input for Menu Selction
        
        while menu_sel not in range(1, 5):                                       # User Input Error-Catch: Ensuring User Inputs Integer in Range of Menu Options
            
            menu_sel = int(input("Invalid Input. Please Make a Selection: "))    # User Input Second Pass
            
            
        if menu_sel == 1:                                                        # If-Condition: If User Chooses Option 1 (Search by Book Title)
            
            menu_counter = 1                                                     # Menu Counter Initialized for Navigation/Selection
            
            title_find = input("Please Enter the Title of the Book: ").title()   # User Input - String Input of the Book's Title to Search; String is Converted to .title() format
            title_findsplit = title_find.split()                                 # User Inputted String is Split at Spaces and Stored in List labeled 'title_findsplit'
            
            for book in lms.lib_db:                                              # Iteration through Every Book in Library's Book Catalogue/Database
                
                result_bucket = []                                               # List Initialized for Collecting Matching Results in Search Process
                
                title = book.title                                               # Title is taken from Book Object Being Iterated 
                titlesplit = title.split()                                       # Title from Book Object is Split At Spaces and Stored In List Labelled 'titlesplit'
                
                for find_part in title_findsplit:                                # Every Word Component from User's Title Search is Iterated Through
                    for title_part in titlesplit:                                # Every Word Component from Book Object Title is Iterated Through
                        
                        if ":" in title_part:                                    # If-Condition: If a Colon is Detected inside Word Part from Book Object Title
                            title_part = title_part[:-1]                         # Word Part with Colon is Modified to Remove the Colon (For Word Matching Accuracy)
                            
                        if ":" in find_part:                                     # If-Condition: If a Colon is Detected inside User's Title Search String
                            find_part = find_part[:-1]                           # Word Part with Colon is Modified to Remove the Colon (For Word Matching Accuracy)
                        
                        if find_part == title_part.title():                      # If-Condition: If Word Part from Book Object Title Matches Word Part from User's Input Search String
                            result_bucket.append(title_part)                     # The Word Part from the Book Object's Title is Appended to the Result Bucket
                
                match_up = book.title.split()                                    # The Current Book Object's Title is Split and Stored Cleanly in 'match_up' variable                               

                if len(result_bucket) == 0:                                      # If-Condition: If the length/size of the results bucket is empty/zero
                    continue                                                     # Continue On the Loop Without Enacting Anything                                             
                
                else:                                                            # Else-Condition: If the length/size of the results bucket is NOT empty/zero
                    if " ".join(result_bucket) in " ".join(match_up):            # If-Condition: Result Bucket Entries is Combined as a String and Checked if the Words Appear in The Book Object's Title
                        result_output.append(book)                               # If Matched: Current Book Object is Appended to Results Output List for Display to User/Admin
            
            print('\n------ SEARCH RESULTS FOR:', title_find, "------")          # LMS Catalogue/Database Search Results Page Header
            
            for found_book in result_output:                                     # Iteration Through Every Book Object in Results Output List
                
                print(menu_counter, ".) ", found_book.title, " | Written By: ", found_book.auth_name, " | Genre: ", found_book.genre, sep = '')   # Book Object Displayed to User (title, auth, genre)
                menu_counter += 1                                   # Menu Counter Increments by 1 every book object iteration
                
                
                
        
        elif menu_sel == 2:                                                        # If-Condition: If User Selects Option 2 (Search by Author)
            
            menu_counter = 1                                                       # Menu Counter Initialized for Navigation/Selection
            auth_list = []                                                         # List Intialized Containing All Found Authors in Library Catalogue/Database
            
            for book in lms.lib_db:                                                # For-Loop Initialized: Iterating Through Every Book in Library CataLogue/Database
                
                if book.auth_name in auth_list:                                    # If-Condition: If Book Object's Author Name Already in Author List
                    pass                                                           # Pass Through and Iterate Next
                
                else:                                                              # Else-Condition: If Book Object's Author Name NOT in Author List
                    auth_list.append(book.auth_name)                               # Author's Name from Book Object is Appended to Author List
                
            print("\n------ AVAILABLE AUTHORS IN LIBRARY CATALOGUE -----")         # Availble Authors in Library Catalogue/Database Page Header
            
            for author in auth_list:                                               # For-Loop Initialized: Iterating Throuugh Every Author Name Collected in Author List
                print(menu_counter, ".) ", author, sep = '')                       # Author Name with Menu Selection Option is Displayed to User/Admin
                menu_counter += 1                                                  # Menu Counter Variable is Incremented by 1 Every Author Name Iteration
        
            auth_sel = int(input("\nSelect an Author to Search: "))                # User Input - Integer Input for Menu Selection in Author Search
            
            while auth_sel not in range(1, menu_counter):                          # User Input Error-Catch: Ensuring User Inputs Integer Selection in Range of Menu Options
                
                auth_sel = int(input("Invalid Input. Please Select an Author: "))  # User Input Second Pass
            
            auth_sel -= 1                                                          # User Integer Input Readjusted for Author List Indexing & Selection
            
            selected = auth_list[auth_sel]                                         # Author Name is Selected from Index Readjustment from User's Integer Input
            
            print("\n------ SEARCH RESULTS FOR:", selected, "------")              # Search Results for Author Search in Library Database/Catalogue
            
            for book_match in lms.lib_db:                                          # For-Loop Initialized: Iterating Through Every Book in Library Database/Catalogue
                
                if book_match.auth_name == selected:                               # If-Condition: If Book Object's Author Name Matches Author Name from User Search
                    print(book_match.title)                                        # Mathing Author's Book Objects are Displayed to the User/Admin
            
        
        
        
        elif menu_sel == 3:                                                        # If-Condition: If User Selects Option 3 (Search by Genre)
            
            menu_counter = 1                                                       # Menu Counter Initialized for Navigation/Selection
            genre_list = []                                                        # List Created to Store Found Genres in Library Database/Catalogue
            
            for book in lms.lib_db:                                                # For-Loop Initialized: Iterating Through Every Book in Library Database/Catalogue
                
                if book.genre in genre_list:                                       # If-Condition: If Book Object's Genre Already in Genre Collection List
                    pass                                                           # Pass Through and Iterate Next
                
                else:                                                              # Else-Condition: If Book Object's Genre NOT in Genre Collection List
                    genre_list.append(book.genre)                                  # Book Object's Genre is Appended to Genre Collection List
            
            print("\n------ AVAILABLE GENRES IN LIBRARY CATALOGUE ------")         # Available Genres in Library Catalogue/Database Page Header
            
            for genre in genre_list:                                               # For-Loop Initialized: Iterating Through Every Genre in Genre Collections List
                
                print(menu_counter, ".) ", genre)                                  # Genre is Displayed to Admin/User for Selection
                menu_counter += 1                                                  # Menu Counter is Incremented by 1 Every Iteration
            
            gen_sel = int(input("\nPlease Make a Selection: "))                    # User Input - Integer Input for Menu Selection in Choosing Genre
            
            while gen_sel not in range(1, menu_counter):                           # User Input Error-Catch: Ensuring User Inputs Integer in Range of Menu Options
                gen_sel = int(input("Invalid Input. Please Make a Selection: "))   # User Input Second Pass
            
            gen_sel -= 1                                                           # User Inputted Integer Readjusted for Index Position
            selection = genre_list[gen_sel]                                        # Readjusted User Inputted Integer Used to Access Chosen Genre in Genre List
            
            print("\n------ SEARCH RESULTS FOR:", selection, "------")             # Search Results for Genre Search in Library Database/Catalogue
            
            for book in lms.lib_db:                                                # For-Loop Initialized: Iterating Through Every Book in Library Catalogue/Database
        
                if book.genre == selection:                                        # If-Condition: If Book Object's Genre Matches User Selected Genre in Search
                    print(book.title, " | Written By: ", book.auth_name, sep = '') # Display Book Object with Author Name of Selected Genre in Search in LMS Database/Catalogue
            
                
                        
                                     
def sub_main():                      # Program Function Defined --- Sub Main (Used for Flow Handling and Provides Menu Pathways)
    
    for account in lms.logged_on:    # For-Loop Initialized: Iterating Through Every Account Currently Logged On LMS
        
        if account.isAdmin:          # If-Condition: If Current Iterated Account is an Administrator
            sys_admin = True         # System State Switch into Administrator Mode
        
        else:                        # Else-Condition: If Current Iterated Account is NOT an Administrator
            sys_admin = False        # System State Switch does NOT go into Administrator Mode
        

    if sys_admin:                    # If-Condition: If System State is: Administrator
        
        print("\n---Library Management System (ADMINISTRATOR LEVEL) ---")    # Menu Header for Administrator Mode Menu
        print("1.) Add Book to Library")                                     # Administrator Menu Option 1 - Adding Books to the LMS Book Catalogue/Database
        print("2.) Remove Book from Library")                                # Administrator Menu Option 2 - Deleting Books from the LMS Book Catalogue/Database
        print("3.) Check Library Inventory")                                 # Administrator Menu Option 3 - Checking All Available Books in LMS Book Catalogue/Database
        print("4.) Check Borrowed Books")                                    # Administrator Menu Option 4 - Checking All Books Out on Loan with User/Member in LMS Database
        print("5.) Check Overdue Books")                                     # Administrator Menu Option 5 - Checking All Overdue Books with User/Member in LMS Database
        print("6.) Check Outstanding Fines")                                 # Administrator Menu Option 6 - Checking All Member's Outstanding Fines in LMS Database
        print("7.) Check Waiting Lists")                                     # Administrator Menu Option 7 - Checking All Wait Lists with Users in LMS Database
        print("8.) Check Book Reservations")                                 # Administrator Menu Option 8 - Checking All Book Reservations with Users in LMS Database
        print("9.) Check Current Logged on Users")                           # Administrator Menu Option 9 - Checking All Currently Logged On/Active Users in LMS Database
        print("10.) Search Library Inventory")                               # Administrator Menu Option 10 - Search Inventory in LMS Database/Catalogue
        print("11.) Search User")                                            # Administrator Menu Option 11 - Search Specific User in LMS Database
        
        sub_sel = int(input("\nPlease Make a Selection from the Menu: "))    # User Input - Integer Input for Menu Selection in Adminstrator Mode
        
        while sub_sel not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11):            # User Input Error-Catch: Ensuring User Inputs Integer in Range of Menu Selection Options
            
            sub_sel = int(input("\nInvalid Selection. Please Make a Selection from the menu: "))  # User Input Second Pass
        
        if sub_sel == 1:         # If-Condition: If User Chooses Option 1 (Adding Book to Library)
            lms.add_book()       # Function Call to Library Management System (add book)
        
        elif sub_sel == 2:       # If-Condition: If User Chooses Option 2 (Deleting Book from Library)
            lms.del_book()       # Function Call to Library Management System (delete book)
            
        elif sub_sel == 3:       # If-Condition: If User Chooses Option 3 (Checking Library Inventory)
            lms.chk_inv()        # Function Call to Library Management System (Check Inventory)
            
        elif sub_sel == 4:       # If-Condition: If User Chooses Option 4 (Check Borrowed Books)
            lms.chk_borrows()    # Function Call to Library Management System (Check Borrowed)
            
        elif sub_sel == 5:       # If-Condition: If User Chooses Option 5 (Check Overdue Books)
            lms.chk_overdue()    # Function Call to Library Management System (Check Overdues)
        
        elif sub_sel == 6:       # If-Condition: If User Chooses Option 6 (Check Outstanding Fines)
            lms.chk_fines()      # Function Call to Library Management System (Check Fines)
        
        elif sub_sel == 7:       # If-Condition: If User Chooses Option 7 (Check Wait Lists)
            lms.chk_wlist()      # Function Call to Library Management System (Check Wait List)
        
        elif sub_sel == 8:       # If-Condition: If User Chooses Option 8 (Check Book Reservations)
            lms.chk_reserves()   # Function Call to Library Management System (Check Reserves)
        
        elif sub_sel == 9:       # If-Condition: If User Chooses Option 9 (Check Users in Database)
            lms.chk_users()      # Function Call to Library Management System (Check Users)
        
        elif sub_sel == 10:      # If-Condition: If User Chooses Option 10 (Search Library Inventory)
            lms.search_inv()     # Function Call to Library Management System (Search Inventory)
        
        elif sub_sel == 11:      # If-Condition: If User Chooses Option 11 (Search User in LMS Database)
            lms.search_usr()     # Function Call to Library Management System (Search User)
    
    else:                                              # Else-Condition: If System State is NOT Administrator
        
        print("\n--- Library Management System ---")   # Menu Header for Basic User Mode Menu
        print("1.) Take Out Book")                     # Basic User Menu Option 1 - Take Out a Book from the Library (Loan Out)
        print("2.) Return Book")                       # Basic User Menu Option 2 - Return a Book to the Library (Book Return)
        print("3.) Search for Book")                   # Basic User Menu Option 3 - Search for a Book in the LMS Catalogue/Database
        print("4.) Account Details")                   # Basic User Menu Option 4 - View Account Details (Loans, Fines, Overdues, etc)
        print("5.) Exit LMS")                          # Basic User Menu Option 5 - Exit the Library Management System
        
        sub_sel = int(input("Please Make a Selection from the Menu: "))    # User Input: Integer Input for Menu Option Selection
        
        while sub_sel not in (1, 2, 3, 4, 5):                              # User Input Error-Catch: Ensuring User Inputs Integer in Range of Menu Selection Options
            sub_sel = int(input("Invalid Selection. Please Make a Selection From the Menu: "))   # User Input Second Pass
        
        if sub_sel == 1:           # If-Condition: If User Option is 1 (Take Book Out from Library)
            lms.take_book()        # Function Call to Library Management System (Take Book)
        
        elif sub_sel == 2:         # If-Condition: If User Option is 2 (Return Book to Library)
            lms.return_book()      # Function Call to Library Management System (Return Book)
        
        elif sub_sel == 3:         # If-Condition: If User Option is 3 (Search Inventory)
            lms.search_inv()       # Function Call to Library Management System (Search Inventory)
        
        elif sub_sel == 4:             # If-Condition: If User Option is 4 (Viewing Account Details)
            print("Checking Borrows")  # Function Call to Library Management System (Accound Details)
            
            for book_lent in user_basic.details['Borrowed']: # For-Loop Initialized: Iterating Through Every Borrowed Book in Account
                print(book_lent.title)                       # Displaying Borrowed Books to User
        
        elif sub_sel == 5:                                   # If-Condition: If User Option is 5 (Exit LMS)
            print("Exiting...")                              # General Print Statement for Loop Manipulation







def main():                                                                      # Program Function Defined --- Main (Used as Foundation for bridging Menu Logic and Library Management System
    
    print("\nWelcome to the Library Management System -- Version 0.7")           # Menu Header for Library Management System Main Program Landing Page/Boot Page
    print("1.) Log On")                                                          # Landing Menu Option 1 - Log On to Library Management System
    print("2.) Create New Account")                                              # Landing Menu Option 2 - Create a New Account in Library Management System
    print("3.) Exit")                                                            # Landing Menu Option 3 - Exit the Main Library Management System Program
    
    menu_sel = int(input("\nPlease Make a Selection (1-3): "))                   # User Input - Integer Input for Landing Menu Option Selection
    
    while menu_sel not in (1,2,3):                                               # User Input Error-Catching: Ensuring User Inputs Integer in Range of Menu Selection Options
        menu_sel = int(input("Invalid Selection. Please Make a Selection (1-3): "))  # User Input Second Pass
    
    if menu_sel == 1:                                                            # If-Condition: If User Option is 1 (Log On to Library Management System)
        
        while True:                                                              # While Loop Initialized: Logic Loop Used for User Name Check Flows
            usr_match = False                                                    # Boolean Initialized: Used for state switch during matching
            name = input("\nEnter Your User Name: ")                             # User Input - User Puts in Name as String
            index = 0                                                            # Index Variable Initialized at 0
            
            for account in lms.usr_accounts:                                     # For-Loop Initialized: Iterating Through Every Account Known in Library Management System Database
                
                if account.usr_name == name:                                     # If-Condition: If the Current Iterated Account User Name in Database Matches with User Inputted User Name
                    usr_match = True                                             # User Match State Switches to True
                    break                                                        # Once Matched, the for-loop will terminate
                    
                else:                                                            # Else-Condition: If Current Iterated Account User Name does NOT Match with User Inputted String User Name
                    index += 1                                                   # Index Variable Increments by 1 every Account Iteration
            
            if usr_match:                                                        # If-Condition: If User Match State is True
                break                                                            # Loop Terminates
            
        if usr_match:                                                            # If Condition: If User Match State is True
            while True:                                                          # While-Loop Initialized: Logic Loop Used for Password Check Flows
                password = input("Enter Your Password: ")                        # User Input - User Inputs Password as String
                
                if password in admin_pass:                                       # If-Condition: If User Inputted Password is Found in Administrator Passwords List
                    user_admin = SystemUser(name, password, isLogon=True, isAdmin=True)  # System User Object Created with Administrator Priveledge
                    lms.logged_on.append(user_admin)                                     # System User Objected Appended to Currently Logged On Users List
                    
                    while True:                                                  # Nested While Loop Initialized (Used for Handling Logic Flow for sub_main program function
                        sub_main()                                               # Program Function Call --- Sub Main (Used for Main Menu Logic & Flow)
                
                else:                                                            # Else-Condition: If User Inputted Password NOT Found in Administrator Passwords List
                    
                    if password != lms.usr_accounts[index].usr_pass or password in admin_pass: # If-Condition: If User Inputted Password Does NOT Match with Known Password Stored in Database
                        
                        print("Invalid Password. Try Again.")                    # Message Displayed to User incase of Invalid Password
                    
                    else:                                                        # Else-Condition: If Iterated Account is NOT Administrator
                        user_basic = SystemUser(name, password, isLogon=True, isAdmin = False)  # System User Object is Created with Basic Priveledges
                        lms.logged_on.append(user_basic)                                        # System User Object is Appended to LMS Database
                        
                        while True:                                                             # While-Loop Initialized
                            sub_main()                                                          # Program Function Call to sub_main for Menu Flows & Logic
                
                
                
    
    elif menu_sel == 2:                                            # If-Condition: If User Chooses Option 2 (Create a New Account)
        
        new_name = input("\nPlease Enter Your User name: ")        # User Input - User Inputs Desired Name as String
        
        while True:                                                # While-Loop Initialized (Used for Logic Handling and Flow for Account Creation)
            
            new_pass = input("Please Enter a Password: ")                    # User Input - User Inputs Desired Password as String
            pass_chk = input("Please Confirm Your Password (Enter Again): ") # User Input - User Inputs Desired Password as String again for Verification
            
            if new_pass in admin_pass or pass_chk in admin_pass:             # If-Condition: If User's Newly Created Password is in Administrator Password List
                print("\nInvalid Password. Please Try Again")                # Display Message to User Indicating the Inputted Password is Invalid
            
            else:                                                            # Else-Condition: If User's Newly Created Password NOT in Administrator Password List
                if pass_chk == new_pass:                                     # If-Condition: If Re-Entered Password Matches First Entered Newly Created Password
                
                    user_basic = SystemUser(new_name, new_pass, isLogon=False, isAdmin=False)    # System User Object is Created with Newly Created User Name and Password with NO Admin Priveledges
                    lms.usr_accounts.append(user_basic)                                          # Newly Created System User Object is Appended to Library Management System's List of Known Accounts
                    break                                                                        # Break Statement - Terminates While-Loop Logic Handling
            
                else:                                                   # Else-Condition: If Re-Entered Password Does NOT Match First Entered Password
                    print("Confirmation Password Does Not Match!")      # Message Display to User Noticing that The Re-Entered Password Does Not Match Original Inputted Password
        
        print("\nAccount Created Successfully!")                        # Message Display to User Informing Successful Account Creation
        
        
        
    else:                        # Else-Condition: If User Chooses Neither 1 and 2      
        main_state = False       # Main Program State Switches to False; Signals to Exit Library Management System
    
        
        
                
                
                    
            
            
    
    
  
# Main Code Testing Area ----------- TESTING PURPOSES ONLY! --------------------





# Administrator Passwords List (Used for LMS Testing)

admin_pass = ['Doom', 'MassEffect', 'ResidentEvil', 'Quake', 'DukeNukem', 
              'RainbowSix', 'GhostRecon', 'SWAT3', 'SWAT4', 'RavenShield',
              'RogueSpear', 'EagleWatch', 'BlackThorn', 'ChaosTheory', 'Doom2']






# System User Object Created for Manual Testing & Debugging Purposes

user_basic = SystemUser('Danny', 'bb', isLogon=True, isAdmin=False)         # System User Object Created for Testing (Basic Account with NO Administrator Priveledges)

""" Although the testing SystemUser object is created and labelled here as a
basic user, if you input an Administrator Password then you can still logon as
an Admin in order to operate the Admin Level Menus... """


# Library Management System Instantiation & Initialization

lms = LibraryManagementSystem()           # Library Management System Object Created and Stored in Variable Labelled 'lms'
lms.usr_accounts.append(user_basic)       # System User Object is Appended to Library Management System's List of Known Users/Accounts





# Filling Up Library Inventory --- Creating Data for Book Object Creation ------ USED FOR TESTING ONLY!


collection = [
    
    # Tuple Formatting: (Book Title, Book Author, Book Genre, Book ISBN #)
    
    ('Pale Blue Dot', 'Carl Sagan', 'Fact', '100000'),                
    ('Mass Effect: Revelations', 'Drew Kapryshyn', 'Science-Fiction', '100001'),
    ('Doom: Knee Deep in the Dead', 'John Doe', 'Science-Fiction', '100002'),
    ('Doom: Hell on Earth', 'John Doe', 'Science-Fiction', '100003'),
    ('Star Wars: Yoda Stories', 'George Lucas', 'Science-Fiction', '100004'),
    ('Star Wars: Jedi Stories', 'George Lucas', 'Science-Fiction', '100005'),
    ('Cosmos', 'Carl Sagan', 'Fact', '100006'),
    ('Battletech: Decision at Thunder Rift', 'William H. Keith', 'Science-Fiction', '100007'),
    ('Battletech: Wolves on the Border', 'Robert N. Charrette', 'Science-Fiction', '100008'),
    ('Resident Evil: The Umbrella Conspiracy', 'S.D. Perry', 'Horror', '100009')
    
]

for test_book in collection:                                             # For-Loop Initialized: Iterating Through Every Tuple with Book Data in Book Collection's List
    
    book = Book(test_book[0], test_book[1], test_book[2], test_book[3])  # Book Object Created as 'book' from Tuple Data
    lms.lib_db.append(book)                                              # Book Object is Appended to Library Management System's Book Database/Catalogue
    





# Filling Up User Account Database in the Library Management System for Testing

usr_collection = [
    
    # Tuple Format (User Name, User Password, Is Online?, Is Administrator?)
    
    ('Mike', 'quake321', True, False),              # Expected: Mike - Basic User (Online)
    ('Charles', 'indianapolis96', False, False),    # Expected: Charles - Basic User (Offline)
    ('Ryan', 'MassEffect', True, True),             # Expected: Ryan - Admin User (Online)
    ('Keith', 'Doom2', False, True),                # Expected: Keith - Admin User (Offline)
    ('Dave', 'darkofperfect2121', True, False),     # Expected: Dave - Basic User (Online)
    ('Larry', 'biohazard3', True, False),           # Expected: Larry - Basic User (Online)
    ('Luke', 'groundbranch111', False, False),      # Expected: Luke - Basic User (Offline)
    ('Gordon', 'RogueSpear', False, True),          # Expected: Gordon - Admin User (Offline)
    ('Flynn', 'tron421', True, False),              # Expected: Flynn - Basic User (Online)
    ('Chris', 'stars!101', True, False)             # Expected: Chris - Basic User (Online)


]

for test_user in usr_collection:      # For-Loop Initialized: Iterating Through Every Tuple with User Data 
    
    if test_user[3]:                  # If-Condition: If User Data in Index Position 3 (Is Administrator?) is TRUE
        
        user_admin = SystemUser(test_user[0], test_user[1], test_user[2], test_user[3])     # System User Object is Created with Administrator Priveledges Using Tuple Data
        lms.usr_accounts.append(user_admin)                                                 # System Administrator User Object is Appended to Library Management System's Known User Accounts List
        
        if test_user[2]:                           # Nested If-Condition: If User Data Tuple in Index Position 2 (Is Online?) is TRUE
            lms.logged_on.append(user_admin)       # System User Object (Administrator) is Appended to Library Management System's Currently Logged On List
                 
    else:                             # Else-Condition: If User Data Tuple in Index Position 3 (Is Administrator?) NOT TRUE
        user_basic = SystemUser(test_user[0], test_user[1], test_user[2], test_user[3])     # System User Object is Created with Basic Priveledges Using Tuple Data
        lms.usr_accounts.append(user_basic)                                                 # System User Object (Basic) is Appended to Library Management System's Known User Accounts List
        
        if test_user[2]:        # Nested If-Condition: If User Data in Inded Position 2 (Is Online?) is TRUE
            
            lms.logged_on.append(user_basic)     # System User Object (Basic) is Appended to Library Management System's Logged On List





# Manually Setting User 'Account Details' Dictionary Values for Testing 

lms.usr_accounts[1].details['Fines'] = 5                    # Expected: Mike | $5 of Fines
lms.usr_accounts[1].details['Borrowed'] = [lms.lib_db[6]]   # Expected: Mike | Borrowed 1 Book
lms.usr_accounts[1].details['Overdue'] = [lms.lib_db[6]]    # Expected: Mike | Has 1 Book Overdue
lms.usr_accounts[1].details['Reserve'] = [lms.lib_db[4]]    # Expected: Mike | Has 1 Book Reserved

lms.usr_accounts[2].details['Borrowed'] = [lms.lib_db[2], lms.lib_db[5]]    # Expected: Charles | Borrowed 2 Books
lms.usr_accounts[2].details['Wait'] = [lms.lib_db[8]]                       # Expected: Charles | Wait List for 1 Book

lms.usr_accounts[5].details['Borrowed'] = [lms.lib_db[8]]                   # Expected: Dave | Borrowed 1 Book
lms.usr_accounts[5].details['Wait'] = [lms.lib_db[9], lms.lib_db[2]]        # Expected: Dave | Wait List for 2 Books

lms.usr_accounts[6].details['Borrowed'] = [lms.lib_db[3], lms.lib_db[9], lms.lib_db[1]]      # Expected: Larry | Borrowed 3 Books

lms.usr_accounts[9].details['Fines'] = 10       # Expected: Flynn | $10 of Fines





# Main Program Initialization 

main_state = True      # Main State Boolean Variable Initialized (Program Power Switch)

while main_state:      # While-Loop Initialized (Used for Keeping Program Running)
    main()             # Function Call to Main Program Execution