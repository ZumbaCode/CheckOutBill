print("Welcome to the Tip Calculator ")
bill = float(input("Enter The Total Bill? $ "))
tip = int(input("Enter the Percentage: "))
people = int(input("Enter People: "))
billWithTip = tip / 100 * bill + bill
print("Total Bill: ", billWithTip)