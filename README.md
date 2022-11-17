# API com Django 3: 
### Validações, buscas, filtros e deploy

> Status: Em aprendizagem

## Aula 02: 

#### Aprendemos como validar campo a campo criando uma função, por exemplo:
```
def validate_<nome_do_campo>(self, nome_do_campo):
  if len(nome_do_campo) < 11:
    raise serializers.ValidationError("O campo deve ter 11 dígitos")
  return nome_do_campoCOPIAR CÓDIGO
```
#### Vimos que podemos criar uma função chamada validate para validar todos os campo, validate(self, data) e acessar cada campo com data['<nome_do_campo>'];

#### Melhoramos nosso código removendo a lógica de validação do serializer.

<div align=center>
  <h4>Curso, by #Alura</h4>