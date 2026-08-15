def calculate_total(price, quantity):
    return price * quantity


def calculate_discount(total, discount_rate=10):
    discount = total * discount_rate / 100
    return total - discount


def main():
    price = 100
    quantity = 2

    total = calculate_total(price, quantity)
    final_amount = calculate_discount(total)

    print(f"Total amount: ₹{total}")
    print(f"Final amount after 10% discount: ₹{final_amount}")


if __name__ == "__main__":
    main()
