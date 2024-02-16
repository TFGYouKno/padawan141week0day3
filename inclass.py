obj= [1,2,3]

print(obj)

len(obj)

# funtion
#syntax:
# def [NAME}():

def talk():
    print("...")
    print('crazy')
    print('...')
    print('i was crazy once!')


def blender(fruit1, fruit2):
    print('...blending...')
    smoothie = 'you made a ' + fruit1 + ' and' + fruit2 + ' smoothie!'
    return smoothie


si = blender(' kiwi', ' strawberry')
s2 = blender(' strawberry', ' banana')
s3 = blender(' blueberry', ' mango')

print(s3)

print(blender(' passionfruit', ' watermlon'))



def print_up_to(num):
    for num in range(num + 1):
        print(num)
      
print_up_to(15)

print_up_to(8)

def area(length, width):
        return length * width
print(area(10,20))
print(area(11,15))
print(area(36,54))



def get_max(nums):
     current_biggest = None
     for num in nums:
            if current_biggest==None:
                 current_biggest=num
            
            if current_biggest<num:
                 current_biggest=num
            return current_biggest


big = [100,200,111,222,333,9]

print(max(big))
print(get_max(big))