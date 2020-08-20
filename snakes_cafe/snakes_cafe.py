if __name__=='__main__':
    print("This from terminal")

hello="""
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""
print(hello)
content="""
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears


"""
print(content)
inputMessage="""
***********************************
** What would you like to order? **
***********************************

>
"""
my_list=['Wings','Cookies','Spring' 'Rolls','Salmon','Steak','Meat Tornado','A Literal Garden','Ice Cream','Cake','Pie','Coffee','Tea','Unicorn Tears']
a=input(inputMessage).capitalize()
# item={
#     "name":"",
#     "repetition":""
# }

# class item:  
#     name=""
#     rep=1
print(a in my_list)
class Student:  
    def function (self,name, num):  
         self.name   = name  
         self.num    = num  
         return [name,num]
         


# b=item()
# b.name=a
list=[]

print(len(list))
# while not()
if list==[] and a in my_list:
    s=Student().function(a,1)
    list.append(s)
    print("** %d order of %s have been added to your meal **" % (list[0][1],list[0][0]))
 

while a!="quit":
    a=input(inputMessage).capitalize()
    # print(len(list))
    if a in my_list:
        if list==[]:
            s=Student().function(a,0)
            list.append(s)
            # print("** %d order of %s have been added to your meal **" % (list[0][1],list[0][0]))
        if a =="quit":
            exit()
        else:
            for x in list:
                # print(x,list.index(x))
                if x[0]==a:
                    x[1]+=1
                    # print("from home",list)
                    # print(list.index(x))
                    print("** %d order of %s have been added to your meal **" % (x[1],x[0]))
                    break
                elif len(list)==1 :
                    s=Student().function(a,1)
                    list.append(s)
                    print("** %d order of %s have been added to your meal **" % (s[1],s[0]))
                    break
                    # print(len(list))
                    # print("from else",list)
                elif(list.index(x)==len(list)-1):
                    s=Student().function(a,1)
                    list.append(s)
                    print("** %d order of %s have been added to your meal **" % (s[1],s[0]))
                    break
            
    else:
        print("Not Exist in the menu, Please try again")
        continue




