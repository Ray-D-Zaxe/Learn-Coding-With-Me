fun main() {
    // For Loop
    for (i in 1..5) {
        // i = 1, 2, 3, 4, 5
    }

    // While Loop
    var t = 1
    while (t <= 5) {
        // t = 1, 2, 3, 4, 5
        t++
    }

    // Do While Loop
    var k = 1
    do {
        // k = 1, 2, 3, 4, 5
        k++
    } while (k <= 5)

    // Nested Loop
    for (i in 1..10) {
        for (j in 1..10) {
            // i = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
            // j = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        }
    }



    // Break
    for (i in 1..10) {
        if (i == 5) {
            break
        }
        // i = 1, 2, 3, 4, 5
    }

    // Continue
    for (i in 1..10) {
        if (i == 5) {
            continue
        }
        // i = 1, 2, 3, 4, 6, 7, 8, 9, 10
    }



    // Break with Label
    loop@ for (i in 1..10) {
        for (j in 1..10) {
            if (i == 5) {
                break@loop
            }
            // i = 1, 2, 3, 4, 5
            // j = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        }
    }

    // Continue with Label
    loop@ for (i in 1..10) {
        for (j in 1..10) {
            if (i == 5) {
                continue@loop
            }
            // i = 1, 2, 3, 4, 6, 7, 8, 9, 10
            // j = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        }
    }
}