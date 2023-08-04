fn get_division(num1:i8, num2:i8)->i8{
    num1/num2
}
fn main(){
    let test_cases = [(10, 5, 2), (100, 100, 1)];

    for (x, y, expected) in &test_cases {
        let result = get_division(*x, *y);
        assert_eq!(result, *expected);
    }
}


// 이 Rust 코드는 두 개의 i8 정수를 받아 첫 번째 수를 두 번째 수로 나눈 몫을 반환하는 `get_division` 함수를 정의하고 있습니다.

// 여기서 `i8`은 8비트 정수형을 나타내며, 값의 범위는 -128에서 127까지입니다.

// 그 다음에는 `main` 함수를 보면, 우선 `(10, 5, 2)`와 `(100, 100, 1)`라는 두 개의 튜플을 요소로 가진 배열 `test_cases`를 선언합니다. 각 튜플의 첫 번째와 두 번째 요소는 `get_division` 함수의 인자로, 세 번째 요소는 해당 인자들로 함수를 호출했을 때의 예상 결과입니다.

// 이어지는 `for` 루프에서는 `test_cases`의 각 요소에 대해 `get_division` 함수를 호출하고, 그 결과가 예상 값과 일치하는지 검사합니다. 만약 일치하지 않으면 프로그램은 panic 상태에 빠지고, 해당 오류 메시지를 출력합니다.

// `assert_eq!(result, *expected);`라는 구문에서 `assert_eq!`는 두 개의 인자가 같은지 확인하는 매크로입니다. 두 인자가 다르면 프로그램은 panic합니다. 이는 주로 테스트에서 많이 사용되는 기법입니다. `*expected`에서의 `*` 기호는 레퍼런스 해제를 의미합니다. 이는 레퍼런스 변수에 저장된 실제 값을 가져오는 데 사용됩니다. 

// 따라서 이 코드는 `get_division` 함수가 올바르게 작동하는지 테스트하는 단위 테스트(unit test)로 볼 수 있습니다.