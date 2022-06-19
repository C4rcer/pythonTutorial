has_high_income = True
has_good_credit = False
# has_criminal_record = False

# if has_good_credit and not has_criminal_record:  # if good credit and criminal record is not true
#    print("Eligible for loan")

if has_good_credit or has_high_income:  # AND: both, OR: at least one (NOT reverse the bool value)
    print("Eligible for loan")
