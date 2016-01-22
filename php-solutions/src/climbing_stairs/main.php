<?php
/**
 * User: zadoev@gmail.com
 * Date: 22.01.16
 * Time: 10:41
 * https://www.codeeval.com/open_challenges/64/
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
    /*
     * I can reach $n stair jumping to one, or jumping for two. So attempts to
     * reach it it attemps for $n-2 + attempt for $n-1, so it's fibbonaci seq
     * but with offset
     */
    $fh = fopen($argv[1], "r");

    while ( ($test = fgets($fh)) !== false ) {
        $test = trim($test);
        echo fib(1 + $test).PHP_EOL;
    }
}