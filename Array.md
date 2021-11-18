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