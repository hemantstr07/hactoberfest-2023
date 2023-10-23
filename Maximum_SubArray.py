# Python3 program to find Maximum Product Subarray

# Returns the product of max product subarray.


def maxSubarrayProduct(arr, n):

	# Initializing result
	result = arr[0]

	for i in range(n):

		mul = arr[i]

		# traversing in current subarray
		for j in range(i + 1, n):

			# updating result every time
			# to keep an eye over the maximum product
			result = max(result, mul)
			mul *= arr[j]

		# updating the result for (n-1)th index.
		result = max(result, mul)

	return result


# Driver code
arr = [1, -2, -3, 0, 7, -8, -2]
n = len(arr)
print("Maximum Sub array product is", maxSubarrayProduct(arr, n))

# This code is contributed by divyeshrabadiya07
