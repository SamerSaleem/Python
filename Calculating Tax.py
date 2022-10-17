income = float(input("Enter the annual income: "))

#
# Write your code here
# if the income is more than tax_rule value then it would be subtracted from the 14839 and then multiplied with 0.32 otherwise it will only be multiplied by 18% - 556.2
# be .
tax_rule= 85_528
hi_income = 14_839.2
if income > tax_rule:
    tax = (income - hi_income) * 0.32
elif income < tax_rule:
    tax = (income * 0.18) - 556.2

#output will be rounded.
tax = round(tax, 0)
print("The tax is:", tax, "thalers")