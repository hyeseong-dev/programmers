fn sum_of_even(n: u32) -> u32 {
    let mut sum = 0;
    for i in 0..=n{
        if i % 2 == 0 {
            sum += i;
        }
    }
    sum
}

fn main(){
    let test_cases = [
        (10,30),
        (4,6)
        ];

    for (x, y) in &test_cases {
        let result = sum_of_even(*x);
        assert_eq!(result, *y);
    }
}
