import matplotlib.pyplot as plt


def displayBarGraph(array):
    categories = ['Bubble', 'Merge', 'Quick', 'Radix', 'Linear Search']
    values = array

    # Set the dark background
    plt.figure(facecolor='#2E3440')  # Background of entire figure
    ax = plt.gca()
    ax.set_facecolor('#2E3440')  # Background of the plot area

    # Create a bar chart with custom colors
    bar_colors = ['#5E81AC', '#88C0D0', '#81A1C1', '#B48EAD', '#A3BE8C']
    bars = plt.bar(categories, values, color=bar_colors, edgecolor='white', linewidth=1.5)

    # Add labels and title with white text
    plt.xlabel('Algorithms', fontsize=12, color='white')
    plt.ylabel('Milliseconds', fontsize=12, color='white')
    plt.title('Algorithms Time of Execution', fontsize=14, color='white')

    # Adjust y-axis scale for better visibility
    plt.ylim(0, max(values) * 1.2)

    # Add grid lines for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.5, color='white')

    # Set tick colors
    plt.xticks(color='white', fontsize=10)
    plt.yticks(color='white', fontsize=10)

    # Show the graph
    plt.show()

    
