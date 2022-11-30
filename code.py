import pandas
from contextlib import redirect_stdout
terms = []
keys = []
vec_Dic = {}
dicti = {}
dummy_List = []
def filter(documents, rows, cols):
	for i in range(rows):
		for j in range(cols):
			if(j == 0):
				keys.append(documents.loc[i].iat[j])
			else:
				dummy_List.append(documents.loc[i].iat[j])
				if documents.loc[i].iat[j] not in terms:
					terms.append(documents.loc[i].iat[j])
		copy = dummy_List.copy()
		dicti.update({documents.loc[i].iat[0]: copy})
		dummy_List.clear()

def bool_Representation(dicti, rows, cols):
	terms.sort()
	for i in (dicti):
		for j in terms:
			if j in dicti[i]:
				dummy_List.append(1)
			else:
				dummy_List.append(0)
		copy = dummy_List.copy()
		vec_Dic.update({i: copy})
		dummy_List.clear()

def query_Vector(query):
	qvect = []
	for i in terms:
		if i in query:
			qvect.append(1)
		else:
			qvect.append(0)
	return qvect
	
def prediction(q_Vect):
	dictionary = {}
	listi = []
	count = 0
	term_Len = len(terms)
	for i in vec_Dic:
		for t in range(term_Len):
			if(q_Vect[t] == vec_Dic[i][t]):
				count += 1
		dictionary.update({i: count})
		count = 0
	for i in dictionary:
		listi.append(dictionary[i])
	listi = sorted(listi, reverse=True)
	ans = ' '
	with open('output.txt', 'w') as f:
		with redirect_stdout(f):
			print("ranking of the documents")
			for count, i in enumerate(listi):
				key = check(dictionary, i)
				if count == 0:
					ans = key
				print(key, "rank is", count+1)
				dictionary.pop(key)
			print(ans, "is the most relevant document for the given query")

def check(dictionary, val):
	for key, value in dictionary.items():
		if(val == value):
			return key

def main():
	documents = pandas.read_csv(r'documents.csv')
	rows = len(documents)
	cols = len(documents.columns)
	filter(documents, rows, cols)
	bool_Representation(dicti, rows, cols)
	print("Enter query")
	query = input()
	query = query.split(' ')
	q_Vect = query_Vector(query)
	prediction(q_Vect)

main()
