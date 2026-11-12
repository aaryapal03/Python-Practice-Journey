
# Example 1 : Voting Eligibility
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("You are eligible to vote.")
    else:
        print("You must be a citizen to vote.")
else:
    print("You are not eligible to vote.")

print()


# Example 2 : College Admission
percentage = 82
entrance_exam = True

if percentage >= 75:
    if entrance_exam:
        print("Admission Confirmed.")
    else:
        print("Clear the entrance exam first.")
else:
    print("Minimum percentage not achieved.")

print()


# Example 3 : ATM Withdrawal
balance = 5000
amount = 2000

if balance >= amount:
    if amount > 0:
        print("Withdrawal Successful.")
    else:
        print("Enter a valid amount.")
else:
    print("Insufficient Balance.")

print()



# Example 4 : Employee Bonus
experience = 4
performance = "Excellent"

if experience >= 3:
    if performance == "Excellent":
        print("Bonus Approved.")
    else:
        print("No Bonus due to performance.")
else:
    print("Minimum experience not completed.")


# End of Program
