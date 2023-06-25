<?php

function solution($list, $height){
    $count = 0;
    foreach($list as $item){
        if ($item > $height){
            $count += 1;
        }
    }
    return $count;
}

$params = [
    [[149, 180, 192, 170], 167, 3],
    [[180, 120, 140], 190, 0],
];

foreach($params as $param){
    $result = solution($param[0], $param[1]);
    echo $result.PHP_EOL;
}
