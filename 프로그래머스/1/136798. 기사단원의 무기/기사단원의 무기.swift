import Foundation

func solution(_ number:Int, _ limit:Int, _ power:Int) -> Int {
    var result = [Int]()
    
    for number in 1...number{
        var count = 0

        for i in 1...Int(sqrt(Double(number))){
            if number % i == 0{
                if( i * i) == number{
                    count += 1
                }else{
                    count += 2
                }
            }
        }
        count = count > limit ? power : count
        result.append(count)
        
    }
    return result.reduce(0,+)
}