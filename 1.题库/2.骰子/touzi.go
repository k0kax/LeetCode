package main

import (
	"fmt"
)

func numRollsToTarget(n int, k int, target int) int {
	mod := int(1e9) + 7
	dp := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]int, target+1)
	}
	dp[0][0] = 1

	for i := 1; i <= n; i++ {
		for j := 1; j <= target; j++ {
			for x := 1; x <= k && x <= j; x++ {
				dp[i][j] = (dp[i][j] + dp[i-1][j-x]) % mod
			}
		}
	}

	return dp[n][target]
}

// 示例测试
func main() {
	n := 1
	k := 6
	target := 3
	result := numRollsToTarget(n, k, target)
	fmt.Println(result)
}
