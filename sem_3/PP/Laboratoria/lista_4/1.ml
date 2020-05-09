let calkuj func a b n =
  let h = (b -. a) /. float_of_int n in
  let rec helper i s =
    if i >= n then s
    else helper (succ i) (s +. (fun f x h -> (f x +. f (x +. h)) /. 2. ) func (a +. h *. float_of_int i) h)
  in h *. helper 0 0.;;

calkuj (fun x -> x) 0.0 1.1 1;;
calkuj (fun x -> 2.0 *. x +. 5.0) 0.0 1.1 1;;
calkuj (fun x -> x *. x *. x) 0.0 1.1 1;;