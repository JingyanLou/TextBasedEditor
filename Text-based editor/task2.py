class ListADT:

    def __init__(self, size=40):
        """
        @param:               size number of items in containing array, if not given, set it to 100
        @return:              a list data structure
        @pre-condition:       the size has to be an integer.
        @post-condition:      an empty list object is create
        @complexity           best and worst case: the complexity of [None]*size, which it is
                              probably O(size)
        """
        self.length = 0

        if size < 40:
            # if size is smaller than 40
            size = 40
            # then set it default to 40
            self.the_array = [None] * size

        else:
            # if size is correct
            self.the_array = [None] * size

    def __str__(self):
            """
            @param:               none
            @return:              a string that represent the list elements, or empty string if list is empty
            @pre-condition:       none (list can be empty )
            @post-condition:      a string that represent the list is made,
            @complexity           best complexity would be when the list given is empty, which will not get into the for loop,
                                  hence it has O(1) time complexity for returning the empty string
                                  worst complexity would be when the list is full of elements, where the complexity would be O(n)
                                  ,where n represents the number of elements in the list
             """
            temp = str()
            print(temp)

            if self.is_empty():
                return temp

            for i in range(self.length):
                temp = temp + str(self.the_array[i])
                temp = temp + "\n"

            return temp

    def __len__(self):
        """
        @param:               none
        @return:              an integer that represents the length of the list
        @pre-condition:       an object needs to be created before.
        @post-condition:      none
        @complexity           best and worst case: the complexity of get the length will be O(1)
        """
        return self.length

    def __getitem__(self, index):

        """
        @param:               index
        @return:              the elements of the index given
        @pre-condition:       the index has to be within range from -len(self) to len(self)-1
        @post-condition:      none
        @complexity           best and worst case: the complexity of get an elenments would be O(1)
        """

        # check for IndexError
        lower_bound = -self.length
        if index < lower_bound:
            raise IndexError("Index cannon be less than -len(self) !")

        if index > self.length - 1:
            raise IndexError("Index cannon be greater than len(self)-1 !")

        # if index given is positive and 0
        if index >= 0:
            return self.the_array[index]

        # if index given is negative, hence need to convert to normal index
        if index < 0:
            index = index + self.length  # add the length, so negative index become the equal positive index
            return self.the_array[index]

    def __setitem__(self, index, item):
        """
        @param:               index , item
        @return:              none
        @pre-condition:       the index has to be within range from -len(self) to len(self)-1
        @post-condition:      the index position's elements will be set to item
        @complexity           best and worst case: the complexity of set an elenments would be O(1)
        """

        # check for IndexError
        # check if index is range inside -len(self) to len(self)-1
        lower_bound = -self.length
        if index < lower_bound:
            raise IndexError("Index cannon be less than -len(self) !")

        if index > self.length - 1:
            raise IndexError("Index cannon be greater than len(self)-1 !")

        if index >= 0:
            self.the_array[index] = item

        if index < 0:
            index = index + self.length
            self.the_array[index] = item

    def __eq__(self, other):
        """
        @param:               other objects
        @return:              True if they have exact same elements in the same order with the same type, else False
        @pre-condition:       none
        @post-condition:      none
        @complexity           worst case would be comparing each elements of two list one by one, the loop lead to a
                              complexity of O(n), where the n is the numbers of elements within the self.list
                              best  case would be  O(1)
        """

        # boolean to return
        flag = True

        if type(other) != type(self):
            flag = False
            return flag

        for i in range(self.length):
            if self.the_array[i] != other.the_array[i]:
                flag = False

        return flag

    def insert(self, index, item):
        """
        @param:               index , item
        @return:              none
        @pre-condition:       the list cannot be full, the index given should within the range from -len(self)-1 to len(self)
        @post-condition:      the item has been insert to the given positon, the rest of the elements will shuffle towards the end of the list,
                              the length of the list will be increased by one
        @complexity           best and worst case: the complexity of set an elenments would be O(N), where n is the numbers of elements behind
                              that given indexs .
        """

        self.expand_space()   # calling the expand

        if index > self.length:
            raise IndexError("Index should not be greater than len(self)")

        lower_Bound = -self.length - 1  # lower bound = -len(self)-1

        if index < lower_Bound:
            raise IndexError("Index should not be smaller than -len(self)-1")

        if index >= 0:
            # print("index", index)
            # print("length", self.length)

            for i in range(self.length - 1, index - 1, -1):  # ( len-1 , index-1, -1 )

                # print("i : ", i, "th item :", self.the_array[i], "  i+1: ", i + 1, "th item :",self.the_array[i + 1])
                self.the_array[i + 1] = self.the_array[i]

            self.the_array[index] = item
            self.length += 1

        if index < 0:

            # print("index",index)

            diff = len(self.the_array) - self.length  # subtract the none elements
            # print("diff = ",diff)

            real_index = index - diff  # real_index is the index that does not care about none
            # print("real index =",real_index)

            # print("from -1 to",real_index,)

            for i in range(-1, real_index + 1, -1):
                # let list[i] replaced by list[i+1]
                # print("i : ",i,"th item :",self.the_array[i], "       i+1: ",i+1, "th item :",self.the_array[i+1])

                self.the_array[i] = self.the_array[i - 1]

            self.the_array[real_index + 1] = item
            self.length += 1

    def delete(self, index):
        """
        @param:               index
        @return:              none
        @pre-condition:       the index has to be within range from -len(self) to len(self)-1
        @post-condition:      the elements in that given index will be removed from the list,
                              the length of the list will be decreased by one
        @complexity           best and worst case: the complexity of set an elenments would be O(n), where n is the numbers of
                              elements between the given index and the end of the list
        """
        # if index > (self.length - 1):  # raise expection if index is greater than len-1
        # raise Exception("Index cannot be greater than len(self)-1")

        # if index < (-(self.length)):  # raise expection if index is smaller than -(len)
        # raise Exception("Index cannot be smaller than -len(self) ")

        self.shrink_space()     # calling the insert

        # print("for i index",index)
        # print("for range len",self.length)

        if index >= 0:  # if index is positive or zero

            del_item = self.the_array[index]  # del_item = the item that needs to be deleted

            #print(index)
            #print(self.length)

            for i in range(index, self.length-1):
                #print(i)
                #print(i+1)
                self.the_array[i] = self.the_array[i + 1]

            self.the_array[self.length - 1] = None

            self.length = self.length - 1

        if index < 0:  # if index is negative

            diff = len(self.the_array) - self.length  # subtract the none elements

            real_index = index - diff  # real_index is the index that does not care about none

            del_item = self.the_array[real_index]  # del_item is the item that we are deleting

            for i in range(real_index, -1, 1):
                # let list[i] replaced by list[i+1]
                self.the_array[i] = self.the_array[i + 1]

            self.the_array[self.length - 1] = None  # set list[-1] to None

            self.length = self.length - 1  # reduce the length by one (delete one item)

        return del_item

    def is_empty(self):
        """
         @param:               none
         @return:              none
         @pre-condition:       none
         @post-condition:      none
         @complexity           O(1)
         """
        return self.length == 0

    def is_full(self):
        """
         @param:               none
         @return:              True if the list is full, False if the list is not full
         @pre-condition:       none
         @post-condition:      none
         @complexity           O(1)
         """
        return self.length == len(self.the_array)

    def __contains__(self, item):
        """
         @param:               item
         @return:              true if the the array contains the itme, false if not
         @pre-condition:       none
         @post-condition:      noen
         @complexity           O(N) where N is the numbers of items in array
         """
        for i in range(self.length):
            if item == self.the_array[i]:
                return True
        return False

    def append(self, item):
        """
         @param:               item
         @return:              none
         @pre-condition:       none
         @post-condition:      if the list is full, the size of the array will be increased, the length will decreased by one
         @complexity           ?
         """
        if not self.is_full():
            self.the_array[self.length] = item
            self.length += 1
        else:
            self.expand_space()
            #raise Exception('List is full')

    def unsafe_set_array(self, array, length):
        """
        UNSAFE: only to be used during testing to facilitate it!! DO NOT USE FOR ANYTHING ELSE
        """
        try:
            assert self.in_test_mode
        except:
            raise Exception('Cannot run unsafe_set_array outside testing mode')

        self.the_array = array
        self.length = length

    def expand_space(self):
        """
        @param:               none
        @return:              none
        @pre-condition:       1. the array has to be full of elemenets, where is_full == True
        @post-condition:      1. the size of the array will be expaned by 1.9 times then before
                              2. the new expaned array have the exact same elements in the same order
        @complexity           best and worst case: the complexity of set an elenments would be O(n), where n is the numbers of
                              elements between the given index and the end of the list
        """
        if self.is_full():  # if the array is not full, then it is ready to expand

            # print("condition meet")

            og_len = self.length

            og_array = self.the_array  # make a copy

            size = round(og_len * 1.9)  # round the size

            self.__init__(size)  # reset the objects

            for i in range(og_len):  # restore the array from our copy
                self.the_array[i] = og_array[i]

            self.length = og_len  # the length will be 0 after reset, hence restore it from temp

    def shrink_space(self):
        """
        @param:               none
        @return:              none
        @pre-condition:       the numbers of elements take less than 1/4 of the array size
        @post-condition:      1.  the size of the array will be shrinked by half
                              2.  the elements in the shrinked array will be the same
        @complexity           best case and worst case would be O(N), where n is the numbers of elements in the old array
        """

        one_fourth = len(self.the_array) / 4

        # print("one_fourth_limit :",one_fourth)

        # print("current length   :",self.length)

        if self.length <= one_fourth:  # if the current length is less than the 1/4 bound

            og_len = self.length  # make copy in order to restores later

            og_array = self.the_array  # make copy of the list for restore

            size = round(len(self.the_array) / 2)  # shrink the size

            self.__init__(size)  # reset objects's setting

            for i in range(og_len):  # restores the list
                self.the_array[i] = og_array[i]

            self.length = og_len  # after reset, the length will be 0 , hence restore it from our temp value

if __name__ == '__main__':

    y=ListADT()