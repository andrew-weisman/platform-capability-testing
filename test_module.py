# Load and preprocess the data
def load_data(csv_file):
    """Load a CSV file into a Pandas dataframe and clean it up a bit.

    Args:
        csv_file (str): Name of the local CSV file, including the extension

    Returns:
        Pandas dataframe: Contents of the CSV file as a dataframe
    """

    # Import relevant library
    import pandas as pd

    # Load the CSV file into a Pandas dataframe
    df = pd.read_csv(csv_file)

    # Get the non-ideally-formatted header line
    column_names_orig = df.columns

    # Get a better-formatted header
    column_names_new = [x.strip().strip('"').split('(')[0].strip().lower() for x in column_names_orig]

    # Rename the columns accordingly
    df = df.rename(dict([x for x in zip(column_names_orig, column_names_new)]), axis='columns')

    # If the original index column is trivial, then drop it
    if (pd.Series(df.index) + 1).equals(df['index']):
        df = df.drop('index', axis='columns')

    # Return the final dataframe
    return df

def plot_histograms(df, column=None, bins=10):
    """Create a set of histograms from a Pandas dataframe.

    Args:
        df (Pandas dataframe): Dataframe containing the data from the CSV file
        column (str or list of strings): Name(s) of the column(s) for which to plot a histogram
        bins (int): Number of bins for each histogram

    Returns:
        fig, ax: Handles to the generated figure and axis
    """

    # Import relevant library
    import matplotlib.pyplot as plt

    # Create a figure/axis pair
    fig, ax = plt.subplots()

    # Plot the histograms on the axis
    df.hist(column=column, bins=bins, ax=ax)

    # Return the figure and axis
    return fig, ax

def print_output(animal, df):
    """Print the animal and the averages of the columns in a dataframe.

    Args:
        animal (str): Type of animal
        df (Pandas dataframe): Dataframe containing the data from the CSV file
    """
    print('{}, here are the averages:\n{}'.format(animal.upper()[0] + animal.lower()[1:], df.mean()))
