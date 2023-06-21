<?php
# 시간 복잡도 O(n)
# 공간 복잡도 O(1)

function solution($array, $n){
    $answer = 0;
    
    foreach($array as $item){
        if ($item === $n){
            $answer ++;
        }
    }
    return $answer;
}

$params = [
    [[1, 1, 2, 3, 4, 5],	1,	2],
    [[0, 2, 3, 4],	1,	0],
];
$result = solution($params[0][0], $params[0][1]);
assert($result === $params[0][2]);