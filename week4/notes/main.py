# week 4 Notes

'''
Notes:

    1. Name mangling -- add two underscores in front of the private val
    2. __iter__ = can turn a class object into a list
        example :

            def __iter__(self):
                return self.__bookmarks.__iter__()

            def print_bookmarks(cls):
                for bookmark in cls.__all_bookmarks:
                    print(bookmarks)


            __bookmarks.__next__() = next in the list
'''