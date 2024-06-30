let answer = readLine()!.map { Int(String($0))! }
var goorm = readLine()!.map { Int(String($0))! }
var count = 1
var judge = [Character]()

while answer != goorm {
	count += 1
	judge = []
	for i in 0..<4 {
		if answer[i] == goorm[i] { 
			judge.append("s")
		} else if answer.contains(goorm[i]) {
			judge.append("b")
		} else {
			judge.append("f")
		}
	}
	
	for j in 0..<4 {
		if judge[j] == "f" {
			goorm[j] = fail(goorm[j])
		}
	}
	
	if judge.contains("b") {
		ball()
	}
}

print(count)

func ball() {
	var ball_Idx = [Int]()
	var ball_nums = [Int]()
	
	for i in 0..<4 {
		if judge[i] != "s" {
			ball_Idx.append(i)
			ball_nums.append(goorm[i])
		}
	}
	
	let last = ball_nums.removeLast()
	ball_nums.insert(last, at:0)
	for i in ball_Idx {
		goorm[i] = ball_nums.removeFirst()
	}
}

func fail(_ i: Int) -> Int {
	let fail_num = (i+1) % 10
	return goorm.contains(fail_num) ? fail(fail_num) : fail_num
}

