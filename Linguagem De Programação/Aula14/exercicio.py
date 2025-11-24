import pyautogui
import time



pyautogui.alert(text='Bem vindos ao sistema automatizado',
                title='Inicioda automação...',
                button='ok')




nome=pyautogui.prompt(text='Digite seu nome:',title='informação obrigatoria')
email=pyautogui.prompt(text='Digite seu  email:',title='informação obrigatoria')



resposta = pyautogui.confirm(
    text=f'confirme seus dados', 
    buttons=['sim', 'nao', 'cancelar']

)


if resposta== 'sim':
    pyautogui.alert('prepare-se! A captura de tela sera feita em 3 seg....', title='captura de tela')
    time.sleep(3)
    pyautogui.screenshot('captura_usuario.png')
    pyautogui.alert('captura realizada com sucesso! Arquivo salvo como "captura_usuario.png".', title='Sucesso')
elif resposta == 'nao':
    pyautogui.alert('processo cancelado pelo usuário.', title='cancelado')
else:
    pyautogui.alert('A automação foi interrompida.', tittle='Encerrado')


print(f'Nome:  {nome}')
print(f'E-mail:  {email}')
print(f'Resposta do usuário:  {resposta}')




                