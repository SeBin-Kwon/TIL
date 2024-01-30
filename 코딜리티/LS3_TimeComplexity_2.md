## 문제

An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

> ```
> public func solution(_ A : inout [Int]) -> Int
> ```

that, given an array A, returns the value of the missing element.

For example, given array A such that:

```
  A[0] = 2  A[1] = 3  A[2] = 1  A[3] = 5
```

the function should return 4, as it is the missing element.

Write an ***\*efficient\**** algorithm for the following assumptions:

> - N is an integer within the range [0..100,000];
> - the elements of A are all distinct;
> - each element of array A is an integer within the range [1..(N + 1)].

Copyright 2009–2024 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

## 풀이

```swift
public func solution(_ A : inout [Int]) -> Int {
    let sumA = A.reduce(0) { $0 + $1 }
    let sumB = Array(1...A.count+1).reduce(0) { $0 + $1 }
    return sumB - sumA
}
```

