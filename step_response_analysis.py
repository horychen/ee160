import control
from pylab import np, plt, mpl
mpl.rc('font', family='Times New Roman', size=10.0)
mpl.rc('legend', fontsize=10)
mpl.rcParams['lines.linewidth'] = 0.75 # mpl.rc('lines', linewidth=4, linestyle='-.')
mpl.rcParams['mathtext.fontset'] = 'stix'


if True:
    omega_n = 1.0
    def get_attr(zeta, key='Overshoot'):
        T = control.TransferFunction([omega_n ** 2], [1, 2 * zeta * omega_n, omega_n ** 2])
        return control.step_info(T)['Overshoot']
    # zeta_list = np.concatenate(( np.arange(0.0, 0.3, 0.01), np.arange(0.3, 1, 0.05) ))
    zeta_list3 = np.arange(0.0, 1.1, 0.05)
    approximated_Overshoot_list = [100*np.exp(-zeta*np.pi/np.sqrt(1-zeta**2)) for zeta in zeta_list3]
    Overshoot_list = [get_attr(zeta, key='Overshoot') for zeta in zeta_list3]
    plt.figure()
    plt.plot(zeta_list3, Overshoot_list, 'o', color='red', label=r'Simulated PO')
    plt.plot(zeta_list3, approximated_Overshoot_list, 'x', color='black', label=r'Textbook PO')
    plt.xlabel(r'Zeta $\zeta$ [1]')
    plt.ylabel(r'Overshoot P.O. [%]')
    plt.title(r'Overshoot P.O. vs. Zeta $\zeta$')
    plt.grid(); plt.legend()
    plt.savefig(r'D:\horyc\Desktop\OvershootVsZeta.pdf', dpi=400, bbox_inches='tight', pad_inches=0)
    # plt.show()

if True:
    omega_n = 1.0
    def get_attr(zeta, key='PeakTime'):
        T = control.TransferFunction([omega_n ** 2], [1, 2 * zeta * omega_n, omega_n ** 2])
        return control.step_info(T)['PeakTime']
    zeta_list2 = np.concatenate(( np.arange(0.0, 0.3, 0.01), np.arange(0.3, 1, 0.05) ))
    approximated_Peak_time_list = [np.pi / np.sqrt(1-zeta**2) / omega_n for zeta in zeta_list2]
    Peak_time_list = [get_attr(zeta, key='PeakTime') for zeta in zeta_list2]
    plt.figure()
    plt.plot(zeta_list2, Peak_time_list, 'o', color='red', label=r'Simulated $T_p$')
    plt.plot(zeta_list2, approximated_Peak_time_list, 'x', color='black', label=r'Textbook $T_p$')
    plt.xlabel(r'Zeta $\zeta$ [1]')
    plt.ylabel(r'Peak Time $T_p$ [s]')
    plt.title(r'Peak Time $T_p$ vs. Zeta $\zeta$')
    plt.grid(); plt.legend()
    plt.savefig(r'D:\horyc\Desktop\PeakTimeVsZeta.pdf', dpi=400, bbox_inches='tight', pad_inches=0)
    # plt.show()

    omega_n = 1.0
    def get_attr(zeta, key='PeakTime'):
        T = control.TransferFunction([omega_n ** 2], [1, 2 * zeta * omega_n, omega_n ** 2])
        return control.step_info(T)['PeakTime']
    # zeta_list2 = np.concatenate(( np.arange(0.0, 0.3, 0.01), np.arange(0.3, 1, 0.05) ))
    zeta_list2 = np.arange(0.0, 0.3, 0.01)
    approximated_Peak_time_list = [np.pi / np.sqrt(1-zeta**2) / omega_n for zeta in zeta_list2]
    Peak_time_list = [get_attr(zeta, key='PeakTime') for zeta in zeta_list2]
    plt.figure()
    plt.plot(zeta_list2, Peak_time_list, 'o', color='red', label=r'Simulated $T_p$')
    plt.plot(zeta_list2, approximated_Peak_time_list, 'x', color='black', label=r'Textbook $T_p$')
    plt.xlabel(r'Zeta $\zeta$ [1]')
    plt.ylabel(r'Peak Time $T_p$ [s]')
    plt.title(r'Peak Time $T_p$ vs. Zeta $\zeta$')
    plt.grid(); plt.legend()
    plt.savefig(r'D:\horyc\Desktop\PeakTimeVsZeta2.pdf', dpi=400, bbox_inches='tight', pad_inches=0)
    # plt.show()

