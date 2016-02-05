<?php
/**
 * Created by IntelliJ IDEA.
 * User: zadoev@gmail.com
 * Date: 05.02.16
 * Time: 10:37
 */

function point_to_str($row, $col) {
    return $row. ':'. $col;
}


class WordSearch {
    function __construct($initData) {
        $rows = count($initData);
        $cols = count($initData[0]);  # we if index array - invalid initial data
        $this->matrix = SplFixedArray::fromArray($initData);


        $this->possibleWays = [];
        $this->charPoints = [];

        for($row = 0; $row < $rows; $row++) {
            for($col=0; $col<$cols; $col++) {
                $char = $this->matrix[$row][$col];
                $pointAsStr = point_to_str($row, $col);
                if ( ! array_key_exists($char, $this->charPoints)) {
                    $this->charPoints[$char] = [];
                }

                if ( ! array_key_exists($pointAsStr, $this->possibleWays)) {
                    $this->possibleWays[$pointAsStr] = [];
                }

                $this->charPoints[$char][] = [$row, $col];


                if ( $row -1 >= 0 ) {
                    $this->possibleWays[$pointAsStr][] = [$row-1, $col];
                }
                if ( $row +1 < $rows ) {
                    $this->possibleWays[$pointAsStr][] = [$row +1, $col];
                }

                if ( $col - 1 >= 0 ) {
                    $this->possibleWays[$pointAsStr][] = [$row, $col - 1];
                }

                if ($col + 1 < $cols) {
                    $this->possibleWays[$pointAsStr][] = [$row, $col + 1];
                }
            }
        }

        $this->totalSize = $rows * $cols;
    }

    public function find($word, $visited, $row, $col) {
        $point = point_to_str($row, $col);
        if ( array_key_exists($point, $visited)) {
            return false;
        }

        $currentChar = $word[0];
        if ( $this->matrix[$row][$col] !== $currentChar ) {
            return false;
        }

        if (strlen($word) === 1) {
            return true;
        }

        $visited[$point] = 1;

        foreach($this->possibleWays[$point] as $newPoint) {
            if ( $this->find(substr($word, 1), $visited, $newPoint[0], $newPoint[1]))
                return true;
        }

        return false;
    }
}


if ( $argv ) {
    $searcher = new WordSearch([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E'],
    ]);

    $fh = fopen($argv[1], "r");

    while ( ($test = fgets($fh)) !== false ) {
        $word = rtrim($test);

        $result = false;

        if (strlen($word) <= $searcher->totalSize ) {
            foreach($searcher->charPoints[$word[0]] as $point) {
                if ( $searcher->find($word, [], $point[0], $point[1])) {
                    $result = True;
                    break;
                }

            }
        }

        echo $result ? 'True': 'False';
        echo PHP_EOL;
    }
}