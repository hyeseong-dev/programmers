fn solution(food_num:u32, beverage_num:u32) -> u32 {
    let main_food_price:u32 = 12000;
    let beverage_price:u32 = 2000;

    let a:u32 = food_num * main_food_price;
    let b:u32 = beverage_num * beverage_price;
    let discounted_beverage_num:u32 = food_num / 10;

    let c = discounted_beverage_num * beverage_price;
    a + b - if c < b { c } else { b }
}

fn main(){
    let test_cases = [
        (10, 3, 124000),
        (64, 6, 768000),
    ];

    for (x, y, expected) in &test_cases {
        let result = solution(*x, *y);
        assert_eq!(result, *expected);
    }
}
