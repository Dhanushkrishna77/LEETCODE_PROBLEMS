from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks, workers, p, strength):
        n = len(tasks)
        m = len(workers)

        # Sorting the tasks and workers in increasing order
        tasks.sort()
        workers.sort()
        lo = 0
        hi = min(m, n)
        ans = None

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            count = 0
            flag = True

            # Inserting all workers in a sorted list
            st = SortedList(workers)

            # Checking if the mid smallest tasks can be assigned
            for i in range(mid - 1, -1, -1):

                # Case 1: Trying to assign to a worker without the pill
                it = st[-1]
                if tasks[i] <= it:

                    # Case 1 satisfied!
                    st.remove(it)
                else:

                    # Case 2: Trying to assign to a worker with the pill
                    it = st.bisect_left(tasks[i] - strength)
                    if it != len(st):

                        # Case 2 satisfied!
                        count += 1
                        st.pop(it)
                    else:

                        # Case 3: Impossible to assign mid tasks
                        flag = False
                        break

                # If at any moment, the number of pills required for mid tasks exceeds
                # the allotted number of pills, we stop the loop
                if count > p:
                    flag = False
                    break

            if flag:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans