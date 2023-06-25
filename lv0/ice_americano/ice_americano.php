<?php

function solution($money){
    return [
        (int)($money / 5500), $money % 5500
    ];
}

$params = 15_000;
$reulst = solution($params);
print_r($reulst);
