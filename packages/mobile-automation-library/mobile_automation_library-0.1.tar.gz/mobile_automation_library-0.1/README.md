# Mobile Automation Library

Esta é uma biblioteca para automação de testes mobile utilizando Robot Framework e Appium.

## Instalação

Você pode instalar a biblioteca utilizando o pip:

```bash
pip install mobile-automation-library
```

## Uso

Aqui está um exemplo de como usar a biblioteca no Robot Framework:

```robot
*** Settings ***
Library    MobileAutomationLibrary

*** Test Cases ***
Teste Verificação de Elemento
    FW Verificar Localizador Visível e Habilitado    xpath=//button[@id='submit']
```

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Basta fazer um fork e enviar um pull request.
