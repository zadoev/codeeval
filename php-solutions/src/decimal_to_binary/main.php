<?php
/**
 * User: zadoev@gmail.com
 * Date: 22.01.16
 * Time: 11:27
 * https://www.codeeval.com/open_challenges/27/
 */

if ( $argv ) {
    /*
     * I can reach $n stair jumping to one, or jumping for two. So attempts to
     * reach it it attemps for $n-2 + attempt for $n-1, so it's fibbonaci seq
     * but with offset
     */
    $fh = fopen($argv[1], "r");

    while ( ($test = fgets($fh)) !== false ) {
        $test = trim($test);
        if ( strlen($test) > 0 ) {
            echo decbin($test).PHP_EOL;
        }
    }
}