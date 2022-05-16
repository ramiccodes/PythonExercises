
income=int(input("How much is your annual income?:"))
employment_time=int(input("How many years have you been with your company?:"))
if income>=30000:
    if employment_time>=2:
        print("You qualify for the loan.")
    else:
        print("You must have been on your current job for at least two years to qualify.")
else:
    print("You must earn at least $30,000 per year to qualify.")
