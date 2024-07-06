func solution(_ num:Int) -> Int {
    var count = 0
    var n = num
    var flag = true
    if n == 1 {
        return 0
    }
    while count < 500 {
        count += 1
        if n % 2 == 0 {
            n /= 2
        } else {
            n = n*3+1
        }
        if n == 1 {
            break
        }
    }
    if n != 1 {
        flag = false
    }
    
    return flag ? count : -1
}