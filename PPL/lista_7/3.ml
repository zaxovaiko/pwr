type 'a llist = 
  | LNil 
  | LCons of 'a * (unit -> 'a llist)
;;

let rec lfrom k = LCons (k, function () -> lfrom (k + 1));;
let ltake lxs =
  let rec tailrec l a =
  match l with
  | (0, _) -> a
  | (_, LNil) -> a
  | (n, LCons(x, xf)) -> tailrec (n - 1, xf()) (a@[x])
  in tailrec lxs []
;;

ltake(5, lfrom 30);;