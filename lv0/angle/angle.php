<?php

function solution($angle){
    $acute_angle = (0 < $angle  && $angle< 90);
    $right_angle = (90 == $angle);
    $obtuse_angle = (90 < $angle && $angle < 180);
    $flat_angle = (180 == $angle);
    
    if ($acute_angle) {
       return 1;
    }elseif($right_angle){
        return 2;
    }elseif($obtuse_angle){
        return 3;
    }elseif($flat_angle){
        return 4;
    } else {
        throw new Exception("각도는 0 ~ 180 사이여야만 합니다.");
    }
}

$test_cases = [
    [70,1],
    [91, 3], 
    [180, 4]
];

foreach ($test_cases as $test_case){
    $angle = $test_case[0];
    $expected = $test_case[1];
    $result = solution($angle);

    if ($result !== $expected){
        echo "Expected {$expected}, but got {$result}\n";
    }
}