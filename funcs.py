import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


def faz_grafico(dry_ctr, dry_sts, wet_ctr, wet_sts):
    count = 0

    # tabela = tabela.T

    for i in dry_ctr.iloc:
        tab = pd.DataFrame(i)

        fig = px.line(tab,
                      y=tab.columns.values.tolist(),
                      title=f'Gene {tab.columns.values.tolist()[0]}',
                      # y=tabela.index,
                      # labels={'value': 'Expression'},
                      # title=f'{count}: Relation between {reg} and {targ}: Max_R: {max_r}, Min_R: {min_r}, Max_T: {max_t}, Min_T: {min_t}',
                      # color_discrete_sequence=['#fcba03', '#0324fc']
                      )

        # newnames = {reg: f'Regulator_{reg}', targ: f'Target_{targ}'}
        # fig.for_each_trace(lambda t: t.update(name=newnames[t.name]))

        st.plotly_chart(fig, use_container_width=True)


def faz_grafico2(dry_ctr, dry_sts, wet_ctr, wet_sts):
    indices = dry_sts.index.tolist()

    for i in indices:
        fig = go.Figure()

        dc = dry_ctr.filter(items=[i], axis=0)
        ds = dry_sts.filter(items=[i], axis=0)
        wc = wet_ctr.filter(items=[i], axis=0)
        ws = wet_sts.filter(items=[i], axis=0)

        ## add the two lines

        fig.add_trace(go.Scatter(y=dc.T[i],
                                 x=dc.columns.values.tolist(),
                                 name='Dry_Ctr',
                                 mode='lines',
                                 line=dict(color="red", width=2)))
        fig.add_trace(go.Scatter(y=ds.T[i],
                                 x=ds.columns.values.tolist(),
                                 name='Dry_Sts',
                                 mode='lines',
                                 line=dict(color="blue", width=2)))
        fig.add_trace(go.Scatter(y=wc.T[i],
                                 x=wc.columns.values.tolist(),
                                 name='Wet_Ctr',
                                 mode='lines',
                                 line=dict(color="green", width=2)))
        fig.add_trace(go.Scatter(y=ws.T[i],
                                 x=ws.columns.values.tolist(),
                                 name='Wet_Sts',
                                 mode='lines',
                                 line=dict(color="yellow", width=2)))
        fig.update_layout(title_text=f"Gene {i}")

        st.plotly_chart(fig, use_container_width=True)


def faz_grafico3(dry_ctr, dry_sts, wet_ctr, wet_sts):
    indices = dry_sts.index.tolist()

    for i in indices:
        fig = go.Figure()

        dc = dry_ctr.filter(items=[i], axis=0)
        ds = dry_sts.filter(items=[i], axis=0)
        wc = wet_ctr.filter(items=[i], axis=0)
        ws = wet_sts.filter(items=[i], axis=0)

        ## add the two lines

        fig.add_trace(go.Bar(y=dc.T[i],
                             x=dc.columns.values.tolist(),
                             name='Dry_Ctr',
                             # mode='lines',
                             # line=dict(color="red", width=2)
                             ))
        fig.add_trace(go.Bar(y=ds.T[i],
                             x=ds.columns.values.tolist(),
                             name='Dry_Sts',
                             # mode='lines',
                             # line=dict(color="blue", width=2))
                             ))
        fig.add_trace(go.Bar(y=wc.T[i],
                             x=wc.columns.values.tolist(),
                             name='Wet_Ctr',
                             # mode='lines',
                             # line=dict(color="green", width=2))
                             ))
        fig.add_trace(go.Bar(y=ws.T[i],
                             x=ws.columns.values.tolist(),
                             name='Wet_Sts',
                             # mode='lines',
                             # line=dict(color="yellow", width=2))
                             ))
        fig.update_layout(title_text=f"Gene {i}")

        st.plotly_chart(fig, use_container_width=True)


