<?php
/**
 * Created by IntelliJ IDEA.
 * User: zadoev@gmail.com
 * Date: 21.01.16
 * Time: 17:32
 *
 * https://www.codeeval.com/open_challenges/23/
 */


function solution_mt($cols, $rows, $width) {
    for($r=1; $r<= $rows; $r++) {
        for($c=1; $c <= $cols; $c++ ) {
            yield str_pad($r*$c, $width, ' ', STR_PAD_LEFT);
        }
        yield "\n";
    }
}
if ( $argv ) {
    foreach(solution_mt(12, 12, 4) as $v){
        echo $v;
    }
}