<?php

function solution($my_string, $letter){
    $my_array = [];
    foreach(str_split($my_string) as $char){
        if ($char != $letter){
            $my_array[] = $char;
        }
    }
    return implode('', $my_array);
}

$params = [
    ["abcdef","f","abcde"],
    ["BCBdbe","B","Cdbe"]
];
foreach($params as $idx => $case){
    $display = solution($case[0], $case[1]);
    assert($display === $case[2]);
    echo "케이스{$idx} - 성공했습니다: {$case[2]}".PHP_EOL;

};
  