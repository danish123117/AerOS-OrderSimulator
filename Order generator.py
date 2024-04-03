import random
import time
from datetime import datetime, timedelta
import requests
class Order:
    def __init__(self, order_id, arrival_time, product_type, quantity):
        self.order_id = order_id
        self.arrival_time = arrival_time
        self.product_type = product_type
        self.quantity = quantity
    def generate_order(v_mode, min_arrival_gap, max_arrival_gap, product_types, min_quantity, max_quantity):
        arrival_time = datetime.now() + timedelta(seconds=random.randint(min_arrival_gap, max_arrival_gap))
        product_type = random.choice(product_types)
        quantity = random.randint(min_quantity, max_quantity)
        if v_mode == 0: # Random, balanced orders
        # No additional logic needed
            pass
        elif v_mode == 1: # Orders requiring AGV coordination
        # Add logic to potentially delay arrival based on queue status
            queue_is_full = False # add a function
            if queue_is_full:
        # Delay arrival until queue has free space
                arrival_time += timedelta(seconds=random.randint(10, 30))
        elif v_mode == 2: # Saturation scenario
        # Increase quantity, potentially trigger make-or-buy
            quantity = random.randint(max_quantity, max_quantity * 2)
            if quantity > order_limit:# Trigger make-or-buy decision
                print(f"Order{new_order.order_id}exceeds limit ({quantity}), initiating make-or-buy analysis.")
                order = Order(len(orders_list) + 1, arrival_time, product_type, quantity)
                orders_list.append(order)
        return order
if __name__ =="__main__":
    orders_list = []
    v_mode = int(input("Enter V_mode (0 for random, 1 for AGV coordination, 2 for saturation): "))
    min_arrival_gap = int(input("Enter minimum arrival gap (seconds): "))
    max_arrival_gap = int(input("Enter maximum arrival gap (seconds): "))
    product_types = input("Enter comma-separated list of product types: ").split(",")
    min_quantity = int(input("Enter minimum order quantity: "))
    max_quantity = int(input("Enter maximum order quantity: "))
    order_limit = int(input("Enter quantity limit for triggering make-or-buy: "))
    while True:
        new_order = Order.generate_order(v_mode, min_arrival_gap, max_arrival_gap, product_types, min_quantity, max_quantity)
        print(f"Generated order:{new_order.order_id}, arrives at{new_order.arrival_time}, product type:{new_order.product_type}, quantity:{new_order.quantity}")
        # Simulate processing or handling the order
        processing_time = random.randint(5, 15)
        print(
        f"Order{new_order.order_id}processing for{processing_time}seconds...")
        time.sleep(processing_time)
        # Optionally, add logic to check queue status and update `queue_is_full` flag
        # Wait until next order's arrival time
        wait_time = (new_order.arrival_time - datetime.now()).total_seconds()
        if wait_time > 0:
            print(f"Waiting for next order for{wait_time:.2f}seconds...")
            time.sleep(wait_time)
