class Group:
    def __init__ (self, name, females, males):
        self.name = name
        self.females = females
        self.males = males

def getGroupInfo():
    num_groups = input("How many groups there are (i.e. churches): ")
    groups = []

    for i in range(num_groups):
        group_name = raw_input("What is the group name: ")
        num_females = input("How many females in the group: ")
        num_males = input("How many males in the group: ")
        groups.append(Group(group_name, num_females, num_males))

    return groups
