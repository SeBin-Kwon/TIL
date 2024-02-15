## 문제

This is a demo task.

Write a function:

> ```
> public func solution(_ A : inout [Int]) -> Int
> ```

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an ***\*efficient\**** algorithm for the following assumptions:

> - N is an integer within the range [1..100,000];
> - each element of array A is an integer within the range [−1,000,000..1,000,000].

## 풀이

```swift
public func solution(_ A : inout [Int]) -> Int {
    var answer = 1
    let setA = Set(A)
    let sortA = Array(setA).sorted()
    
    for i in sortA {
        if answer < i {
            break
        } else {
            if i > 0 {
                answer += 1
            }
        }
    }
    return answer
}
```

