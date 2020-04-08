from collections import defaultdict
class Server():
  def __init__(self):
    self.customer = defaultdict(list)
    self.cust_queue = defaultdict(list)
  
  def add_customer(self, queue_no, p_list):
    self.customer[queue_no] = (p_list)

  def add_cust_queue(self, queue_no, p_value):
    self.cust_queue[p_value].append(queue_no)

  def sort_customer(self, cust_list):
    return sorted(cust_list)

  def max_serve(self, cust_list):
    counter = 0
    while cust_list:
      c_next = cust_list[0]
      c_queue_no = self.cust_queue[c_next][0]
      queue_customer = self.customer[c_queue_no].pop(0)
      if c_next == queue_customer:
        self.cust_queue[c_next].pop(0)
        cust_list.pop(0)
      else:
        cust_list.remove(cust_list[cust_list.index(queue_customer)])
      if queue_customer > counter:
        counter = counter+1
      else:
        return counter
    return counter

s = Server()
cust = []
n = int(input()) 
for i in range(0, n):
  ele = input().split(" ")
  el = list(map(int, ele))
  for e in el[1:]:
    s.add_cust_queue(i+1, e)
    cust.append(e)
  s.add_customer(i+1, el[1:])

print(s.max_serve(s.sort_customer(cust)))