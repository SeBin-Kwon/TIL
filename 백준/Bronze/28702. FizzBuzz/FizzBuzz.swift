import Foundation

let input1 = readLine()!
let input2 = readLine()!
let input3 = readLine()!
var number = 0
var result = ""

if let num1 = Int(input1) {
    number = num1 + 3
} else if let num2 = Int(input2) {
    number = num2 + 2
} else if let num3 = Int(input3) {
    number = num3 + 1
}

if number % 3 == 0 && number % 5 == 0 {
    result = "FizzBuzz"
} else if number % 3 == 0 && number % 5 != 0 {
    result = "Fizz"
} else if number % 3 != 0 && number % 5 == 0 {
    result = "Buzz"
} else {
    result = String(number)
}
print(result)