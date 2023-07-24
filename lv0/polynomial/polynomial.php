<?php
function solution($polynomial) {
    // 다항식을 ' + ' 기준으로 분리합니다.
    $terms = explode(" + ", $polynomial);

    // x 항의 계수와 상수항을 저장할 변수를 초기화합니다.
    $xnum = 0;
    $const = 0;

    // 각 항을 순회하며 x 항과 상수항을 분리하여 계산합니다.
    foreach ($terms as $term) {
        if (is_numeric($term)) { // 항이 숫자인 경우(상수항)
            $const += intval($term);
        } else { // 항이 x를 포함하는 경우
            // 항이 'x'인 경우 계수는 1, 그렇지 않은 경우 숫자 부분을 계수로 사용합니다.
            $xnum += ($term == 'x') ? 1 : intval(substr($term, 0, -1));
        }
    }

    // x 항의 계수와 상수항에 따라 결과 문자열을 반환합니다.
    if ($xnum == 0) {
        return strval($const); // x 항이 없는 경우 상수항만 반환합니다.
    } elseif ($xnum == 1) {
        // x 항의 계수가 1인 경우, 상수항이 0인지 아닌지에 따라 다르게 반환합니다.
        return $const != 0 ? 'x + '.strval($const) : 'x';
    } else {
        // x 항의 계수가 1보다 큰 경우, 상수항이 0인지 아닌지에 따라 다르게 반환합니다.
        return $const != 0 ? strval($xnum).'x + '.strval($const) : strval($xnum).'x';
    }
}

// 테스트
$test = "3x + 7 + x";
echo solution($test); // 결과 출력
