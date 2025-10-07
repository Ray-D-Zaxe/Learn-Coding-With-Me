void main(){
  print(greet("Robert", 27));
  final greeting = greet("Mario", 25);
  print(greeting);

  print(greet2("Yoo", 26));
  print(greet3("Yoo", 26));

  var greeting2 = greet4(age :27, name : "Yoo");
  print(greeting2);

  var greeting3 = greet4(age : 26);
  print(greeting3);
}

greet(name, age) {
  return "Hello, $name. You are $age years old.";
}

greet2(String name, int age) {
  // String name, int age, we have specified the data types
  return "Hello, $name. You are $age years old.";
}

String greet3(String name, int age) {
  // we have specified the return type
  return "Hello, $name. You are $age years old.";
}

String greet4({String? name, required int age}){
  // using {} lets us have optional (nullable) [using ?] and required [using the required keyword] parameters
  return "Hello, $name. You are $age years old.";
}

String greet5(String name, int age) => "Hello, $name. You are $age years old.";