<?php

function solution($n)
{
    $answer = [];
    for($i=1; $i<=$n; $i+=2){
        array_push($answer, $i);
    }
    return $answer;
}


$params = [
    [10,	[1, 3, 5, 7, 9]],
    [15,	[1, 3, 5, 7, 9, 11, 13, 15]],
];

foreach($params as $param){
    $result = solution($param[0]);
    assert($result === $param[1]);
    echo "성공했습니다. 예상값: ".json_encode($param[1])." 결과값: ".json_encode($result).PHP_EOL;
};
