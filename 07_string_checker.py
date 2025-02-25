# function goes here
def string_checker(question, valid_ans_list=('yes', 'no'), num_letters=1):
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


# main routine goes here
payment_list = ["cash", "credit"]

for case in range(0,5):
    want_instructions = string_checker("Do you want to read the instructions? ")
    print(f"You chose {want_instructions}")

for case in range(0,5):
    pay_method = string_checker("Choose a payment method (cash/credit)", 2)
    print(f"You chose {pay_method}")