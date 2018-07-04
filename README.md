## Synopsis
This solution uses a greedy algorithm to minimize the weighted sum of job completion times.
An accompanying text file describes a set of jobs with positive and integral weights and lengths. It has the format

[number_of_jobs]
[job_1_weight] [job_1_length]
[job_2_weight] [job_2_length]
...

For example, the third line of the file is "74 59", indicating that the second job has weight 74
and length 59.

Do NOT assume that edge weights or lengths are distinct.

The task here is to run the greedy algorithm that schedules jobs in decreasing order
of the difference (weight - length). Recall that this algorithm is not always
optimal. IMPORTANT: if two jobs have equal difference (weight - length), schedule the
job with higher weight first. Beware: if one breaks ties in a different way, one is likely to get
the wrong answer. Report the sum of weighted completion times of the resulting schedule--a positive integer.

## Motivation

This job scheduling algorithm, which minimizes the weight sum of job completion times, demonstrates how the greedy algorithm design paradigm is applicable when we make iterative myopic decisions.

## Acknowledgements

This algorithm is part of the Stanford University Algorithms 4-Course Specialization on Coursera, instructed by Tim Roughgarden.
