from plot_generic_line import plot_generic_line

if __name__ == '__main__':
    print('--- sample_app4: Average Service Time ---')
    plot_generic_line(1, 5, 'Service Time (sec)', 'ALL_APPS', '', 'lower right')
    plot_generic_line(1, 5, 'Service Time for\nAugmented Reality App (sec)', 'AUGMENTED_REALITY', '', 'lower right')
    plot_generic_line(1, 5, 'Service Time for Health App (sec)', 'HEALTH_APP', '', 'lower right')
    plot_generic_line(1, 5, 'Service Time for\nInfotainment App (sec)', 'INFOTAINMENT_APP', '', 'lower right')

    plot_generic_line(2, 5, 'Service Time on Edge (sec)', 'ALL_APPS', '', 'lower right')
    plot_generic_line(2, 5, 'Service Time on Edge\nfor Augmented Reality App (sec)', 'AUGMENTED_REALITY', '', 'lower right')
    plot_generic_line(2, 5, 'Service Time on Edge for Health App (sec)', 'HEALTH_APP', '', 'lower right')
    plot_generic_line(2, 5, 'Service Time on Edge\nfor Infotainment App (sec)', 'INFOTAINMENT_APP', '', 'lower right')

    plot_generic_line(3, 5, 'Service Time on Cloud (sec)', 'ALL_APPS', '', 'upper left')
    plot_generic_line(3, 5, 'Service Time on Cloud\nfor Augmented Reality App (sec)', 'AUGMENTED_REALITY', '', 'upper left')
    plot_generic_line(3, 5, 'Service Time on Cloud for Health App (sec)', 'HEALTH_APP', '', 'upper left')
    plot_generic_line(3, 5, 'Service Time on Cloud\nfor Infotainment App (sec)', 'INFOTAINMENT_APP', '', 'upper left')
