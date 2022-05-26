import wolframalpha,time
client=wolframalpha.Client('INSERT YOUR WOLFRAM API-KEY HERE')
n = input('How Many Question Do You Want Answer Of: ')
n=int(n)
while(n>0):
    question = str(input('What Is Your Question? ')) 
    res = client.query(question)
    if res['@success']=='false':
        print('No results')
    else:
        result = next(res.results, None)
        print(result.text if result else 'No results')
    n-=1
