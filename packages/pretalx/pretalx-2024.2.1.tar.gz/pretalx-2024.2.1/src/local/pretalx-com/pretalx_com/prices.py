PRICES = {
    "attendee_steps": ["0-100", "100-200", "200-300", "300-400", "400-500", "500+"],
    "ticket_steps": [
        "EUR 0-100",
        "EUR 100-200",
        "EUR 200-300",
        "EUR 300-400",
        "EUR 400-500",
        "EUR 500+",
    ],
    "price_steps": [],  # First price, then attendees
}


def print_prices():
    row_format = "{:>15}" * (len(PRICES["ticket_steps"]) + 1)
    print(row_format.format("", *PRICES["attendee_steps"]))
    for price, row in zip(PRICES["ticket_steps"], PRICES["price_steps"]):
        print(row_format.format(price, *row))


for attendees in range(len(PRICES["attendee_steps"])):
    prices = []
    for price in range(len(PRICES["ticket_steps"])):
        prices.append(((attendees + 1) * 100) * ((price + 1) * 100) * 0.005 + 149)
    PRICES["price_steps"].append(prices)
