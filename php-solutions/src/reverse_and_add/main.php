<?php
/**
 * User: zadoev@gmail.com
 *
 * Date: 02.02.16
 * Time: 23:25
 *
 * Url: https://www.codeeval.com/open_challenges/45/
 */


function reverse_and_add_solution($number) {

    $attempts = 1;

    while ( true ) {
        $number += (int)strrev($number);

        if ( $number == strrev($number)) {
            return $attempts. ' '.$number;
        }

        $attempts++;
    }
}

if ( $argv ) {
    $fh = fopen($argv[1], "r");

    while ( ($test = fgets($fh)) !== false ) {
        echo reverse_and_add_solution($test).PHP_EOL;
    }
}