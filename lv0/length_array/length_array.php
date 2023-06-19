<?php

$solution = function($strlist) {
    return array_map('strlen', $strlist);
};
$strlist = ['apple', 'banana', 'cherry'];
print_r($solution($strlist));