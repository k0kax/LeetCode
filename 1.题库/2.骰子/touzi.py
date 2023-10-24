"""
这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。

给定三个整数 n ,  k 和 target ，返回可能的方式(从总共 kn 种方式中)滚动骰子的数量，使正面朝上的数字之和等于 target 。

答案可能很大，你需要对 109 + 7 取模 。

 

示例 1：

输入：n = 1, k = 6, target = 3
输出：1
解释：你扔一个有 6 个面的骰子。
得到 3 的和只有一种方法。

"""


def numRollsToTarget(n, k, target):
    mod = 10**9 + 7
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            for x in range(1, min(k, j) + 1):
                dp[i][j] = (dp[i][j] + dp[i - 1][j - x]) % mod

    return dp[n][target]


# 示例测试
n = 1
k = 6
target = 3
result = numRollsToTarget(n, k, target)
print(result)