import os


def search(dirName):
    filenames = os.listdir(dirName)
    listnames = []
    for filename in filenames:
        real_filename = os.path.join(dirName, filename)

        fileext = os.path.splitext(real_filename)[-1]
        if fileext == '.png':
            listnames.append([int(os.path.splitext(filename)[0]), str(dirName)])

    listnames.sort()
    print(listnames)
    # for box in range(0, len(listnames) - 1, 3):
    #
    #     print listnames[box]
    #     print listnames[box+1]
    #     print listnames[box+2]

search('/home/gim/Downloads/PWC-Net/Multi_Frame_Flow/tmp/ex/1')