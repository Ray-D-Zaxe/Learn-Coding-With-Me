void main(){
  print("Hello World!!!");
  
  
  
  // This is a comment in dart
  
  /*
    This is a multi-line comment
    in dart
  */



  var name = "Yoo";           // declares a string variable called name
  print(name);                // prints, Yoo

  final age = 26;             // declares an integer variable called age with the final value 26
  print(age);                 // prints, 26

  const pi = 3.14;            // declares a constant variable called pi
  print(pi);                  // prints, 3.14



  // final keyword is used to create a runtime constant
  // so its used when we don't know what the value will be at compile time
  // i.e, when the value of var is dependent on external factors
  
  // const keyword is used to create a compile time constant



  print("Name : " + name);     // prints, Name : Yoo
  print("Name : $name");       // prints, Name : Yoo
  print("Age : $age");         // prints, Age : 26
}