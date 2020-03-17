def twoSum(nums, target):
    chk_map={}
    for index, val in enumerate(nums):
        compl=target-val
        if compl in chk_map:
            indices = [chk_map[compl], index]
            print(indices)
            return [indices]
        else:
            chk_map[val] = index
    return False

if __name__ == '__main__':
    user_input = input("Enter numbers separated by comma: \n").strip()
    collection = [int(item) for item in user_input.split(",")]

    target_input = input("Enter a single number to find sum in the list: \n")
    target = int(target_input)

    result = twoSum(collection, target)