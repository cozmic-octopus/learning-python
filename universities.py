
def enrollment_stats(list_of_lists):
    """takes as an input a list of lists where each individual list contains:
    a) the name of a uni, b) total number of students, c) annual tuition fees
    the function returns two lists: student enrollment values, all of the tuition fees"""
    students = []
    tuition = []
    for i in list_of_lists:
        students.append(i[1])
        tuition.append(i[2])
    return students, tuition


def mean(single_list):
    return sum(single_list)/len(single_list)


def median(single_list):
    single_list.sort()
    return single_list[len(single_list)//2]


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

stds, fees = enrollment_stats(universities)
print("*"*31)
print(f"Total students:   {sum(stds):,}\nTotal tuition:  $ {sum(fees):,}\n")
print(f"Student mean:     {mean(stds):,.2f}\nStudent median:   {median(stds):,}\n")
print(f"Tuition mean:   $ {mean(fees):,.2f}\nTuition median: $ {median(fees):,}")
print("*"*31)
