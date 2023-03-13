computer_amount = int(input("Enter the number of computers: "))
in_business_hours = input("Is the service time in business hours? (yes/no): ").lower() == "yes"
drop_off_pick_up = input("Is the customer willing to drop off and pick up? (yes/no): ").lower() == "yes"

if computer_amount == 1 or computer_amount == 2:
    base_fee = 50
    additional_fee = 0
elif 3 <= computer_amount <= 10:
    base_fee = 100
    additional_fee = 10
else:
    base_fee = 500
    additional_fee = 10

peripheral_count = int(input("Enter the number of peripherals: "))
additional_fee *= peripheral_count

if not in_business_hours:
    base_fee *= 2

if drop_off_pick_up:
    total_base_fee = base_fee / 2
else:
    total_base_fee = base_fee

total_fee = total_base_fee + additional_fee
print(f"Total fee: ${total_fee:.2f}")
