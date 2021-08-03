from date_input import date
from month_input import time_frame
from input_existant_centres import centre_input
from opening_new_centre import monthly_centre
from trainee_generation import trainee_gen
from stu_assignment import student_assignment
from num_full_centers import num_full
today = date(0)
months = time_frame()
end_date = date(months)
month_tick = 0
centers = centre_input()
wait_list = 0

while date(month_tick) != end_date:
    month_tick += 1
    if month_tick & 2 == 0 and month_tick != 0:
        # generates new centre every two months
        centers = monthly_centre(centers)
    intake = trainee_gen()
    centers, wait_list = student_assignment(centers, wait_list, intake)

print(len(centers), centers, wait_list, sum(centers.values()), num_full(centers))