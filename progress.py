from datetime import datetime

this_year = datetime.now().year
start_time_of_this_year = datetime(this_year, 1, 1, 0, 0, 0).timestamp()
end_time_of_this_year = datetime(this_year, 12, 31, 23, 59, 59).timestamp()
progress_of_this_year = (datetime.now().timestamp() - start_time_of_this_year) / (end_time_of_this_year - start_time_of_this_year)

def generate_progress_bar():
    progress_bar_capacity = 30
    passed_progress_bar_index = int(progress_of_this_year * progress_bar_capacity)
    progress_bar = ['▁' if i >= passed_progress_bar_index else '█' for i in range(progress_bar_capacity)]
    return '{ ' + ''.join(progress_bar) + ' }'

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

progress_bar_of_this_year = generate_progress_bar()
