fn average(numbers: &[u32]) -> f32 {
    let mut sum = 0;
    for &number in numbers {
        sum += number;
    }
    sum as f32 / (numbers.len() as f32)
}

fn main(){
    let test_cases = [
        (vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
        (vec![89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], 94.0),
    ];

    for (x, y) in &test_cases {
        let result = average(&x);
        assert_eq!(result, *y);
    }
}
