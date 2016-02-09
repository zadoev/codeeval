<?php

include( __DIR__.DIRECTORY_SEPARATOR.'main.php');


class LUNTest extends PHPUnit_Framework_TestCase
{
    public function test1()
    {
        $this->assertEquals(
            1,
            lun_solution('1 2')
        );
    }

    public function test2()
    {
        $this->assertEquals(
            0,
            lun_solution('1 1')
        );
    }

    public function test3()
    {
        $this->assertEquals(
            5,
            lun_solution('3 3 9 1 6 5 8 1 5 3')
        );
    }
}
