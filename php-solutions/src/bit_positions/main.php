<?php
/**
 * User: zadoev@gmail.com
 *
 * Date: 22.01.16
 * Time: 0:19
 *
 * https://www.codeeval.com/open_challenges/19/
 */


function bit_positions_solver($num, $pos1, $pos2) {
    $pos2 = (int)$pos2;
    return ($num >> ($pos1 - 1) & 1) == ($num >> ($pos2 - 1) & 1);
}

if ( $argv ) {
    $fh = fopen($argv[1], "r");

    while ( ($test = fgets($fh)) !== false ) {
        list($num, $pos1, $pos2) = explode(',', $test);
        echo (bit_positions_solver($num, $pos1, $pos2) ? 'true' : 'false').PHP_EOL;
    }
}
