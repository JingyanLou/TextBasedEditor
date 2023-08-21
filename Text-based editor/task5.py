
from task2 import ListADT

class Editor:

    def __init__(self):

        self.text_lines = ListADT()

        self.search=ListADT() # for search function's return

        #self.insert=ListADT() # for insert

    def read_filename(self, file_name):
        """
        @param:               file name
        @return:              a list of strings contains each line of the text
        @pre-condition:       the file within the same folder
        @post-condition:      none
        @complexity           best and worst are all O(N), where N is the numbers of lines in the file
        """

        f = open(file_name)  # open the file

        self.text_lines=ListADT()   # initialize the_array

        for line in f:

            line = line.strip()

            self.text_lines.append(str(line))

        f.close()  # close the file

        return self.text_lines

    def print_num(self, line_num=""):
        """
        @param:               line_num   (actual_index = line_numeber -1 ) eg. line_num=1 , line 1 , index 0 of list
        @return:              none
        @pre-condition:       line_num has to be >= 1 and <= self.length
        @post-condition:      prints the line at that given line number if line_num is given
                              prints all lines if line_num is None
        @complexity           best case: the number is given, hence only one line will be print, where it has a O(1).
                              worst case: no number is given, hence it will prints out all the lines in the file, hence
                              it will have time complexity of O(N), where N is the numbers of lines in the file
        """

        # prints all lines

        if self.text_lines.is_empty():
            raise Exception("TextLine Empty Error")

        if line_num == "":
            for i in range(len(self.text_lines)):
                print(self.text_lines[i])

        # prints the line of the given line number
        else:
            lower_bound=1
            upper_bound=self.text_lines.length

            if int(line_num)>upper_bound:
                raise IndexError("Line number out of range ")

            if int(line_num)<lower_bound:
                raise IndexError("Line number out of range ")

            actual_index = int(line_num) - 1   # if line_num=1, the list index would be 0, hence need to -1
            print(self.text_lines[actual_index])

    def delete_num(self, line_num=""):
        """
        @param:               line_num(string) or None
        @return:              none
        @pre-condition:       1.line_num can be transferred to integer
                              2.int(line_num) has to be within the range
        @post-condition:      the given index line is removed if line_num is given
                              the whole lines is removed if line_num is not given
        @complexity           none

        """
        lower_bound=-(self.text_lines.length)

        upper_bound=self.text_lines.length+1

        if line_num != "":
            # delete the given index's line

            # positive index

            if int(line_num) < lower_bound:
                raise IndexError("Index can not be less than lower bound ")

            if int(line_num) > upper_bound:
                raise IndexError("Index can not be greater than upper bound")

            if int(line_num)>0:

                actual_index = int(line_num) - 1

                self.text_lines.delete(actual_index)


            if int(line_num)<0: # line is negative

                actual_index=int(line_num)+self.text_lines.length

                self.text_lines.delete(actual_index)


            if int(line_num)==0: # if line = 0 , treat it as line 1

                raise IndexError("Index can not be zero ")

        else: # if input = ""

            self.text_lines=ListADT()

    def insert_num_strings(self, line_num, list_of_strings):
        """
        @param:               line_num(string), list_of_strings
        @return:              none
        @pre-condition:       the line_num has to be >= -(self.res.length)-1, <= self.res.length+1
        @post-condition:      for each lines in the list_of_strings, it will be inserted to the given index
        @complexity           best and worst would be O(n) where n is the number of line in the list of strings

         """
        upper_bound=self.text_lines.length+1
        lower_bound=-(self.text_lines.length)-1

        if int(line_num)>upper_bound:
            raise IndexError("line number is out of upper bound")

        if int(line_num)<lower_bound:
            raise IndexError("line number is out of lower bound")


        # positive line num from 0 to ....
        if int(line_num)>0:

            actual_index=int(line_num)-1

            for line in list_of_strings:
                self.text_lines.insert(actual_index,line)
                actual_index+=1 # add one to make the list element inserted in order

        # line_num=0, works as line 1
        if int(line_num)==0:

            actual_index=int(line_num)

            for line in list_of_strings:
                self.text_lines.insert(actual_index,line)
                actual_index+=1


        # line_num is negative
        if int(line_num)<0:

            actual_index=int(line_num)+self.text_lines.length+1 # actual index

            for line in list_of_strings:

                self.text_lines.insert(actual_index,line) #insert to actual index

                actual_index+=1 # increase 1 in order to get the right index for next elements in the list

    def search_string(self,string):
        """
        @param:               string
        @return:              a list contains the line number where the strings appears
        @pre-condition:       the file to be searched  cannot be empty
        @post-condition:      none
        @complexity           it will have a time complexity of O(n) where n is the numbers of line within the file

        """
        # local functions

        def char(str):
            """
            @param:               string
            @return:              a list contains all the char in that string
            @pre-condition:       none
            @post-condition:      none
            @complexity           best case and worst case would be O(n), where n is the number of char contained in that string

            """
            return [char for char in str]

        def contain(str, line):
            """
            @param:               str, line
            @return:              True, if str is in given line, False if str is not in the given line (is a substring or not)
            @pre-condition:       none
            @post-condition:      none
            @complexity           two for loop is used, the inner loop is depended on the first loop, hence it would have a time complexity
                                  of O(n^2) where n is the numbers of lines
            """

            lis = char(line)   # lis contains single chars eg. lis=['h','e','l','l','o']
            n_str = len(str)   # n_str is the lenght of a single stirng, string "apple" has a length of 5
            n_lis = len(lis)   # n_lis is the length of the lis

            for i in range(n_lis - n_str):
                char_first = lis[i] # starting char

                for j in range(i + 1, i + n_str):  # make combination of n_str length string
                    char_first += lis[j]

                #print(str_random)

                if char_first == str:  # in this stage, len(char_first) will be equal to len(str)
                    return True # found

            return False # not found

        self.search=ListADT() # make the search empty, so it dont get messed up by last call

        if self.text_lines.is_empty(): # if nothing can be read
            raise Exception("File Empty Error ")


        # Main :

        for i in range(len(self.text_lines)): # i+1 is the line number

            each_line=self.text_lines[i] # each line = "this is a test file"

            if contain(string,each_line):  # if contains is True

                self.search.append(i+1)   # append that to the final list

        return self.search

    def undo(self):
        """
        @param:               none
        @return:              none
        @pre-condition:       none
        @post-condition:      none
        @complexity           none

         """

        # :)
        pass

        raise NotImplementedError

    def interface(self):
        """
        @param:               none
        @return:              none
        @pre-condition:       none
        @post-condition:      editor started to work  after calling it
        @complexity           none
        """

        valid_option=["insert","delete","print","read","quit","search","restart"]

        print("")
        print("                          command options are :                               ")
        print("______________________________________________________________________________")
        print("|                                                                            |")
        print("|                             insert num                                     |")
        print("|                             delete num                                     |")
        print("|                             print  num                                     |")
        print("|                             read   filename                                |")
        print("|                             search                                         |")
        print("|                             quit                                           |")
        print("|                             restart                                        |")
        print("|                                                                            |")
        print("______________________________________________________________________________")

        print("______________________________________________________________________________")
        print("|                                Examples                                    |")
        print("|                                                                            |")
        print("|    1.        insert 1               #insert the lines into first line      |")
        print("|              Insert the line :  This is line 1                             |")
        print("|              Insert the line :  This is line 2                             |")
        print("|              Insert the line :  .                                          |")
        print("|                                                                            |")
        print("|    2.        read small.txt         #read   the file named small.txt       |")
        print("|                                                                            |")
        print("|    3.        print  1               #print  the first line of the text     |")
        print("|                                                                            |")
        print("|    4.        delete 1               #delete the first line of the text     |")
        print("|                                                                            |")
        print("|    5.        search                 #search                                |")
        print("|              search for : this is                                          |")
        print("|                                                                            |")
        print("|    6.        quit                   # quit the program                     |")
        print("|                                                                            |")
        print("|                                                                            |")
        print("|    Student ID : 30510996                                                   |")
        print("|    Student Name : Jingyan Lou                                              |")
        print("|                                                                            |")
        print("______________________________________________________________________________")


        while True:

            command = input(":")

            print("")

            capture=command.split()  # eg. ['read', 'small.txt']

            #print("Capture = ", capture)

            if capture[0] not in valid_option:
                print("?")
                continue


            if capture[0]=="read":

                if len(capture)==2:  # len(capture)==2, when capture=[read,filename]

                    try:
                        self.read_filename(capture[1])

                    except FileNotFoundError:
                        print("?")

                else:
                    print("?")
                    continue

            elif capture[0]=="print":

                if len(capture)==2:  # len(capture)==2, when capture=[print,line_number]

                    try:
                        self.print_num(capture[1])
                        print("")

                    except Exception: # has nothing to print
                        print("?")

                elif len(capture)==1: # len(capture)==1 , when capture=[print]

                    try:
                        self.print_num()
                        print("")

                    except Exception: # has nothing to print
                        print("?")

                else:# not in correct format
                    print("?")
                    continue


            elif capture[0]=="delete":
                if len(capture)==1:
                    # len(capture)==1 , when capture=[delete]
                    self.delete_num()

                elif len(capture)==2:
                    # len(capture)==2 , when capture=[delete,line_num]

                    try:
                        self.delete_num(capture[1])

                    except IndexError: # check if index is ok

                        print("?")

                else:
                    print("?")


            elif capture[0]=="insert":

                if len(capture)==2:
                    # len(capture)==2 , when capture=[insert,line_num]

                    self.insert=ListADT() # initialize

                    print("Note: Enter . to stop ")

                    print("")

                    while True:

                        data=input("Insert the  line :  ")

                        if data==".": # stop command received
                            break

                        self.insert.append(data)

                    try:

                        self.insert_num_strings(capture[1],self.insert) # check if index is ok

                    except IndexError:

                        print("?")


                else:
                    print("?")


            elif capture[0] =="search":

                if len(capture)==1:

                    # len(capture)==1 , when capture=[search]

                    if self.text_lines.is_empty():# cannot search empty file
                        print("?")

                    else:

                        str=input("search for : ")

                        for lines in self.search_string(str):
                            print("")
                            print("The string （",str,"）  appeared in line ", lines)


                else:
                    print("?")


            elif capture[0]=="quit":
                if len(capture)==1:
                    print("see you next time  ")
                    break
                else:
                    print("?")


            elif capture[0]=="restart":
                if len(capture)==1:
                    self.restart()

                else:
                    print("?")

    def restart(self):
        # initalize the text_lines
        self.text_lines=ListADT()

