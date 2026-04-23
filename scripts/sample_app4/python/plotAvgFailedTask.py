from plot_generic_line import plot_generic_line

if __name__ == '__main__':
    print('--- sample_app4: Failed tasks (%) ---')
    plot_generic_line(
        1, 2, 'Failed Tasks (%)', 'ALL_APPS', calculate_percentage='percentage_of_all', legend_pos='upper left'
    )
    plot_generic_line(
        1,
        2,
        'Failed Tasks for\nAugmented Reality App (%)',
        'AUGMENTED_REALITY',
        calculate_percentage='percentage_of_all',
        legend_pos='upper left',
    )
    plot_generic_line(
        1, 2, 'Failed Tasks for Health App (%)', 'HEALTH_APP', calculate_percentage='percentage_of_all', legend_pos='upper left'
    )
    plot_generic_line(
        1,
        2,
        'Failed Tasks for\nInfotainment App (%)',
        'INFOTAINMENT_APP',
        calculate_percentage='percentage_of_all',
        legend_pos='upper left',
    )

    plot_generic_line(
        2, 2, 'Failed Tasks on Edge (%)', 'ALL_APPS', calculate_percentage='percentage_of_all', legend_pos='upper left'
    )
    plot_generic_line(
        2,
        2,
        'Failed Tasks on Edge for\nAugmented Reality App (%)',
        'AUGMENTED_REALITY',
        calculate_percentage='percentage_of_all',
        legend_pos='upper left',
    )
    plot_generic_line(
        2, 2, 'Failed Tasks on Edge for Health App (%)', 'HEALTH_APP', calculate_percentage='percentage_of_all', legend_pos='upper left'
    )
    plot_generic_line(
        2,
        2,
        'Failed Tasks on Edge for Infotainment App (%)',
        'INFOTAINMENT_APP',
        calculate_percentage='percentage_of_all',
        legend_pos='upper left',
    )

    plot_generic_line(
        3, 2, 'Failed Tasks on Cloud (%)', 'ALL_APPS', calculate_percentage='percentage_of_all', legend_pos='upper left'
    )
    plot_generic_line(
        3,
        2,
        'Failed Tasks on Cloud for\nAugmented Reality App (%)',
        'AUGMENTED_REALITY',
        calculate_percentage='percentage_of_all',
        legend_pos='upper left',
    )
    plot_generic_line(
        3, 2, 'Failed Tasks on Cloud for Health App (%)', 'HEALTH_APP', calculate_percentage='percentage_of_all', legend_pos='upper left'
    )
    plot_generic_line(
        3,
        2,
        'Failed Tasks on Cloud for Infotainment App (%)',
        'INFOTAINMENT_APP',
        calculate_percentage='percentage_of_all',
        legend_pos='upper left',
    )
