import copy
import random

import numpy as np
from matplotlib import pyplot as plt

SAMPLE_RATE = 100
DURATION = 10
TARGET_FREQ = 2
TARGET_RADIUS = 1


# создать обычный гармонический сигнал
# создать модулирующий сигнал миандра
# провести три типа модуляции - амплитудная, частотная и фазовая
# найти их спектры
# по амплитудой модуляции провести синтез - обрезать высокие и низкие частоты, получить график
# отфильтровать (?) синтезированный график так, чтобы он стал похож на модулирующий сигнал
def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    y = np.sin((2 * np.pi) * frequencies)
    return x, y


def get_square_wave(x, y):
    sq_x = copy.deepcopy(x)
    sq_y = np.sign(y)
    return sq_x, sq_y


def draw_plot(x, y, name, h):
    plt.subplot(3, 1, h)
    plt.plot(x, y)
    plt.title(name)


def get_am(sq_x, sq_y, sine_y):
    am_x = copy.deepcopy(sq_x)
    m = max(sq_y) / max(sine_y)
    am_y = (m * (sq_y + 1) * sine_y) / 2
    return am_x, am_y


def get_pm(sq_x, sq_y, sine_y):
    fm_x = copy.deepcopy(sq_x)
    fm_y = np.sin((2 * np.pi) * sq_x * TARGET_FREQ * 2 * sq_y)
    return fm_x, fm_y


def get_fm(sq_x, sq_y, sine_y):
    fm_x = copy.deepcopy(sq_x)
    test_y = np.sin((2 * np.pi) * TARGET_FREQ * sq_x * 2)
    fm_y = 2 * np.sin((2 * np.pi) * TARGET_FREQ * sq_x * 2) * (2 + sq_y)
    # fm_y = 2 * np.sin((2 * np.pi) * TARGET_FREQ * sq_x * 2 * (2 + sq_y)) / 2
    return fm_x, fm_y


if __name__ == '__main__':
    plt.figure(figsize=(19.20, 10.80))
    sine_x, sine_y = generate_sine_wave(TARGET_FREQ * 2, SAMPLE_RATE, DURATION)
    draw_plot(sine_x, sine_y, 'Красивый график синуса', 1)
    sine_for_sq_x, sine_for_sq_y = generate_sine_wave(TARGET_FREQ / 4, SAMPLE_RATE, DURATION)
    sq_x, sq_y = get_square_wave(sine_for_sq_x, sine_for_sq_y)
    draw_plot(sq_x, sq_y, 'график модулирующего миандра', 2)
    am_x, am_y = get_am(sq_x, sq_y, sine_y)
    draw_plot(am_x, am_y, 'график амплитудной модуляции', 3)
    plt.show()
    plt.figure(figsize=(19.20, 10.80))
    sine_x, sine_y = generate_sine_wave(TARGET_FREQ * 2, SAMPLE_RATE, DURATION)
    draw_plot(sine_x, sine_y, 'Красивый график синуса', 1)
    sine_for_sq_x, sine_for_sq_y = generate_sine_wave(TARGET_FREQ / 4, SAMPLE_RATE, DURATION)
    sq_x, sq_y = get_square_wave(sine_for_sq_x, sine_for_sq_y)
    draw_plot(sq_x, sq_y, 'график модулирующего миандра', 2)
    fm_x, fm_y = get_fm(sq_x, sq_y, sine_y)
    draw_plot(fm_x, fm_y, 'график частотной модуляции', 3)
    plt.show()
    # N = SAMPLE_RATE * DURATION
    # yf = rfft(y_noise)
    # xf = rfftfreq(N, 1 / SAMPLE_RATE)
    # draw_plot(sorted(xf), np.abs(yf), 'Частотный спектр сигнала')
    # points_per_freq = len(xf) / (SAMPLE_RATE / 2)
    # target_idx = int(points_per_freq * TARGET_FREQ)
    # yf[target_idx - TARGET_RADIUS:target_idx + TARGET_RADIUS] = 0 # для удаления конкретной частоты
    # yf[0:target_idx] = 0
    # yf[target_idx + 1:N] = 0
    # draw_plot(xf, np.abs(yf), 'Частотный спектр сигнала после удаления ')
    # new_y = irfft(yf)
    # draw_plot(x, new_y, 'После обратного преобразования')
