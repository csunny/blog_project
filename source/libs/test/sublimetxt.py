import os

def main():
	if not os.path.exists('D:\magic'):
		os.makedirs('D:\magic')
	with open('D:\magic\magic.txt', 'w+') as fp:
		fp.write("hello magic!")
		print "Write succssfully!"

if __name__ == '__main__':
	print("ok")
	main()