def solution(nums, target):
    nums_index = []
    for i, item in enumerate(nums):
        nums_index.append((item, i))
    nums_index.sort(key =lambda x:x[0])
    lower = 0
    higher = len(nums_index) - 1
    while True:
        lower_num = nums_index[lower][0]
        higher_num = nums_index[higher][0]
        cur_sum = lower_num + higher_num
        if cur_sum == target:
            return [nums_index[lower][1], nums_index[higher][1]]
        elif cur_sum < target:
            lower+=1
        elif cur_sum > target:
            higher-=1


    
print(solution( [3,2,4], 6))
print(solution([3,3], 6))
print(solution([2,7,11,15], 9))