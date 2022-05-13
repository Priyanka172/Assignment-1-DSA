#using sorting

def find_pair(nums,target):

    #sorting the nums in increasing order
    nums.sort()

    #find the low and high endpoints

    (low, high) = (0, len(nums)-1)

    #now we have endpoints we can reduce the search for every iteration

    #loop till search space is exhausted

    while low < high:
        if nums[low] + nums[high] == target: #here low and high are indexes 
            print("Pair found", (nums[low], nums[high]))
            return
        #we can increment 'low' if the total is less than target 
        #we can decrement 'high' if the total is greater than target

        if nums[low] + nums[high] < target:
            low = low + 1
        else:
            high = high - 1
        
    #no pair found 
    print("No pair found")

if __name__ == '__main__':
 
    nums = [8, 7, 2, 7, 3, 1]
    target = 10
 
    find_pair(nums, target)
