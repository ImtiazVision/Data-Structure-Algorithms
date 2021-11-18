**Array** : An array is a grouping of things. Items might be numbers, strings, DVDs, video games, novels, or anything else. The elements are saved in memory regions that are close together (contiguous). Because they're stored together, it's simple to go through the full collection of items.

**Array Capacity**: the maximum number of elements that an array can contain at any one moment.

**Array Length**: the number of elements in the array at any given time. Example:

```
// Create a new array with a capacity of 7.
int[] array = new int[7];

// Current length is 0, because it has 0 elements.
int length = 0;

// Add 4 items into it.
for (int i = 0; i < 4; i++) {
    array[i] = i * i;
    // Each time we add an element, the length goes up by one also known as the 'increment'.
    length++;
}

System.out.println("The Array has a capacity of " + array.length);
System.out.println("The Array has a length of " + length);
```

1. **Description** : Find the max consecutive 1's in an array. In another words, find the longer contiguous segments of ones than zeros

  **Solution** :
```
    class Solution {
      public int findMaxConsecutiveOnes(int[] nums) {
        int count = 0;
        int maxCount = 0;
        for(int i = 0; i < nums.length; i++) {
          if(nums[i] == 1) {
            // Increment the count of 1's by one.
            count += 1;
          } else {
            // Find the maximum till now.
            maxCount = Math.max(maxCount, count);
            // Reset count of 1.
            count = 0;
          }
        }
        return Math.max(maxCount, count);
      }
    }
```

2. **Description** : Return the indices of the two numbers so that they add up to target given an array of integers nums and an integer target.

  **Solution** :
```
    class Solution {
        public int[] twoSum(int[] nums, int target) {
            for (int i = 0; i < nums.length; i++) {
                for (int j = i + 1; j < nums.length; j++) {
                    if (nums[j] == target - nums[i]) {
                        return new int[] { i, j };
                    }
                }
            }
            // If there is no solution, we will just return null.
            return null;
        }
    }
```