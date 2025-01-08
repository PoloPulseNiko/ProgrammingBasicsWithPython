pool_size = int(input())
p1 = int(input())
p2 = int(input())
hours = float(input())
p1_amount = p1 * hours
p2_amount = p2 * hours
total_amount = p1_amount + p2_amount

if total_amount <= pool_size:
    print(f"The pool is {((total_amount / pool_size) * 100):.2f}% full. Pipe 1: {((p1_amount / total_amount) * 100):.2f}%. Pipe 2: {((p2_amount / total_amount) * 100):.2f}%.")
else:
    print(f"For {hours:.2f} hours the pool overflows with {(total_amount - pool_size):.2f} liters.")