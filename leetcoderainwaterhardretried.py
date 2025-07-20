class Solution:
    def trap(self, height) -> int:
        n = len(height)
        if n == 0:
            return 0

        left = [0] * n
        right = [0] * n
        trappedWater = 0

        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])

        right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        print(left)
        print(right)    

        for i in range(n):
            minHeight = min(left[i], right[i])
            trappedWater += minHeight - height[i]

        return trappedWater

# Test
solution = Solution()
print(solution.trap([4, 2, 0, 3, 2, 5]))  # Output: 9
