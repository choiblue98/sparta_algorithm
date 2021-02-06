# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

# 1. 시작 노드를 큐에 넣습니다.
# 2. 현재 큐의 노드를 빼서 visited에 추가합니다.
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 추가합니다.


def bfs_queue(adj_graph, start_node):
    # 구현해보세요!
    queue = [start_node]
    visited = []

    while queue:
        cur_node = queue.pop(0)     # 맨 앞의 원소를 빼와야 하기 때문에 0번째를 써줘야!
        visited.append(cur_node)
        for adj_node in adj_graph[cur_node]:
            if adj_node not in visited:
                queue.append(adj_node)


    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!