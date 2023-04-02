class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        # Binary search for the minimum possible capacity
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) / 2
            # Check if the current capacity is feasible
            if self.isFeasible(weights, days, mid):
                right = mid
            else:
                left = mid + 1
        return left
    
    def isFeasible(self, weights, days, capacity):
        # Initialize the number of days and the current capacity
        num_days = 1
        curr_capacity = 0
        for weight in weights:
            # If the weight exceeds the capacity, it is not feasible
            if weight > capacity:
                return False
            # If the current capacity plus the weight exceeds the capacity,
            # we need to add the current weight to the next day's shipment
            if curr_capacity + weight > capacity:
                num_days += 1
                curr_capacity = weight
            else:
                curr_capacity += weight
        # If the number of days is less than or equal to the given days, it is feasible
        return num_days <= days