def add(list1: List[Any], list2: List[Any]) : List[Any] = {
    if (list2 == Nil) Nil
    else if (list1 != Nil) add(list1.tail, list2) ::: List(list1.head)
    else if (list1 == Nil) add(Nil, list2.tail) ::: List(list2.head)
    else Nil
}

println(add(List('a', 'b', 'c'), List('d', 'e', 'f')))