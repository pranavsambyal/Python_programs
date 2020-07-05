
def strip_punctuation(st):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    new_l=[]
    for x in punctuation_chars:
        print(x)
        st=(st.replace(x,''))
    return st

str1='@FirstFinals'
print(strip_punctuation(str1))



