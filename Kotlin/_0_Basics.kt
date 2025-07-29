fun main() {
    // Data types in Kotlin
    // Kotline has several built-in data types

    // Numbers
    var var_Int: Int = 42                       // Int: 32-bit (4 Byte) signed integer, whole numbers from -2,147,483,648 to 2,147,483,647
    var bar_Byte: Byte = 17                     // Byte: 8-bit (1 Byte) signed integer, whole numbers from -128 to 127
    var var_Short: Short = 30000                // Short: 16-bit (2 Byte) signed integer, whole numbers from -32,768 to 32,767
    var var_Long: Long = 1234567890123L         // Long: 64-bit (8 Byte) signed integer, whole numbers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
    
    // Kotline by defaults uses Int unless the size reaches the limit, then it uses Long
    var var_Default_Long = 123L                 // Default Long value, can be used without 'L' suffix if it fits in Int range

    var var_Int2 : Int = 1_000_000              // Underscores are only for readability, and are ignored, must be used in between digits

    var var_Hex: Int = 0xFf_f                   // Hexadecimal representation, 0x prefix, _ are ignored, capatilazitaion doesn't matter, returns the integer equivalent
    var var_Binary: Int = 0b01_10               // Binary representation, 0b prefix, _ are ignored, returns the integer equivalent
    println("Hex: $var_Hex, Binary: $var_Binary")

    // Every Integer Number has an unsigned version
    var var_UInt: UInt = 42u                    // UInt: 32-bit (4 Byte) unsigned, whole numbers from 0 to 4,294,967,295
    var var_UByte: UByte = 17u                  // UByte: 8 (1 Byte), unsigned, whole numbers from 0 to 255
    var var_UShort: UShort = 30000u             // UShort: 16-bit (2 Byte) unsigned, whole numbers from 0 to 65,535
    var var_ULong: ULong = 1234567890123uL      // ULong: 64-bit (8 Byte) unsigned, whole numbers from 0 to 18,446,744,073,709,551,615

    
    // Floating-point numbers
    var var_Float: Float = 3_998.1_4f
    var var_Double: Double = 2_878.718_28

    // Kotlin by default uses Double for floating-point numbers
    var var_Float2: Float = 3.14f               // Float value, 'f' suffix is required for Float

    var var_Float3: Float = 1.0e10f             // Scientific notation, 1.0 * 10^10, 'f' suffix for Float
    var var_Double2: Double = 1.0e1_0           // Scientific notation, 1.0 * 10^10

    // Infinity and NaN (Not a Number), only present in floating-point types
    // 2 Infinities for the same signs and types are always equal
    var var_Double_Positive_Infinity: Double = Double.POSITIVE_INFINITY
    var var_Double_Negative_Infinity: Double = Double.NEGATIVE_INFINITY
    var var_Float_Positive_Infinity: Float = Float.POSITIVE_INFINITY
    var var_Float_Negative_Infinity: Float = Float.NEGATIVE_INFINITY
    
    // NaN is not equal to anything, even itself
    var var_Double_NaN: Double = Double.NaN
    var var_Float_NaN: Float = Float.NaN


    // Boolean values
    var var_Bool1: Boolean = true               // Generally 8-bit (1 Byte)
    var var_Bool2: Boolean = false
    var var_Bool3: Boolean = 1 > 2              // Boolean expression, evaluates to false
    

    // Characters, generally 16 bits (2 Bytes), Unicode characters
    var var_Char: Char = 'K'
    // Char requires single quotation ('')
    // Use escaped characters for special characters,
    /*
        \n - New Line (LF), Line Feed
        \t - Tab
        \' - Single Quote
        \" - Double Quote
        \\ - Backslash
        \r - Carriage Return (CR), used to return the cursor to the beginning of the line
        \b - Backspace
        \$ - Dollar Sign, used to escape dollar sign in string templates
        \uFFXX - Unicode character, where XX is the hexadecimal code point, FF41 is lowercase 'a'
     */

    

    // Strings, generally 16 bits (2 Bytes) per character
    var var_String: String = "Kotlin"
    // Strings can be defined using double quotes ("")
    // Escape characters can be used in strings as well
    // Use triple quotes (""") for multi-line strings, they preserve line breaks and indentation
    // Triple quotes can also be used to avoid escaping special characters



    // (is) operator is used to check the type of the variable
    if (var_Int is Char) {
        println("var_Int is of type Char")
    }
    else {
        println("var_Int is not of type Char")
    }

    // (!is) is used to check if the variable is not of a certain type
    if (var_Int !is Char) {
        println("var_Int is of type Char")
    }



    // Casting types
    // Use toInt(), toByte(), toShort(), toLong(), toFloat(), toDouble(), toUInt(), toUByte(), toUShort(), toULong() methods for casting
    var var_Cast_Float: Float = var_Int.toFloat()  // Casting Int to Float

    // unsafe casting using (as) operator
    var var_Cast_Unsafe: Any = "7"                  // Any type can hold any value, every non-nullable type inherits implicitly from Any
    var var_Cast_String: String = var_Cast_Unsafe as String
    
    // safe casting using (as?) operator, returns null if the cast fails
    var var_Cast_Safe: Any = 7
    var var_Cast_Safe_String: String? = var_Cast_Safe as? String

    
    // null
    
    // Using (?) after type makes that type nullable, i.e., allows it to be null
    val val_Null_Int: Int? = null
    var var_Null_Int: Int? = null

    // Elvis Operator (?:) returns the argument at the right if the argument at the left evaluates to null
    var var_Elvis_Int: Int = val_Null_Int ?: 7

    // Not null Assertion (!!) forces NullPointerException (NPE) if the argument at the left evaluates to null
    var var_Not_null_Assertion = var_Elvis_Int!!
}