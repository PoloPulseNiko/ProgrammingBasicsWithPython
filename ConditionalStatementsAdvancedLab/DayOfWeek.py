number = int(input())
day = ""

match number:
    case 1:
        day = "Monday"
    case 2:
        day = "Tuesday"
    case 3:
        day = "Wednesday"
    case 4:
        day = "Thursday"
    case 5:
        day = "Friday"
    case 6:
        day = "Saturday"
    case 7:
        day = "Sunday"
    case default:
        day = "Error"

print(day)