def faz_grafico4(dry_ctr, dry_sts, wet_ctr, wet_sts):
    indices = dry_sts.index.tolist()

    for i in indices:
        fig = go.Figure()

        dc = dry_ctr.filter(items=[i], axis=0)
        ds = dry_sts.filter(items=[i], axis=0)
        wc = wet_ctr.filter(items=[i], axis=0)
        ws = wet_sts.filter(items=[i], axis=0)

        m_dc = np.mean(dc)
        m_ds = np.mean(ds)
        m_wc = np.mean(wc)
        m_ws = np.mean(ws)

        dp_dc = np.std(dc, axis=1)
        dp_ds = np.std(ds, axis=1)
        dp_wc = np.std(wc, axis=1)
        dp_ws = np.std(ws, axis=1)

        st.divider()

        col0, col1 = st.columns(2)

        col0.write(f'Media Dry Control: {m_dc:.2f}')
        col0.write(f'Media Dry Stressed: {m_ds:.2f}')
        col0.write(f'Media Wet Control: {m_wc:.2f}')
        col0.write(f'Media Wet Stressed: {m_ws:.2f}')

        col1.write(f'Desv. Padrao Dry Control: {dp_dc}')
        col1.write(f'Desv. Padrao Dry Stressed: {dp_ds}')
        col1.write(f'Desv. Padrao Wet Control: {dp_wc}')
        col1.write(f'Desv. Padrao Wet Stressed: {dp_ws}')

        print(f'Desv. Padrao Dry Control: {dp_dc}')

        fig.add_trace(go.Box(y=dc.T[i],
                             # x=dc.columns.values.tolist(),
                             name='Dry_Ctr',
                             boxmean='sd',
                             # mode='lines',
                             # line=dict(color="red", width=2)
                             ))
        fig.add_trace(go.Box(y=ds.T[i],
                             # x=ds.columns.values.tolist(),
                             name='Dry_Sts',
                             boxmean='sd',
                             # mode='lines',
                             # line=dict(color="blue", width=2))
                             ))
        fig.add_trace(go.Box(y=wc.T[i],
                             # x=wc.columns.values.tolist(),
                             name='Wet_Ctr',
                             boxmean='sd',
                             # mode='lines',
                             # line=dict(color="green", width=2))
                             ))
        fig.add_trace(go.Box(y=ws.T[i],
                             # x=ws.columns.values.tolist(),
                             name='Wet_Sts',
                             boxmean='sd',
                             # mode='lines',
                             # line=dict(color="yellow", width=2))
                             ))
        fig.update_layout(title_text=f"Gene {i}")

        st.plotly_chart(fig, use_container_width=True)


