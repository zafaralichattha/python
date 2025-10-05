list=[]
while True:
    work = input("Enter add or show ,edit and 0 to exit:").strip()
    match work:
        case 'add':
            work1=input("please enter a work:")
            final1=work1.title()
            #final=work1.capitalize()

            work.append(final1)

        case 'show'| 'display':
           #for i in range(5):print(i)
            for item in work:
             print(item)
        case 'edit':
            index=int(input("Please enter index to edit: "))
            index=index-1
            new=input("Now enter the word to replace it: ")
            work[index]=new
        case '0':
         break
        case  _: #or we can also use "whatever" insted of _
            print("you have entered wrong key please try again:".capitalize())

# for commenting a line
    """ for commenting more lines """