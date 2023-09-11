bill= float(input ("What is the total bill amount? "))
tip_pct= float(input ("What percentage of tip do you want to give? "))
pax= float(input ("How many people? "))

total_bill = bill * ( 1+(tip_pct/100))
print (total_bill)

per_pax = total_bill/ pax
print (round(per_pax,2))

per_pax_round= round(per_pax,2)
print (f"Per person to pay $ {per_pax_round}")