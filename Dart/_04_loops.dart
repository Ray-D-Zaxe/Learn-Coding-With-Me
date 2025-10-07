void main(){
  for(int i = 0; i < 5; i++)
    print(i);
  print("Yo");

  List<int> scores = [10, 20, 30, 40, 50];
  for (int i = 0; i < scores.length; i++) {
    print("The score is: ${scores[i]}");
  }
  
  for (int score in scores) {
    print("The score is: $score");
  }

  for (int score in scores.where((s) => s > 20)) {
    print("The score: $score");
  }

}