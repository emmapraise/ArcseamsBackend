
# Order Status
CANCELED = 0
PENDING = 1
ACCEPTED = 2
PAID = 3
SHIPPED =4
COMPLETED = 5


def order_status():
    """Enum field for order status"""
    status = [
        (PENDING, "Pending"),
        (CANCELED, "Canceled"),
        (ACCEPTED, "Accepted"),
        (PAID, "Paid"),
        (SHIPPED, "Shipped"),
        (COMPLETED, "Completed"),
    ]
    return status
