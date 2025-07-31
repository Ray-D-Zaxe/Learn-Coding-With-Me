fun main() {
    var a = 5
    var b = 11
    var c = 15


    // If Statement
    if (a < b) println("a < b")
    
    // If-Else Statement
    if (a < b) println("a < b")
    else println("a > b")

    // If-Else-If Statement
    if (a < b) println("a < b")
    else if (a < c) println("a < c")
    else println("a > c")

    // Ternary Operator
    var max = if (a > b) a else b

    // Block Assignment
    max = if (a > b) {
        print("Choose a")
        a
    } else {
        print("Choose b")
        b
    }



    // When Expression
    when (a) {
        1 -> print("a is 1")
        2 -> print("a is 2")
        else -> print("a is neither 1 or 2")
    }

    // When Expression with multi-conditions
    when (a) {
        1, 2 -> print("a is 1 or 2")
        else -> print("a is neither 1 or 2")
    }

    // When Expression with Range
    when (a) {
        in 1..10 -> print("a is in the range 1..10")
        in 10..20 -> print("a is in the range 10..20")
        !in 10..20 -> print("a is outside the range 10..20")
        else -> print("a is not in the range 1..10")
    }

    // When Expression with Type
    when (a) {
        is Int -> print("a is an Int")
        is String -> print("a is a String")
        else -> print("a is neither an Int nor a String")
    }

    // When Assignment
    val txt = when (a) {
        1 -> "a is 1"
        2 -> "a is 2"
        else -> "a is neither 1 or 2"
    }
}