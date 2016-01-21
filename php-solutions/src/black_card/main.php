<?php
/**
 * User: zadoev@gmail.com
 * Date: 22.01.16
 * Time: 0:54
 *
 * https://www.codeeval.com/open_challenges/222/
 */

function black_card_solver($number, $people) {
    $length = count($people);

    while ( $length > 1 ) {
        array_splice($people, $number % $length-- - 1, 1);
    }

    return array_pop($people);
}

if ( $argv ) {
    $fh = fopen($argv[1], "r");

    while ( ($test = fgets($fh)) !== false ) {
        list($people, $number) = explode('|', $test);
        echo black_card_solver($number, explode(' ', rtrim($people))).PHP_EOL;
    }
}