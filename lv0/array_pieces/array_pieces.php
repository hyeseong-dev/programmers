<?php

function solution($arr, $query) {
    $start = 0;
    $end = count($arr);
    foreach ($query as $i => $item) {
        if ($i % 2 == 0) {
            $end = $start + $item + 1;
        } else {
            $start = $start + $item;
        }
    }
    return array_slice($arr, $start, $end - $start);
}

$params = [
    [[0, 1, 2, 3, 4, 5], [4, 1, 2], [1, 2, 3]]
];

foreach ($params as $param) {
    $result = solution($param[0], $param[1]);
    echo "결과값 : ";
    print_r($result);
    echo "     기대값: ";
    print_r($param[2]);
    echo "\n";
}

?>
