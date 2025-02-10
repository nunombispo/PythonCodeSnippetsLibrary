def validate_credit_card(card_number: str) -> bool:
    # Remove spaces and ensure the card number contains only digits
    card_number = card_number.replace(" ", "")
    if not card_number.isdigit():
        return False

    total = 0
    reverse_digits = card_number[::-1]

    for i, digit in enumerate(reverse_digits):
        d = int(digit)
        # For every second digit (when counting from 0), double it
        if i % 2 == 1:
            d *= 2
            # If doubling results in a number > 9, subtract 9 from it
            if d > 9:
                d -= 9
        total += d

    # A valid credit card number will have a total that is a multiple of 10
    return total % 10 == 0


# Example usage
card = "4539 1488 0343 6467"
print(validate_credit_card(card))  # Output: True (if the card number is valid)


# Why?
# This snippet implements the Luhn algorithm, a common checksum formula used to validate credit card numbers and
# other identification numbers.
# It’s a practical tool for payment processing systems, fraud detection, and any application that requires input
# validation for numerical identifiers.
