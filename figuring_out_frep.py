import numpy as np
import matplotlib.pyplot as plt
import clipboard_and_style_sheet
import fractions as frac
import scipy.constants as sc

clipboard_and_style_sheet.style_sheet()

"""This is for f0=0 case"""


# obtains the numbers of the comb teeth n1 and n2 for which the first
# overlap occurs for two combs with rep rates fr1 and fr2
def get_lowest_overlap_n1_n2(fr1, fr2):
    _ = frac.Fraction(fr1 / fr2).limit_denominator()
    return _.denominator, _.numerator


# given the cw laser frequency, the beat note frequency, and the rep-rate,
# obtain the index comb tooth that you are locking to. You also need to
# specify whether you are locking to the positive or negative "sideband",
# whatever the right term is
def get_n_from_cw_df_fr(wl_cw_nm, df, fr, sgn='positive'):
    nu_cw = sc.c / (wl_cw_nm * 1e-9)
    if sgn == 'positive':
        return (nu_cw - df) / fr
    elif sgn == 'negative':
        return (nu_cw + df) / fr
    else:
        raise ValueError("sgn should either be 'positive' or 'negative'")
