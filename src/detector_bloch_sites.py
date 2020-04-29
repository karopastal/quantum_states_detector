import numpy as np
import matplotlib.pyplot as plt
from src.ring_electric_field import RingElectricField

N = 200
A = 1
ELECTRIC_FIELD = 0.05
HOPPING_AMPLITUDE = 100
TAUS = 380
TAU_INTERVAL = 10
SITE_ZERO = 100
DETECTOR = 0
DETECTOR_FREQUENCY = 25
ENABLE_DETECTOR = False


class DetectorBlochSites:
    def __init__(self,
                 n=3,
                 a=1,
                 electric_field=1,
                 taus=6,
                 site_zero=0,
                 detector=0,
                 detector_frequency=1,
                 tau_interval=25,
                 hopping_amp=1,
                 enable_detector=False):

        self.n = n
        self.a = a
        self.electric_field = electric_field
        self.taus = np.arange(0, taus)
        self.site_zero = site_zero
        self.detector_frequency = detector_frequency
        self.detector = detector
        self.hopping_amp = hopping_amp
        self.enable_detector = enable_detector

        self.ring = RingElectricField(n=self.n,
                                      a=self.a,
                                      electric_field=electric_field,
                                      site_zero=site_zero,
                                      detector=self.detector,
                                      detector_frequency=self.detector_frequency,
                                      tau_interval=tau_interval,
                                      enable_detector=self.enable_detector)

        self.time, psi, probabilities = self.ring.compute_psi_tau(taus=self.taus)
        self.psi_t = np.stack(psi, axis=0)
        self.probabilities_t = np.stack(probabilities, axis=0)

    def plot_probability_per_site(self):
        fig, ax = plt.subplots()

        for i in range(len(self.probabilities_t.T)):
            ax.plot(self.time, self.probabilities_t.T[i], label='site ' + str(i))

        plt.legend(bbox_to_anchor=(1.125, 1), loc='upper right', borderaxespad=0.1, fontsize=14)

        if self.enable_detector:
            detector = '| %s >' % self.detector
            detections = 'every %s [tau]' % self.detector_frequency
        else:
            detector = 'disabled'
            detections = 'None'

        plt.title('%s sites, particle(t=0): | %s >, c: %s, f: %s' %
                  (self.n,  self.site_zero, self.hopping_amp, self.electric_field), fontsize=17)

        plt.xlabel('Time [tau]', fontsize=20)
        plt.ylabel('Probability', fontsize=20)

        ax.grid()
        plt.show()

    def plot_probability_density(self):
        fig, ax = plt.subplots(figsize=(15, 9))

        img = ax.imshow(self.probabilities_t.T,
                        extent=(0, len(self.taus), self.n, 0),
                        interpolation='nearest',
                        aspect='auto',
                        cmap='pink')

        ax.set_ylim(0, self.n)
        fig.colorbar(img, ax=ax)

        if self.enable_detector:
            detector = '| %s >' % self.detector
            detections = 'every %s [tau]' % self.detector_frequency
        else:
            detector = 'disabled'
            detections = 'None'

        plt.title('%s sites, particle(t=0): | %s >, c: %s, f: %s' %
                  (self.n,  self.site_zero, self.hopping_amp, self.electric_field), fontsize=17)

        plt.xlabel('Time [tau]', fontsize=20)
        plt.ylabel('Position', fontsize=20)

        plt.show()

    def save_plot(self, title, path):
        fig, ax = plt.subplots(figsize=(15, 9))
        img = ax.imshow(self.probabilities_t.T,
                        extent=(0, len(self.taus), self.n, 0),
                        interpolation='nearest',
                        aspect='auto',
                        cmap='pink')

        ax.set_ylim(0, self.n)

        fig.colorbar(img, ax=ax)

        plt.title(title, fontsize=20)
        plt.xlabel('Time [tau]', fontsize=18)
        plt.ylabel('Position', fontsize=18)

        plt.savefig(path)


def main():
    detector = DetectorBlochSites(n=N,
                                  taus=TAUS,
                                  site_zero=SITE_ZERO,
                                  electric_field=ELECTRIC_FIELD,
                                  detector=DETECTOR,
                                  detector_frequency=DETECTOR_FREQUENCY,
                                  tau_interval=TAU_INTERVAL,
                                  hopping_amp=HOPPING_AMPLITUDE,
                                  enable_detector=ENABLE_DETECTOR)

    detector.plot_probability_density()
    # detector.plot_probability_per_site()


if __name__ == '__main__':
    main()
