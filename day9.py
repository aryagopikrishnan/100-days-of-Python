#Dictionaries

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >=81:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)

#-------------------------------------------------------------------

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country, num_visits, cities):
    travel_log.append({"country" : country,"visits" : num_visits, "cities":cities})


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


#-------------------------------------------------------------------------------------

# Auction program


#HINT: You can call clear() to clear the output in the console.

auction_bids = {}
bidding_finsihed = False

def finding_highest_bid(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
    


while not bidding_finsihed:
  name = input("What is your name?")
  bid = int(input("What is your bid? $"))
  auction_bids[name] = bid
  should_continue = input("Anymore bidders? yes or no: ")
  if should_continue == "no":
    bidding_finsihed = True
  

finding_highest_bid(auction_bids)



