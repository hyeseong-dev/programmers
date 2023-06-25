<?php
function solution($my_string, $n) {
    $result_length = strlen($my_string) * $n;
    $result = str_repeat($my_string, $n);
    
    if (strlen($result) > $result_length) {
        $result = substr($result, 0, $result_length);
    }
    
    return $result;
}

$params = [
    "hello", 3, "hhheeellllllooo"
];

$result = solution($params[0], $params[1]);
echo $result;
