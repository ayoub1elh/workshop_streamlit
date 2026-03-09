"""
Display/UI Module
Handles all user interface display components
"""

import streamlit as st
import pandas as pd
from datetime import datetime


def setup_page_config():
    """Configure the Streamlit page settings."""
    st.set_page_config(
        page_title='Analyseur de Sentiments',
        page_icon='🎭',
        layout='centered'
    )


def display_header():
    """Display the header section of the app."""
    st.title('🎭 Analyseur de Sentiments IA')
    st.write('Entrez un texte et découvrez son sentiment !')
    st.divider()


def display_input_section():
    """
    Display the input section for text analysis.
    
    Returns:
        str: The text entered by the user
    """
    texte = st.text_area(
        'Votre texte à analyser :',
        placeholder='Ex: This product is absolutely amazing!',
        height=150
    )
    return texte


def display_results(score: float, sentiment: str, emoji: str, color: str):
    """
    Display the analysis results.
    
    Args:
        score (float): The sentiment score
        sentiment (str): The sentiment classification
        emoji (str): The emoji to display
        color (str): The color for the message ('success', 'error', 'info')
    """
    st.divider()
    
    # Display metrics in two columns
    col1, col2 = st.columns(2)
    col1.metric('Score de sentiment', f'{score:.2f}')
    col2.metric('Résultat', f'{emoji} {sentiment}')
    
    # Display colored message
    message = f'Texte {sentiment} détecté {emoji}'
    
    if color == 'success':
        st.success(message)
    elif color == 'error':
        st.error(message)
    else:
        st.info(message)


def display_history(df: pd.DataFrame):
    """
    Display the analysis history as a table.
    
    Args:
        df (pd.DataFrame): The history dataframe
    """
    st.divider()
    st.subheader('📊 Historique des analyses')
    st.dataframe(df, use_container_width=True, hide_index=True)


def display_chart(scores: list, num_analyses: int = None):
    """
    Display a line chart of sentiment evolution.
    
    Args:
        scores (list): List of sentiment scores
        num_analyses (int): Number of analyses (defaults to length of scores)
    """
    st.subheader('📈 Évolution des scores de sentiment')
    
    if num_analyses is None:
        num_analyses = len(scores)
    
    # Create dataframe for chart
    df_chart = pd.DataFrame({
        'Analyse': range(1, num_analyses + 1),
        'Score': scores
    })
    
    st.line_chart(df_chart.set_index('Analyse'))


def display_download_button(csv_data: bytes, filename: str = None):
    """
    Display a download button for CSV export.
    
    Args:
        csv_data (bytes): The CSV data to download
        filename (str): The filename for the download
    """
    st.divider()
    
    if filename is None:
        filename = f'sentiment_analysis_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    
    st.download_button(
        label='📥 Télécharger l\'historique (CSV)',
        data=csv_data,
        file_name=filename,
        mime='text/csv',
        type='secondary'
    )


def display_warning(message: str):
    """Display a warning message."""
    st.warning(message)


def display_info(message: str):
    """Display an info message."""
    st.info(message)


def display_error(message: str):
    """Display an error message."""
    st.error(message)
