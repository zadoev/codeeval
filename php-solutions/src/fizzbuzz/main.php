<?php
/*
https://www.codeeval.com/open_challenges/1/
FizzBuzz

*/


function solution($line) {

    list($divider1, $divider2, $count) = explode(' ', $line);

    $result = [];
    foreach(range(1, $count) as $i) {

        if ($i % $divider1 == 0 ) {
            if ( $i % $divider2 == 0) {
                $result[] = 'FB';
            } else {
                $result[] = 'F';
            }
        } elseif( $i % $divider2 == 0 ) {
            $result[] = 'B';
        } else {
            $result[] = $i;
        }
    }

    return implode(' ', $result);
}

if ( isset($argv[1])) {
    $fh = fopen($argv[1], "r");

    while ( ($test = fgets($fh)) !== false ) {
        echo solution($test).PHP_EOL;
    }
}
