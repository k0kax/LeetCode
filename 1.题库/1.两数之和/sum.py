#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
#同时列出数据和数据下标，一般用在 for 循环当中
def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):#i 键，num值
        complement = target - num#求差值
        if complement in num_dict:#插值是否在新的字典里
            return [num_dict[complement], i]#如果在，返回键值，键索引
        num_dict[num] = i #当前数字 num 作为键，索引 i 作为值，将其添加到字典 num_dict 中，以便后续查找
    return []

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)