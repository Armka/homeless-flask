import requests
import json

url="https://gateway.watsonplatform.net/personality-insights/api/v2/profile"
username="d2941e53-6616-4f35-8ed9-c16475f8a171"
password="OwsBVns1mGJP"
input_data = {
    'body' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc dui ligula, vestibulum ut porta sed, scelerisque ut lectus. Maecenas commodo augue libero, nec efficitur sem pulvinar quis. Nunc congue, nisl non ullamcorper sollicitudin, neque lacus sollicitudin est, at sagittis ligula dolor sed elit. Quisque nunc lacus, volutpat non porttitor quis, convallis ac turpis. Donec non sem eget diam tempor accumsan ac ac elit. Fusce sit amet augue est. Pellentesque eu lacus tortor. Fusce rutrum dui est, rhoncus aliquet libero lacinia a. Praesent a ligula lacus. In accumsan lectus sed ipsum elementum aliquet. Vestibulum vitae congue eros, ac tristique odio. Ut et malesuada neque. Suspendisse at posuere augue. Maecenas fermentum erat et ipsum commodo, quis tempus erat molestie. Integer porttitor consectetur egestas. Nam eu congue ipsum. Donec mauris lorem, iaculis et urna eget, tristique pharetra nibh. Duis varius semper nisl. Integer sit amet mauris ac risus molestie lacinia. Nunc eu ultricies massa. Phasellus rhoncus viverra cursus. Maecenas blandit nisi nec augue ornare ultrices. In mollis ipsum tempus risus iaculis, vestibulum ultrices ante viverra. Maecenas quis nunc in nulla lobortis commodo. Nam tempor erat id aliquet vulputate. Vivamus ac dolor malesuada, suscipit diam eget, pellentesque velit. Proin a dictum nisl. Vestibulum sodales euismod lacus, eu imperdiet felis tincidunt sit amet. Sed id ligula elementum, mollis justo non, sodales urna. Fusce iaculis libero egestas ullamcorper volutpat. Proin dictum scelerisque nulla, quis hendrerit eros porttitor in. Vivamus laoreet malesuada est, et convallis lorem tristique sed. Integer non lectus sed dui sodales iaculis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Quisque bibendum neque eros, ac fermentum erat convallis nec. Quisque efficitur est in leo viverra, ac aliquet nisl iaculis. Nam augue leo, condimentum sit amet vulputate eu, congue sed ex. Pellentesque porttitor quam et rutrum posuere. Proin sit amet viverra lectus. Vivamus ex diam, fermentum vitae turpis eu, pretium suscipit velit. Duis at mi auctor, consequat felis sit amet, mollis leo. Proin mattis egestas odio, ut convallis odio volutpat malesuada. Duis ut dui pulvinar, lobortis purus et, accumsan est. In non erat a massa bibendum condimentum. Nullam auctor dictum dolor, id dignissim mi faucibus at. Donec vel sapien quis mauris pulvinar commodo. Sed sit amet purus velit. Duis id elit mauris. Phasellus tempor orci a malesuada dignissim"
}

response = requests.post(url, auth=(username, password), body=input_data)
try:
    response.raise_for_status()
    print response.text
except requests.exceptions.HTTPError as e:
    print("And you get an HTTPError: %s"% e.message)
