<?php

function solution($my_string){
    $vowels = 'aeiou';
    $answer = '';
    for ($i = 0; $i < strlen($my_string); $i++){
        $char = $my_string[$i];
        if (strpos($vowels, $char) === false){
            $answer .= $char;
        }
    }
    return $answer;
}

$params = ["hello", "hll"];

$result = solution($params[0]);

if($result === $params[1]){
    echo "Success";
} else{
    echo "Fail";
}
?>