from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

""" Creates a visualization of one dice's rolls."""


def create_die_visual(num_sides=6):

    # Creates a Die
    die = Die(num_sides)

    # Makes rolls and store the results in a list

    results = []
    for roll_num in range(1000):
        result = die.roll()
        results.append(result)

    # Analyze the results

    frequencies = []
    for value in range(1, die.num_sides + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # Visualize the results
    x_values = list(range(1, die.num_sides + 1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Result'}
    y_axis_config = {'title': 'Frequency of Result'}
    title = f"Results of rolling one D{num_sides} 1000 times"
    my_layout = Layout(title=title,
                       xaxis=x_axis_config, yaxis=y_axis_config)
    filename = f"D{num_sides}.html"
    offline.plot({'data': data, 'layout': my_layout}, filename=filename)

create_die_visual()