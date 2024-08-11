import os, sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "pyplot":
            import tools.pyplot as pyplot
            pyplot.matplot_example_plot()
        elif sys.argv[1] == "cplot":
            import tools.cplot as cplot
            from pylab import plt
            cplot.main(sys.argv[2])
            plt.show()
    else:
        os.chdir(os.path.dirname(__file__))
        os.system('streamlit run visualize.py')

# Path: emachinery/visualize.py
# shell command: streamlit run visualize.py
