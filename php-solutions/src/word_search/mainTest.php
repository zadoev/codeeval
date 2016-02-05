<?php
/**
 * User: zadoev@gmail.com
 * Date: 05.02.16
 * Time: 10:37
 */

include( __DIR__.DIRECTORY_SEPARATOR.'main.php');


class WordSearchTestCase extends PHPUnit_Framework_TestCase {

    function testMatrixCreatedOk() {

        $searcher = new WordSearch([
            ['a', 'b'],
            ['c', 'd']
        ]);

        # matrix build correctly
        $this->assertEquals(
            'a',
            $searcher->matrix[0][0]
        );
        $this->assertEquals(
            'd',
            $searcher->matrix[1][1]
        );

        # char Points
        $this->assertEquals(
            [[0,0]],
            $searcher->charPoints['a']
        );

        $this->assertEquals(
            [[1,1]],
            $searcher->charPoints['d']
        );

        # possible ways

        $this->assertEquals(
            [[1, 0], [0,1]],
            $searcher->possibleWays['0:0']
        );
        $this->assertEquals(
            [ [0,1], [1,0]],
            $searcher->possibleWays['1:1']
        );

        $this->assertEquals(4, $searcher->totalSize);
    }

    public function testFind() {
        $searcher = new WordSearch([
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E'],
        ]);

        $this->assertFalse($searcher->find('ASADB', [], 0, 0));
        $this->assertTrue($searcher->find('ABCCED', [], 0, 0));
        $this->assertTrue($searcher->find('AB', [], 0, 0));
        $this->assertTrue($searcher->find('ADF', [], 2, 0));
        $this->assertTrue($searcher->find('ASADFBCCEESE', [], 0, 0));
        $this->assertFalse($searcher->find('ADA', [], 2, 0));
    }

}