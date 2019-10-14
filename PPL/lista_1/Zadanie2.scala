object Zadanie2 {
  def main(args: Array[String]): Unit = {
    println(usun(List(5, 4, 3, 2, 1), 3))
  }

  def usun(list: List[Any], num: Any): List[Any] = {
    if (list.isEmpty) List()
    else if (list.head == num) List() ::: usun(list.tail, num)
    else List(list.head) ::: usun(list.tail, num)
  }
}