<?php
/**
 * User: zadoev@gmail.com
 * Date: 05.02.16
 * Time: 0:47
 *
 * Url: https://www.codeeval.com/open_challenges/103/
 */

function lun_solution($str) {
    $data = explode(' ', $str);

    $values = array_count_values($data);

    $uniqueValues = array_filter($values, function($v) { return $v == 1;});
    if ( ! $uniqueValues ) {
        return 0;
    } else {
        $value=min(array_keys($uniqueValues));
        return array_search($value, $data) + 1;
    }
}

if ( $argv ) {
    $fh = fopen($argv[1], "r");

    while ( ($test = fgets($fh)) !== false ) {
        $test = rtrim($test);
        echo lun_solution($test).PHP_EOL;
    }
}