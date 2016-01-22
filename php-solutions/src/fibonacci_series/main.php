<?php
/**
 * User: zadoev@gmail.com
 * Date: 22.01.16
 * Time: 10:41
 * https://www.codeeval.com/open_challenges/22/
 */

/**
 * Calculates fibbonaci number for $n
 *
 * @param $n
 * @return int
 */
function fib($n)
{
    if ($n < 2) {
        return $n;
    }

    $a = 0;
    $b = 1;

    for($i =2; $i <= $n; $i++ ) {
        $oldB = $b;
        $b = bcadd($a, $b);
        $a = $oldB;
    }


    return $b;
}


if ( $argv ) {
    $fh = fopen($argv[1], "r");

    while ( ($test = fgets($fh)) !== false ) {
        $test = trim($test);
        echo fib($test).PHP_EOL;
    }
}