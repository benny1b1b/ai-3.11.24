def my_evg(num1:int, num2:int) ->float:
    """A function that receives two numbers and outputs an average"""
    return (num1+ num2) /2

# avg1= (my_evg(90, 99))
# print(avg1)

if '__name__' == '__main__':
    def headline_my(word: str) -> str:
        return word.upper() + "!"
    head1 = headline_my("world the concurred has python")
    print(head1)
    print(head1)

if '__name__' == '__main__':
    def list_concat(l1: list[int],l2: list[int], l3: list[int]) -> list[int]:
        #total_list:list[int]= []
        #total_list.extend(l1 + l2 + l3)
        total_list = l1 + l2 + l3
        return total_list

    res_con = list_concat([1,2], [3,4,5,6], [7,8,9])
    print(res_con, 'long list:', len(res_con))


