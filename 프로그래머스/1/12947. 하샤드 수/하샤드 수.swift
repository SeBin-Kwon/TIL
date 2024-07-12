func solution(_ x:Int) -> Bool {
  var sum = 0
  for i in String(x) {
    guard let number = Int(String(i)) else { break }
    sum += number
  }
  return x % sum == 0
}