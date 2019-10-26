object Lab_2 {
  def main(args: Array[String]): Unit = {
    println(fib(6));
    println(fibTail(6));
    println(replace(List("x", "b", 0, "_")));
    println(replace(List(("a", 0), (1, 2))));
  }

  def fib(n: Int): Int = n match {
    case 0 | 1 => n
    case _ => fib(n - 1) + fib(n - 2)
  }

  def fibTail(n: Int): Int = {
    @scala.annotation.tailrec
    def fib_tail(n: Int, a: Int, b: Int): Int = n match {
      case 0 => a
      case _ => fib_tail(n - 1, b, a + b)
    }

    fib_tail(n, 0, 1);
  }

  def replace(list: List[Any]): List[Any] = {
    if (list == Nil) Nil
    else if (list.head == 0) List("x") ::: replace(list.tail)
    else List("_") ::: replace(list.tail)
  }


}
