import pandas as pd


def convert_to_dataframe(tables):

    all_rows = []

    for page in tables:
        for table in page:
            if table:
                for row in table:
                    all_rows.append(row)

    if not all_rows:
        return pd.DataFrame()

    header = all_rows[0]
    column_count = len(header)

    cleaned_rows = []

    for row in all_rows[1:]:

        if len(row) < column_count:
            row = row + [None] * (column_count - len(row))

        if len(row) > column_count:
            row = row[:column_count]

        cleaned_rows.append(row)

    df = pd.DataFrame(cleaned_rows, columns=header)

    df = df.replace({'n': '', ',': ''}, regex=True)

    return df