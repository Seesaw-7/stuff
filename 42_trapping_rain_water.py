class Solution:
    # Time limit
    def trap1(self, height: list[int]) -> int:
        n = len(height)
        start = 0 # position of the currant left bar
        level = 0 # height of the currant left bar
        water = [0 for _ in range(n)] # water capacity

        for i,num in enumerate(height):
            if num >= level:
                for j in range(start+1, i):
                    water[j] = level - height[j]
                start = i
                level = num
            else:
                for j in range(start+1, i):
                    water[j] = max(num - height[j], water[j])

        return sum(water)

    # O(N) with DP and Two-pass, first iterate forward, then iterate backward
    def trap2(self, height: list[int]) -> int:
        n = len(height)
        water = [0 for _ in range(n)]
        left = right = 0

        for i,num in enumerate(height):
            if num > left:
                left = num
            water[i] = left - num

        for i,num in reversed(list(enumerate(height))):
            if num > right:
                right = num
            water[i] = min(water[i], right-num)

        return sum(water)

    # Using stack and finishing up little by little
    # seems to be O(N^2), but each elt in the stack can be put in and poped out only once, 
    # So still O(N) despite the while loop
    def trap(self, height: list[int]) -> int:
        n = len(height) # Number of elements in the height list
        water = 0       # Initialize the total trapped water volume
        stack = []      # Stack to store indices of height elements
        # Iterate through the heights
        for right in range(n):
            # Process each height to trap water
            while stack and height[stack[-1]] < height[right]:
                # If the current height is greater than the height at the top of the stack
                mid = stack.pop() # Get the index of the height at the top of the stack
                # If the stack becomes empty, no more water can be trapped
                if not stack:
                    break
                left = stack[-1]                                                          # Get the index of the next height from the top of the stack
                minHeight = min(height[right] - height[mid], height[left] - height[mid]) # Calculate the minimum height of the two borders
                width = right - left - 1                                                 # Calculate the width between the left and right borders
                water += minHeight * width                                                # Calculate the trapped water volume and add it to the total
            stack.append(right) # Push the current index onto the stack
        return water # Return the total trapped water volume
    