fn = open('Codingal.txt', 'r')

fn1 = open('CodingalUpdated2.txt', 'w')

content = fn.readlines()
for i in range(1, len(content)+1):
    if(1 % 2!= 0):
        fn1.write(content[i-1])
    else:
        pass

fn1.close()

fn1 = open('CodingalUpdated2.txt', 'r')

content1 = fn1.read()
print(content1)

fn.close()
fn1.close()