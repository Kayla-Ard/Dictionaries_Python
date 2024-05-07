# 1. Read the problem out loud
# 2. Making assumptions, ask clarifying questions 
#   a. Communication is key 
# 3. Coming up with the approach (draw mental picture for myself & audience) 
#   a. Make sure they know what I am thinking and doing 
# 4. Write code out (this should take small amount of time)
# 5. Debug/ re-evaluate 

# Find Even numbers

# Create a function that, given a list as a parameter, finds the even numbers inside the list. The function should then return a list.
# Example:
# Input: [2, 7, 10, 11, 12]
# Output: [2, 10, 12]

numbers = [2, 7, 10, 11, 12]

def evens(nums):
    evens_list = []
    for i in nums:
        if i % 2 == 0:
            evens_list.append(i)
    return evens_list
print(evens(numbers)) 
