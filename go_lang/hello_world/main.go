package main

import "fmt"

func main() {
	fmt.Println("Hello World!")
	// This is a comment
	/*
		This is a multi-line comment
	*/

	var x int = 10
	fmt.Println(x)

	var y = 20
	fmt.Println(y)

	z := 30
	fmt.Println(z)

	var a, b = 10, 20
	fmt.Println(a, b)

	var aa int8 = 10 // 8-bit integer var hehe
	fmt.Println(aa)

	var ab int16 = 10 // 16-bit integer var
	fmt.Println(ab)

	// var int can be 8, 16, 32, 64
	var ac int64 = 10 // 64-bit integer var
	fmt.Println(ac)

	// var float can only be 32 or 64 but never empty
	var f32 float32 = 3.14
	fmt.Println(f32)

	var ba byte = 'A'
	// returns the ASCII value??
	fmt.Println(ba)

	var s string = "Hello World!"
	fmt.Println(s)

	var bb bool = true
	fmt.Println(bb)

	var bc complex64 = 1 + 2i
	// complex can be 64 or 128 but never empty
	fmt.Println(bc)
}
