<?php

function solution($my_string, $letter){
    return str_replace($letter, '', $my_string);
}

$params = [
    ["abcdef","f","abcde"],
    ["BCBdbe","B","Cdbe"]
];

foreach($params as $idx => $case){
    $display = solution($case[0], $case[1]);
    assert($display === $case[2]);
    echo "케이스{$idx} - 성공했습니다: {$case[2]}".PHP_EOL;

};

/*
위의 코드에서 시간 복잡도는 O(n)입니다. 여기서 n은 입력 문자열의 길이입니다. 왜냐하면 str_split 함수는 문자열의 모든 문자를 순회하고, 
그 결과를 배열로 반환하기 때문입니다. 그 후 foreach 문에서 이 배열의 모든 원소를 한 번 더 순회하게 됩니다. 
따라서 시간 복잡도는 문자열의 길이에 비례합니다.

하지만, 사실 이 코드는 이미 매우 효율적입니다. 문자열의 모든 문자를 한 번씩만 검사하므로 더 이상 최적화할 수 있는 부분이 없습니다. 
문자열의 모든 문자를 검사하지 않고 이 작업을 수행하는 방법은 없습니다.

그럼에도 불구하고, PHP에서 제공하는 str_replace 함수를 사용하여 코드를 좀 더 간결하게 만들 수 있습니다. 
str_replace 함수는 문자열에서 특정 문자 또는 문자열을 다른 문자 또는 문자열로 교체합니다. 
이 경우에는 특정 문자를 공백으로 교체하려고 하므로, 이 함수를 사용하여 리팩토링 할 수 있습니다. 

이렇게 수정하면, str_split 함수와 foreach 문을 사용하지 않아도 되므로 코드가 더 간결해집니다. 
하지만 시간 복잡도는 여전히 O(n)입니다. 왜냐하면 str_replace 함수도 내부적으로 문자열의 모든 문자를 순회하기 때문입니다.
*/