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
a=input(inputMessage).capitalize()
# item={
#     "name":"",
#     "repetition":""
# }

# class item:  
#     name=""
#     rep=1

class Student:  
    def function (self,name, num):  
         self.name   = name  
         self.num    = num  
         return [name,num]
         


# b=item()
# b.name=a
list=[]

print(len(list))
if list==[]:
    s=Student().function(a,1)
    list.append(s)
    print("** %d order of %s have been added to your meal **" % (list[0][1],list[0][0]))
    # print(len(list))


# a=input(inputMessage).capitalize()
# s=Student().function(a,1)
# list.append(s)
# print(len(list))
# print(list)

while a!="quit":
    a=input(inputMessage).capitalize()
    # print(len(list))
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
        




    
    # else:
    #     for x in list:
    #         # a=input(inputMessage).capitalize()
            
    #         # print("nbnn")
    #         # print(x.name,x.rep)
    #         if x[0]==a:
    #             print("this from xxxxxxxxxxxxxb",x)
    #             x[1]+=1
    #             print(list)
    #             # b.name=a
    #             # list.append(b)
                
    #             print("** %d order of %s have been added to your meal **" % (x[1],x[0]))
    #             # break
    #         # else:
    #         #     s=Student().function(a,1)
    #         #     list.append(s)
    #         #     print("this from else :   ",list)
    #         #     print("** %d order of %s have been added to your meal **" % (s[1],s[0]))
    #         #     # print("els",x.rep)
    #         #     break
            
                

