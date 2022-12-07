array = [5, 1, 9, 6, 1]
# def largestNumber(array):
#     loop = 0
#     first = array[loop]
#     largest = 0
#     count = 0  
#     for x in array:
#         if x > first:
#             largest = x
#         count += 1
#         if loop < count - 1:
#             loop += 1
#         first = array[loop]
#     return largest

# remove = largestNumber(array)
# array2 = array
# array2.remove(remove)
# print(largestNumber(array2))

array.sort()
print(array[-2])