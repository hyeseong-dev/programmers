fn solution(num_list: Vec<i32>) -> [i32;2] {
    let mut event_count = 0;
    let mut odd_count = 0;

    for &num in &num_list{
        if num % 2 == 0{
            event_count += 1;
        }else {
            odd_count += 1;
        }
    }
    [event_count, odd_count]
}

fn main(){
    
    let test_cases = [
        (vec![1, 2, 3, 4, 5], [2, 3]),
        (vec![1, 3, 5, 7], [0, 4]),
        ];

    for (num_list, expected) in &test_cases {
        let result = solution(num_list.to_vec());
        assert_eq!(result, *expected);
    }
}
