#Movie Ticket Booking Summary
c_name=input("Customer name:")
age=int(input("age:"))
num=int(input("Number of tickets:"))
ticket_price=0
if age<12:
    ticket_price=120
elif age>12 and age<=59:
    ticket_price=180
else:
    ticket_price=150
tot_amo=ticket_price*num
dis=0
tot_price_dis=tot_amo
if num>=5:
     dis=(tot_amo/100)*10
     tot_price_dis=tot_amo-dis
print(f"Customer Name: {c_name}")
print(f"Number of Tickets: {age}")
print(f"Total Before Discount: {tot_amo}")
print(f"Discount: {dis}")
print(f"Final Amount: {tot_price_dis }")
