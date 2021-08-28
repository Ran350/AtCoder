N = int(input())
S = list(input())


# 東/西側を向いている人数の累積和
east_cum_sum = [0] * (N+1)
west_cum_sum = [0] * (N+1)

for i, s in enumerate(S):
    if s == "E":
        east_cum_sum[i+1] += east_cum_sum[i] + 1
        west_cum_sum[i+1] += west_cum_sum[i]

    if s == "W":
        east_cum_sum[i+1] += east_cum_sum[i]
        west_cum_sum[i+1] += west_cum_sum[i] + 1


answers = [west_cum_sum[i] +                        # 西側で西を向いている人数 : 0 ~ i
           (east_cum_sum[N] - east_cum_sum[i + 1])  # 東側で東を向いている人数 : i+1 ~ N
           for i in range(N)]


print(min(answers))
