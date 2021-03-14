import subprocess as sp
import os




def createpv() :

    fdisk = sp.getoutput("fdisk -l")

    print(fdisk)

    disk = input("\nEnter Your Disk Name: ")

    oput = sp.getoutput("pvcreate {}".format(disk))

    print(oput)



def createvg():

    pv1 = input("\nEnter the name of 1st pv : ")

    pv2 = input("Enter the name of 2nd pv : ")

    vgname=input("Enter the name of volume group you want to create : ")

    oput=sp.getoutput("vgcreate {} {} {}".format(pv1,pv2,vgname))

    print(oput)





def lvcreate():

    size=int(input("\nEnter the size of logical volume : "))

    vgname=input("Please enter  the volume group name to create LV : ")

    lv=input("Enter the name to create logical volume : ")

    oput=sp.getoutput("lvcreate --size {}G --name {} {}".format(size,lv,vgname))

    print(oput)



def mpoint():

    dir=input("\nPlease enter the directory name to create  : ")

    lv=input("Please enter the full name of  volume group that is to be mount :  ")

    oput=sp.getoutput("mkdir {}".format(dir))

    oput1=sp.getoutput("mount {} {}".format(lv,dir))


def displaypv():

    disk = input("\nEnter Your Disk Name : ")

    oput = sp.getoutput("pvdisplay {}".format(disk))

    print(oput)



def displayvg():

    vgname=input("\nEnter the name of the volume group : ")

    oput=sp.getoutput("vgdisplay {}".format(vgname))

    print(oput)



def displaylv():

    dir=input("\nEnter full directory of LV ex. [vgname/lvname] : ")

    oput=sp.getoutput("lvdisplay {}".format(dir))

    print(oput)



def resizelv():

    lv = input("\nEnter name of the lv to be resized : ")

    size=int(input("Please enter the size do you want to contribute:"))

    oput=sp.getoutput("lvresize --resizefs --size {}G {}".format(size,lv))



def resizevg():

    fdisk = sp.getoutput("fdisk -l")

    print(fdisk)

    hd=input("\nEnter name of hard disk to add : ")

    vgname=input("Enter the name of volume group : ")

    oput=subprocess.getoutput("vgextend {} {}".format(vgname,hd))






col, lines = os.get_terminal_size()

welcome = "-----Welcome To LVM Automation-----".center(col)



while True :

    os.system('clear')

    print(welcome)



    print("""\n\n   1) Create a New Physical Volume 

   2) Create New Volume Group

   3) Create New Logical Volume

   4) Create A Mount Point

   5) Resize Logical Colume

   6) Resize Volume Group
   
   7) Show Physical Volume

   8) Show Volume Group

   9) Show Logical Volume

   10) Quit\n""")

    try:

        choice = int(input("Please Choose an Option To Continue : "))



    except ValueError:

        print("\n\nwhoops Please Enter the Choice in Number, for eg. 2 for Creating A Volume Group.. ")

        input('\nPress Enter to continue..')

        continue



    if choice == 1:

        createpv()


    elif choice == 2:

        createvg()


    elif choice == 3:

        lvcreate()

    elif choice == 4:

        mpoint()


    elif choice == 5:

        resizelv()


    elif choice == 6:

        resizevg()


    elif choice == 7:

        displaypv()


    elif choice == 8:

        displayvg()


    elif choice == 9:

        displaylv() 


    elif choice == 10:

        print('THANKS FOR USING THIS SERVICE'.center(col))

        input('\n\nPress Enter To Exit..')

        os.system('clear')

        break

    input('\nPress Enter To Continue..') 
