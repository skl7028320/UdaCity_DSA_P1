class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

parent_user = "parent_user"
parent.add_user(parent_user)

child_user_1 = "child_user_1"
child_user_2 = "child_user_2"
child.add_user(child_user_1)
child.add_user(child_user_2)

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    :param user: user name/id
    :param group: group to check user membership against
    :return: boolean indicating if user is a member of group
    """
    user_in_group = False

    group_users = group.get_users()
    for group_user in group_users:
        if user == group_user:
            return True

    sub_groups = group.get_groups()
    for sub_group in sub_groups:
        user_in_group = is_user_in_group(user, sub_group)
        if user_in_group is True:
            return user_in_group

    return user_in_group


print("Test user in group")
print("Pass" if is_user_in_group(sub_child_user, parent) is True else "Fail")
print("Pass" if is_user_in_group(child_user_1, parent) is True else "Fail")
print("Pass" if is_user_in_group(child_user_2, parent) is True else "Fail")
print("Pass" if is_user_in_group(parent_user, parent) is True else "Fail")
print("Test user not in group")
print("Pass" if is_user_in_group("user_not_in_group", parent) is False else "Fail")
