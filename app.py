import streamlit as st
import streamlit_ext as ste
from funcs import *

st.set_page_config(page_title='Analise Count Table', layout='wide')

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """

st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title('Analise Count Tables')

tabela_ct = st.file_uploader(label='Upload the excel file',
                             type='txt',
                             help='Upload the file with the genes of interest')

if tabela_ct:

    tabela_ct = pd.read_csv(tabela_ct, sep='\t')
    tabela_ct.set_index('Feature', inplace=True)

    # tabela_ct = tabela_ct.T

    # tabela['Number'] = tabela.index.astype('str')
    # tabela['Transcriptome'] = 'Transcriptome_' + tabela['Number']

    st.write(tabela_ct)

    # filtro = st.multiselect(label='Genes', options=[column for column in tabela_ct.index])
    filtro = st.text_input('Input')

    fil = filtro.split()
    # st.write(filtro)

    if filtro:

        tabela_ct = tabela_ct.filter(items=fil, axis=0)

        # dry_ctr = tabela_ct[['AF_T2021_OilPalm_A1', 'AF_T2021_OilPalm_A2',
        #                     'AF_T2021_OilPalm_A3', 'AF_T2021_OilPalm_A4', 'AF_T2021_OilPalm_A5',
        #                     'AF_T2021_OilPalm_A6']]
        # dry_sts = tabela_ct[['AF_T2021_OilPalm_S1', 'AF_T2021_OilPalm_S2',
        #                     'AF_T2021_OilPalm_S3', 'AF_T2021_OilPalm_S4', 'AF_T2021_OilPalm_S5',
        #                     'AF_T2021_OilPalm_S6']]
        wet_ctr = tabela_ct[['AF_T2022_OilPalm_A1', 'AF_T2022_OilPalm_A2',
                             'AF_T2022_OilPalm_A3', 'AF_T2022_OilPalm_A4', 'AF_T2022_OilPalm_A5',
                             'AF_T2022_OilPalm_A6']]
        wet_sts = tabela_ct[['AF_T2022_OilPalm_S1', 'AF_T2022_OilPalm_S2',
                             'AF_T2022_OilPalm_S3', 'AF_T2022_OilPalm_S4', 'AF_T2022_OilPalm_S5',
                             'AF_T2022_OilPalm_S6']]

        # with st.form('formulario'):
        #    selection = dataframe_with_selections(tabela_ct)
        #    submitted = st.form_submit_button("Submit")

        st.write("Your selection:")
        # st.write(selection)
        st.write(f'Seleção de {tabela_ct.shape[0]} genes')
        st.write(tabela_ct)

        tipo_gr = st.radio('Selecione o tipo de grafico: ',
                           options=['Linha', 'Coluna', 'BoxPlot', 'Media'])

        if tipo_gr == 'Linha':
            pass
            # faz_grafico2(dry_ctr, dry_sts, wet_ctr, wet_sts)

        if tipo_gr == 'Coluna':
            pass
            # faz_grafico3(dry_ctr, dry_sts, wet_ctr, wet_sts)

        if tipo_gr == 'BoxPlot':
            pass
            # faz_grafico4(dry_ctr, dry_sts, wet_ctr, wet_sts)

        if tipo_gr == 'Media':
            faz_grafico5(wet_ctr, wet_sts)
