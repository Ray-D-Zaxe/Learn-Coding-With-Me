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


  var roast = MenuItem('veggie roast dinner', 12.49);
  var kebab = MenuItem('plant kebab', 7.49);



  // Generics
  // We use <MenuItem> as the type for our generic class Collection
  var foods = Collection<MenuItem>(
    'MenuItems',
    [noodles, pizza, roast, kebab]
  );

  var random = foods.randomItem();
  print(random);
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

// Generics
class Collection<T> {
  // Here <T>, represents types
  String name;
  // Here we specify that the tyoe of list much match the specified type of the Collection
  List<T> data;

  Collection(this.name, this.data);

  T randomItem() {
    // Using T here specifies that this function returns value of type T
    data.shuffle();

    return data[0];
  }
}