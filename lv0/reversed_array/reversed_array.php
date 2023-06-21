<?php

function solution(array $num_list){
    $answer = [];
    for ($i = count($num_list) - 1; $i >= 0; $i--){
        $answer[] = $num_list[$i];
    }
    return $answer;
}
$example1 = [1, 2, 3, 4, 5];
print_r(solution($example1));