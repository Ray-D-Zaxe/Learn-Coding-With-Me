// This is a simple Kotlin program that prints "Hello World!" to the console.
// Only stuff inside the main() is executed
fun main() {
    println("Hello World!")

    // Kotlin comments work just like C comments
    // This is a single-line comment
    /*
     * This is a multi-line comment
     * It can span multiple lines
    */

// Indentation is not required
print("Yoo")                    // print() doesn't add a newline on its own
print(", sup mate?\n")



    // In Kotlin, constants are defined using 'val' and variables with 'var'
    val x = 5
    println(x)
    var a = 8
    println(a)

    // val values can't be changed or reassigned
    // x = 9 will thus cause an error
    a = 10                      // var values can be changed or reassigned
    println(a)

    // a = "Hello" would cause an error, as a is an Int data typr var
    // we can mention data types explicitly, but it's not necessary
    val y: Int = 10
    println(y)
    var b: Int = 20
    println(b)
    
    // We can format our output using string templates
    println("x = $x, y = $y, a = $a, b = $b")
    
    // Everything inside ${} is evaluated
    println("x + y = ${x + y}, a + b = ${a + b}")

    // Using format specifiers with format()
    println("x = %d, y = %d, a = %d, b = %d".format(x, y, a, b))
}
