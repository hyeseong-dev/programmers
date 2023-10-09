fn letter(message: &str) -> u32 {
    let length = message.len();
    (length * 2) as u32
}

fn main(){
    let test_cases = [
    ("happy birthday!",	30),
    ("I love you~",	22)
    ];

    for (x, expected) in &test_cases {
        let result = letter(x);
        assert_eq!(result, *expected);
    }
}
