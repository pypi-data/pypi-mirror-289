
from datetime import datetime, timedelta
from pandas import DataFrame, concat, to_datetime

#notes_due = "dei:Security12bTitle"
#fy2023 = df.drop_duplicates(subset="fiscal_period", keep="first")
#calculated_values = fy2023.sort_index(ascending=False).value.diff()
#calculated_values.iloc[-1] = fy2023.iloc[-1]["value"]
#fy2023.loc[:, "change"] = calculated_values
#fy2023 = fy2023.convert_dtypes()


def process_concept(data: Dict, fiscal_period: Optional[FISCAL_PERIODS] = None):
    """Parse the concept by year and layout Q1-Q4 + FY with period changes."""

    output = DataFrame()
    df = DataFrame(data)
    if df.empty:
        raise ValueError("Could not create DataFrame with supplied input.")
    years = df.fy.unique().tolist()

#    fy_df = df[df["fp"] == "FY"].copy()
#    fy_df.start = to_datetime(fy_df.start)
#    fy_df.end = to_datetime(fy_df.end)
#    fy_df["period_days"] = (fy_df.end - fy_df.start)
#    fy_df["days_ago"] = (fy_df.iloc[0].end - fy_df.start)
#    fy_df = fy_df[fy_df["period_days"] > timedelta(days=100)].drop_duplicates(subset="start", keep="first").sort_values(by="start")
#    fy_df["change_1y"] = fy_df["val"].diff()
#    fy_df["change_percent_1y"] = fy_df["val"].pct_change()
#    quarters_df = df.query("fp.str.contains('Q')").sort_values(by=["start", "end"]).drop_duplicates(subset="start", keep="first")
#    quarters_df.start = to_datetime(quarters_df.start)
#    quarters_df.end = to_datetime(quarters_df.end)
#    for year in years:
#       year_df = df[df["fy"] == year].query("fp.str.contains('Q')")
#       if "Q1" not in year_df["fp"]:
#           continue
#       q1_start = fy_df[fy_df["fy"] == year].iloc[0].start
#       year_df.start = to_datetime(year_df.start)
#       year_df.end = to_datetime(year_df.end)
#       year_df["period_days"] = year_df.end - year_df.start
#       year_df["days_ago"] = year_df.end - q1_startq1

    for year in years:
        year_df = df[df["fy"] == year].copy()
        if len(year_df) == 0:
            continue
        year_df.start = to_datetime(year_df.start)
        year_df.end = to_datetime(year_df.end)
        year_df["period_days"] = (year_df.end - year_df.start)
        year_df["days_ago"] = (year_df.iloc[0].end - year_df.start)

        # FY
        fy_df = year_df[year_df["fp"] == "FY"].copy()
        if len(fy_df) > 0:
            fy = fy_df.iloc[0].copy()
            fy.name= f"{year}-FY"
            last_fy = fy_df[fy_df["end"] == fy.start - timedelta(days=1)]
            if len(last_fy) > 0:
                fy["change_1y"] = fy.val - last_fy.iloc[0].val
                fy["change_percent_1y"] = (fy.val - last_fy.iloc[0].val) / last_fy.iloc[0].val
            if fy_df.iloc[-1].days_ago > timedelta(days=900) and fy_df.iloc[-1].days_ago > timedelta(days=300):
                fy["change_2y"] = fy.val - fy_df.iloc[-1].val
                fy["change_percent_2y"] = (fy.val - fy_df.iloc[-1].val) / fy_df.iloc[-1].val

        # Q1
        q1_df = year_df[year_df["fp"] == "Q1"]
        if len(q1_df) > 0:
            q1 = q1_df[q1_df["start"] == q1_df.start.max()].copy().iloc[0]
            q1.name = f"{year}-Q1"
            q1.fp = "Q1"
            last_q1 = q1_df[q1_df["days_ago"] > timedelta(days=365)]
            if len(last_q1) > 0:
                q1["change_1y"] = q1.val - last_q1.iloc[-1].val
                q1["change_percent_1y"] = (q1.val - last_q1.iloc[-1].val) / last_q1.iloc[-1].val
            prev_q = fy_df[fy_df["end"] == (q1.start - timedelta(days=1))]
            if len(prev_q) > 0:
                q1["change_1q"] = q1.val - prev_q.iloc[-1].val
                q1["change_percent_1q"] = (q1.val - prev_q.iloc[-1].val) / prev_q.iloc[-1].val
            q1 = q1.drop(["days_ago", "period_days"])

        # Q4
        q4 = fy_df.copy().iloc[1] if len(fy_df) > 1 else DataFrame()
        if not q4.empty and len(last_q1) > 4:
            q4.fp = "Q4"
            q4["change_1y"] = q4.val - last_q1.iloc[4].val
            q4["change_percent_1y"] = (q4.val - last_q1.iloc[4].val) / last_q1.iloc[4].val
            prev_q = fy_df[fy_df["end"] == (q4.start - timedelta(days=1))]
            if len(prev_q) > 0:
                q4["change_1q"] = q4.val - prev_q.iloc[-1].val
                q4["change_percent_1q"] = (q4.val - prev_q.iloc[-1].val) / prev_q.iloc[-1].val
            q4 = q4.drop(["days_ago", "period_days"])

        # Q3
        q3 = fy_df.copy().iloc[2] if len(fy_df) > 2 else DataFrame()
        if not q3.empty and len(last_q1) > 5:
            q3.fp = "Q3"
            q3["change_1y"] = q3.val - last_q1.iloc[5].val
            q3["change_percent_1y"] = (q3.val - last_q1.iloc[5].val) / last_q1.iloc[5].val
            prev_q = fy_df[fy_df["end"] == (q3.start - timedelta(days=1))]
            if len(prev_q) > 0:
                q3["change_1q"] = q3.val - prev_q.iloc[-1].val
                q3["change_percent_1q"] = (q3.val - prev_q.iloc[-1].val) / prev_q.iloc[-1].val
            q3 = q3.drop(["days_ago", "period_days"])

        # Q2
        q2 = fy_df.copy().iloc[3] if len(fy_df) > 3 else DataFrame()
        if not q2.empty and len(last_q1) > 6:
            q2.fp = "Q2"
            q2["change_1y"] = q2.val - last_q1.iloc[6].val
            q2["change_percent_1y"] = (q2.val - last_q1.iloc[6].val) / last_q1.iloc[6].val
            prev_q = fy_df[fy_df["end"] == (q2.start - timedelta(days=1))]
            if len(prev_q) > 0:
                q2["change_1q"] = q2.val - prev_q.iloc[-1].val
                q2["change_percent_1q"] = (q2.val - prev_q.iloc[-1].val) / prev_q.iloc[-1].val
            q2 = q2.drop(["days_ago", "period_days"])

        output = concat([q1, q2, q3, q4, fy], axis=1).T.reset_index(drop=True)

        else:
            print(f"No FY data found for, {year}")

    return output
