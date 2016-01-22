<?php
/**
 * User: zadoev@gmail.com
 * Date: 22.01.16
 * Time: 11:27
 * https://www.codeeval.com/open_challenges/27/
 */

if ( $argv ) {
    $fh = fopen($argv[1], "r");

    while ( ($test = fgets($fh)) !== false ) {
        $test = trim($test);
        if ( strlen($test) > 0 ) {
            echo decbin($test).PHP_EOL;
        }
    }
}