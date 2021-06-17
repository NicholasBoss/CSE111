

#Enter the number of items: 8
#Enter the number of items per box: 5

#For 8 items, packing 5 items in each box, you will need 2 boxes.

import math

items = int(input("Enter the number of items: "))
items_box = float(input("Enter the number of items per box: "))

boxes = items / items_box

total_boxes = math.ceil(boxes)

print(f"For {items} items, packing {items_box} items in each box, you will need {total_boxes} boxes.")