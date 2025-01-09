import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(data):
    """
    Function to visualize numeric data provided by the client.
    :param data: List of numbers
    """
    if not all(isinstance(i, (int, float)) for i in data):
        print("Error: Please provide a list of numeric values only.")
        return

    # Plotting the data using Matplotlib
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=range(len(data)), y=data, marker='o', color='blue', label='Data Trend')
    plt.title("Data Visualization", fontsize=16)
    plt.xlabel("Index", fontsize=12)
    plt.ylabel("Values", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

def main():
    """
    Main function to accept client input and generate the chart.
    """
    print("Welcome to the Data Visualization Project!")
    print("Please enter your numeric data separated by commas (e.g., 10, 20, 30, 40):")

    try:
        # Taking input from the client
        user_input = input()
        data = [float(i.strip()) for i in user_input.split(",")]

        # Visualizing the data
        visualize_data(data)
    except ValueError:
        print("Error: Invalid input. Please provide a list of numeric values only.")

if __name__ == "__main__":
    main()
