def calculate_final_price(amount,time):
    if amount<=0 or time<=0:
        raise ValueError("Amount or time cannot be zero")
    return (amount + (amount*.1*time)/100)