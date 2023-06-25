<?php

function solution($my_string){
    $answer = 0;
    foreach(str_split($my_string) as $char){
        if (is_numeric($char)){
            $answer += $char;
        }
    }
    return $answer;
}

$params = [
    ["aAb1B2cC34oOp"	,10],
    ["1a2b3c4d123"	,16]
];

foreach ($params as $param){
    $my_string = $param[0];
    $expected = $param[1];
    $result = solution($my_string);

    if ($result !== $expected){
        echo "Fail Expected {$expected}, but got {$result}\n";
    }
    echo "Pass: Expected {$expected}, got {$result}\n";
}