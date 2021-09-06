def fun1(a,b=0,*args,**kwargs):
    print(a,b,args,kwargs)
    
    
    
fun1(45)
fun1(45,30)
fun1(34,56,67,85,23)
fun1(45,34,25,34,21,23,45,name='varshini',age='10')



# it prints 
#45 0 () {}                                                                        -> for fun1(45)
#45 30 () {}                                                                      -> for fun1(45,30)
#34 56 (67, 85, 23) {}                                                      -> for fun1(34,56,67,85,23)
#45 34 (25, 34, 21, 23, 45) {'name': 'varshini', 'age': '10'} -> for fun1(45,34,25,34,21,23,45,name='varshini',age='10')

