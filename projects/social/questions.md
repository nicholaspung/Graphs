To create 100 users with an average of 10 friends each, how many times would you need to call addFriendship()? Why?
    total_friendships = num_users * avg_friendships
    total_friendships = 1000
    addFriendships creates 2 friendships
    1000/2 = 500 times addFriendship() is called.

If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network?
    I modified social.py in order to get a small sample size of each percentages.
    Percent of user's in extended social network: 98%-100%
    Average Degree of Separation: 5-6 users

You might have found the results from question #2 above to be surprising. Would you expect results like this in real life? If not, what are some ways you could improve your friendship distribution model for more realistic results?
    In real life, going day by day, probably not. However, it makes sense, if you have friends with some super connectors. A way to make the friendship distribution model more realistic would be to use a better randomness algorithm, but it's likely you would end up with the same result.

If you followed the hints for part 1, your populateGraph() will run in O(n^2) time. Refactor your code to run in O(n) time. Are there any tradeoffs that come with this implementation?
