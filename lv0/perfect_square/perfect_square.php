<?php
function solution($number){
    $sqrt = $number ** 0.5;
    return ($sqrt == intval($sqrt)) ? 1 : 2;
}
$result = solution(16);
echo $result;
?>
