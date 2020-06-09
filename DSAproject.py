import os,sys
fnew=open("new.txt","w")

class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif self.data < data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def traversal(self):
        fnew=open("new.txt",'a')
        data=self.data+"\n"
        fnew.write(data)
        fnew.close()
        if self.left:
            self.left.traversal()
        if self.right:
            self.right.traversal()


def searc(root,data):

        if root == None:
            valid = False
            return valid
        else:
            if root.data == data:
                valid = True
                return valid
                exit(0)
            if root.data < data:
                return searc(root.right,data)
            elif root.data > data:
                return searc(root.left,data)

        
def search(root,data,num):

        if root == None:
            valid = False
            return valid
        else:
            if(data in root.data):
                valid = True 
                return valid
                exit(0)
            elif root.data < data:
                return search(root.right,data,0)
            elif root.data > data:
                return search(root.left,data,0)

        
def create_file(filename):
    os.chdir(direct)
    f = open(filename,"w")
    content = str(input("Enter the content for the file: "))
    f.write(content)
    f.close()

def keywords(query):
    query = query.lower()
    text = query.split(" ")
    non_key = ["this","the",".",",","?","is","on","be","in","and","what","when","where","what","that","those","how","a","an","if","but","can","my","am","him","her","always","we","to","under","over","she","he"]
    for i in non_key:
        if i in text:
            text.remove(i)

    return text

class searchquery():

    def __init__(self,filename,query):
        self.filename = filename
        self.index_score = 0
        self.query = query

    def find(self,filename):
        os.chdir(direct)
        f = open(filename,'r')
        r = f.read().lower().splitlines()
        t=[]
        for i in r:
            i=i.split(" ")
            t=t+i
        for i in self.query:
            self.index_score+=10*t.count(i)

        f.close()
        return self.index_score



def main_search():


    file_list = os.listdir(direct)
    file_list.remove(file_list[0])
    print("1 to search for a file name and 2 to search a query")
    cho=int(input())
    priority_queue=[[],[]]
    if(cho==1):
        se=input("enter the file you want to search")
        if searc(search_file,se):
            print("file found in", direct)
            print("contents :-")
            os.chdir(direct)
            sev=open(se)
            print(sev.read())
            sev.close()
            r=int(input("Do you want to edit file 1 for yes 2 for no"))
            if(r==1):
                create_file(se)
                
            
        else:
            print("file does not exists")
        
    else:
        user_query = str(input("Enter Your Query: "))
        keyword = keywords(user_query)
        for i in file_list:
            g = searchquery(i,keyword)
            a = g.find(i)
            if(a>0):
                priority_queue[0].append(i)
                priority_queue[1].append(a)
                #insertion sorting
                y=len(priority_queue[1])-2
                while(a>priority_queue[1][y] and y>=0):
                    priority_queue[1][y+1]=priority_queue[1][y]
                    priority_queue[0][y+1]=priority_queue[0][y]
                    y-=1
                priority_queue[0][y+1]=i
                priority_queue[1][y+1]=a
                

        for j in priority_queue[0]:
            print(j,end="\n\n")



def main():
    f=0
    ch=0
    choice=0
    f_reg = open("Reg.txt",'r')
    p=f_reg.read().splitlines()
    if p!=[]:
        root= Node(p[0])
        p.remove(p[0])
        for i in p:
            root.insert(i)
        choice = int(input("Press 1 for login and Press 2 for new user: "))
    else:
        username = input("First registration\nEnter your username: ")
        pwd = str(input("Enter thee password: "))
        credentials=username+","+pwd
        root=Node(credentials)
        root.traversal()
        os.remove("Reg.txt")
        os.rename("new.txt","Reg.txt")
        main()
    f_reg.close()
    if choice == 1:
        username = input("Enter the your username: ")
        pwd = str(input("Enter thee password: "))
        credentials = username+','+pwd
        if searc(root,credentials):
            print("logged in")
            while(ch==0):
                print("press 1 to create a new file \n2 to search \n3 to log out")
                wish=int(input())
                if(wish==1):
                    filename=input("Enter the new file name")
                    create_file(filename)
                    search_file.insert(filename)
                elif(wish==2):
                    main_search()
                elif(wish==3):
                    f_reg.close()
                    print("logout successful")
                    ch=1
                    main()
        else:
            print("wrong username or password")
            main()
    elif(choice==2):
        while(f==0):
            username=input("enter new username")
            username=username+","
            a=search(root,username,0)
            if a:
                print("user already exists")
            else:
                f=1
        pwd=str(input("Enter thee password: ")) 
        credentials = username+pwd
        root.insert(credentials)
        root.traversal()
        os.remove("Reg.txt")
        os.rename("new.txt","Reg.txt")
        main()


fnew.close()
direct=input("enter the location of the folder you want to work with")
file_list = os.listdir(direct)
file_list.remove(file_list[0])
search_file=Node(file_list[0])
for i in file_list:
    search_file.insert(i)
main()

