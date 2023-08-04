fn compare_num(num1:i16, num2:i16)->i8{
    if num1 == num2 {1} else {-1}
}

fn main(){
    let test_cases = [
        (2, 3, -1), 
        (11, 11, 1), 
        (7, 99, -1)
        ];

    for (x, y, expected) in &test_cases {
        let result = compare_num(*x, *y);
        assert_eq!(result, *expected);
    }
}