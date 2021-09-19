from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

"""A file that creates a visualization of dice rolls. """

# Create two D6 dice and D10

def create_dice_visual(num_sides_1 = 6, num_sides_2 = 6):
    die_1 = Die(num_sides_1)
    die_2 = Die(num_sides_2)
    # Makes rolls and stores the results in a list

    results = []
    for roll_num in range(10000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    # Analyzes the results
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(0, max_result + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # Visualize the reuslts
    x_values = list(range(0, max_result + 1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Result', 'dtick': 1}
    y_axis_config = {'title': 'Frequency of Result'}
    title = f"Results of rolling a D{num_sides_1} and D{num_sides_2} 10000 " \
            f"times"
    my_layout = Layout(title=title,
                       xaxis=x_axis_config, yaxis=y_axis_config)
    name = f"D{num_sides_1}_D{num_sides_2}.html"
    offline.plot({'data': data, 'layout': my_layout}, filename=name)

create_dice_visual(6, 6)
create_dice_visual(10,8)
