type 'a llist = 
  | LNil 
  | LCons of 'a * (unit -> 'a llist)
;;

let rec lfrom k = LCons (k, function () -> lfrom (k + 1));;
let rec toLazyList = function
  | [] -> LNil
  | h :: t -> LCons(h, function () -> toLazyList t)
;;

let rec ltake l =
  match l with
  | (0, _) -> []
  | (_, LNil) -> []
  | (n, LCons(x, xf)) -> x :: ltake(n - 1, xf())
;;

let rec merge l1 l2 =
  match (l1, l2) with
  | (LNil, _) -> l2
  | (_, LNil) -> l1
  | (LCons(head1, tail1), LCons(head2, tail2)) -> 
    if head1 <= head2 then LCons(head1,  function () -> merge (tail1()) l2)
    else LCons(head2, function () -> merge l1 (tail2()))

let a = toLazyList [1; 3; 5; 7; 9; 11];;
let b = toLazyList [2; 4; 6; 8];;

let c = merge a b;;

ltake (10, c);;