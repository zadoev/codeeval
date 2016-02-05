<?php
/**
 * Created by IntelliJ IDEA.
 * User: zadoev@gmail.com
 * Date: 21.01.16
 * Time: 17:33
 */

include( __DIR__.DIRECTORY_SEPARATOR.'main.php');


class ReverseAndAddTestCase extends PHPUnit_Framework_TestCase {
    function test_one() {
        $this->assertEquals('1 2', reverse_and_add_solution('1'));
    }

    function test_195() {
        $this->assertEquals('4 9339', reverse_and_add_solution('195'));
    }

}