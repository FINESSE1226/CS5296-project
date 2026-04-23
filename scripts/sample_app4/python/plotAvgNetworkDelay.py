from plot_generic_line import plot_generic_line

if __name__ == '__main__':
    print('--- sample_app4: Average Network Delay ---')
    plot_generic_line(1, 7, 'Average Network Delay (sec)', 'ALL_APPS', '', 'upper left')
    plot_generic_line(1, 7, 'Average Network Delay\nfor Augmented Reality App (sec)', 'AUGMENTED_REALITY', '', 'upper left')
    plot_generic_line(1, 7, 'Average Network Delay for Health App (sec)', 'HEALTH_APP', '', 'upper left')
    plot_generic_line(1, 7, 'Average Network Delay\nfor Infotainment App (sec)', 'INFOTAINMENT_APP', '', 'upper left')

    plot_generic_line(5, 1, 'Average WLAN Delay (sec)', 'ALL_APPS', '', 'upper left')
    plot_generic_line(5, 1, 'Average WLAN Delay\nfor Augmented Reality App (sec)', 'AUGMENTED_REALITY', '', 'upper left')
    plot_generic_line(5, 1, 'Average WLAN Delay for Health App (sec)', 'HEALTH_APP', '', 'upper left')
    plot_generic_line(5, 1, 'Average WLAN Delay\nfor Infotainment App (sec)', 'INFOTAINMENT_APP', '', 'upper left')

    plot_generic_line(5, 2, 'Average MAN Delay (sec)', 'ALL_APPS', '', 'upper right')
    plot_generic_line(5, 2, 'Average MAN Delay\nfor Augmented Reality App (sec)', 'AUGMENTED_REALITY', '', 'upper right')
    plot_generic_line(5, 2, 'Average MAN Delay for Health App (sec)', 'HEALTH_APP', '', 'upper right')
    plot_generic_line(5, 2, 'Average MAN Delay\nfor Infotainment App (sec)', 'INFOTAINMENT_APP', '', 'lower left')

    plot_generic_line(5, 3, 'Average WAN Delay (sec)', 'ALL_APPS', '', 'upper left')
    plot_generic_line(5, 3, 'Average WAN Delay\nfor Augmented Reality App (sec)', 'AUGMENTED_REALITY', '', 'upper left')
    plot_generic_line(5, 3, 'Average WAN Delay for Health App (sec)', 'HEALTH_APP', '', 'upper left')
    plot_generic_line(5, 3, 'Average WAN Delay\nfor Infotainment App (sec)', 'INFOTAINMENT_APP', '', 'upper left')
