var p = [1,1,1]
for _ in 0...97 {
    p.append(p[p.count-3]+p[p.count-2])
}
for _ in 0..<Int(readLine()!)! {
    print(p[Int(readLine()!)!-1])
}
