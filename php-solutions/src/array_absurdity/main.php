<?php
/**
 * Created by IntelliJ IDEA.
 * User: cd
 * Date: 21.01.16
 * Time: 23:59
 * https://www.codeeval.com/open_challenges/41/
 */


/**
 * Using fact that is arithmetic progression and one extra value from sequence
 *
 * @param $n int number
 * @param $seq array sequence
 * @return number
 */
function solution_array_absurdity($n, $seq) {
    return array_sum($seq) - ($n-1) * ($n-2) / 2;
}

if ( $argv ) {
    $fh = fopen($argv[1], "r");

    while ( ($test = fgets($fh)) !== false ) {
        list($n, $seq) = explode(';', $test);
        print solution_array_absurdity($n, explode(',', $seq)).PHP_EOL;
    }
}