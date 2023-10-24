function twoSum($nums, $target) {
    $numMap = array();
    foreach ($nums as $i => $num) {
        $complement = $target - $num;
        if (isset($numMap[$complement])) {
            return array($numMap[$complement], $i);
        }
        $numMap[$num] = $i;
    }
    return null;
}

$nums = array(2, 7, 11, 15);
$target = 9;
$result = twoSum($nums, $target);
print_r($result);