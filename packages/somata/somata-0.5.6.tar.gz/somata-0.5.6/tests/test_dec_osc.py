"""
Author: Mingjian He <mh1@stanford.edu>

Testing functions for the dOsc algorithm in somata/oscillator_search/decomp_osc.py
"""

from somata.oscillator_search import DecomposedOscillatorModel as DecOsc
from somata import OscillatorModel as Osc
from test_load_data import _load_data  # type: ignore
import numpy as np
import pickle


def test_decomposed_osc(plot_on=False):
    np.random.seed(1)
    o1 = Osc(a=[0.996, 0.95], freq=[0.1, 10], sigma2=[0.4, 0.2], R=1.2, Fs=100)
    x, y = o1.simulate(duration=10)

    do_test = DecOsc(y, o1.Fs)
    do_test.iterate(plot_fit=plot_on)

    # Verify diagnostic statistical tests
    acf = do_test.diagnose_residual_acf()
    assert 1.9 < acf['Durbin-Watson d'].item() < 2.1, "Failed Durbin-Watson test."
    assert acf['Ljung-Box'].item() > 0.05, "Failed Ljung-Box test."
    assert acf['Lagrange Multiplier'].item() > 0.05, "Failed Lagrange Multiplier test."
    assert acf['Brock-Dechert-Scheinkman'].item() > 0.05, "Failed Brock-Dechert-Scheinkman test."

    norm = do_test.diagnose_residual_norm()
    assert norm['Shapiro-Wilk'].item() > 0.05, "Failed Shapiro-Wilk test."
    assert norm['D\'Agostino and Pearson'].item() > 0.05, "Failed D'Agostino and Pearson test."
    assert norm['Anderson-Darling H'].item() is False, "Failed Anderson-Darling test."
    assert norm['Cramer-von Mises'].item() > 0.05, "Failed Cramer-von Mises test."

    if plot_on:
        # Plot frequency domain (from parameters and from estimated x_t_n)
        for version in ['theoretical', 'actual']:
            _ = do_test.get_knee_osc().visualize_freq(version, y=y, sim_osc=o1, sim_x=x[:, 1:])

        # Plot time domain estimated x_t and the true simulated x_t
        _ = do_test.get_knee_osc().visualize_time(y=y, sim_x=x[:, 1:])

        # Plot likelihood and selected model (may not be the highest likelihood)
        _ = do_test.plot_log_likelihoods()

        # Plot multitaper spectrogram and mean spectrum
        _ = do_test.plot_mtm()

        # Plot raw time trace
        _ = do_test.plot_trace()

        # Plot fitted spectra (equivalent to calling .visualize_freq(version) manually)
        _ = do_test.plot_fit_spectra()

        # Plot fitted traces (equivalent to calling .visualize_time() manually)
        _ = do_test.plot_fit_traces()

        # Plot the residual spectrum shifted by white noise processes
        _ = do_test.plot_residual()

        # Plot residual linear line fit
        _ = do_test.plot_residual_fit()

        # Plot autocorrelation function of the residuals
        _ = do_test.plot_acf()

        # Plot partial autocorrelation function of the residuals
        _ = do_test.plot_pacf()

    with open(_load_data('test_dec_osc_obj.pkl', return_path=True), 'rb') as inp:
        do_true = pickle.load(inp)

    assert do_true.knee_index == do_test.knee_index, "Does not choose the same oscillator."
    assert len(do_true.fitted_osc) == len(do_test.fitted_osc), "Does not have the same number of maximum oscillators."
    assert np.allclose(do_true.ll, do_test.ll), 'Log-likelihoods are not the same.'

    osc_true = do_test.get_knee_osc()
    osc_orig = do_test.get_knee_osc()

    assert np.allclose(osc_true.freq, osc_orig.freq), "Frequencies in DecOsc are not the same."
    assert np.allclose(osc_true.a, osc_orig.a), "Radii in DecOsc are not the same."
    assert np.allclose(osc_true.sigma2, osc_orig.sigma2), "sigma^2 in DecOsc are not the same."
    assert np.allclose(osc_true.R, osc_orig.R), "R (obs noise) in DecOsc are not the same."


if __name__ == "__main__":
    test_decomposed_osc()
    print('Decomposed oscillator test finished without exception.')
