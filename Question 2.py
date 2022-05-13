def reverse_array(arr):

    #simple solution can be obtained by traversing the array in reverse order

    for i in range(len(arr)-1,-1,-1):
        print(arr[i])
        
    
if __name__ == '__main__':

    arr = [1,2,3,4,5,6,7]

    reverse_array(arr)