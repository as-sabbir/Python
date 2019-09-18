st = 'Print every word in this sentence that has an even number of letters';
x=st.split();

mylist1=[len(letter)%2==0 for letter in x];
mylist2=[letter[0]=='P' for letter in x];
mylist3=[letter for letter in st.split() if letter[0]=='P']
mylist4=[letter for letter in st.split() if len(letter)%2==0]

print(mylist1);
print(mylist2);
print(mylist3);

for newlist in mylist4:
    print(newlist);
