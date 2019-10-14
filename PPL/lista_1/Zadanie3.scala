object Zadanie3 {
  def main(args: Array[String]): Unit = {
    println(polacz(List("To", "jest", "napis"), "-"))
  }

  def polacz(list: List[String], sep: String): String = {
    if (list.tail.isEmpty) list.head
    else list.head + sep + polacz(list.tail, sep)
  }
}
