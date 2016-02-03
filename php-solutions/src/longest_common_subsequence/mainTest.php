<?php
/**
 * Created by IntelliJ IDEA.
 * User: zadoev@gmail.com
 * Date: 21.01.16
 * Time: 17:33
 */

include( __DIR__.DIRECTORY_SEPARATOR.'main.php');


class LCSTestCase extends PHPUnit_Framework_TestCase {

    function testSame() {
        $this->assertEquals(
            'ab',
            lcs('ab', 'ab')
        );
    }
    function testExtraChar() {
        $this->assertEquals(
            'ab',
            lcs('cab', 'ab')
        );
    }

    function testSurrounded() {
        $this->assertEquals(
            'qerty',
            lcs('qerty', '1q22e333r4444t555y666')
        );
    }
    function testSurroundedAndReverted() {
        $this->assertEquals(
            'qerty',
            lcs('1q22e333r4444t555y666', 'qerty')
        );
    }

    function testEmptyLCS(){
        $this->assertEquals(
            '',
            lcs('abc', 'def')
        );
    }
}