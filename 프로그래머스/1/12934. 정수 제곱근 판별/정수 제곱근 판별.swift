func solution(_ n:Int64) -> Int64 {
    var answer = 0
    if n == 1 {
        return 4
    }
    if n < 4 {
        return -1
    }
    for i in 2...n/2 {
        if i*i == n {
            return (i+1)*(i+1)
        }
    }
    return -1
}