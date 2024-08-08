# Central functions for table making
from typing import TYPE_CHECKING, Dict, List, Union

import polars as pl

from showstats.utils import _add_empty_strings

if TYPE_CHECKING:
    import pandas


def _make_tables(
    df: Union[pl.DataFrame, "pandas.DataFrame"],
) -> Dict[str, pl.DataFrame]:
    """
    Calculate summary statistics for a DataFrame.

    Args:
        df (pl.DataFrame): The input DataFrame. If not a polars.DataFrame, will try
        to cast

    Returns:
        Dict[str, pl.DataFrame]: A dictionary of summary statistics DataFrames for each data type.
    """
    from polars import selectors as cs

    functions = {}
    functions_all = ["null_count", "min", "max"]

    # Map vars to functions
    vars = {}
    cols_num = df.select(
        pl.col(
            pl.Decimal,
            pl.Float32,
            pl.Float64,
            pl.Int16,
            pl.Int32,
            pl.Int64,
            pl.Int8,
            pl.UInt16,
            pl.UInt32,
            pl.UInt64,
            pl.UInt8,
            pl.Boolean,
        )
    ).columns
    if len(cols_num) > 0:
        vars["num"] = cols_num
        functions["num"] = functions_all + ["mean", "median", "std"]

    vars_cat = df.select(
        pl.col(pl.String), pl.col(pl.Enum), pl.col(pl.Categorical)
    ).columns
    if len(vars_cat) > 0:
        vars["cat"] = vars_cat
        functions["cat"] = functions_all

    vars_datetime = df.select(cs.datetime()).columns
    if len(vars_datetime) > 0:
        vars["datetime"] = vars_datetime
        functions["datetime"] = functions_all + ["mean", "median"]

    vars_date = df.select(cs.date()).columns
    if len(vars_date) > 0:
        vars["date"] = vars_date
        functions["date"] = functions_all

    vars_null = df.select(pl.col(pl.Null)).columns
    if len(vars_null) > 0:
        vars["null"] = vars_null
        functions["null"] = ["null_count"]

    exprs = []
    for var_type in vars:
        functions_var_type = functions[var_type]
        vars_var_type = vars[var_type]
        for var in vars_var_type:
            for fun in functions_var_type:
                varname = f"{fun}_{var}"
                expr = getattr(pl.col(var), fun)().alias(varname)
                exprs.append(expr)

    # Compute summary statistics in one go, leveraging Polars' query planner
    stats = df.select(exprs).row(0, named=True)

    # Make split summary tables
    dfs = {}
    for var_type in vars:
        functions_var_type = functions[var_type]
        vars_var_type = vars[var_type]
        rows = []
        for var in vars_var_type:
            row = {"Variable": var}
            for fun in functions_var_type:
                row[fun] = stats[f"{fun}_{var}"]
            rows.append(row)
        dfs[var_type] = pl.DataFrame(rows)

    return dfs


