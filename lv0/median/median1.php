<?php 

function solution(array $arr): int{
    sort($arr);
    $median_idx = (sizeof($arr) /2 );
    return $arr[$median_idx];
}


$params = [
    [[1, 2, 7, 10, 11],	7],
    [[9, -1, 0],	0]
];

foreach($params as $idx => $case){
    $result = solution($case[0]);
    assert($result === $case[1]);

}
    