if True:
    omega_n = 1.0
    def get_attr(zeta, key='SettlingTime'):
        T = control.TransferFunction([omega_n ** 2], [1, 2 * zeta * omega_n, omega_n ** 2])
        return control.step_info(T)['SettlingTime']
    zeta_list1 = np.concatenate(( np.arange(0.0, 0.2, 0.01), np.arange(0.2, 5, 0.2) ))
    approximated_settling_time_list = [4 / zeta / omega_n for zeta in zeta_list1]
    settling_time_list = [get_attr(zeta, key='SettlingTime') for zeta in zeta_list1]
    plt.figure()
    plt.plot(zeta_list1, settling_time_list, 'o', color='red', label=r'Simulated $T_s$')
    plt.plot(zeta_list1, approximated_settling_time_list, 'x', color='black', label=r'Textbook $T_s$')
    plt.xlabel(r'Zeta $\zeta$ [1]')
    plt.ylabel(r'Settling Time $T_s$ [s]')
    plt.title(r'Settling Time $T_s$ vs. Zeta $\zeta$')
    plt.grid(); plt.legend(); #plt.show()
    plt.savefig(r'D:\horyc\Desktop\SettlingTimeVsZeta.pdf', dpi=400, bbox_inches='tight', pad_inches=0)



if False:
    # Three in one for comparison
    plt.figure()
    plt.plot(zeta_list1, settling_time_list, '-o', color='red', label=r'True $T_s$')
    plt.plot(zeta_list1, approximated_settling_time_list, '-x', color='black', label=r'Estimated $T_s$')
    plt.plot(zeta_list2, np.array(Peak_time_list), '--o', color='red', label=r'True $T_p$')
    plt.plot(zeta_list2, np.array(approximated_Peak_time_list), '--x', color='black', label=r'Estimated $T_p$')
    plt.plot(zeta_list3, Overshoot_list, 'o', color='red', label=r'True PO')
    plt.plot(zeta_list3, approximated_Overshoot_list, 'x', color='black', label=r'Estimated PO')
    plt.title(r'Settling Time $T_s$ vs. Zeta $\zeta$')
    plt.grid(); plt.legend(); plt.show()
    plt.savefig(r'D:\horyc\Desktop\ThreeMetricsVsZeta.pdf', dpi=400, bbox_inches='tight', pad_inches=0)



# backup non-compact version
if False:
    import control
    from pylab import np, plt, mpl
    mpl.rc('font', family='Times New Roman', size=10.0)
    mpl.rc('legend', fontsize=10)
    mpl.rcParams['lines.linewidth'] = 0.75 # mpl.rc('lines', linewidth=4, linestyle='-.')
    mpl.rcParams['mathtext.fontset'] = 'stix'

    omega_n = 1.0
    zeta = 0.707
    T = control.TransferFunction([omega_n ** 2], [1, 2 * zeta * omega_n, omega_n ** 2])
    # data_x , data_y = control.step_response(T)
    Ts_approximated = 4 / zeta / omega_n

    def get_attr(zeta, key='SettlingTime'):
        T = control.TransferFunction([omega_n ** 2], [1, 2 * zeta * omega_n, omega_n ** 2])
        return control.step_info(T)['SettlingTime']

    # Zeta
    zeta_list = np.concatenate(( np.arange(0.0, 0.2, 0.01), np.arange(0.2, 5, 0.2) ))
    print(f'{zeta_list=}')

    # Settling time
    approximated_settling_time_list = [4 / zeta / omega_n for zeta in zeta_list]
    settling_time_list = [get_attr(zeta, key='SettlingTime') for zeta in zeta_list]

    plt.plot(zeta_list, settling_time_list, 'o', color='red', label=r'True $T_s$')
    plt.plot(zeta_list, approximated_settling_time_list, 'x', color='black', label=r'Estimated $T_s$')
    plt.xlabel(r'Zeta $\zeta$ [1]')
    plt.ylabel(r'Settling Time $T_s$ [s]')
    plt.grid()
    plt.title(r'Settling Time $T_s$ vs. Zeta $\zeta$')
    plt.legend()
    plt.savefig(r'D:\horyc\Desktop\SettlingTimeVsZeta.pdf', dpi=400, bbox_inches='tight', pad_inches=0)
    plt.show()