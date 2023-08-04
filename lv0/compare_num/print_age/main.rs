fn calculate_age(age:i16)->i16{
    (2022-age + 1).into()
}
fn main(){
    let test_cases = [(40, 1983), (23, 2000)];

    for (x, expected) in &test_cases {
        let result = calculate_age(*x);
        assert_eq!(result, *expected);
    }
}