import requests
def search_and_save(query):
    websites = ['URL GOEZ HERRRR']
    
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko)'}
    
    with open('output.txt', 'w') as output_file:
        for website in websites:
            response = requests.get(website, headers=headers, params={'q': query})
            output_file.write(f'Website: {website}\n\n')
            output_file.write(f'HTML:\n{response.text}\n\n')
            output_file.write(f'JavaScript:\n{response.text}\n\n')
            output_file.write(f'{response.text}\n\n')
            output_file.write(f'{response.text}\n\n')

def post_and_save(query):
    with open('output2.txt', 'w') as output_file:
        for website in websites:
            response = requests.post(website, headers=headers, params={'*': POST})
            output_file.write(f'Website: {website}\n\n')
            output_file.write(f'HTML:\n{response.text}\n\n')
            output_file.write(f'JavaScript:\n{response.text}\n\n')
            output_file.write(f'{response.text}\n\n')
            output_file.write(f'{response.text}\n\n')

search_and_save('*')
