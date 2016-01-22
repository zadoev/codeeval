<?php
/**
 * Created by IntelliJ IDEA.
 * User: zadoev@gmail.com
 * Date: 22.01.16
 * Time: 11:50
 */

function getEndianness() {
    $pattern = 0x00FF;
    $p = pack('S', $pattern);
    return $pattern===current(unpack('v', $p)) ? 'LittleEndian' : 'BigEndian';
}

echo getEndianness().PHP_EOL;
