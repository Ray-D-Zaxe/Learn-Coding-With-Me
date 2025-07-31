fun main() {
    // Assignment Operator
    var a = 56                          // assigns the value 56 to a
    a += 4                              // a becomes a + 4, i.e, 60
    a -= 20                             // a becomes a - 20, i.e, 40
    a *= 2                              // a becomes a * 2, i.e, 80
    a /= 2                              // a becomes a / 2, i.e, 40
    a %= 3                              // a becomes a % 2, i.e, 1, i.e, the remainder or mod/modulus



    // Arithmetic Operators
    var b = 10
    a + b                               // evaluates to: a + b, i.e, 11, uses a.add(b)
    a - b                               // evaluates to: a - b, i.e, 9, uses a.minus(b)
    a * b                               // evaluates to: a * b, i.e, 100, uses a.times(b)
    a / b                               // evaluates to: a / b, i.e, 5, uses a.div(b)
    a % b                               // evaluates to: a % b, i.e, 1, i.e, the remainder or mod/modulus, uses a.mod(b)



    // Unary Operators
    a++                                 // evaluates to: a, then adds 1
    a--                                 // evaluates to: a, then subtracts 1
    ++a                                 // evaluates to: a + 1, uses a.inc()
    --a                                 // evaluates to: a - 1, uses a.dec()
    
    a = -1
    +a                                  // evaluates to: -1, uses a.unaryPlus()
    -a                                  // evaluates to: 1, uses a.unaryMinus()

    var c: Boolean = true
    !c                                  // evaluates to: false, uses a.not()

    
    
    // Comparison Operators
    a > b                               // evaluates to: false
    a < b                               // evaluates to: true
    a == b                              // evaluates to: false
    a != b                              // evaluates to: true
    a >= b                              // evaluates to: false
    a <= b                              // evaluates to: true



    // Logical Operators
    true && false                              // evaluates to: false
    true || false                              // evaluates to: true
}