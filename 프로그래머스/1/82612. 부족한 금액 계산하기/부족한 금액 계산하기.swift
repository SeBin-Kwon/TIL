import Foundation

func solution(_ price:Int, _ money:Int, _ count:Int) -> Int64{
    var newPrice = 0
    for i in 1...count {
        newPrice += price * i
    }
    return money - newPrice >= 0 ? Int64(0) : Int64(newPrice - money)
}