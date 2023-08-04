fn multiply(x:i32, y:i32) -> i32 {
    x * y
}

fn main(){
    let test_cases = [(3, 4, 12), (27, 9, 243)];

    for (x, y, expected) in &test_cases {
        assert_eq!(multiply(*x, *y), *expected);
    }
}
