# implementation of binary search algorithm
def binary_search(list_of_elements,target):
    low, high = 0, len(list_of_elements)

    while low <= high:
        mid= (low + high)/2
        mid = int(mid)

        # check if the middle element is the target
        if list_of_elements[mid] == target:
            return mid
        # if the target is smaller, ignore the right half
        elif list_of_elements[mid] > target:
            high = mid - 1
        # if the target is larget, ignor the right half
        else:
            low = mid + 1
    # if the target is not found in the array
    return -1

def user_input():
    while True:
        user_input_str = input("Enter an element (Number) you want to search using binary search: ")

        # Check if the user entered nothing
        if not user_input_str.strip():
            print("You have not entered any element, please try again")
            continue

        try:
            element = int(user_input_str)
            return element
        except ValueError:
            print("Invalid input, please enter a valid number.")

if __name__ == "__main__":
    list_of_elements = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    element = user_input()
    result = binary_search(list_of_elements,element)
    if result != -1:
        print(f"Target {element} found at index {result}")
    else:
        (f"Target {element} not found in tha list")