def faz_grafico5_todos(dry_ctr, dry_sts, wet_ctr, wet_sts):
    indices = dry_sts.index.tolist()

    for i in indices:
        fig = go.Figure()

        dc = dry_ctr.filter(items=[i], axis=0)
        ds = dry_sts.filter(items=[i], axis=0)
        wc = wet_ctr.filter(items=[i], axis=0)
        ws = wet_sts.filter(items=[i], axis=0)

        m_dc = np.mean(dc)
        m_ds = np.mean(ds)
        m_wc = np.mean(wc)
        m_ws = np.mean(ws)

        dp_dc = np.std(dc.values, axis=1)
        dp_ds = np.std(ds, axis=1)
        dp_wc = np.std(wc, axis=1)
        dp_ws = np.std(ws, axis=1)

        st.divider()

        col0, col1 = st.columns(2)

        col0.write(f'Media Dry Control: {m_dc:.2f}')
        col0.write(f'Media Dry Stressed: {m_ds:.2f}')
        col0.write(f'Media Wet Control: {m_wc:.2f}')
        col0.write(f'Media Wet Stressed: {m_ws:.2f}')

        col1.write(f'Desv. Padrao Dry Control: {dp_dc[0]}')
        col1.write(f'Desv. Padrao Dry Stressed: {dp_ds[0]}')
        col1.write(f'Desv. Padrao Wet Control: {dp_wc[0]}')
        col1.write(f'Desv. Padrao Wet Stressed: {dp_ws[0]}')

        print(f'Desv. Padrao Dry Control: {dp_dc}')

        fig.add_trace(go.Scatter(y=[m_dc],
                                 x=['Dry_CTR'],
                                 error_y=dict(
                                     type='data',  # value of error bar given in data coordinates
                                     array=dp_dc,
                                     visible=True),
                                 # x=dc.columns.values.tolist(),
                                 name='Dry_Ctr',
                                 # mode='lines',
                                 # line=dict(color="red", width=2)
                                 ))
        fig.add_trace(go.Scatter(y=[m_ds],
                                 x=['Dry_STS'],
                                 error_y=dict(
                                     type='data',  # value of error bar given in data coordinates
                                     array=dp_ds,
                                     visible=True),
                                 name='Dry_Sts',
                                 # mode='lines',
                                 # line=dict(color="blue", width=2))
                                 ))
        fig.add_trace(go.Scatter(y=[m_wc],
                                 x=['Wet_CTR'],
                                 error_y=dict(
                                     type='data',  # value of error bar given in data coordinates
                                     array=dp_wc,
                                     visible=True),
                                 name='Wet_Ctr',
                                 # mode='lines',
                                 # line=dict(color="green", width=2))
                                 ))
        fig.add_trace(go.Scatter(y=[m_ws],
                                 x=['Wet_STS'],
                                 error_y=dict(
                                     type='data',  # value of error bar given in data coordinates
                                     array=dp_ws,
                                     visible=True),
                                 name='Wet_Sts',
                                 # mode='lines',
                                 # line=dict(color="yellow", width=2))
                                 ))
        fig.update_layout(title_text=f"Gene {i}")

        st.plotly_chart(fig, use_container_width=True)


def faz_grafico5(wet_ctr, wet_sts):
    indices = wet_ctr.index.tolist()

    for i in indices:
        fig = go.Figure()

        wc = wet_ctr.filter(items=[i], axis=0)
        ws = wet_sts.filter(items=[i], axis=0)

        m_wc = np.mean(wc)
        m_ws = np.mean(ws)

        dp_wc = np.std(wc, axis=1)
        dp_ws = np.std(ws, axis=1)

        st.divider()

        col0, col1 = st.columns(2)

        col0.write(f'Media Wet Control: {m_wc:.2f}')
        col0.write(f'Media Wet Stressed: {m_ws:.2f}')

        col1.write(f'Desv. Padrao Wet Control: {dp_wc[0]}')
        col1.write(f'Desv. Padrao Wet Stressed: {dp_ws[0]}')

        fig.add_trace(go.Scatter(y=[m_wc],
                                 x=['Wet_CTR'],
                                 error_y=dict(
                                     type='data',  # value of error bar given in data coordinates
                                     array=dp_wc,
                                     visible=True),
                                 name='Wet_Ctr',
                                 # mode='lines',
                                 # line=dict(color="green", width=2))
                                 ))
        fig.add_trace(go.Scatter(y=[m_ws],
                                 x=['Wet_STS'],
                                 error_y=dict(
                                     type='data',  # value of error bar given in data coordinates
                                     array=dp_ws,
                                     visible=True),
                                 name='Wet_Sts',
                                 # mode='lines',
                                 # line=dict(color="yellow", width=2))
                                 ))
        fig.update_layout(title_text=f"Gene {i}")

        st.plotly_chart(fig, use_container_width=True)


def dataframe_with_selections(df):
    df_with_selections = df.copy()
    df_with_selections.insert(0, "Select", False)

    # Get dataframe row-selections from user with st.data_editor
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=False,
        column_config={"Select": st.column_config.CheckboxColumn(required=True)},
        # disabled=df.columns,
    )

    # Filter the dataframe using the temporary column, then drop the column
    selected_rows = edited_df[edited_df.Select]
    return selected_rows.drop('Select', axis=1)
