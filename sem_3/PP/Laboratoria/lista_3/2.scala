// ogonowa
def polacz1(xs: List[String], ys: List[String]) = {
    def zip(xs: List[String], ys: List[String], acc: List[String]): List[String] = {
        if (xs == Nil && ys == Nil) acc.reverse
        else if (xs == Nil && ys != Nil) zip(Nil, ys.tail, ys.head :: acc)
        else if (xs != Nil && ys == Nil) zip(xs.tail, Nil, xs.head :: acc)
        else zip(xs.tail, ys.tail, xs.head + ys.head :: acc )
    }

    zip(xs, ys, Nil)
}

println(polacz1(List("a", "b", "c", "d", "w", "y", "z", "q"), List("e", "f", "g", "h")))    
println(polacz1(List("a", "b", "c", "d", "w", "y", "z", "q"), List("e", "f", "g", "h", "w")))

// nie ogonowa
def polacz2(xs: List[String], ys: List[String]): List[String] = {
    (xs, ys) match {
        case (x::xs, y::ys) => x + y :: polacz2(xs, ys)
        case (Nil, y::ys) => y :: polacz2(Nil, ys)
        case (x::xs, Nil) => x :: polacz2(xs, Nil)
        case _ => Nil
    }
}

println(polacz2(List("a", "b", "c", "d", "w", "y", "z", "q"), List("e", "f", "g", "h")))    
println(polacz2(List("a", "b", "c", "d", "w", "y", "z", "q"), List("e", "f", "g", "h", "w")))    