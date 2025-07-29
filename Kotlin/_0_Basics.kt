fun main() {
    // Data types in Kotlin
    // Kotline has several built-in data types

    // Numbers
    var var_Int: Int = 42                       // Int: 32-bit signed integer, whole numbers from -2,147,483,648 to 2,147,483,647
    var bar_Byte: Byte = 17                     // Byte: 8-bit signed integer, whole numbers from -128 to 127
    var var_Short: Short = 30000                // Short: 16-bit signed integer, whole numbers from -32,768 to 32,767
    var var_Long: Long = 1234567890123L         // Long: 64-bit signed integer, whole numbers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
    
    // Kotline by defaults uses Int unless the size reaches the limit, then it uses Long
    var var_Default_Long = 123L                 // Default Long value, can be used without 'L' suffix if it fits in Int range
    var var_Float: Float = 3.14f
    var var_Double: Double = 2.71828
    var var_Char: Char = 'K'
    var var_String: String = "Kotlin"
    var var_Boolean: Boolean = true
}