<?php
/**
 * Created by IntelliJ IDEA.
 * User: zadoev@gmail.com
 * Date: 21.01.16
 * Time: 17:33
 */

include( __DIR__.DIRECTORY_SEPARATOR.'main.php');


class MultiplicationTablesTestCase extends PHPUnit_Framework_TestCase {

    function test_simpliest_solution() {
        $this->assertEquals(
            "   1\n",
            implode('', iterator_to_array(solution_mt(1, 1, 4)))
        );
    }

    function test_2x2_solution() {
        $this->assertEquals(
            "   1   2\n   2   4\n",
            implode('', iterator_to_array(solution_mt(2, 2, 4)))
        );
    }

    function test_10x1_solution() {
        $this->assertEquals(
            "   1   2   3   4   5   6   7   8   9  10\n",
            implode('', iterator_to_array(solution_mt(10, 1, 4)))
        );
    }
}