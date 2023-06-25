<?php

function solution($s1, $s2)
{
    $s1_set = array_flip($s1);
    $s2_set = array_flip($s2);
    $intersection = array_intersect_key($s1_set, $s2_set);
    $answer = count($intersection);
    return $answer;
}


$params = [
    [["a", "b", "c"],    ["com", "b", "d", "p", "c"],    2],
    [["n", "omg"],    ["m", "dot"],    0],

];

foreach ($params as $param) {
    $result = solution($param[0], $param[1]);
    echo $result.PHP_EOL;
}

/*
위 코드의 시간 복잡도는 O(N+M)입니다. 
이유는 array_intersect_key() 함수를 사용하여 두 개의 배열의 교집합을 구할 때, 
해당 함수의 시간 복잡도가 입력 배열의 크기에 선형적으로 비례하기 때문입니다. 
따라서 입력 배열 s1의 길이를 N, s2의 길이를 M이라고 할 때, 전체 알고리즘의 시간 복잡도는 O(N+M)입니다.

공간 복잡도는 O(N+M)입니다. 입력 배열 s1과 s2를 각각 집합으로 변환한 후, 
교집합을 저장하기 위해 array_flip() 함수를 사용하여 키와 값의 위치를 바꾸는 배열을 생성합니다. 
이 때, 배열의 크기는 각각 N과 M입니다. 따라서 전체 알고리즘의 공간 복잡도는 O(N+M)입니다.
*/