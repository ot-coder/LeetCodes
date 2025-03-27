def trap(height):
    if not height or len(height) < 3:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    result = 0
    while left < right:
        if left_max < right_max:
            left += 1
            # Water trapped at current position = max possible height - current height
            result += max(0, left_max - height[left])
            # Update left_max if we found a higher bar
            left_max = max(left_max, height[left])
        else:
            right -= 1
            # Water trapped at current position = max possible height - current height
            result += max(0, right_max - height[right])
            # Update right_max if we found a higher bar
            right_max = max(right_max, height[right])
    return result