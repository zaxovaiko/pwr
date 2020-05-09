object UzycieWyjatkow {
  def main(args: Array[String]) {
    try {
      metoda1()
    } catch {
      case e: Exception =>
        System.err.println(e.getMessage + "\n")
        e.printStackTrace()
    }
  }
  def metoda1() {
    metoda2()
  }
  def metoda2() {
    metoda3()
  }

  def metoda3() {
    throw new Exception("Wyjatek zgloszony w metoda3")
  }
}
