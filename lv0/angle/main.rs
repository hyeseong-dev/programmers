fn angle(angle: u8) -> u8 {
    if 0<angle && angle < 90{
        return 1;
    } else if angle == 90 {
        return 2;
    } else if 90<angle && angle < 180 {
        return 3;
    } else if angle == 180 {
        return 4;
    } else {
        return 0;  // additional else branch for angles outside the expected range
    }
}

fn main(){
    let test_cases = [
        (70,1),
        (91,3),
        (180,4),
        ];

    for (x, y) in &test_cases {
        let result = angle(*x);
        assert_eq!(result, *y);
    }
}
