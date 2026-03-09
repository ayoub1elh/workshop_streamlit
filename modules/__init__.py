"""
Modules package for Sentiment Analysis Application
"""

from .analysis import analyze_sentiment, get_sentiment_color
from .history import (
    initialize_history, 
    add_to_history,
    get_history_dataframe,
    export_history_csv,
    clear_history,
    get_history_count
)
from .display import (
    setup_page_config,
    display_header,
    display_input_section,
    display_results,
    display_history,
    display_chart,
    display_download_button
)

__all__ = [
    # Analysis
    'analyze_sentiment',
    'get_sentiment_color',
    
    # History
    'initialize_history',
    'add_to_history',
    'get_history_dataframe',
    'export_history_csv',
    'clear_history',
    'get_history_count',
    
    # Display
    'setup_page_config',
    'display_header',
    'display_input_section',
    'display_results',
    'display_history',
    'display_chart',
    'display_download_button'
]
