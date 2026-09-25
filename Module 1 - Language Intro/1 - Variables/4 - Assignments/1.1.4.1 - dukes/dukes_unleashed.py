"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

JMU 2022-2023 Annual:
In-state total cost: 30792 USD
Out-of-state total cost: 47882 USD

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

### Your code here ###

# Basically I need to find the principal amount that when invested at 5% will result in the In and Out of state tuition costs
# We can use the formula: Investment = Cost / Rate 

in_state_gift = 30792 / 0.05

out_state_gift = 47882 / 0.05

#Use print statments to determine if the values are in an acceptable range
print("The amount needed to pay for an in-state student is:", in_state_gift)
print("The amount needed to pay for an out-of-state student is:", out_state_gift)