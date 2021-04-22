"""
There are two stacks of cards.

I want to draw one card from the left stack and one card from the right stack,
so that the product of the two numbers is the largest.
How can you find the largest product?

1. The function max_product takes a list left_cards and a list right_cards as parameters.
2. Left_cards is the number of the left stack, right_cards is the number of the right stack, and max_product returns the maximum value
when multiplying by drawing one card from left_cards and one card from right_cards.

"""


def max_product(left_cards, right_cards):
    max_number = 0
    for left_index in range(len(left_cards)):
        for right_index in range(len(right_cards)):
            result = left_cards[left_index] * right_cards[right_index]
            if max_number < result:
                max_number = result
    return max_number


print(max_product([1, 6, 5, 2], [4, 2, 3, 1]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))