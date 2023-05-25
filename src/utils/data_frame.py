import pandas as pd


def create_result_data_frame(data, columns):
    """
    create result data frame for further use
    :return: df
    """
    df = pd.DataFrame(data, columns=columns)
    df.info()
    print(df)

    # return df
