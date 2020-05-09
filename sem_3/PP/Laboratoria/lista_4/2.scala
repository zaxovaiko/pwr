sealed trait BT[+A]
case object Empty extends BT[Nothing]
case class Node[+A](e: A, l: BT[A], r: BT[A]) extends BT[A]

def suma(t: BT[Int]): Int = {
  t match {
    case Empty => 0
    case Node(e, l, r) => e + suma(l) + suma(r)
  }
}

println(suma(Node(1, Node(2, Empty, Node(3, Empty, Empty)), Empty)))
println(suma(Node(1, Node(2, Empty, Node(3, Empty, Node(6, Empty, Empty))), Empty)))