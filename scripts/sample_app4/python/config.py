"""Plotting configuration for sample_app4 (fuzzy / campus scenario) results."""

import os

# Directory containing SIMRESULT_*.log files (relative to this file)
RESULTS_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'sim_results', 'ite1'))

# Figures (PDF + PNG) go here (created automatically)
PLOTS_SUBDIR = 'plots'


def get_configuration():
    """
    Same keys as tutorial1 python config where possible, plus sample_app4-specific fields.
    """
    return {
        'folder_path': RESULTS_DIR,
        'plots_subdir': PLOTS_SUBDIR,
        # All SIMRESULT files for this app use this middle segment (after SIMRESULT_, before policy name)
        'simresult_scenario_tag': 'TWO_TIER_WITH_EO',
        # True: logs sit directly in folder_path (sample_app4 default: sim_results/ite1/)
        'flat_results_layout': True,
        'num_iterations': 1,
        'x_tick_interval': 1,
        'scenario_types': [
            'NETWORK_BASED',
            'UTILIZATION_BASED',
            'FUZZY_BASED',
            'FUZZY_COMPETITOR',
            'HYBRID',
        ],
        'legends': ['NET', 'UTIL', 'FUZZY', 'FUZZ-C', 'HYBRID'],
        'figure_position': [6, 3, 15, 15],
        'font_sizes': [13, 12, 12],
        'x_axis_label': 'Number of mobile devices',
        'min_devices': 200,
        'step_devices': 200,
        'max_devices': 2400,
        'use_scientific_notation_x_axis': False,
        'save_figure_as_pdf': True,
        'save_figure_as_png': True,
        'png_dpi': 200,
        'plot_confidence_interval': False,
        'use_color': True,
        'colors': [
            [0.55, 0, 0],
            [0, 0.15, 0.6],
            [0, 0.23, 0],
            [0.6, 0, 0.6],
            [0.08, 0.08, 0.08],
        ],
        'bw_markers': ['-k*', '-ko', '-ks', '-kv', '-kp'],
        'color_markers': ['-*', '-o', '-s', '-v', '-p'],
    }
