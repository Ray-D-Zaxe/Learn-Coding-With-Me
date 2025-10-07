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



  // Types
  String name2 = "Casenova";        // String var
  name2 = "Rashputin";
  final int age2 = 26;              // Integer final var
  double pi2 = 3.14;                // Double var
  const bool isTrue = true;         // Boolean const var

  print(name2);
  print(age2);
  print(pi2);
  print(isTrue);

  int? nullAbleVar;                 // nullAbleVar can be null
  print(nullAbleVar);



  // Data Structures

  // Lists
  var list1 = [1, 2, 3, "Yoo"];
  // While a list can contain multiple diffrent data types
  // after initilization, all elements must be of same type(s)
  // We can use <> to specify the data types we want inside our list
  List<int> list3;
  // The list above and below can only ever contain integers
  var scores = [1, 2, 3, 4, 5];
  // printing lists
  print(scores);
  print(scores[0]);
  // Changing values inside lists
  scores[0] = 100;
  print(scores);
  // Adding new values
  scores.add(2);
  print(scores);
  // Removing values, removes the first instance/occurence if the element
  scores.remove(2);
  print(scores);
  // Removes the last element
  scores.removeLast();
  print(scores);
  // returns the length of the list
  print(scores.length);
  // shuffels the list in arandom order
  scores.shuffle();
  print(scores);
  // returns the index of the first occurence of the element and -1 if the element doesn't exist
  print(scores.indexOf(2));
  print
  (scores.
  indexOf(3));


  // Sets
  var set1 = {1, 2, 5, 3, "Yoo"};
  print(set1);
  // duplicates are ignored
  Set<String> names = {"mario", "luigi", "yoshi", "mario"};
  print(names);
  names.add("peach");
  print(names);
  names.add("luigi");
  print(names);
  names.remove("peach");
  print(names);


  // Maps, basically dictionaries
  Map<String, String> planets = {
    "First" : "mercury",
    "Second" : "venus",
    "Third" : "earth",
    "Fourth" : "mars",
    "Fifth" : "jupiter"
  };
  print(planets);
  print(planets["First"]);
  planets["Fifth"] = "abcdefg";
  print(planets);
  planets["Sixth"] = "saturn";
  print(planets);
  print(planets.containsKey("Third"));
  print(planets.containsKey("Seventh"));
  print(planets.containsValue("earth"));
  print(planets.containsValue("Seventh"));
  planets.remove("Fifth");
  print(planets);
  print(planets.keys);
  print(planets.values);
}