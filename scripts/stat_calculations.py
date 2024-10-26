import pandas as pd

def calculate_daily_stats(order_data):
    df = pd.DataFrame(order_data)
    # Aquí podrías calcular las estadísticas que desees
    daily_orders = df.groupby("date").size()
    return daily_orders

def export_stats_to_csv(stats, file_path):
    stats.to_csv(file_path)
