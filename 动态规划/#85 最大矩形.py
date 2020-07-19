# 纯粹的广告牌问题
def cal_max_area(nums):
    '''
    :param nums: 每一行的高度数组
    :return:
    '''
    dp = [0] * len(nums)
    for i in range(len(nums)):
        if i == 0:
            dp[i] = nums[i]
        else:
            # 首先向左右找连续的大于等于nums[i]的列数
            count = 0
            for j in range(i, -1, -1):
                if nums[j] >= nums[i]:
                    count += 1
                else:
                    break
            for j in range(i+1, len(nums)):
                if nums[j] >= nums[i]:
                    count += 1
                else:
                    break
            dp[i] = max(dp[i-1], min(nums[: i+1]) * (i+1), count * nums[i])
    return max(dp)

def maximalRectangle(matrix):
    '''
    # 跟广告牌思路一样的
    ## 相当于现在可以一层一层，假设矩形地的底以此为第0 1 2 …… 层
    dp[i][j]: 记录以 i，j为右下角
    max_area: 记录最大面积
    '''
    width = len(matrix)
    length = len(matrix[0])
    max_area = 0
    for row in range(width):
        nums = [0] * length
        for idx, num in enumerate(matrix[row]):
            if matrix[row][idx] == 0:
                nums[idx] = 0
            else:
                for col in range(row, -1, -1):
                    if matrix[col][idx] == '1':
                        nums[idx] += 1
                    else:
                        break
        max_area = max(max_area, cal_max_area(nums))
    return max_area

matrix = [["0","1","1","0","1"],
          ["1","1","0","1","0"],
          ["0","1","1","1","0"],
          ["1","1","1","1","0"],
          ["1","1","1","1","1"],
          ["0","0","0","0","0"]]

maximalRectangle(matrix)




