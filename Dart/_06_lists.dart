void main(){
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
}