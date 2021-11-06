# Função de conversão de temperatura: 
def temp_convert(temperatura, de, para):
    try:
        float(temperatura)
        check_num = True
    except ValueError:
        check_num = False

    if ((de =='c') and (para == 'f') and (check_num ==True)):
        temperatura = float(temperatura)
        temp_em_fahrenheit = 1.8 * temperatura + 32
        return temp_em_fahrenheit
    elif ((de =='f') & (para == 'c') and (check_num ==True)):
        temperatura = float(temperatura)
        temp_em_celsius = (temperatura - 32) / 1.8
        return temp_em_celsius
    else: 
        erro = 'Erro! Alguma variavél está incorreta.'
    return erro