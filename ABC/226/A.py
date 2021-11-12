from decimal import Decimal, ROUND_HALF_UP

X = Decimal(input())
ans = X.quantize(Decimal('0'), rounding=ROUND_HALF_UP)
print(ans)
