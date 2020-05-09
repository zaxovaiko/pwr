type 'a llist = 
  | LNil 
  | LCons of 'a * (unit -> 'a llist)
;;

let lpodziel(l) = 
  let rec tll = function
  | [] -> LNil
  | h :: t -> LCons(h, function () -> tll t)
  and split(i, a, b, l) =
	match l with
    | [] -> [tll(a); tll(b)]
    | head :: tail -> 
    	match i mod 2 with
    	| 0 -> split(i + 1, a@[head], b, tail)
    	| _ -> split(i + 1, a, b@[head], tail)
  in split(0, [], [], l) 
;;

lpodziel([5; 6; 3; 2; 1]);;
lpodziel([0; 11; 22; 33]);;