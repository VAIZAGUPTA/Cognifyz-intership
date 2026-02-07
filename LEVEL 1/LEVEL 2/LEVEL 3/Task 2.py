import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [1200, 1500, 1700, 1600, 2000]

plt.figure()
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Report")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

