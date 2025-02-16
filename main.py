"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if x ==0:
        return 0
    if x ==1:
        return 1
    return foo(x-1) +foo(x-2)
    pass

def longest_run(mylist, key):
    run = 0
    longest_run =0
    for i in mylist:
        if i == key:
            run = run+1
        else:
            if run>longest_run:
                longest_run = run
            run = 0
    if run > longest_run:
        longest_run = run
    return longest_run
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
        """
        Recursive divide-and-conquer approach to find the longest contiguous sequence of `key` in `myarray`.
        """

        def helper(left, right):
            # Base case: For a single element list
            if left == right:
                if mylist[left] == key:
                    return Result(1, 1, 1, True)  # Single key element: all metrics are 1
                else:
                    return Result(0, 0, 0, False)  # Single non-key element: all metrics are 0

            mid = (left + right) // 2
            left_result = helper(left, mid)
            right_result = helper(mid + 1, right)

            # Compute the longest contiguous run crossing the middle
            left_size = left_result.left_size
            right_size = right_result.right_size

            if left_result.is_entire_range:
                left_size += right_result.left_size  # Left part contributes to left run

            if right_result.is_entire_range:
                right_size += left_result.right_size  # Right part contributes to right run

            # Compute cross-boundary maximum contiguous run
            cross_best = 0
            if mylist[mid] == key and mylist[mid + 1] == key:
                cross_best = left_result.right_size + right_result.left_size

            # Determine the longest sequence in this segment
            longest_size = max(left_result.longest_size, right_result.longest_size, cross_best)

            # Check if the entire range consists of `key`
            is_entire_range = left_result.is_entire_range and right_result.is_entire_range

            return Result(left_size, right_size, longest_size, is_entire_range)

        if not mylist:
            return 0  # Edge case: empty array

        return helper(0, len(mylist) - 1).longest_size



