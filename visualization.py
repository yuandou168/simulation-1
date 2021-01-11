
print('DQN-based MARL Gantt图========')
    c_tmp = pd.read_excel("./datasets/WSP_dataset.xlsx", sheet_name="Containers Price")
    CONTAINERS = list(c_tmp.loc[:, 'Configuration Types'])
    m_keys = [j + 1 for j in range (len(CONTAINERS))]
    j_keys = [j for j in range (5)]
    df = []

    record = []
    for k in opt_strategy:
        start_time = str (datetime.timedelta (seconds=k[2]))
        end_time = str (datetime.timedelta (seconds=k[3]))
        record.append ((k[0], k[1], [start_time, end_time]))
    print(len(record))

    for m in m_keys:
        for j in j_keys:
                for i in record:
                    if (m, j) == (i[1], i[0]):
                            df.append (dict (Task='Container %s ' % (CONTAINERS[m - 1]), Start='2020-01-16 %s' % (str(i[2][0])),
                                                        Finish='2020-01-16 %s' % (str (i[2][1])),
                                                        Resource='Workflow %s' % (j + 1)))
    fig = ff.create_gantt (df, index_col='Resource', show_colorbar=True, group_tasks=True,
                                            showgrid_x=True,
                                            title='DQN-based MARL Workflow Scheduling')
    py.plot(fig, filename='DQN-based_MARL_workflow_scheduling', world_readable=True)