import Foundation

func solution(_ number:String, _ k:Int) -> String {
    var count = k
    var stack = [Character]()
    
    for num in number{
        while !stack.isEmpty && stack.last! < num && count != 0{
            stack.removeLast()
            count -= 1
        }
        stack.append(num)
    }
    return String(String(stack).prefix(stack.count - count))
}