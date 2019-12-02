def lrepeat(stream: LazyList[Int]): LazyList[Int] = {
    def helper(reps: Int, rest: LazyList[Int]): LazyList[Int] = {
        (reps, rest) match {
            case (_, LazyList()) => LazyList()
            case (0, head #:: LazyList()) => helper(head, LazyList())
            case (0, _#::head #:: tail) => helper(head, head #:: tail)
            case (_, head #:: _) => head #:: helper(reps - 1, rest)
        }
    }

    helper(stream.head,stream)
}

lrepeat(LazyList(3, 5, 7, 9)).force