# test for insert and delete
def test_insert():
    t=Editor()
    t.read_filename("TestFile.txt")
    test_contents_01=["This is line 1","This is line 2",'This is a test file', 'It is a file that is used for testing.', 'It has several lines.', 'Those lines contain words.']
    t.insert_num_strings("1",["This is line 1","This is line 2"]) # insert the list into 1 line
    assert if_excat_same_elements(t,test_contents_01)==True,"Test 01 Failed, they dont have the excat same elements"
    print("Inserting to the first line test passed !")

    t = Editor()
    t.read_filename("small.txt")
    test_contents_02=["Yossarian decided","not to utter","another word.","This is the first line","This is the second line"]
    t.insert_num_strings("-1",["This is the first line","This is the second line"]) # insert the list into -1 line
    assert if_excat_same_elements(t, test_contents_02) == True, "Test 02 Failed, they dont have the excat same elements"
    print("Inserting to the -1 line test passed !")

    t = Editor()
    t.read_filename("TrailFile.txt")
    test_contents_03 =['This is a test file',"This is the first line","This is the second line", 'It is a file that is used for testing.', 'It has several lines. And some trailing space ->', 'Those lines contain words.']
    t.insert_num_strings("2",["This is the first line","This is the second line"]) # insert the list into 2 line
    assert if_excat_same_elements(t, test_contents_03) == True, "Test 02 Failed, they dont have the excat same elements"
    print("Inserting to the 2 line test passed !")

    print("Run 3 out of 3 tests ")
    print("all tests passed for inserting  ")

def test_delete():
    t=Editor()
    t.read_filename("small.txt")
    t.delete_num("1") # delete the first line
    test_conten01=['not to utter', 'another word.']
    assert if_excat_same_elements(t,test_conten01),"delete first line failed " # check if they are equal
    print("deleting the first line passed ")

    t.delete_num("2") # delete the second line
    test_conten02=['not to utter']
    assert if_excat_same_elements(t, test_conten02), "delete second line failed "
    print("deleting the second line passed ")

    t = Editor()
    t.read_filename("small.txt")
    t.delete_num("-1") # delete the -1 line
    test_conten03=['Yossarian decided', 'not to utter']
    assert if_excat_same_elements(t, test_conten03), "delete -1 line failed "
    print("deleting the -1 line passed ")

def if_excat_same_elements(object,test_content):
    # this function is used in test case for comparing if two array is equal.
    for i in range(object.text_lines.length):
        if object.text_lines.the_array[i]!=test_content[i]:
            return False

    return True

if __name__ == '__main__':
    x=Editor()
    #print(x.search_string("is a"))
    x.interface()
    #test_insert()
    #test_delete()





