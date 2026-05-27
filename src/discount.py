def calculate_discount(purchase_amount: float, is_member: bool) -> float:
    
    """
    Rules: 
        - Purchases under $0 are invalid and should raise an error.
        - Purchases from $0 up to, but not including, $50 receive no discount.
        - Purchases of $50 or more receive a 10% discount.
        - Members receive an additional 5% discount on the final price after any other discounts are applied.
        
    returns the final price the customer has to pay
    """
    if purchase_amount < 0:
        raise ValueError("Purchase amount cannot be negative.")


    #Base discount calculation
    if purchase_amount > 50:
        price = purchase_amount * 0.9 
    else:
        price = purchase_amount 
        
    if is_member:
        price *= 0.95

    discount = 0.0

    return round(price, 2)