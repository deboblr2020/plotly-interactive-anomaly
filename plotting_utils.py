import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def create_box_violin_plots(df, event_type):
    """
    Create box plot and violin plot for a specific event type.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame containing the data
    event_type : str
        The event type to filter the data
        
    Returns:
    --------
    plotly.graph_objects.Figure
        Figure containing both plots
    """
    # Filter data for the specific event type
    filtered_df = df[df['eventType'] == event_type]
    
    # Create subplot figure with 1 row and 2 columns
    fig = make_subplots(rows=1, cols=2,
                       subplot_titles=('Box Plot', 'Violin Plot'),
                       shared_yaxes=True)
    
    # Add box plot
    fig.add_trace(
        go.Box(y=filtered_df['reconstruction_error'],
               name='Box Plot',
               boxpoints='all',
               jitter=0.3,
               pointpos=-1.8),
        row=1, col=1
    )
    
    # Add violin plot
    fig.add_trace(
        go.Violin(y=filtered_df['reconstruction_error'],
                 name='Violin Plot',
                 box_visible=True,
                 meanline_visible=True),
        row=1, col=2
    )
    
    # Update layout
    fig.update_layout(
        title=f'Distribution of Reconstruction Error for {event_type}',
        height=600,
        width=1000,
        showlegend=False,
        template='plotly_white'
    )
    
    # Update y-axis labels
    fig.update_yaxes(title_text='Reconstruction Error', row=1, col=1)
    fig.update_yaxes(title_text='Reconstruction Error', row=1, col=2)
    
    return fig 