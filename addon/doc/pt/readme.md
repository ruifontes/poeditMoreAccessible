# poedit Mais Acessível

## Informações
* Autores: Abel Passos Júnior, Ângelo Abrantes e Rui Fontes, com base no trabalho de Prasad Gautam
* Actualizado: 26 de Abril  de 2022
* Descarregar [versão estável][1]
* Compatibilidade: NVDA versão 2019.3 e posterior


## Apresentação
Este extra torna o Poedit mais acessível e informativo em muitos aspectos dos comandos do Poedit.
Também indica as diferentes categorias de mensagens através de um sinal sonoro ou de um anúncio prévio com asterisco. O som indicativo ajudará a identificar os tipos de possíveis erros e ajudará na correcção. É também possível dar um comando para anunciar o erro.
Agora, pode conhecer o texto original e da tradução separadamente. Além disso, as mensagens formadas no plural (se existirem) podem agora ser reconhecidas distintamente. Isto irá ajudá-lo a julgar mais facilmente a exactidão da tradução. Evita a ida e volta de TAB e shift+TAB se desejar conhecer estas mensagens individualmente.


## Características
- Anúncio da acção feita ao premir comandos de atalho do Poedit;
- Indicação da categoria específica da mensagem através de um bip distinto e/ou asteriscos;
- Dentro da actual sessão do NVDA, o modo de Bip pode ser alternado entre 'ligado' ou 'desligado';
- No modo "bip desligado", forma alternativa de indicação da categoria da mensagem;
- Anúncio de forma plural;
- Comandos para o anúncio de:
	- Texto da tradução;
	- Texto fonte;
	- Erro de sintaxe da tradução Poedit;
	- Diferente número de parâmetros ou símbolos '&';
	- Texto da janela de comentários;
	- Texto da janela de 'Nota para tradutores';
	- Primeiras sugestões, até ao máximo de 5.


## Indicação do tipo de mensagem
### No modo "bip ligado":
- Tom alto: Sem tradução;
- Tom médio: Tradução imprecisa;
- Tom baixo:
	- a fonte e a tradução é a mesma;
	- O número de parâmetros ou símbolo "&" na fonte e na tradução difere;
- Sem bip: A tradução é normal.


### No modo "bip desligado":
- Mensagem seguida de "Sem texto na tradução.": Sem tradução;
- Mensagem precedida por um asterisco e Fuzzy (* Fuzzy): Tradução imprecisa;
- Mensagem precedida por duplo asterisco (**):
	- a fonte e o texto de tradução são os mesmos;
	- O número de parâmetros e símbolo "&" na fonte e tradução não é igual;
- Mensagem precedida por um asterisco triplo (***): Erro devido a violação das regras de tradução;
- Mensagem sem asterisco: Tradução normal.


### Em ambos os modos beep
- sinal sonoro extra agudo: Erro devido à violação das regras de tradução.


## Comandos do teclado
- controlo+b: Copia o texto original para a caixa de tradução e anuncia;
- control+k: Elimina a tradução e anuncia. Informa se não houver texto disponível;
- control+s: guarda o ficheiro notificando a acção que está a ser executada;
- controlo+u: A alternar o tipo de mensagem entre fuzzy ou normal e anuncia. Informa se não houver texto disponível;
- control+shift+r:
	- Anuncia o texto da mensagem de origem.
	- Em caso de forma plural, pressionando duas vezes anuncia o texto fonte no plural;
- control+shift+t:
	- Anuncia o texto da mensagem de tradução.
	- Em caso de forma plural, ao pressionar duas vezes, é apresentada a próxima forma de tradução;
- controlo+shift+a: Anuncia o texto da janela 'Nota para tradutores';
- controlo+shift+c: Anuncia o texto da janela de comentários;
- control+shift+e: Descreve a causa do erro;
- controlo+shift+s: Anunciar as primeiras sugestões até um máximo de 5;
- controlo+shift+b: Alterna temporariamente o modo bip para o modo ON ou OFF e anuncia;
- control+shift+v: Alterna o nível do sinal sonoro para agudo ou suave.


[1]: https://github.com/ruifontes/poeditMoreAccessible/releases/download/2022.04/poeditMoreAccessible-2022.04.nvda-addon
