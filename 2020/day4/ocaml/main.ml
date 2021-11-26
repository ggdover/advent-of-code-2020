(* pp = passport *)

module String = struct
    include String
    let split = Base.String.split
    let lsplit2_exn = Base.String.lsplit2_exn
    let to_list = Base.String.to_list
    let is_empty = Base.String.is_empty
end

module List = struct
    include List
    let hd_exn = Base.List.hd_exn
    let tl_exn = Base.List.tl_exn
    let map = Base.List.map
    let for_all = Base.List.for_all
    let unzip = Base.List.unzip
end

module Int = struct
    let of_string = Base.Int.of_string
end

module Char = struct
    let is_hex_digit c = 
        match c with
        | '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' -> true
        | _ -> false
end

(*****************************************************************************)

let validate_part1 pp_str =
    let pp_str_fields = String.split pp_str ~on:' ' in

    let get_key field_str = (List.hd_exn (String.split field_str ~on:':')) in
    let pp_keys = List.map ~f:get_key pp_str_fields in

    let req_keys = ["byr"; "iyr"; "eyr"; "hgt"; "hcl"; "ecl"; "pid"] in
    let validate_field req_key = (Stdlib.List.mem req_key pp_keys) in
    List.for_all ~f:validate_field req_keys

let validate_part2 pp_str =
    let pp_str_fields = String.split pp_str ~on:' ' in

    let get_pair field_str = String.lsplit2_exn field_str ~on:':' in
    let pp_pair_fields = List.map ~f:get_pair pp_str_fields in
    let pp_keys, _ = List.unzip pp_pair_fields in

    let req_keys = ["byr"; "iyr"; "eyr"; "hgt"; "hcl"; "ecl"; "pid"] in
    let validate_key req_key = Stdlib.List.mem req_key pp_keys in
    let has_req_fields = List.for_all ~f:validate_key req_keys in

    if has_req_fields then
        let validate_field (key, value) = 
            match key with
            | "byr" -> 
                (Int.of_string value) >= 1920 && 
                (Int.of_string value) <= 2002

            | "iyr" -> 
                (Int.of_string value) >= 2010 && 
                (Int.of_string value) <= 2020

            | "eyr" -> 
                (Int.of_string value) >= 2020 && 
                (Int.of_string value) <= 2030

            | "hgt" -> 
                let re = Str.regexp "\\([0-9]+\\)\\(cm\|in\\)" in
                let res = Str.string_match re value 0 in

                if res then
                    let num = Str.matched_group 1 value in
                    let meas = Str.matched_group 2 value in

                    match meas with
                    | "cm" -> 
                        (Int.of_string num) >= 150 && 
                        (Int.of_string num) <= 193
                    | "in" -> 
                        (Int.of_string num) >= 59 && 
                        (Int.of_string num) <= 76
                    | _ -> failwith "Regex matching height failed"
                else
                    false

            | "hcl" ->
                let chars = String.to_list value in
                let hex_chars = List.tl_exn chars in

                List.hd_exn chars == '#' && 
                (List.length hex_chars) == 6 &&
                List.for_all hex_chars ~f:Char.is_hex_digit

            | "ecl" -> 
               (match value with
                | "amb" | "blu" | "brn" | "gry" | "grn" | "hzl" | "oth" -> true
                | _ -> false )

            | "pid" -> 
                (String.length value == 9) && 
                (int_of_string_opt value != None)

            | "cid" -> true
            | _ -> false
        in
        List.for_all ~f:validate_field pp_pair_fields
    else
        false

let sum_valid_passports pp_str_list validator =
    let rec next_passport pp_list valid_count =
        match pp_list with
        | [] -> valid_count
        | pp_str::rest -> 
            let valid_int = Bool.to_int (validator pp_str) in
            next_passport rest (valid_int + valid_count)
    in
    next_passport pp_str_list 0

let merge_non_empty_lines ?(sep = "") lines =
    let rec next_line lines (new_lines, curr_line) =
        let merge_line line new_lines curr_line =
            let merger = 
                if String.is_empty curr_line then
                    line
                else
                    curr_line ^ sep ^ line
            in

            match line with
            | "" -> (curr_line :: new_lines, "")
            | str -> (new_lines, merger)
        in

        match lines with
        | [] -> curr_line :: new_lines
        | first_line::rem_lines -> 
            next_line rem_lines (merge_line first_line new_lines curr_line)
    in
    next_line lines ([], "")

let input_all_lines ic =
    let rec build_list ic accum =
        match input_line ic with
        | line -> build_list ic (line :: accum)
        | exception End_of_file -> accum
    in
    build_list ic []

let () =
    let ic = open_in "input.txt" in
    let lines = input_all_lines ic in
    let pps = merge_non_empty_lines ~sep:" " lines in
    let part1 = sum_valid_passports pps validate_part1 in
    let part2 = sum_valid_passports pps validate_part2 in

    print_string "\npart1 total: "; 
    print_int part1;
    print_string "\npart2 total: ";
    print_int part2
