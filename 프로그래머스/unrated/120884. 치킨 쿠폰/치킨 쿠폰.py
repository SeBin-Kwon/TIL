def solution(chicken):
    service = chicken
    coupon = 0
    result = 0
    while True:
        result += service // 10
        coupon += service % 10
        service //= 10
        if service < 10:
            if (coupon + service) >= 10:
                service += coupon
                coupon = 0
            else:
                break
    return result
