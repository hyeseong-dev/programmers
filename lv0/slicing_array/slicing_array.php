<?php

function solution($numbers, $num1, $num2){
    $data = array_slice($numbers, $num1, $num2);
    return $data;
}

$params = [
    [[1, 2, 3, 4, 5], 1,	3,	[2, 3, 4]],
    [[1, 3, 5], 1, 2, [3,  5]],
];

foreach($params as $param){

    $result = solution($param[0], $param[1], $param[2]);
    print_r($result);
}
