<?php
/**
 * User: zadoev@gmail.com
 * Date: 03.02.16
 * Time: 23:32
 * Used http://algolist.ru/search/lcs/simple_lcs.php
 *
 */

function lcs($a, $b) {
    $aLen = strlen($a);
    $bLen = strlen($b);

    $matrix = new SplFixedArray($aLen+1);

    for($i = 0; $i <= $aLen; $i++) {
        $matrix[$i] = SPlFixedArray::fromArray(array_fill(0, $bLen + 1, 0));
    }

    for ( $i = $aLen -1; $i>=0; $i--) {
        for ($j = $bLen -1; $j >= 0; $j--) {
            if ( $a[$i] == $b[$j]) {
                $matrix[$i][$j] = 1 + $matrix[$i+1][$j+1];
            } else {
                $matrix[$i][$j] = max($matrix[$i+1][$j], $matrix[$i][$j+1]);
            }
        }
    }

    $result = '';
    $i = 0;
    $j = 0;
    while ($i < $aLen && $j < $bLen ) {
        if ($a[$i] == $b[$j]) {
            $result .= $a[$i];
            $i++;
            $j++;
        } elseif ( $matrix[$i+1][$j] >= $matrix[$i][$j+1]) {
            $i++;
        } else {
            $j++;
        }
    }

    return $result;
}


if ( $argv ) {
    $fh = fopen($argv[1], "r");

    while ( ($test = fgets($fh)) !== false ) {
        list($a, $b) = explode(';', rtrim($test));
        echo lcs($a, $b).PHP_EOL;
    }
}