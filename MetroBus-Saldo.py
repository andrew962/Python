#Simple programa que consume una api para verificar el saldo de las targetas de metrobus
#Api utilizada es del github https://github.com/molekilla/panamenio
#Andres Abadia
#sab/11/2017
import  requests, json

if __name__ == '__main__':

    # payload = {'key1': 'value1', 'key2': 'value2'}
    # url = 'http://panamenio.herokuapp.com/api/com/metrobus/'
    # responde = requests.get(url,params=payload)
    # todo = responde.url
    # print(todo)
    # hola = todo.get('cardId')
    # balanse = todo.get('balance')
    # print(hola, ' ', balanse)
    numero = input('Numero de targeta: ')
    url = 'http://panamenio.herokuapp.com/api/com/metrobus/{}'.format(numero)
    response = requests.get(url)
    print(response.url)
    if response.status_code == 200:
        #todo = response.text
        #print(todo)
        response.text
        todo = json.loads(response.text)
        print(todo)
        try:
            print('Numero de Targeta: ',str(todo['cardId']), '\nSaldo: ', str(todo['balance']),'\nUltimo uso: ', str(todo['lastTransactionAt']))
        except Exception as e:
            print(e)