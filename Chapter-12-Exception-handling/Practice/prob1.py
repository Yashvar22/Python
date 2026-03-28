#Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not

try:
  with open("1.txt",'r') as f:
    print(f.read());
  with open("2.txt",'r') as f:
    print(f.read());
  with open("3.txt",'r') as f:
    print(f.read());

except Exception as e:
    print(e)
#bhai sun hmko yhn har file ko try exception block mai likhn hai

   