<?php
/**
 * User: zadoev@gmail.com
 * Date: 09.02.16
 * Time: 17:55
 * Url: https://www.codeeval.com/open_challenges/32/
 */

function trailing_strings_solution($a, $b) {
    $aLen = strlen($a);
    $bLen = strlen($b);

    if ( $aLen < $bLen ) {
        return '0';
    }
    if ( substr_compare($a, $b, $aLen - $bLen) === 0 )
        return '1';
    else
        return '0';
}


if ( $argv ) {
    $fh = fopen($argv[1], "r");

    while ( ($test = fgets($fh)) !== false ) {
        $test = rtrim($test);

        if ( !$test )
            continue;

        list($a, $b) = explode(',', $test);

        echo trailing_strings_solution($a, $b).PHP_EOL;
    }
}