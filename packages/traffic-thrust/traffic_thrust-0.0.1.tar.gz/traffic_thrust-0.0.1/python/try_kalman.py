# %%
# %%
from cartes.crs import EuroPP
from traffic.algorithms.filters.kalman import (
    KalmanFilter6D,
    KalmanFilter6DRust,
)
from traffic.data.samples import noisy

# %%
noisy = noisy.compute_xy(EuroPP())
py_kalman = KalmanFilter6D()
rs_kalman = KalmanFilter6DRust()

k = noisy.filter(py_kalman)
kr = noisy.filter(rs_kalman)

# %%
import numpy as np

df = py_kalman.preprocess(noisy.data)
R = (
    np.diag(
        [
            (df.x - df.x.rolling(17).mean()).std(),
            (df.y - df.y.rolling(17).mean()).std(),
            (df.z - df.z.rolling(17).mean()).std(),
            (df.dx - df.dx.rolling(17).mean()).std(),
            (df.dy - df.dy.rolling(17).mean()).std(),
            (df.dz - df.dz.rolling(17).mean()).std(),
        ]
    )
    ** 2
)
R

# %%
import polars as pl

ddf = pl.from_pandas(df)
R = (
    np.diag(
        [
            (ddf["x"] - ddf["x"].rolling_mean(window_size=17)).std(),
            (ddf["y"] - ddf["y"].rolling_mean(window_size=17)).std(),
            (ddf["z"] - ddf["z"].rolling_mean(window_size=17)).std(),
            (ddf["dx"] - ddf["dx"].rolling_mean(window_size=17)).std(),
            (ddf["dy"] - ddf["dy"].rolling_mean(window_size=17)).std(),
            (ddf["dz"] - ddf["dz"].rolling_mean(window_size=17)).std(),
        ]
    )
    ** 2
)
R

# %%
%%timeit
k = noisy.filter(py_kalman)
# %%
%%timeit
kr = noisy.filter(rs_kalman)
# %%
