def get_target_min_index(index, distance, route_list, N):
    for i in range(N):
        if route_list[index][i] == 1:
            if distance[i] > distance[index]+1:
                distance[i] = distance[index]+1
                previous_nodes[i] = index+1



N, M = map(int, input().split())

route_list = [[0 for i in range(N)] for j in range(N)]

for i in range(M):
    a,b = map(int, input().split())
    route_list[a-1][b-1] = 1
    route_list[b-1][a-1] = 1

unsearched_nodes = list(range(N))
distance = [float('inf') for i in range(N)]
distance[0] = 0
previous_nodes = [-1] * N



print(route_list) 


"""
while(len(unsearched_nodes) != 0): #未探索ノードがなくなるまで繰り返す
    # まず未探索ノードのうちdistanceが最小のものを選択する
    posible_min_distance = float('inf') # 最小のdistanceを見つけるための一時的なdistance。初期値は inf に設定。
    for node_index in unsearched_nodes: # 未探索のノードのループ
        if posible_min_distance > distance[node_index]: 
            posible_min_distance = distance[node_index] # より小さい値が見つかれば更新
    target_min_index = get_target_min_index(posible_min_distance, distance, unsearched_nodes) # 未探索ノードのうちで最小のindex番号を取得
    unsearched_nodes.remove(target_min_index) # ここで探索するので未探索リストから除去

    target_edge = route_list[target_min_index] # ターゲットになるノードからのびるエッジのリスト
    for index, route_dis in enumerate(target_edge):
        if route_dis != 0:
            if distance[index] > (distance[ target_min_index] + route_dis):
                distance[index] = distance[ target_min_index] + route_dis # 過去に設定されたdistanceよりも小さい場合はdistanceを更新
                previous_nodes[index] =  target_min_index #　ひとつ前に到達するノードのリストも更新

for i in range(N):
    if i == 0:
        print('yes')
    else:
        print(previous_nodes[i]+1)
"""
