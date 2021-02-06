import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]   # -> 4일에 20톤 10일에 5톤 15일에 10톤
supply_recover_k = 30

# 4일에 공급을 받으면 4일 스톡 = 20
# 15일날 받으면 그때 스톡은 9


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # 풀어보세요!
    heap = []
    for day in range(len(dates)):
        if sum(supplies[day]) >= 26:
            heapq.heappush(heap, supplies[day])


    return


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
