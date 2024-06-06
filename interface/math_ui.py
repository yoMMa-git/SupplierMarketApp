import seaborn as sns
import matplotlib.pyplot as plt


def draw_graphics_ui(data):
    try:
        stats = data['data']
        players = data['nicknames']
    except KeyError:
        print("ERROR!")
    else:
        labels = []
        sizes = []
        for player in stats:
            sizes.append(stats[player])
            labels.append(players[player])

        plt.pie(sizes, labels=labels)
        plt.axis('equal')
        plt.show()

