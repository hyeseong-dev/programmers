<?php

function solution($my_string){
    $vowels = 'aeiou';
    $chars = str_split($my_string);
    $filtered_chars = array_filter($chars, function($char) use ($vowels) {
        return strpos($vowels, $char) === false;
    });
    return implode('', $filtered_chars);
}

$params = ["hello", "hll"];

$result = solution($params[0]);

if($result === $params[1]){
    echo "Success";
} else{
    echo "Fail";
}



$data = [
    "search_keyword" => [],
    "tags"=> [],
    "total_count" => 123,
    "posts" =>[
        0=>[],
    ],
    
    ]

?>