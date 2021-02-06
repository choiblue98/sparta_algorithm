input = 50

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}

# 1. 만약 메모에 있으면 그 값을 바로 반환하고
# 2. 없으면 수식대로 구한다.
# 3. 그리고 그 값을 다시 메모에 기록한다.


def fibo_dynamic_programming(n, fibo_memo):
    # 구현해보세요!
    if n in fibo_memo:
        return fibo_memo[n]
    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo

    return nth_fibo

# Fibo(100) -> Fibo(99) ... -> Top down
# Fibo(1) -> Fibo(2) ... -> Bottom up
print(fibo_dynamic_programming(input, memo))