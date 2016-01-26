<?php
/**
 * Created by IntelliJ IDEA.
 * User: zadoev@gmail.com
 * Date: 26.01.16
 * Time: 17:16
 */



if ( $argv ) {
    $fh = fopen($argv[1], "r");

    while ( ($test = fgets($fh)) !== false ) {
        $test = trim($test);
        $res = filter_var($test, FILTER_VALIDATE_EMAIL) ? 'true': 'false';
        echo $res.PHP_EOL;
    }
}