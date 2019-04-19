from Location import getLocations
from Group import getGroupInfo
def main():
    locations = []
    locations = getLocations()
    print(locations[0].name)

    groups = []
    groups = getGroupInfo()
    for i in range(len(groups)):
        print(groups[i].name)
main()
