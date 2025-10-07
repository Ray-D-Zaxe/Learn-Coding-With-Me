void main() {
  var noodles = MenuItem('veg noodles', 9.99);
  var pizza = Pizza(
    ["mushrooms", "peppers"],
    'volcano pizza', 15.99
    );

  print(noodles.title);
  print(noodles);
  print(pizza);
  print(noodles.format());
  print(pizza.format());
}


class MenuItem {
  String title;
  double price;

  // Constructor
  MenuItem(this.title, this.price);

  // a class function that returns a string
  String format() {
    return "$title --> $price";
  }

  @override
  String toString() {
    return format();
  }
}

class Pizza extends MenuItem {
  List<String> toppings;

  // Constructor
  //Pizza(this.toppings, String title, double price) : super(title, price);
  Pizza(this.toppings, super.title, super.price);

  // Overloading the format function
  @override
  String format() {
    var formattedToppings = 'Contains: ';

    for (final t in toppings) {
      formattedToppings = '$formattedToppings $t';
    }

    return "$title --> $price --> \n\t$formattedToppings";
  }

  @override
  String toString() {
    return 'Instance of Pizza: $title, $price, $toppings';
  }
}