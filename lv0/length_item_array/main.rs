// fn solution(strlist: Vec<&str>) -> Vec<usize> {
//     let mut lengths: Vec<usize> = Vec::new();

//     for &s in strlist.iter() {
//         lengths.push(s.len());
//     }
//     lengths
// }

fn solution(strlist: Vec<&str>) -> Vec<u32> {
    strlist.iter().map(|s| s.len()).collect()
}


fn main(){
    let test_cases = [
        (vec!["We", "are", "the", "world!"],	vec![2, 3, 3, 6]),
        (vec!["I", "Love", "Programmers."],	vec![1, 4, 12]),
    ];

    for (x, expected) in &test_cases {
        let result = solution(x.to_vec());
        assert_eq!(result, *expected);
    }
}
