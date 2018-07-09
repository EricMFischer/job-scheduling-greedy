'''
In this programming problem and the next you'll code up the greedy algorithms from lecture for
minimizing the weighted sum of completion times.
This file describes a set of jobs with positive and integral weights and lengths. It has the format

[number_of_jobs]
[job_1_weight] [job_1_length]
[job_2_weight] [job_2_length]
...

For example, the third line of the file is "74 59", indicating that the second job has weight 74
and length 59.

You should NOT assume that edge weights or lengths are distinct.

Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order
of the difference (weight - length). Recall from lecture that this algorithm is not always
optimal. IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the
job with higher weight first. Beware: if you break ties in a different way, you are likely to get
the wrong answer. You should report the sum of weighted completion times of the resulting schedule
--- a positive integer --- in the box below.

ADVICE: If you get the wrong answer, try out some small test cases to debug your algorithm (and
post your test cases to the discussion forum).
'''
import time
import pprint


# input: array of job info [weight, length]
# output: greedy score of job for sorting
def calc_greedy_score(job):
    weight = job[0]
    length = job[1]
    return weight - length
    # return weight / length


# input: sorted jobs e.g. [1, 3, 2], and
# job greedy scores, weights, and lengths e.g. {1: [10,12,2], 2: [4,5,3], 3: [8,10,4]}
# output: weighted sum of completion times
def calc_weighted_sum_completion_times(sorted_jobs, scores):
    time = 0
    weighted_sum = 0
    for job in sorted_jobs:
        job_info = scores[job]
        time += job_info[2]
        # weighted sum = weight * completion time
        weighted_sum += job_info[1] * time
    return weighted_sum


# input: filename with job weights and lengths
# output: weighted sum of completion times
def schedule_jobs(filename):
    scores = {}
    n = 0
    with open(filename) as f_handle:
        f_handle.readline()
        for line in f_handle:
            n += 1
            job = [int(x) for x in line.split()]
            scores[n] = [calc_greedy_score(job), job[0], job[1]]

    # jobs sorted by decreasing order of greedy scores, and if equal by decreasing weights
    sorted_jobs = sorted(scores, key=lambda k: (scores[k][0], scores[k][1]), reverse=True)
    return calc_weighted_sum_completion_times(sorted_jobs, scores)


def main():
    start = time.time()

    result = schedule_jobs('job_scheduling.txt')
    # example:
    # (weight - length) = 68615
    # (weight / length) = 67247

    print('result: ', result)
    print('elapsed time: ', time.time() - start)


main()
