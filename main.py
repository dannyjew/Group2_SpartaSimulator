from date_input import date
from month_input import time_frame
from input_existent_centres import centre_input
from opening_new_centre import monthly_centre
from trainee_generation import trainee_gen
from stu_assignment import student_assignment
from num_full_centers import num_full
from plotting import time_centers, time_trainees,  show
today = date(0)
month = time_frame()
print(f"This simulation will show you what Sparta will look like in {month} months.") # this is to confirm the month or the user can re-start
end_date = date(month)
month_tick = 0
centers = centre_input()
wait_list = 0
centers_month = [len(centers,)]
trainees_month = [0,]
month = [0,]
month_c = [0,]
while date(month_tick) != end_date:
    month_tick += 1
    month.append(month[-1]+1)
    if month_tick % 2 == 0 and month_tick != 0:
        month_c.append(month_c[-1]+2)
        centers_month.append(centers_month[-1] + 1)
        # generates new centre every two month
        centers = monthly_centre(centers)
    intake = trainee_gen()
    trainees_month.append(trainees_month[-1] + intake)
    centers, wait_list = student_assignment(centers, wait_list, intake)


time_centers(month_c, centers_month, month)
time_trainees(month, trainees_month)


print(f"There are {len(centers)} center(s), training {sum(centers.values())} trainees, {num_full(centers)} center(s) is/are full, and there are {wait_list} on the wait list.")
# comment out show if being run through gui
show()