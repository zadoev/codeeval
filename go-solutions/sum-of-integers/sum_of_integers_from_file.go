package main

import (
	"fmt"
	"bufio"
	"os"
	"strings"
)

func main() {
	file, _ := os.Open(os.Args[1])

	defer file.Close()

	scanner := bufio.NewScanner(file)

	var sum uint = 0

	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		var number uint
		fmt.Sscanf(line, "%d", &number)
		sum += number
	}

	fmt.Println(sum)
}
