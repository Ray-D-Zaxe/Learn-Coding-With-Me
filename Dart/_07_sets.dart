void main() {
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
}