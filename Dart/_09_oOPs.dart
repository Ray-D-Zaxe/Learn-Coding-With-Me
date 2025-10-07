void main() {
  var noodles = MenuItem('veg noodles', 9.99);
  var pizza = MenuItem('volcano pizza', 12.99);

  print(noodles.title);
  print(noodles.price);
  print(pizza.title);
  print(pizza.price);
}


class MenuItem {
  String title;
  double price;

  MenuItem(this.title, this.price);
}