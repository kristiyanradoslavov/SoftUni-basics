pen = int(input())
markers = int(input())
cleaning = int(input())
discount = int(input())

pen_price = (pen * 5.80)
marker_price = (markers * 7.20)
cleaning_price = (cleaning * 1.20)

total_price = pen_price + marker_price + cleaning_price
discount = total_price - (total_price * discount/100)

print(discount)