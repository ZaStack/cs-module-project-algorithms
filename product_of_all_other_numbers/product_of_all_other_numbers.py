"""
Input: a List of integers
Returns: a List of integers
"""


def product_of_all_other_numbers(arr):
    # Your code here
    l = len(arr)

    if l == 1:
        print(0)
        return

    # Allocate memory for temp arrays
    left = [0] * l
    right = [0] * l

    # ALlocate memory for product array
    prod = [0] * l

    # Left most element of left array is always 1
    left[0] = 1

    # Right most element of right array is always 1
    right[l - 1] = 1

    # Construct left array
    for i in range(1, l):
        left[i] = arr[i - 1] * left[i - 1]

    # Construct right array
    for j in range(l - 2, -1, -1):
        right[j] = arr[j + 1] * right[j + 1]

    # Construct product array using left and right
    for i in range(l):
        prod[i] = left[i] * right[i]

    # print the constructed product array
    for i in range(l):
        print(prod[i], end="")

    return prod


if __name__ == "__main__":
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [
        2,
        6,
        9,
        8,
        2,
        2,
        9,
        10,
        7,
        4,
        7,
        1,
        9,
        5,
        9,
        1,
        8,
        1,
        8,
        6,
        2,
        6,
        4,
        8,
        9,
        5,
        4,
        9,
        10,
        3,
        9,
        1,
        9,
        2,
        6,
        8,
        5,
        5,
        4,
        7,
        7,
        5,
        8,
        1,
        6,
        5,
        1,
        7,
        7,
        8,
    ]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}"
    )
