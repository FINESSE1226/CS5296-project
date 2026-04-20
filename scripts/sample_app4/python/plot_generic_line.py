"""
Read sample_app4 SIMRESULT logs and draw line plots (matplotlib).

Log naming: SIMRESULT_TWO_TIER_WITH_EO_<POLICY>_<N>DEVICES_<APP>_GENERIC.log

Uses only stdlib + matplotlib (no pandas/numpy in this module) for stability on Windows.

Batch mode: set SAMPLE4_BATCH_PLOTS=1 or run run_all_plots.py
"""

import math
import os
import warnings

import matplotlib

if os.environ.get('SAMPLE4_BATCH_PLOTS') == '1':
    matplotlib.use('Agg')

import matplotlib.pyplot as plt

from config import get_configuration

warnings.filterwarnings('ignore', category=UserWarning)


def _resolve(base, *parts):
    if os.path.isabs(base):
        root = base
    else:
        root = os.path.normpath(os.path.join(os.path.dirname(__file__), base))
    return os.path.normpath(os.path.join(root, *parts))


def _device_range(start, step, end):
    out = []
    n = start
    while n <= end:
        out.append(n)
        n += step
    return out


def _nanmean(values):
    nums = [v for v in values if v is not None and not (isinstance(v, float) and math.isnan(v))]
    if not nums:
        return float('nan')
    return sum(nums) / len(nums)


def _read_line_fields(path, line_index):
    """Return list of fields for the physical line at 0-based line_index, or None."""
    with open(path, encoding='utf-8', errors='replace') as f:
        for i, line in enumerate(f):
            if i == line_index:
                line = line.strip()
                if not line or line.startswith('#'):
                    return None
                return line.split(';')
    return None


def _read_cell(path, row_0based, col_1based):
    """row_0based: 0-based line index in file. col_1based: 1-based column."""
    fields = _read_line_fields(path, row_0based)
    if not fields or len(fields) < col_1based:
        return float('nan')
    try:
        return float(fields[col_1based - 1])
    except ValueError:
        return float('nan')


def plot_generic_line(
    row_offset,
    column_offset,
    y_label,
    app_type='ALL_APPS',
    calculate_percentage=None,
    legend_pos='best',
    divisor=1,
    ignore_zero_values=False,
    show_plot=None,
):
    """
    row_offset: passed through to log reader — same convention as pandas skiprows in tutorial:
    physical line index to read (0-based). Tutorial uses skiprows=row_offset with row_offset>=1
    meaning "skip header line 0, read data starting at line row_offset".
    For row_offset=1 we read file line index 1 (first semicolon data row after #auto).
    """
    if show_plot is None:
        show_plot = os.environ.get('SAMPLE4_BATCH_PLOTS') != '1'

    config = get_configuration()
    folder_path = _resolve(config['folder_path'])
    plots_dir = os.path.join(folder_path, config.get('plots_subdir', 'plots'))
    os.makedirs(plots_dir, exist_ok=True)

    num_simulations = config['num_iterations']
    scenarios = config['scenario_types']
    tag = config['simresult_scenario_tag']
    flat = config.get('flat_results_layout', True)

    start_devices = config['min_devices']
    step_devices = config['step_devices']
    end_devices = config['max_devices']
    device_counts = _device_range(start_devices, step_devices, end_devices)
    num_device_steps = len(device_counts)
    n_sc = len(scenarios)

    all_results = [
        [[float('nan') for _ in range(num_device_steps)] for _ in range(n_sc)]
        for _ in range(num_simulations)
    ]

    data_row_index = row_offset
    total_row_index = 1

    for s in range(1, num_simulations + 1):
        for i, scenario in enumerate(scenarios):
            for j, num_devices in enumerate(device_counts):
                file_name = f'SIMRESULT_{tag}_{scenario}_{num_devices}DEVICES_{app_type}_GENERIC.log'
                iter_dir = folder_path if flat else os.path.join(folder_path, f'ite{s}')
                file_path = os.path.join(iter_dir, file_name)
                try:
                    value = _read_cell(file_path, data_row_index, column_offset)
                    if ignore_zero_values and value == 0:
                        value = float('nan')

                    if calculate_percentage == 'percentage_of_all':
                        completed = _read_cell(file_path, total_row_index, 1)
                        failed_hdr = _read_cell(file_path, total_row_index, 2)
                        total_tasks = completed + failed_hdr
                        fail_count = _read_cell(file_path, data_row_index, column_offset)
                        value = (100 * fail_count) / total_tasks if total_tasks > 0 else 0.0

                    all_results[s - 1][i][j] = value
                except FileNotFoundError:
                    print(f'Warning: File not found -> {file_path}')
                except OSError as e:
                    print(f'Error reading {file_path}: {e}')

    results = []
    for ii in range(n_sc):
        row = []
        for jj in range(num_device_steps):
            col_vals = [all_results[s][ii][jj] for s in range(num_simulations)]
            row.append(_nanmean(col_vals) / divisor)
        results.append(row)

    fig, ax = plt.subplots()
    fig_pos_cm = config['figure_position']
    fig.set_size_inches(fig_pos_cm[2] / 2.54, fig_pos_cm[3] / 2.54)
    font_sizes = config['font_sizes']
    plt.rcParams.update({'font.family': 'serif'})

    legends = config['legends']
    for ii in range(n_sc):
        color = config['colors'][ii] if config['use_color'] else 'k'
        marker_style = config['color_markers'][ii] if config['use_color'] else config['bw_markers'][ii]
        ax.plot(device_counts, results[ii], marker_style, label=legends[ii], color=color)

    ax.set_xlabel(config['x_axis_label'], fontsize=font_sizes[0])
    ax.set_ylabel(y_label, fontsize=font_sizes[0])
    ax.legend(fontsize=font_sizes[1], loc=legend_pos)
    ax.tick_params(axis='both', which='major', labelsize=font_sizes[2])
    ax.set_xlim(start_devices - 50, end_devices + 50)
    ax.grid(True, linestyle='--', alpha=0.6)
    fig.tight_layout()

    safe_app = app_type.replace(' ', '_')
    base_name = f'{row_offset}_{column_offset}_{safe_app}'

    def _savefig(path, **kwargs):
        try:
            fig.savefig(path, **kwargs)
            print(f'Figure saved to {path}')
        except OSError as e:
            print(f'Warning: could not save {path}: {e}')

    # PNG first: on Windows an open PDF viewer can lock the .pdf and block writes.
    if config.get('save_figure_as_png', False):
        png_path = os.path.join(plots_dir, f'{base_name}.png')
        dpi = int(config.get('png_dpi', 200))
        _savefig(png_path, bbox_inches='tight', dpi=dpi)

    if config['save_figure_as_pdf']:
        output_path = os.path.join(plots_dir, f'{base_name}.pdf')
        _savefig(output_path, bbox_inches='tight')

    if show_plot:
        plt.show()
    else:
        plt.close(fig)
