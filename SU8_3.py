# Dante le Roux 45911398

import matplotlib.pyplot as plt

# Values of budget
budget = [500, 3500, 550, 2000, 1200]
# Labels of budget
slice_labels = ["Leisure","Rent","Internet","Food","Petrol"]
plt.pie(budget, labels = slice_labels)
# Title of chart
plt.title("Monthly Budget")
plt.show()
