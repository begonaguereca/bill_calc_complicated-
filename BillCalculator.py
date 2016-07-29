def tip_amount(bill):
	total_tip = bill* 0.2
	return total_tip

def total_bill(tip, bill):
	total_bill = tip + bill
	return total_bill

def individual_bill(people, total_bill):
	total= total_bill/ people 
	return total

def main():

	answer= raw_input("Enter 1 - if you want to calculate tip; enter 2 - if you want to split the bill")

	if answer == "1":
		bill = raw_input(int("How much was your bill?"))
		tip = tip_amount(bill)
		print bill
		print tip 

		answer2 = raw_input("Would you like to split the bill, enter 1 if yes, enter 2 if no")
		if answer2 == 1: 
			people = int(raw_input("How many ways do you want to split the bill"))
			total_bill = total_bill(tip, bill)
			cost_per_person = individual_bill(people, total_bill)
			print cost_per_person
		else: 
			print "Ok great!"
	if answer == 2:
		bill = raw_input(int("How much was your bill?"))
		tip = tip_amount(bill)
		people = int(raw_input("How many ways do you want to split the bill"))
		total_bill = total_bill(tip, bill)
		cost_per_person = individual_bill(people, total_bill)
		print cost_per_person
	


# print total_tip
# print tip_amount(100)
# print total_bill(total_tip, bill)


if __name__ == '__main__':
   main()
