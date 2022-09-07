# class Solution(object):
def containsDuplicate( nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if min(nums) > 0:
        return sum(nums)
    else:
        indexs = []
        for index, value in  enumerate(nums):
            if value < 0:
                indexs.append(index)
        




    # nums_new = set(nums)
    # if len(nums_new) == len(nums):
    #     return False
    # else:
    #     return True
    # nums = sorted(nums)
    #
    # for i in range(len(nums)-1):
    #     if nums[i+1] == nums[i]:
    #         return True
    # return False
if __name__ == '__main__':
    list =[1,2,3,1]
    print(containsDuplicate(list))
    # print()
