<?php

function solution($str1, $str2){
    
    if (strpos($str1, $str2) === false){
        return 2;
    }
    return 1;

}

$params = [
    ["ab6CDE443fgh22iJKlmn1o",	"6CD"	,1],
    ["ppprrrogrammers"	,"pppp"	,2],
    ["AbcAbcA",	"AAA"	,2],
];

foreach($params as $param){
    $str1 = $param[0];
    $str2 = $param[1];
    $expected = $param[2];
    
    $result = solution($str1, $str2);
    echo "expected: {$expected}, result: {$result}".PHP_EOL;
}