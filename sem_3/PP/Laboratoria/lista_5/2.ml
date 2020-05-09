type 'a bt = 
  | Empty 
  | Node of 'a * 'a bt * 'a bt
  (* Node (key, left, right) *)
;;

let sum tree =
  let rec nodes tree =
    match tree with
    | Empty -> 0
    | Node (_, l, r) -> 1 + nodes l + nodes r
  in let rec helper tree = 
    match tree with
    | Empty -> 0
    | Node (k, l, r) -> k + helper l + helper r
  in helper tree / nodes tree
;;

sum(Node(1, Node(2, Empty, Node(3, Empty, Empty)), Empty));;
sum(Node(1, Node(2, Node(3, Empty, Empty), Node(4, Node(5, Empty, Empty), Empty)), Empty));;
sum(Node(1, Node(2, Empty, Empty), Empty));;