#!/usr/bin/env python

import pandas as pd

surveys_df = pd.read_csv("../data/surveys.csv")

les_axes = surveys_df.plot('weight', 'hindfoot_length', kind="scatter")
les_axes.get_figure().savefig("scatter.png")
