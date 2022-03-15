import io
import argparse

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import imageio

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("files", metavar='f', nargs='+',
                        help='CSV files with data')
    parser.add_argument("-s", "--step", type=int,
                        help="Sampling frequency", default=3)
    parser.add_argument("--l1", help="First plot name", default="Test data")
    parser.add_argument("--l2", help="Second plot name", default="Simulation")
    parser.add_argument("--xlabel", help="X axis name", default="Time,s")
    parser.add_argument("--ylabel",
                        help="Y axis name", default="Displacement,mm")

    args = parser.parse_args()

    experimental_data = pd.read_csv(args.files[0])
    simulated_data = pd.read_csv(args.files[1])
    original_x = experimental_data.iloc[:, 0].to_numpy()
    original_y = experimental_data.iloc[:, 1].to_numpy()
    experimental_x = simulated_data.iloc[:, 0]
    experimental_y = simulated_data.iloc[:, 1]

    x_lim = (int(np.min(original_x) - 1), int(np.max(original_x) + 1))
    y_lim = (int(np.min(original_y) - 1), int(np.max(original_y) + 1))

    tmp_x = []
    tmp_y = []

    fig, ax = plt.subplots()
    plt.xlabel(args.xlabel)
    plt.ylabel(args.ylabel)
    ax.set(xlim=x_lim, ylim=y_lim)
    ax.plot(original_x, original_y, label=args.l1)
    p, = ax.plot(tmp_x, tmp_y, label=args.l2)
    ax.legend()
    ax.grid()

    with imageio.get_writer('movie.gif', mode='I') as writer:
        for i in range(0, len(experimental_x)):
            tmp_x.append(experimental_x[i])
            tmp_y.append(experimental_y[i])
            if not i % args.step:

                p.set_xdata(tmp_x)
                p.set_ydata(tmp_y)

                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)
                image = imageio.imread(buf)
                writer.append_data(image)

