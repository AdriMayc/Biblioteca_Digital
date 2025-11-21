### 📂 `readmes/07-helper.md`

Este módulo implementa funções para **executar outras funções de forma segura** e capturar suas saídas impressas no console. Útil para testar funções do sistema ou capturar logs de execução sem interromper o fluxo do aplicativo.

## 🔶 Objetivo

- Executar qualquer função Python de forma segura, sem lançar erros no fluxo principal.
- Capturar todas as saídas de print dentro da função.
- Fornecer uma mensagem amigável caso a função não exista ou falhe.
- Permitir passagem dinâmica de argumentos posicionais, convertendo strings numéricas para inteiros quando necessário.

## 🔶 Estrutura utilizada

- Funções principais:
    - ``call_and_capture(fn, *args, **kwargs)`` → Executa a função fn e retorna uma tupla (resultado, saída impressa)
    - ``safe_invoke(fn, from_fields)`` → Invoca a função de forma segura, analisando assinatura (inspect.signature) e ajustando argumentos automaticamente

- Bibliotecas utilizadas:
    - ``inspect``
    - ``io``
    - ``sys``


## 🔶 Exemplo de uso

```

from components.fn_capture import safe_invoke

def soma(a, b):
    print(f"Soma de {a} + {b}")
    return a + b

resultado, log = safe_invoke(soma, ["5", "7"])
print("Resultado:", resultado)
print("Log capturado:", log)


```

Saída esperada:

```
Resultado: 12
Log capturado: Soma de 5 + 7
```

## 🔶 Benefícios

- Permite testar funções do sistema sem quebrar a aplicação em caso de erro.
- Captura logs impressos para exibição em interface ou relatório.
- Automatiza a conversão de parâmetros simples e protege contra chamadas incorretas.


<hr style="height:2px; background-color:#807f7e; border:none;">