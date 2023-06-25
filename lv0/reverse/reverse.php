<?php

function solution($my_string){
    return strrev($my_string);
}

$params = [
    ["jaron","noraj"],
    ["bread","daerb"],
];

foreach($params as $param){
    $result = solution($param[0]);
    echo "결과: {$result}, 예상결과: {$param[1]}\n";
    echo ($result == $param[1]) ? '통과' : '실패';
    echo "\n";
}

?>
