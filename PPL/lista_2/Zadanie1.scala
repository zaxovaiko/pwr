def polaczodprawej(list1: List[Any], list2: List[Any]) : List[Any] = {
    if (list1 == Nil && list2 == Nil) Nil
    else if (list1 == Nil) polaczodprawej(Nil, list2.tail) ::: List(list2.head)
    else polaczodprawej(list1.tail, list2) ::: List(list1.head)
}

println(polaczodprawej(List(), List(3, 4)))
println(polaczodprawej(List(1, 2), List()))
println(polaczodprawej(List(1, 2), List(3, 4)))