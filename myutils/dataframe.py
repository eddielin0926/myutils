import pandas as pd


def overview(df, sort_type=False):
    stats = []
    for name, col in df.items():
        stats.append(
            {
                "Column": name,
                "Dtype": col.dtype,
                "Null": col.isna().sum(),
                "Non-Null": col.notnull().sum(),
                "Count": col.count(),
                "Unique": len(col.unique()),
                "Mode": col.mode()[0],
                "Mean": "" if col.dtype == object else col.mean(),
                "Std": "" if col.dtype == object else col.std(),
                "Overview": col.mode().to_list()[:3]
                if col.dtype == object
                else col.quantile([0, 0.25, 0.5, 0.75, 1.0]).to_list(),
                "Sample": col[0],
            }
        )
    return pd.DataFrame(stats)
