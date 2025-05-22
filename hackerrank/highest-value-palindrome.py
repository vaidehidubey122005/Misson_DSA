from collections import Counter

def highest_palindrome(n: int) -> int:
    # Convert number to a list of digits
    digits = list(str(n))
    
    # Count the frequency of each digit
    count = Counter(digits)
    
    # Separate digits with odd counts for the middle part (only one allowed)
    odd_count_digit = None
    first_half = []
    
    # Try to form the largest possible palindrome
    for digit in sorted(count.keys(), reverse=True):  # Sort digits in descending order
        freq = count[digit]
        if freq % 2 != 0:
            if odd_count_digit is None:  # If no odd middle digit exists yet
                odd_count_digit = digit
            else:
                return -1  # If more than one odd count exists, can't form palindrome
        
        # Add half of the even frequency digits to the first half
        first_half.extend([digit] * (freq // 2))
    
    # Form the first half of the palindrome (largest possible)
    first_half = ''.join(first_half)
    
    # The second half of the palindrome is the reverse of the first half
    second_half = first_half[::-1]
    
    # If there is a middle digit (for odd length palindrome)
    if odd_count_digit:
        return int(first_half + odd_count_digit + second_half)
    else:
        return int(first_half + second_half)
