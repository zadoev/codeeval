<?php

include( __DIR__.DIRECTORY_SEPARATOR.'main.php');


class StackTest extends PHPUnit_Framework_TestCase
{
    public function testSolutionLine1()
    {
        $this->assertEquals(
            '1 2 F 4 B F 7 8 F B',
            solution('3 5 10')
        );
    }

    public function testSolutionLine2()
    {
        $this->assertEquals(
            '1 F 3 F 5 F B F 9 F 11 F 13 FB 15',
            solution('2 7 15')
        );
    }
}
