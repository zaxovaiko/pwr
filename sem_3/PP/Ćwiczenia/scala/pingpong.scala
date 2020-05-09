class Person(var years : Int) {
    println("it's a person!")
};

class User(var name : String, years : Int) extends Person(years) {
    println("It's a user!")
}

object Main {
    def main(args: Array[String]) {
        var user = new User("Tom", 30);
        println(user.years)
    }
}

