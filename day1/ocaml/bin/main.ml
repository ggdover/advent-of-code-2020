
let input_all_lines file =
    let rec build_list ic lines =
        match input_line ic with
        | exception End_of_file -> lines
        | line -> build_list ic (line::lines)
    in
    let ic = open_in file in
    let result = build_list ic [] in
    List.rev result

let part1a nums =
    let res = ref 0 in
    for a = 0 to (List.length nums)-1 do
        for b = 0 to (List.length nums)-1 do
            let num_a = List.nth nums a in
            let num_b = List.nth nums b in
            if (num_a + num_b) = 2020 then
                if !res = 0 then
                    res := num_a * num_b
                else
                    print_endline "Part1a, more than one 2020 sum found!"
        done;
    done;
    !res

let part1b nums =
    let res = ref 0 in
    let nums_set = Base.Hash_set.of_list (module Base.Int) nums in
    for i = 0 to (List.length nums)-1 do
        let num_a = List.nth nums i in
        let num_b_opt = Base.Hash_set.find nums_set ~f:(fun num -> (2020-num_a) = num) in
        if num_b_opt != None then
            if !res = 0 then
                res := num_a * (Option.get num_b_opt)
            else
                print_endline "Part1b, more than one 2020 sum found!"
    done;
    !res

let part2 nums =
    let res = ref 0 in
    for a = 0 to (List.length nums)-1 do
        for b = 0 to (List.length nums)-1 do
            for c = 0 to (List.length nums)-1 do
                let num_a = List.nth nums a in
                let num_b = List.nth nums b in
                let num_c = List.nth nums c in
                if (num_a + num_b + num_c) = 2020 then
                    if !res = 0 then
                        res := num_a * num_b * num_c
                    else
                        print_endline "Part2, more than one 2020 sum found!"
            done;
        done;
    done;
    !res

let () = 
	let lines = input_all_lines "sample_input.txt" in
    let sample_nums = List.map int_of_string lines in

    let lines = input_all_lines "input.txt" in
    let nums = List.map int_of_string lines in

    let res = part1a sample_nums in
    print_endline ("Part1a answer (with sample input): " ^ (string_of_int res));

    let res = part1a nums in
    print_endline ("Part1a answer (with puzzle input): " ^ (string_of_int res));

    let res = part1b sample_nums in
    print_endline ("Part1b answer (with sample input): " ^ (string_of_int res));

    let res = part1b nums in
    print_endline ("Part1b answer (with puzzle input): " ^ (string_of_int res));

    let res = part2 sample_nums in
    print_endline ("Part2 answer (with sample input): " ^ (string_of_int res));

    let res = part2 nums in
    print_endline ("Part2 answer (with puzzle input): " ^ (string_of_int res))
