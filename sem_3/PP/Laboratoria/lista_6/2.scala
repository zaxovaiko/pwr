def toPower(n: Int): Int = n match {
  case -1 => 1
  case _ => 4 * toPower(n - 1)
}

// Or we can use Math.pow(4, n).toInt instead of toPower()
lazy val power: LazyList[Int] = {
  def loop(p: Int): LazyList[Int] = toPower(p) #:: loop(p + 1)
  loop(0)
}

power.toStream.foreach(x => println(x)) // print results in inf