def make_stats_df(
    df: Union[pl.DataFrame, "pandas.DataFrame"],
    top_cols: Union[List[str], None, str] = None,
) -> pl.DataFrame:
    """
    Create a summary table for the given DataFrame.

    This function generates a comprehensive summary of the input DataFrame,
    including statistics like percentage of missing values, mean, median,
    standard deviation, minimum, and maximum for each column. It handles
    different data types appropriately and allows for custom ordering of columns.

    Args:
        df (Union[pl.DataFrame, pandas.DataFrame]): The input DataFrame.
        top_cols (Union[List[str], str, None], optional): Column or list of columns
            that should appear at the top of the summary table. Defaults to None.

    Returns:
        pl.DataFrame: A summary table with statistics for each variable.

    Note:
        - For large DataFrames (>100,000 rows), the row count is displayed in scientific notation.
        - Percentage of missing values is grouped into categories for easier interpretation.
        - Datetime columns are formatted as strings in the output.
    """
    from decimal import Decimal

    if isinstance(df, pl.DataFrame) is False:
        print("Attempting to convert input to polars.DataFrame")
        try:
            df = pl.DataFrame(df)
        except Exception as e:
            print(f"Error occurred during attempted conversion: {e}")

    dfs = _make_tables(df)
    num_rows = df.height
    varnames = [
        "Variable",
        "perc_missing",
        "mean",
        "median",
        "std",
        "min",
        "max",
    ]
    var_types = [x for x in ["num", "datetime", "date", "cat", "null"] if x in dfs]

    # Order
    all_columns_in_order = []

    for var_type in var_types:
        df_var_type = dfs[var_type]
        if top_cols is not None:
            # Save column names for later
            all_columns_in_order.extend(df_var_type.get_column("Variable"))

        df_var_type = (
            df_var_type.lazy()
            .with_columns(pl.selectors.float().round_sig_figs(2))
            .with_columns(
                pl.col("null_count")
                .truediv(num_rows)
                .mul(100)
                .round(2)
                .alias("perc_missing")
            )
            .with_columns(
                # Group percentages. Because pl.cut is unstable, manually use pl.when
                pl.when(pl.col("perc_missing").eq(0))
                .then(pl.lit("0%"))
                .when(pl.col("perc_missing") < 1)
                .then(pl.lit("<1%"))
                .when(pl.col("perc_missing") < 2)
                .then(pl.lit("<2%"))
                .when(pl.col("perc_missing") < 3)
                .then(pl.lit("<3%"))
                .when(pl.col("perc_missing") < 5)
                .then(pl.lit("<5%"))
                .when(pl.col("perc_missing") < 10)
                .then(pl.lit("<10%"))
                .when(pl.col("perc_missing") < 20)
                .then(pl.lit("<20%"))
                .when(pl.col("perc_missing") < 30)
                .then(pl.lit("<30%"))
                .when(pl.col("perc_missing") < 40)
                .then(pl.lit("<40%"))
                .when(pl.col("perc_missing") < 50)
                .then(pl.lit("<50%"))
                .when(pl.col("perc_missing") < 60)
                .then(pl.lit("<60%"))
                .when(pl.col("perc_missing") < 70)
                .then(pl.lit("<70%"))
                .when(pl.col("perc_missing") < 80)
                .then(pl.lit("<80%"))
                .when(pl.col("perc_missing") < 90)
                .then(pl.lit("<90%"))
                .when(pl.col("perc_missing") < 100)
                .then(pl.lit("<100%"))
                .when(pl.col("perc_missing") == 100)
                .then(pl.lit("100%"))
                .alias("perc_missing")
            )
        )

        # Special conversion for datetimes
        if var_type == "datetime":
            df_var_type = df_var_type.with_columns(
                pl.col("mean", "median", "min", "max").dt.to_string("%Y-%m-%d %H:%M:%S")
            )
        else:
            df_var_type = df_var_type.with_columns(pl.col("*").cast(pl.String))

        # Add missing values as ""
        if var_type in ("cat", "date"):
            df_var_type = _add_empty_strings(df_var_type, ["mean", "median", "std"])
        elif var_type == "datetime":
            df_var_type = _add_empty_strings(df_var_type, ["std"])
        elif var_type == "null":
            df_var_type = _add_empty_strings(
                df_var_type, ["min", "max", "mean", "median", "std"]
            )

        dfs[var_type] = df_var_type.select(varnames)

    thr = 100_000
    if num_rows < thr:
        name_var = f"Var. N={num_rows}"
    else:
        name_var = f"Var. N={Decimal(num_rows):.2E}"
    stats_df = pl.concat([dfs[key] for key in var_types]).rename(
        {
            "Variable": name_var,
            "perc_missing": "Null %",
            "mean": "Mean",
            "median": "Median",
            "std": "Std.",
            "min": "Min",
            "max": "Max",
        }
    )

    if top_cols is not None:
        if isinstance(top_cols, str):
            top_cols = [top_cols]

        new_order = top_cols + [
            var for var in all_columns_in_order if var not in top_cols
        ]
        stats_df = stats_df.with_columns(
            pl.col(name_var).cast(pl.Enum(new_order))
        ).sort(name_var)

    return stats_df.collect()


def show_stats(
    df: Union[pl.DataFrame, "pandas.DataFrame"],
    top_cols: Union[List[str], str, None] = None,
) -> None:
    """
    Print a table of summary statistics for the given DataFrame.

    This function generates and prints a formatted table of summary statistics
    using the make_stats_df function. It configures the output format for
    optimal readability.

    Args:
        df (Union[pl.DataFrame, pandas.DataFrame]): The input DataFrame.
        top_cols (Union[List[str], str, None], optional): Column or list of columns
            that should appear at the top of the summary table. Defaults to None.

    Raises:
        ValueError: If the input DataFrame has no rows or columns.

    Note:
        - The output is formatted as an ASCII Markdown table with left-aligned cells
          and no column data types displayed.
        - For large DataFrames (>100,000 rows), the row count is displayed in scientific notation.
        - Percentage of missing values is grouped into categories for easier interpretation.
        - Datetime columns are formatted as strings in the output.
    """
    from polars import Config

    if df.height == 0 or df.width == 0:
        raise ValueError("Input data frame must have rows and columns")

    stats_df = make_stats_df(df, top_cols)
    cfg = Config(
        tbl_hide_dataframe_shape=True,
        tbl_formatting="ASCII_MARKDOWN",
        tbl_hide_column_data_types=True,
        float_precision=2,
        fmt_str_lengths=100,
        tbl_rows=stats_df.height,
        tbl_cell_alignment="LEFT",
    )

    with cfg:
        print(stats_df)
