type list = 
  | Elem of bool 
  | Not 
  | And
  | Or
  | Xor
;;

let eval rpn =
  let rec helper stack = function
  | [] -> List.hd stack
  | Elem x :: xs -> helper(x :: stack) xs
  | Not :: xs -> 
    (match stack with
    | a :: ys -> helper((not a) :: ys) xs
    | [] -> failwith "stack is empty")
  | And :: xs ->
    (match stack with
    | a :: b :: ys -> helper((a && b) :: ys) xs
    | a :: _ -> failwith "not enough args for AND"
    | _ -> failwith "not enough args for AND") 
  | Or :: xs ->
    (match stack with
    | a :: b :: ys -> helper((a || b) :: ys) xs
    | a :: _ -> failwith "not enough args for OR"
    | _ -> failwith "not enough args for OR")
  | Xor :: xs ->
    (match stack with
    | a :: b :: ys -> helper((a <> b) :: ys) xs
    | a :: _ -> failwith "not enough args for XOR"
    | _ -> failwith "not enough args for XOR") in 
  helper [] rpn
;;

eval [Elem true; Not];;
eval [Elem true; And];; 
eval [Elem true; Elem false; And];; 
eval [Elem true; Elem false; Xor; Elem false; And; Elem true; And];; 

(* 
Elem true; Elem false; And

push true
push false
get AND
get true
get false
push false

-------------------------------
Elem true; Elem false; And; And

push true
push false
get AND
push false
get AND -> error two args

-------------------------------
Elem true; Elem true; Not

push true
push true
get NOT -> error or push false
*)