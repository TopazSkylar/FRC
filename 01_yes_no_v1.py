# Functions go here

def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def yes_no(question, valid_ans_list=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word or then, letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # checks user response to question
            # only accepts yes or no
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print("Please enter either yes or no")


def show_instructions():
    make_statement("Instructions", "ℹ️")

    print('''\n

For each ticket enter ...
- The person's name (cannot be blank)
- Age (between 12 and 120)
- Payment method (cash / credit)

When you have entered all the users, press 'xxx'  to quit.

the program will display the ticket detail including the cost of each ticket, the total cost 
and the total profit. 

This information will also be automatically written to a text file. 

''')


# main routine goes here

while True:
    instructions = yes_no("Do you want to read the instructions? ")
    print(f"You chose {instructions}")
    print()
