
from enum import Enum
from directCLASSES import VisitorCategory

# Importing classes from directCLASSES.py
from directCLASSES import Visitor, Item, Artwork, Exhibition, Ticket, SpecialEvent

#TEST CASES

#adding Mona Lisa artwork to the Louvre

mona_lisa = {"title": "Mona Lisa" , "color": "Various","artist":"Leonardo da Vinci", "date_of_creation":"1503-1506","historical_significance": "Renaissance masterpiece"}
if mona_lisa["title"] == "Mona Lisa" and mona_lisa["artist"] == "Leonardo da Vinci":
    print("Mona Lisa artwork added successfully")
else:
    print("Failed to add Mona Lisa artwork")


# opening a new exhibition that features the mona lisa

exhibition = {"name": "Mona Lisa Exhibition" , "duration": "6 weeks", "location" : "Grand Gallery"}
if exhibition["name"] == "Mona Lisa Exhibition" and exhibition["duration"] == "6 weeks":
    print("Mona Lisa exhibition opened successfully")
else:
    print("Failed to open Mona Lisa Exhibition")


# purchasing tickets for the mona lisa exhibition
ticket = {"exhibition_name": "Mona Lisa Exhibition", "ticket_date": " 1-1-2024", "visitor_type": "Individual","duration": "6 weeks", "location": "Grand Gallery","visitor_category": VisitorCategory.ADULT,"ticket_price": 50 }
if ticket["exhibition_name"] == "Mona Lisa Exhibition" and exhibition["duration"] == "6 weeks":
    print("Ticket purchaed successfully")
else:
    print("Purchase Failed")


# Test case for displaying payment receipt for Mona Lisa exhibition ticket
total_cost = ticket["ticket_price"]
receipt = f"Thank you for purchasing! Your total cost for the Mona Lisa exhibition ticket is ${total_cost}."
if receipt == "Thank you for purchasing! Your total cost for the Mona Lisa exhibition ticket is $30.":
    print("Payment receipt displayed correctly.")
else:
    print("Failed to display payment receipt.")

print("All test cases executed.")
