let obetnijkrance lista = 
  let lista_without_head = List.tl lista in
  let rec concat arg =
    match arg with
    | [] -> []
    | _::[] -> []
    | h::t -> h :: concat t
  in concat lista_without_head;;

let y = obetnijkrance([1; 2; 3]);;
List.iter print_int y;;