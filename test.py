import numpy as np
import pandas as pd
from pandas import DatetimeIndex

s = pd.Series([1, 3, 5, np.nan, 6, 8])

print(s)

dates = pd.date_range('20230101', periods=6)
print(dates)

DatetimeIndex(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04',
               '2023-01-05', '2023-01-06'],
              dtype='datetime64[ns]', freq='D')

df = pd.DataFrame(np.random.randn(6, 5), index=dates, columns=list("ABCDE"))

print(df)
print()

df2 = pd.DataFrame(
  {
    "1": ["Vermont", "South Dakota", "Washington", "Maine", "Montana"],
    "2": [1, 3, 5, 7, 9],
    "3": ["Montpielier", "Pierre", "Olympia", "Augusta", "Helena"],
    "4": [True, False, True, False, True],
    "5": pd.Timestamp("20130102"),
    "6": pd.Series(1, index=list(range(5)), dtype="float32"),
    "7": pd.Categorical(["Blue", "Red", "Blue", "Blue", "Red"]),
    "8": np.array([7] * 5, dtype="int32" )
  }
)

print(df2)