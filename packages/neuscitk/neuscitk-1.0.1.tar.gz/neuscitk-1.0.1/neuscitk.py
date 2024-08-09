'''
Neuroscience toolkit
Written for Python 3.12.4
@ Jeremy Schroeter, August 2024
'''

import os
import errno
import numpy as np
from scipy.io import loadmat
from scipy import signal
from scipy.signal import lfilter, butter, filtfilt, dimpulse, find_peaks
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


class LabChartDataset:
    def __init__(self, file_path: str) -> None:
        '''
        Dataset wrapper class which organizes and provides a way to interact with
        LabChart data that has been exported as a MATLAB file

        Example usage:
            dataset = LabChartDataset(file_path)
            channel_data = dataset.data['Channel #']
            block_n = dataset.get_block(n)
        '''

        # scipy throw an error w/o this, but this should be less verbose of an error
        if os.path.exists(file_path) == False:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_path)
        
        self.matlab_dict = loadmat(file_name=file_path)
        self.n_channels = len(self.matlab_dict['titles'])

        self.data = {
            f'Channel {ch + 1}' : self._split_blocks(ch) for ch in range(self.n_channels)
        }

    
    def _split_blocks(self, channel_idx: int) -> list[np.ndarray]:
        '''
        Private method for building the data dictionary
        '''

        raw = self.matlab_dict['data'].reshape(-1)
        channel_starts = self.matlab_dict['datastart'][channel_idx] - 1
        channel_ends = self.matlab_dict['dataend'][channel_idx]

        n_blocks = channel_starts.shape[0]
        channel_blocks = []

        for idx in range(n_blocks):
            start = int(channel_starts[idx])
            end = int(channel_ends[idx])
            channel_blocks.append(raw[start : end])
        
        return channel_blocks
    

    def _get_single_block(self, block_index: int) -> np.ndarray:
        '''
        Private method for getting a single block
        '''
        if self.n_channels == 1:
            return self.data['Channel 1'][block_index]
            
        block = []
        for ch in self.data.keys():
            block.append(self.data[ch][block_index])
        return np.stack(block)


    def _get_multiple_blocks(self, block_indices: list[int]) -> np.ndarray:
        '''
        Private method for getting multiple blocks. Blocks must be the same length
        '''
        if self.n_channels == 1:
            return np.stack([self.data['Channel 1'][idx] for idx in block_indices])
        
        blocks = []
        for channel in self.data.keys():
            for idx in block_indices:
                blocks.append(self.data[channel][idx])
        return np.array(blocks)
    

    def get_block(self, indices: list[int] | int) -> np.ndarray:
        '''
        Given a block index number, returns a (channel, timepoints) array
        containing the data for that block. If only 1 channel, returns a
        1D array of size (timepoints,)
        '''

        if type(indices) == int:
            return self._get_single_block(indices)
        else:
            return self._get_multiple_blocks(indices)

    @property
    def fs(self) -> np.ndarray:
        '''
        Property which returns the sample rate for all channels.
        '''
        return self.matlab_dict['samplerate']
    
    @property
    def channels(self) -> int:
        return self.n_channels




class Filter:
    def __init__(self, fs: int, filter_type: str, lowcut: float = None, highcut: float = None) -> None:
        
        if filter_type == 'band':
            if lowcut is None or highcut is None:
                raise ValueError("Both lowcut and highcut must be provided for a bandpass filter.")
            self.lowcut = lowcut
            self.highcut = highcut
            self.b, self.a = butter(4, [lowcut, highcut], btype=filter_type, fs=fs)
        elif filter_type == 'low':
            if highcut is None:
                raise ValueError("Highcut must be provided for a lowpass filter.")
            self.highcut = highcut
            self.b, self.a = butter(4, highcut, btype=filter_type, fs=fs)
        elif filter_type == 'high':
            if lowcut is None:
                raise ValueError("Lowcut must be provided for a highpass filter.")
            self.lowcut = lowcut
            self.b, self.a = butter(4, lowcut, btype=filter_type, fs=fs)
        else:
            raise ValueError("Invalid filter type. Supported types are 'band', 'low', and 'high'.")
        

    def apply(self, arr: np.ndarray) -> np.ndarray:
        return filtfilt(self.b, self.a, arr)

    @property
    def kernel(self) -> np.ndarray:
        system = (self.b, self.a, 1)
        _, h = dimpulse(system, n=100)
        return h[0].flatten()



