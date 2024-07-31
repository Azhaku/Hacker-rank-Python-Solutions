
def acmTeam(topic):
    max_topics = 0
    max_paris = 0
    topic = [int(x,2) for x in topic]
    for attendee in range(len(topic) - 1):
        for attendee2 in range(attendee+1,len(topic)):
            max_subjects = bin(topic[attendee] | topic[attendee2]).count('1')
            if max_topics < max_subjects:
                max_topics = max_subjects
                max_pairs = 1
            elif max_topics == max_subjects:
                max_pairs +=1
    return [max_topics, max_pairs]
            


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

topic = []

for _ in range(n):
    topic_item = input()
    topic.append(topic_item)

max_sub, max_pair = acmTeam(topic)
print(max_sub)
print(max_pair)



# Sample Input

# 4 5
# 10101
# 11100
# 11010
# 00101
# Sample Output

# 5
# 2