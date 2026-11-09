"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data


# Part 1: vowel_count
def vowel_count(text: str) -> int:
    # TODO: Purpose: describe what this function computes.
    # the number of vowels in a word
    # TODO: Input(s): explain each parameter.
    #its an inputted string
    # TODO: Output: explain what the function returns.
    # returns the number of vowels
    # TODO: Replace this exception with your implementation.
    vowels = 0
    for i in text:
        if i == "a" or i=="e" or i=="i" or i=="o" or i=="u":
            vowels += 1
    return vowels


# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: describe what this function computes.
    # condensing a nested list into a short list of 2 elements
    # TODO: Input(s): explain each parameter.
    # nested lists
    # TODO: Output: explain what the function returns.
    # a shortened list of two elements
    # TODO: Replace this exception with your implementation.
    new_list = []
    for i in items:
        if len(i) == 2:
            new_list.append(i)
    return new_list

# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: describe what this function computes.
    # a new list with the elements equal to two be in ascending order
    # TODO: Input(s): explain each parameter.
    # a nested list with different number of elements
    # TODO: Output: explain what the function returns.
    # a new list with the nested list elements that equal two be in ascending order
    # TODO: Replace this exception with your implementation.
    new_list = []
    for i in items:
        if len(i) == 2:
            i.sort()
        new_list.append(i)
    return new_list
# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # TODO: Purpose: describe what this function computes.
    #sum of total price
    # TODO: Input(s): explain each parameter.
    # the dollars and cents
    # TODO: Output: explain what the function returns.
    #the sum of total price
    # TODO: Replace this exception with your implementation.
    first.dollars += second.dollars
    first.cents += second.cents
    if first.cents > 100:
        first.dollars += 1
        first.cents= first.cents % 100
    return first

# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # TODO: Purpose: describe what this function computes.
# area of a rectangle
    # TODO: Input(s): explain each parameter.
    #points of the bottom right and top left
    # TODO: Output: explain what the function returns.
    #the area
    # TODO: Replace this exception with your implementation.
    length = rectangle.bottom_right.x - rectangle.top_left.x
    width = rectangle.bottom_right.y - rectangle.top_left.y
    area = length * width
    return area

# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # TODO: Purpose: describe what this function computes.
    # retrieving the name of a book given an author
    # TODO: Input(s): explain each parameter.
    # the name of the author and a list of books/library
    # TODO: Output: explain what the function returns.
    # author and book
    # TODO: Replace this exception with your implementation.
    new_list = []
    for i in books:
        if author in i.authors:
            new_list.append(i)
    return new_list


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # TODO: Purpose: describe what this function computes.
    # find the center and radius of a circle in a rectangle
    # TODO: Input(s): explain each parameter.
    # the rectangle
    # TODO: Output: explain what the function returns.
    # the center and radius of a circle inside a rectangle
    # TODO: Replace this exception with your implementation.
    radius = (abs(rectangle.top_left.x-rectangle.bottom_right.x)**2 + (rectangle.top_left.y-rectangle.bottom_right.y)**2)**.5 / 2
    center = data.Point(abs(rectangle.top_left.x - rectangle.bottom_right.x)/2, abs(rectangle.top_left.y - rectangle.bottom_right.y)/2)
    return data.Circle(center, radius)
# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # TODO: Purpose: describe what this function computes.
    # finds the average pay rate among employees and filters out those who are below it
    # TODO: Input(s): explain each parameter.
    # list of employees
    # TODO: Output: explain what the function returns.
    # employees whose pay rate is below average
    # TODO: Replace this exception with your implementation.
    avg_pay = 0
    for i in employees:
        avg_pay += i.pay_rate
    if len(employees) != 0:
        avg_pay /= len(employees)
    return [employee.name for employee in employees if employee.pay_rate < avg_pay]