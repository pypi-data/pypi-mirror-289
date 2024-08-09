import numpy as np
import matplotlib.pyplot as plt
import statsmodels.stats.multitest as smt
from ncmcm.helpers.sequence_functions import simulate_markovian, make_random_adj_matrices


# Functions Markov #


def markovian(sequence, sim_memoryless=1000):
    """
        Test for 1st order Markovian behavior in a sequence. H0 is that the process is a 1st order markov process.

        Parameters:
        - sequence:  np.ndarray, required
            Input sequence.

        - sim_memoryless:  int, optional
            Number of simulations for memoryless Markov behavior test statistic.

        Returns:
        - p: float
            Probability of Markovian behavior.

        - P1: np.ndarray
            Transition matrix for first-order Markov behavior.
    """
    sequence = np.asarray(sequence).astype(int)
    Pz0z1z2, states, M, N = compute_transition_matrix_lag2(sequence)

    # This is done here at the start, so it does not need to be checked after each calculation
    epsilon = 1e-8
    Pz0z1z2 = np.where(Pz0z1z2 == 0, epsilon, Pz0z1z2)
    Pz0z1z2 = Pz0z1z2 / np.sum(Pz0z1z2)  # here I normalize it so the sum is 1 again

    # P1 = P(z[t]|z[t-1]) = P(z[t],z[t-1]) / P(z[t-1]) = Pz0z1 / Pz1
    Pz0z1 = np.sum(Pz0z1z2, axis=0)
    Pz1 = np.sum(Pz0z1z2, axis=(0, 2))
    if 0 in Pz1:
        print('This should not happen!!!')
    P1 = (Pz0z1 / Pz1.reshape(-1, 1))

    # P2 = P(z[t]|z[t-1],z[t-2]) = P(z[t],z[t-1],z[t-2]) / P(z[t-1],z[t-2]) = Pz0z1z2 / Pz1z2
    Pz1z2 = np.sum(Pz0z1z2, axis=2)
    if 0 in Pz1z2:
        print('This should not happen!!!')
    P2 = Pz0z1z2 / np.tile(Pz1z2[:, :, np.newaxis], (1, 1, N))

    # Testing
    TH0 = np.zeros(sim_memoryless)
    for kperm in range(sim_memoryless):
        zH0, _ = simulate_markovian(M=M, P=P1)
        Pz0z1z2H0 = np.zeros((N, N, N))
        for m in range(2, M):
            i = zH0[m]  # col
            j = zH0[m - 1]  # row
            k = zH0[m - 2]  # depth
            Pz0z1z2H0[k, j, i] += 1

        Pz0z1z2H0 = Pz0z1z2H0 / (M - 2)
        Pz1z2H0 = np.sum(Pz0z1z2H0, axis=2)

        # I am replacing zeros in Pz1z2H0 with epsilon, so we do not encounter RuntimeWarnings
        epsilon = 1e-8
        Pz1z2H0 = np.where(Pz1z2H0 == 0, epsilon, Pz1z2H0)
        Pz1z2H0 = Pz1z2H0 / np.sum(Pz1z2H0)

        # P2H0 = P(z[t]|z[t-1],z[t-2]) = P(z[t],z[t-1],z[t-2]) / P(z[t-1],z[t-2]) = Pz0z1z2H0 / Pz1z2H0
        P2H0 = Pz0z1z2H0 / np.tile(Pz1z2H0[:, :, np.newaxis], (1, 1, N))
        TH0[kperm] = np.sum(np.var(P2H0, axis=0).flatten())

    # compute p-value
    T = np.sum(np.var(P2, axis=0).flatten())
    p = 1 - np.mean(T >= TH0)
    return p, P1


def compute_transition_matrix_lag2(sequence, normalize=True):
    """
        Compute a transition matrix for a lag-2 Markov process.

        Parameters:
        - sequence:  np.ndarray, required
            Input sequence.

        - normalize:  bool, optional
            Boolean to normalize the transition matrix (default is True).

        Returns:
        - P: np.ndarray
            Transition matrix.

        - states: np.ndarray
            List of unique states in the sequence.

        - M: int
            Length of the sequence.

        - N: int
            Number of unique states.
    """
    states = sorted(np.unique(sequence))
    M = len(sequence)
    N = len(states)
    # tensor is created
    P = np.zeros((N, N, N))
    for m in range(2, M):
        i = sequence[m]
        j = sequence[m - 1]
        k = sequence[m - 2]
        # from k to j to i
        P[k, j, i] += 1
    if normalize:
        P = P / np.sum(P)  # same as P / (M - 2)
    return P, states, M, N


