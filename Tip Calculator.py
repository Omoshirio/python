print("welcome to the tip calculator")
bill=float(input("what was the total bill $"))
tip=int(input("How much tip would you like to give ? 10,12,15"))
people=int(input("how many people split the bill?"))
tip_as_person=tip/100
total_tip_amount=bill*tip_as_person
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
print(f"each person should pay:${final_amount}")