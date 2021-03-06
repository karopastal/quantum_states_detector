from src.detector_momentum import DetectorMomentum

N = 200
HOPPING_AMPLITUDE = 1
TAUS = 150
TAU_INTERVAL = 25
ENABLE_DETECTOR = True
DETECTOR = 100
DETECTOR_FREQUENCY = 2
MOMENTUM_STATE = 50
ENABLE_DETECTOR_VELOCITY = True


def main():

    detector = DetectorMomentum(n=N,
                                taus=TAUS,
                                detector=DETECTOR,
                                detector_frequency=DETECTOR_FREQUENCY,
                                tau_interval=TAU_INTERVAL,
                                hopping_amp=HOPPING_AMPLITUDE,
                                momentum_state=MOMENTUM_STATE,
                                enable_detector=ENABLE_DETECTOR,
                                enable_detector_velocity=ENABLE_DETECTOR_VELOCITY)

    detector.plot_probability_density()
    detector.plot_probability_per_site()

    # print("Energies: \n", detector.ring.energies)
    # print("States: \n", detector.ring.states)


if __name__ == '__main__':
    main()
