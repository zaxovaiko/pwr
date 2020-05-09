(* ogonowa *)
let podziel(list) = 
	let rec split(i, a, b, c, list) =
	match list with
    | [] -> (a, b, c)
    | head :: tail -> 
    	match i mod 3 with
    	| 1 -> split(i + 1, a@[head], b, c, tail)
    	| 2 -> split(i + 1, a, b@[head], c, tail)
    	| _ -> split(i + 1, a, b, c@[head], tail)
	in split(0, [], [], [], list);;

podziel([0; 11; 22; 33]);;