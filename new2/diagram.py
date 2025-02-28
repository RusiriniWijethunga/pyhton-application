import matplotlib.pyplot as plt

# Example data with non-rounded values
trained_data_amount = [12.5, 25.3, 37.8, 50.0, 62.5, 75.0, 87.5, 100.0]  # Percentage of data used (non-rounded)
accuracy = [0.65, 0.72, 0.78, 0.82, 0.85, 0.87, 0.89, 0.92]
precision = [0.63, 0.70, 0.76, 0.80, 0.83, 0.85, 0.87, 0.90]
recall = [0.67, 0.74, 0.79, 0.83, 0.86, 0.88, 0.89, 0.92]

# Create the plot
plt.plot(trained_data_amount, accuracy, marker='o', linestyle='-', color='b', label='Accuracy')
plt.plot(trained_data_amount, precision, marker='s', linestyle='--', color='r', label='Precision')
plt.plot(trained_data_amount, recall, marker='^', linestyle='-.', color='g', label='Recall')

# Add labels and title
plt.xlabel('Percentage of Trained Data')
plt.ylabel('Score')
plt.title('Model Performance vs. Amount of Trained Data (Non-Rounded)')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()