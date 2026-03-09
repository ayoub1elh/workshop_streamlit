"""
Main Sentiment Analysis Application
Uses modular architecture for clean code and scalability
"""

import streamlit as st
from modules.analysis import analyze_sentiment, get_sentiment_color
from modules.history import initialize_history, add_to_history, get_history_dataframe, export_history_csv, get_history_count
from modules.display import (
    setup_page_config, display_header, display_input_section,
    display_results, display_history, display_chart, display_download_button,
    display_warning
)


def main():
    """Main application function."""
    
    # Setup
    setup_page_config()
    initialize_history()
    
    # Display header and input
    display_header()
    texte = display_input_section()
    
    # Analysis button
    if st.button('🔍 Analyser le sentiment', type='primary'):
        if texte:
            # Perform analysis
            result = analyze_sentiment(texte)
            score = result['score']
            sentiment = result['sentiment']
            emoji = result['emoji']
            color = get_sentiment_color(score)
            
            # Add to history
            add_to_history(texte, score, sentiment)
            
            # Display results
            display_results(score, sentiment, emoji, color)
        else:
            display_warning('Veuillez entrer du texte avant d\'analyser !')
    
    # Display history and visualizations if there are entries
    if get_history_count() > 0:
        df_history = get_history_dataframe()
        display_history(df_history)
        
        # Display chart
        scores = [item['Score'] for item in st.session_state.historique]
        display_chart(scores, len(st.session_state.historique))
        
        # Display download button
        csv_data = export_history_csv()
        display_download_button(csv_data)


if __name__ == '__main__':
    main()
