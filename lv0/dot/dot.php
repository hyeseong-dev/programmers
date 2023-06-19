<?php

function solution($dot){
    list($x, $y) = $dot;
    if ($x > 0 && $y > 0){
        return 1;
    }
        
    elseif ($x < 0 && $y > 0){
        return 2;
    }
        
    elseif ($x < 0 && $y < 0){
        return 3;
    }
        
    elseif ($x > 0 && $y < 0){
        return 4;
    }
        
}

