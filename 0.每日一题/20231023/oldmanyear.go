package main

import (
	"fmt"
	"strconv"
	"sync"
)

func countElderlyPassengers(details []string) int {
	count := 0

	for _, passenger := range details {
		age, _ := strconv.Atoi(passenger[11:13]) // 获取乘客的年龄部分并转换为整数
		if age > 60 {
			count++
		}
	}
	return count
}

func countSeniors(details []string) int {
	count := 0
	wg := sync.WaitGroup{}
	mu := sync.Mutex{}

	for _, passenger := range details {
		wg.Add(1)
		go func(p string) {
			defer wg.Done()

			age, _ := strconv.Atoi(p[11:13]) // 获取乘客的年龄部分并转换为整数
			if age > 60 {
				mu.Lock()
				count++
				mu.Unlock()
			}
		}(passenger)
	}

	wg.Wait()

	return count

}

func main() {
	details := []string{"7868190130M7522", "5303914400F9211", "9273338290F4010"}
	elderlyCount := countElderlyPassengers(details)
	fmt.Println("年龄大于 60 岁的乘客人数:", elderlyCount)
	count := countSeniors(details)
	fmt.Println(count)
}