class FiringRate:
    def __init__(self, fs: int, filter_type: str='gaussian', time_constant: float=0.01) -> None:

        self.filter_type = filter_type
        self.time_constant = time_constant
        self.fs = fs
        self.kernel = self._create_filter_kernel()

    
    def _create_filter_kernel(self) -> np.ndarray:

        if self.filter_type == 'gaussian':
            n = int(self.time_constant * self.fs * 5)
            t = np.arange(0, n) / self.fs
            kernel = np.exp(-0.5 * (t / self.time_constant) ** 2)
            kernel /= kernel.sum()

        elif self.filter_type == 'exponential':
            n = int(self.time_constant * self.fs * 5)
            t = np.arange(0, n) / self.fs
            kernel = np.exp(-t / self.time_constant)
            kernel /= kernel.sum()

        elif self.filter_type == 'boxcar':
            n = int(self.time_constant * self.fs)
            t = np.arange(0, n) / self.fs
            kernel = np.ones(n) / n
        
        else:
            raise ValueError('Unsupported filter type. Choose "exponential", "boxcar", or "gaussian"')
        return kernel
    

    def apply(self, spike_train: np.ndarray) -> np.ndarray:
        firing_rate = lfilter(self.kernel, [1], spike_train)
        return firing_rate * self.fs





class SpikeSorter:
    def __init__(self, fs: int, bp_lowcut: float = 100, bp_highcut: float=9000, ma_window_size: float = 0.025) -> None:
        
        self.fs = fs
        self.bp_lowcut = bp_lowcut
        self.bp_highcut = bp_highcut
        self.ma_window_size = ma_window_size

    
    def _apply_band_pass(self, arr: np.ndarray) -> np.ndarray:
        filter = Filter(self.fs, 'band', self.bp_lowcut, self.bp_highcut)
        return filter.apply(arr)
    
    
    def _moving_average(self, arr: np.ndarray) -> np.ndarray:
        n = int(self.fs * self.ma_window_size)
        window = np.ones(n) / n
        return signal.convolve(arr, window, mode='same')
    
    
    def _moving_std(self, arr: np.ndarray) -> np.ndarray:
        avg = self._moving_average(arr)
        avg_sq = self._moving_average(arr ** 2)
        return np.sqrt(avg_sq - avg ** 2)
    

    def _adaptive_threshold_spike_detection(self, arr: np.ndarray) -> np.ndarray:
        mov_avg, mov_std = self._moving_average(arr), self._moving_std(arr)
        adaptive_threshold = mov_avg + 4 * mov_std
        peaks, _ = find_peaks(arr, height=adaptive_threshold)
        return peaks
    

    def _extract_waveforms(self, filtered_arr: np.ndarray, spike_times: np.ndarray) -> np.ndarray:
        return np.vstack([filtered_arr[spike - 20: spike + 20] for spike in spike_times])


    def _apply_pca(self, waveforms: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        pca = PCA()
        scaler = StandardScaler(with_std=False)
        scaled_waveforms = scaler.fit_transform(waveforms)
        pca_embeddings = pca.fit_transform(scaled_waveforms)
        return pca_embeddings, pca.explained_variance_ratio_
    

    def _fit_clusters(self, pca_embeddings: np.ndarray) -> np.ndarray:
        top_two_embeddings = pca_embeddings[:, :2]
        
        scores = []
        cluster_range = range(2, 11)
        for n_clusters in cluster_range:
            kmeans = KMeans(n_clusters, n_init='auto').fit(top_two_embeddings)
            labels = kmeans.labels_
            scores.append(silhouette_score(top_two_embeddings, labels))
        
        best_cluster_number = cluster_range[np.array(scores).argmax()]
        kmeans = KMeans(best_cluster_number, n_init='auto').fit(top_two_embeddings)
        return kmeans.labels_, scores
    

    def _organize_clusters(
            self,
            spike_times: np.ndarray,
            waveforms: np.ndarray,
            labels: np.ndarray,
            pca_embeddings: np.ndarray,
            clustering_scores: np.ndarray,
            pca_var_explained: np.ndarray
        ) -> dict:

        sort_summary = {
            f'cluster_{i + 1}' : {
                'spike_times' : spike_times[np.where(labels == i)],
                'waveforms' : waveforms[np.where(labels == i)]
            }
            for i in np.unique(labels)
        }
        sort_summary['clustering_scores'] = clustering_scores
        sort_summary['pca_var_explained'] = pca_var_explained
        sort_summary['pca_embeddings'] = pca_embeddings
        return sort_summary
    
    def apply(self, recording: np.ndarray) -> dict:

        arr_filtered = self._apply_band_pass(recording)
        spike_times = self._adaptive_threshold_spike_detection(arr_filtered)
        waveforms = self._extract_waveforms(arr_filtered, spike_times)
        pca_embeddings, pca_explained_var = self._apply_pca(waveforms)
        cluster_labels, cluster_scores = self._fit_clusters(pca_embeddings)
        return self._organize_clusters(spike_times, waveforms, cluster_labels, pca_embeddings, cluster_scores, pca_explained_var)


