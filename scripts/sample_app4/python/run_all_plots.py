"""
Batch-generate PDF + PNG figures into sim_results/ite1/plots/ (no GUI).

Usage from repository root:
  pip install -r scripts/sample_app4/python/requirements.txt
  python scripts/sample_app4/python/run_all_plots.py
"""

import os
import runpy

os.environ['SAMPLE4_BATCH_PLOTS'] = '1'

_BASE = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    for script in ['plotAvgServiceTime.py', 'plotAvgNetworkDelay.py', 'plotAvgFailedTask.py']:
        path = os.path.join(_BASE, script)
        print(f'\n=== {script} ===')
        runpy.run_path(path, run_name='__main__')
    print('\nDone. PDF + PNG in sim_results/ite1/plots/')
