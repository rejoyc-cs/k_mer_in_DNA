import matplotlib.pyplot as plt

def count_imers(seq, i):
    counts = {}
    num_imers = len(seq) - i + 1
    for k in range(num_imers):
        imer = seq[k:k+i]
        if imer not in counts:
            counts[imer] = 0
        counts[imer] += 1
    return counts

def main():
	seq = input("Enter the genome sequence: ")
	i = int(input("Enter the value of i in i-mer: "))
	imers = count_imers(seq,i)
	print("Number of occurences of ",i,"-mers in the genome sequence: \n")
	print(imers)

	names = list(imers.keys())
	values = list(imers.values())

	print("\nThe Plot: ")
	plt.barh(range(len(imers)), values, tick_label=names)
	plt.show()

if __name__ == '__main__':
	main()
