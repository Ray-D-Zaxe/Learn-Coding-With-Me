void main() async {

  // Futures --> like promises in JavaScript
  // can have uncompleted or completed state

  final post = await fetchPost();
  print(post.title);
  print(post.userID);
  
  /*
  fetchPost().then((p) {
    print(p.title);
    print(p.userID);
  });
  */
}

Future<Post> fetchPost() {
  const delay = Duration(seconds: 3);

  return Future.delayed(delay, (){
    return Post('my post', 123);
  });
}

class Post {
  String title;
  int userID;

  Post(this.title, this.userID);
}