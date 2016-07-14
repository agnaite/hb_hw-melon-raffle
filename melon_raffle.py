from random import choice
import customer_info

"""Randomly pick customer and print customer info"""

# Add code starting here
# Hint: remember to import any functions you need from
    # other files or libraries


def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers)

    print "Contact {name} at {email} to notify them they've won".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        )

customers = customer_info.organize_customer_data("customers.txt")

pick_winner(customers)
