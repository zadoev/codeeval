<?php
/**
 * User: zadoev@gmail.com
 * Date: 05.02.16
 * Time: 0:42
 *
 * Url: https://www.codeeval.com/open_challenges/20/
 */


if ( $argv ) {
    $fh = fopen($argv[1], "r");

    while ( ($test = fgets($fh)) !== false ) {
        echo strtolower($test);
    }
}