from datetime import datetime, timedelta

def get_free_slots(calendar1, calendar1_limits, calendar2, calendar2_limits, meeting_time):
    # Convertim stringurile de timp în obiecte datetime
    calendar1_limits = [datetime.strptime(t, '%H:%M') for t in calendar1_limits]
    calendar2_limits = [datetime.strptime(t, '%H:%M') for t in calendar2_limits]
    calendar1 = [tuple(datetime.strptime(t, '%H:%M') for t in slot) for slot in calendar1]
    calendar2 = [tuple(datetime.strptime(t, '%H:%M') for t in slot) for slot in calendar2]

    # Combinăm calendarele și le sortăm după timp
    merged_calendar = sorted(calendar1 + calendar2)

    # Găsim intervalele de timp disponibile
    free_slots = []
    start_time = max(calendar1_limits[0], calendar2_limits[0])
    end_time = min(calendar1_limits[1], calendar2_limits[1])
    current_time = start_time
    for slot_start, slot_end in merged_calendar:
        if current_time + timedelta(minutes=meeting_time) <= slot_start:
            free_slots.append((current_time, slot_start))
        current_time = max(current_time, slot_end)
    if current_time + timedelta(minutes=meeting_time) <= end_time:
        free_slots.append((current_time, end_time))

    # Convertim din nou obiectele datetime în stringuri de timp
    free_slots = [(s.strftime('%H:%M'), e.strftime('%H:%M')) for s, e in free_slots]

    return free_slots

calendar1 = [['9:00','10:30'], ['12:00','13:00'], ['16:00','18:00']]
calendar1_limits = ['9:00','20:00']
calendar2 = [['10:00','11:30'], ['12:30','14:30'],['14:30','15:00'], ['16:00','17:00']]
calendar2_limits = ['10:00','18:30']
meeting_time = 30

free_slots = get_free_slots(calendar1, calendar1_limits, calendar2, calendar2_limits, meeting_time)

print(free_slots)
# Output: [('11:30', '12:00'), ('15:00', '16:00'), ('18:00', '18:30')]
