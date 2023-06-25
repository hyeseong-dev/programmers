<?php

function solution($sides) {
    $longest = max($sides);
    unset($sides[array_search($longest, $sides)]);
    return $longest < array_sum($sides) ? 1 : 2;
}

$params = [
    [[1, 2, 3], 2],
    [[3, 6, 2], 2],
    [[199, 72, 222], 1],
];

foreach($params as $param) {
    $expected = $param[1];
    $result = solution($param[0]);
    echo "Expected: {$expected}, Result: {$result}\n";
}

?>
