"""Lab 1 ticket pricing. Test it against contract L1-L2, not against this code."""


def ticket_price(age, student):
    """Return the ticket price in cents.

    L1: age must be an integer from 0 through 120, else ValueError.
    L2: children (0-12) pay 500; adults (13-64) pay 1000, or 800 with a
        student card; seniors (65-120) pay 600. The student flag only
        changes the adult price.
    """
    if age < 0 or age > 120:
        raise ValueError("age must be between 0 and 120")
    if age <= 12:
        return 500
    if age > 65:
        return 600
    return 800 if student else 1000
