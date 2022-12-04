package main

import (
	"flag"
	"fmt"
	"log"
	_ "net/http/pprof"
	"os"
	"runtime/pprof"
)

var cpuprofile = flag.String("cpuprofile", "", "write cpu profile to `file`")

func main() {
	flag.Parse()
	if *cpuprofile != "" {
		f, err := os.Create(*cpuprofile)
		if err != nil {
			log.Fatal("could not create CPU profile: ", err)
		}
		defer f.Close() // error handling omitted for example
		if err := pprof.StartCPUProfile(f); err != nil {
			log.Fatal("could not start CPU profile: ", err)
		}
		defer pprof.StopCPUProfile()
	}

	bytes, _ := os.ReadFile("input.txt")
	// bytes, _ := os.ReadFile("test.txt")
	puzzleInput := string(bytes)
	fmt.Println("Answer1", Answer1(puzzleInput))
	fmt.Println("Answer2", Answer2(puzzleInput))
}

// 477 is to high

func Answer1(puzzleInput string) int {
	values := MakeValues(puzzleInput)
	answer := 0
	for i := 0; i < len(values); i++ {
		if values[i].start1 != 0 {
			if values[i].start1 <= values[i].start2 && values[i].end1 >= values[i].end2 {
				// fmt.Println("2 in 1:\t ", i, values[i].start1, values[i].end1, values[i].start2, values[i].end2)
				answer++
			} else if values[i].start2 <= values[i].start1 && values[i].end2 >= values[i].end1 {
				// fmt.Println("1 in 2:\t ", i, values[i].start1, values[i].end1, values[i].start2, values[i].end2)
				answer++
			}
		}
	}
	return answer
}

func Answer2(puzzleInput string) int {
	values := MakeValues(puzzleInput)
	answer := 0
	for i := 0; i < len(values); i++ {
		if values[i].start1 != 0 {
			if values[i].start2 >= values[i].start1 && values[i].start2 <= values[i].end1 {
				// fmt.Println("2 in 1:\t ", i, values[i].start1, values[i].end1, values[i].start2, values[i].end2)
				answer++
			} else if values[i].start1 >= values[i].start2 && values[i].start1 <= values[i].end2 {
				// fmt.Println("1 in 2:\t ", i, values[i].start1, values[i].end1, values[i].start2, values[i].end2)
				answer++
			}
		}
	}
	return answer
}
