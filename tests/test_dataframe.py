from myutils import dataframe
import pandas as pd
from pandas.testing import assert_frame_equal


def test_overview():
    df = pd.DataFrame({"ints": [1, 2, 3], "floats": [1.0, 2.0, 3.0], "strings": ["a", "b", "c"]})
    df_overview = dataframe.overview(df)
    assert_frame_equal(
        df_overview,
        pd.DataFrame(
            {
                "Column": ["ints", "floats", "strings"],
                "Dtype": ["int64", "float64", "object"],
                "Null": [0, 0, 0],
                "Non-Null": [3, 3, 3],
                "Count": [3, 3, 3],
                "Unique": [3, 3, 3],
                "Mode": [1, 1.0, "a"],
                "Mean": [2.0, 2.0, ""],
                "Std": [1.0, 1.0, ""],
                "Overview": [[1.0, 1.5, 2.0, 2.5, 3.0], [1.0, 1.5, 2.0, 2.5, 3.0], ["a", "b", "c"]],
                "Sample": [1, 1.0, "a"],
            }
        ),
    )
