// fn solution(dots:(i64, i64)) -> u8 {
//     let(a,b) = dots;
//     if a > 0 && b> 0{
//         1
//     }else if a < 0 && b > 0{
//         2
//     }else if a < 0 && b < 0{
//         3
//     }else {
//         4
//     }
    
// }


// fn main(){
//     let test_cases = [
//     ((2, 4),	1),
//     ((-7, 9),	2)
//     ];

//     for &(x, expected) in &test_cases {
//         let result = solution(x);
//         assert_eq!(result, expected);
//     }
// }

fn solution(dots: (i64, i64)) -> u8 {
    match dots {
        (a, b) if a > 0 && b > 0 => 1,
        (a, b) if a < 0 && b > 0 => 2,
        (a, b) if a < 0 && b < 0 => 3,
        _ => 4,
    }
}

fn main() {
    let test_cases = [
        ((2, 4), 1),
        ((-7, 9), 2),
    ];

    for &(x, expected) in &test_cases {
        let result = solution(x);
        assert_eq!(result, expected);
    }
}
