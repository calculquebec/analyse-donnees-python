#!/usr/bin/env python

import os
import pandas as pd

dossier_data = os.path.join(".." if os.path.basename(os.getcwd()) == "solutions" else ".",
                            "..", "..", "vega-datasets", "data")

df = pd.read_csv(os.path.join(dossier_data, "weather.csv"))

neige = df[(df['date'] <= "2012-06-21") &
           (df['weather'] == "snow")].groupby('location')['date'].max()

print(neige)
