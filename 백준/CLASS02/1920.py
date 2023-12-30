def binary_search (arr, target, start, end):
    
    if start > end:
        return 0
    
    mid = (start + end) // 2
    
    if arr[mid] == target:
        return 1

    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
  
    else:
        return binary_search(arr, target, mid+1, end)

    
num1 = open('input.txt', 'rt').read().split('\n')[0]
lst_A = sorted(list(map(int, open('input.txt', 'rt').read().split('\n')[1].split(' '))))
num2 = open('input.txt', 'rt').read().split('\n')[2]
lst_B = list(map(int, open('input.txt', 'rt').read().split('\n')[3].split(' ')))
print(lst_B)
for num in lst_B:
    left = 0 
    right = len(lst_A)-1
    print(binary_search(lst_A, num, left, right))
   