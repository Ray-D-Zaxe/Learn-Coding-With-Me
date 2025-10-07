void main() {
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