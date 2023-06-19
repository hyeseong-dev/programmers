<?php

function solution($people){
    $answer = ceil($people/7);
    return $answer;
}

echo solution(7).PHP_EOL;
echo solution(1).PHP_EOL;
echo solution(15).PHP_EOL;