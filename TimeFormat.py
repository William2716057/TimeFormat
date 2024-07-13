
from datetime import datetime, timedelta

def subtract_13_hours(input_time_str):
    #Time format
    input_time_format = "%Y:%m:%d %H:%M:%S"
    output_time_format = "%Y-%m-%d %H:%M:%S"
    
    
    input_time = datetime.strptime(input_time_str, input_time_format)
    
    # Subtract 13 hours
    new_time = input_time - timedelta(hours=13)
    
    # Return the new time in the specified format
    return new_time.strftime(output_time_format)

# Example usage
input_time_str = input("Enter Time (format: YYYY:MM:DD HH:MM:SS): ")
print(subtract_13_hours(input_time_str))