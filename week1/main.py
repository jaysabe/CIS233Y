# Named arguments versus keyword arguments

def get_integer(prompt, gt=None, ge=None, le=None, ):
    while True:
        try:
            val = int(input(prompt))
            return val
        except ValueError:
            print("Please enter a whole number!")

'''
Keyword arguments -- optional params 

'''
if __name__ == '__main__':
    print(get_integer("Please enter a year: "))
    print(get_integer("Please enter a year between 1915 and 2014: ", ge=1915, le=2014))
    print(get_integer("Please enter a year after 1960", gt=1960))
    print(get_integer("Please enter a year before 2022", lt=2022))