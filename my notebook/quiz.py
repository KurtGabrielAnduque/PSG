def kadane(arr):
    max_current = max_global = arr[0]  # Initialize with the first element

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])  # Extend or start new subarray
        if max_current > max_global:
            max_global = max_current  # Update global max if needed

    return max_global  # Return the maximum sum found


# Example usage
arr = [-1,-2,3,4,8,-6,7,-9,11,12,13]
print("Maximum Subarray Sum:", kadane(arr))