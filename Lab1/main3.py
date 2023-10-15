KILOBYTES_IN_MEGABYTES = 1024
BYTES_IN_KILOBYTES = 1024
ONE_SYMBOL = 4
disk_capacity = 1.44
pages = 100
lines = 50
characters = 25
one_book = ONE_SYMBOL * characters * lines * pages
books_on_disk = int(disk_capacity * KILOBYTES_IN_MEGABYTES * BYTES_IN_KILOBYTES // one_book)
print("Количество книг, помещающихся на дискету:", books_on_disk)
