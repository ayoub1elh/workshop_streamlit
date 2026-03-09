"""
History Management Module
Handles storing and retrieving analysis history
"""

import streamlit as st
import pandas as pd
from datetime import datetime


def initialize_history():
    """Initialize the history in session_state if not already present."""
    if 'historique' not in st.session_state:
        st.session_state.historique = []


def add_to_history(texte: str, score: float, sentiment: str, max_entries: int = 5):
    """
    Add a new analysis to the history.
    
    Args:
        texte (str): The analyzed text
        score (float): The sentiment score
        sentiment (str): The sentiment classification
        max_entries (int): Maximum number of entries to keep
    """
    entry = {
        'Texte': texte[:50] + '...' if len(texte) > 50 else texte,
        'Score': round(score, 2),
        'Sentiment': sentiment,
        'Timestamp': datetime.now().strftime('%H:%M:%S')
    }
    
    st.session_state.historique.append(entry)
    
    # Keep only the last N entries
    if len(st.session_state.historique) > max_entries:
        st.session_state.historique = st.session_state.historique[-max_entries:]


def get_history_dataframe() -> pd.DataFrame:
    """
    Get the history as a pandas DataFrame.
    
    Returns:
        pd.DataFrame: The analysis history
    """
    return pd.DataFrame(st.session_state.historique)


def export_history_csv() -> bytes:
    """
    Export the history as CSV.
    
    Returns:
        bytes: CSV data encoded in UTF-8
    """
    df = get_history_dataframe()
    return df.to_csv(index=False).encode('utf-8')


def clear_history():
    """Clear the entire history."""
    st.session_state.historique = []


def get_history_count() -> int:
    """
    Get the number of entries in history.
    
    Returns:
        int: Number of entries
    """
    return len(st.session_state.historique)
