# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def playlist(songs):
    # Write your code here
    pair_number = 0
    for i in range(len(songs)):
        for j in range(i+1,len(songs)):
            print(i,j,songs[i]+songs[j],len(songs))
            if (songs[i] + songs[j])% 60 == 0:
                pair_number += 1
    return pair_number
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    li = [ 10,50,90,30]

    print(playlist(li))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
