"""
1.1 Get product of all other elements.

Given an array of integers, return a new array such that each element at index i of
the new array is a product of all the numbers in the original array except the one at i.

E.g, if our input is [3, 2, 1] the expected output would be [2, 3, 6]
E.g, if our input is [1, 2, 3, 4, 5] the expected output would be [120, 60, 40, 30, 24]
"""


def solution(arr):
    """
    Find the arrays product and divide by number in array

    Time: O(n) - looping through the array to sum
    Space: O(n) - creating a new results array
    """
    product = 1
    for num in arr:
        product *= num

    res = []
    for num in arr:
        res.append(product / num)

    return res


def solution_2(arr):
    """
    Product at i is equal to prefix_products[i-1] * suffix_products[i+1]

    Time: O(n)
    Space: O(n) - creating two new arrays
    """

    # compute a rolling window of products by using the previous value * current value
    prefix_products = []
    for num in arr:
        prefix_products.append(prefix_products[-1] * num) if prefix_products else prefix_products.append(num)

    # computer a rolling window of suffixed products
    suffix_products = []
    for num in reversed(arr):
        suffix_products.append(suffix_products[-1] * num) if suffix_products else suffix_products.append(num)
    suffix_products = suffix_products[::-1]

    # Calculate the products using pre-computed products
    result = []
    for i in range(len(arr)):
        # print(result, i)
        if i == 0:
            result.append(suffix_products[i+1])
        elif i == len(arr)-1:
            result.append(prefix_products[i-1])
        else:
            result.append(prefix_products[i-1] * suffix_products[i+1])

    print('prefix', prefix_products, 'suffix', suffix_products)
    return result


if __name__ == '__main__':
    for f in [solution_2]:
        print(f([3, 2, 1]))
        print(f([1, 2, 3, 4, 5]))
