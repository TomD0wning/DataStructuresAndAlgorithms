"""
Code file for M269 19J TMA02 Q3
Student version 1: 26/04/19
"""

from TMA02_Q3_graph import Graph

def friends_of_friends(friendships, person):
    """Return the set of friends of the person's friends.
    Don't return people that are already friends of person.
    """
    assert person in friendships.nodes()

    result = set()
    people = friendships.nodes()
    for person1 in people:
        for person2 in people:
            # the () around the whole condition are necessary to
            # break the condition over multiple lines
            if (friendships.has_edge(person1, person2) and
                friendships.has_edge(person2, person) and
                not friendships.has_edge(person1, person) and
                person1 != person):
                result.add(person1)
    return result

def common(friendships, person1, person2):
    """Return the number of common friends of person1 and person2."""
    assert person1 != person2
    assert person1 in friendships.nodes()
    assert person2 in friendships.nodes()
    checkCount =0
    mutual = 0
    for person in friendships.nodes():
        if friendships.has_edge(person, person1):
                if friendships.has_edge(person, person2):
                    mutual = mutual + 1
        else:
            pass
    return mutual

def suggested_friends(friendships, person):
    """Return a list of suggested people for person to befriend.

    Each suggestion is a friend of a friend of person but isn't person's friend.
    The suggestions are ordered from most to fewest mutual friends with person.
    """
    assert person in friendships.nodes()

    scored_suggestions = []
    for friend_of_friend in friends_of_friends(friendships, person):
        score = common(friendships, person, friend_of_friend)
        scored_suggestions.append((score, friend_of_friend))
    scored_suggestions.sort(reverse=True)
    suggestions = []
    for (score, suggestion) in scored_suggestions:
        suggestions.append(suggestion)
    return suggestions
