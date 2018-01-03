def summary_statistics(args, f):
	return f(args)
def max(nums):
	m = nums[0]
	for i in nums:
		if i > m:
			m = i
	return m
def min(nums):
	m = nums[0]
	for i in nums:
		if i < m:
			m = i
	return m
def median(nums):
	nums.sort()
	if len(nums) % 2 == 1:
		m = nums[len(nums) // 2]
	else:
		m = (nums[len(nums) // 2] + nums[(len(nums)) // 2 - 1] ) / 2
	return m
def mean(nums):
	return sum(nums, 0.0) / len(nums)
def variance(nums):
	m = mean(nums)
	return sum((m - v) ** 2 for v in nums) / len(nums)

