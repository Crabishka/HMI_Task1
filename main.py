import random

import numpy as np
from matplotlib import pyplot as plt
from numpy.fft import fft, fftfreq, rfft, rfftfreq, irfft

SAMPLE_RATE = 100
DURATION = 5
TARGET_FREQ = 2
TARGET_RADIUS = 1


def generate_white_noise(sample_rate, duration, radius):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    y = np.array([random.uniform(-1 * radius, 1 * radius) for _ in range(0, sample_rate * duration)])
    return x, y


def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    y = np.sin((2 * np.pi) * frequencies)
    return x, y


def draw_plot(x, y, name):
    fig, ax = plt.subplots()
    ax.set_title(name)
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    x, y = generate_white_noise(SAMPLE_RATE, DURATION, 1)
    sine_x, sine_y = generate_sine_wave(TARGET_FREQ, SAMPLE_RATE, DURATION)
    draw_plot(sine_x, sine_y, 'Красивый график синуса')
    draw_plot(x, y, 'График шума')
    y_noise = np.array(list(map(sum, zip(y, sine_y))))
    draw_plot(x, y_noise, 'График с шумами')
    N = SAMPLE_RATE * DURATION
    yf = rfft(y_noise)
    xf = rfftfreq(N, 1 / SAMPLE_RATE)
    draw_plot(sorted(xf), np.abs(yf), 'Частотный спектр сигнала')
    points_per_freq = len(xf) / (SAMPLE_RATE / 2)
    target_idx = int(points_per_freq * TARGET_FREQ)
    # yf[target_idx - TARGET_RADIUS:target_idx + TARGET_RADIUS] = 0 # для удаления конкретной частоты
    yf[0:target_idx] = 0
    yf[target_idx + 1:N] = 0
    draw_plot(xf, np.abs(yf), 'Частотный спектр сигнала после удаления ')
    new_y = irfft(yf)
    draw_plot(x, new_y, 'После обратного преобразования')
