# 定义一个函数，判断一个数是否为质数
def is_prime(n):
  # 如果n小于等于1，返回False
  if n <= 1:
    return False
  # 如果n等于2，返回True
  if n == 2:
    return True
  # 如果n是偶数，返回False
  if n % 2 == 0:
    return False
  # 从3开始，每次加2，遍历所有可能的因数
  for i in range(3, int(n**0.5) + 1, 2):
    # 如果n能被i整除，返回False
    if n % i == 0:
      return False
  # 如果没有找到因数，返回True
  return True

# 定义一个列表，存储所有的质数
primes = []
# 遍历1到1000之间的所有整数
for i in range(1, 1001):
  # 如果i是质数，将其添加到列表中
  if is_prime(i):
    primes.append(i)
# 打印列表的长度，即质数的个数
print(len(primes))
# 打印列表的内容，即所有的质数
print(primes)
