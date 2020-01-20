trait Debug {
    def debugName() : Unit;
    def debugVars() : Unit;
}

class Point (xv: Int, yv: Int) extends Debug {
    var x: Int = xv
    var y: Int = yv
    var a: String = "test"

    override def debugName() : Unit = {
        println("Klasa: " + this.getClass.getSimpleName)
    }

    override def debugVars() : Unit = {
        for (field <- this.getClass.getDeclaredFields) {
            println("Pole: " + field.getName + " => " + field.getAnnotatedType + ", " + field.get(this))
        }
    }
}

object Main {
    def main(args: Array[String]): Unit = {
        val p : Point = new Point(3, 4)
        p.debugName();
        p.debugVars();
    }
}