def stationarity(sequence, chunks=None, sim_stationary=1000, plot=False, verbose=0, num_states=None):
    """
        Test stationarity in input sequence.

        Parameters:
        - sequence: np.ndarray, required
            Input sequence.

        - chunks: int, optional
            Number of parts to split sequence.

        - sim_stationary: int, optional
            Number of simulations for stationary behavior.

        - plot: bool, optional
            Boolean indicating whether to plot the results.

        - num_states: int, optional
            If not every state of the state space is present here one can set the state space size.

        - verbose: int, optional
            Either 0 or 1 and gives additional print-outs for value 1.

        Returns:
        - mean_unadjusted_p_value: float
            Mean unadjusted p-value.

        - mean_FDR_adjusted_p_value: float
            Mean False Discovery Rate (FDR) adjusted p-value.
    """
    if num_states is None:
        states = np.unique(sequence)
        num_states = len(states)
    transition_dict = {state: [] for state in np.unique(sequence)}
    for i in range(len(sequence) - 1):
        transition = (sequence[i], sequence[i + 1])
        transition_dict[sequence[i]].append(transition)

    if chunks is None:
        min_length = min(len(lst) for lst in transition_dict.values())
        # approximate amount of transitions to each state from the least populated state
        per_state = min_length / num_states
        purposed_parts = max(2, int(per_state ** 0.5) + 1)
        if verbose == 1:
            print(f'We purpose {purposed_parts} parts')
        chunks = purposed_parts

    # Split each type of transition for each state into parts
    parts = [[] for _ in range(chunks)]
    for state, transitions in transition_dict.items():
        # random.shuffle(transitions)
        state_chunk_length = len(transitions) // chunks
        for p in range(chunks - 1):
            start = int(state_chunk_length * p)
            end = int(state_chunk_length * (1 + p))
            parts[p] += transitions[start:end]
        parts[chunks - 1] += transitions[int(state_chunk_length * (chunks - 1)):]

    # Making test statistic
    test_stats = []
    test_matrices = make_random_adj_matrices(num_matrices=sim_stationary, matrix_shape=(num_states, num_states))
    for idx1, m1 in enumerate(test_matrices):
        for idx2, m2 in enumerate(test_matrices[idx1 + 1:]):
            m_diff = m1 - m2
            frobenius_norm = np.linalg.norm(m_diff, 'fro')
            test_stats.append(frobenius_norm)

    # The 0.05 percentile for significance
    first_percentile = np.percentile(test_stats, 5)

    # calculate the empirical transition matrices from the chunks
    emp_transition_matrices = []
    for c in parts:
        emp_m = np.zeros((num_states, num_states))
        for t in c:
            emp_m[t[0], t[1]] += 1
        # Normalize rows to ensure they sum up to 1
        if 0 in emp_m:
            # print('We fill 0 in the transition matrix with very small values.')
            emp_m[emp_m == 0] = 1e-8
        row_sums = emp_m.sum(axis=1, keepdims=True)
        emp_m /= row_sums
        emp_m_t1 = np.sum(emp_m, axis=0)
        emp_m = emp_m / emp_m_t1
        emp_transition_matrices.append(emp_m)

    # calculate frobenius norms between the empirical transition matrices
    frobenius_norms = []
    for idx_1, emp_P1 in enumerate(emp_transition_matrices):
        for idx_2, emp_P2 in enumerate(emp_transition_matrices[idx_1 + 1:]):
            # print(f'We compare matrx {idx_1} to matrix {idx_1+idx_2+1}')
            m_test = emp_P1 - emp_P2
            frobenius_empirical = np.linalg.norm(m_test, 'fro')
            frobenius_norms.append(frobenius_empirical)

    # plot all the results
    if plot:
        plt.hist(test_stats, bins='auto', edgecolor='black')  # Adjust the number of bins as needed
        plt.axvline(0, color='orange', label='True Norm')
        for f in frobenius_norms:
            plt.axvline(f, color='green')
        plt.axvline(f, color='green', label='Frobenius Norm between chunks')
        plt.axvline(first_percentile, color='red', label='First 0.05 percentile')

        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title('Histogram of Float Values')
        plt.legend()  # Display the legend
        plt.grid(True)
        plt.show()

    p_values = [1 - (np.sum(test_stats >= f) / len(test_stats)) for f in frobenius_norms]
    _, FDR_adjusted_p_values, _, _ = smt.multipletests(p_values, method='fdr_bh')
    mean_unadjusted_p_value = 1 - (np.sum(test_stats >= np.mean(frobenius_norms)) / len(test_stats))

    return np.mean(FDR_adjusted_p_values), mean_unadjusted_p_value

