# Páginas da turma

Cada aluno cria uma página HTML e envia uma Pull Request. Após o merge na `main`, a página aparece na galeria publicada.

## Para os alunos

### 1. Criar seu fork e clonar

No GitHub, abra o repositório indicado pelo instrutor e escolha **Fork > Create fork**. No seu fork, copie a URL em **Code > HTTPS**. No Git Bash:

```bash
git clone URL_DO_SEU_FORK turma-git
cd turma-git
git remote add upstream URL_DO_REPOSITORIO_DA_TURMA
git switch -c pagina/SEU_USUARIO
```

Substitua os marcadores pelas URLs reais e `SEU_USUARIO` pelo seu usuário GitHub em letras minúsculas.

### 2. Criar sua página

Abra a pasta clonada no VS Code. Copie `modelo.html` para `pages/SEU_USUARIO.html`. Altere o texto do `<h1>` e as cores `--fundo` e `--destaque`. Salve e abra seu HTML no navegador.

Altere apenas seu arquivo. O nome deve usar letras minúsculas, números e hífens. A galeria incluirá sua página automaticamente após o merge e a publicação.

### 3. Registrar e enviar

```bash
git status
git add pages/SEU_USUARIO.html
git diff --staged
git commit -m "Adiciona minha página à turma"
git push -u origin pagina/SEU_USUARIO
```

### 4. Abrir e revisar a PR

No GitHub, abra **Compare & pull request**. Confira a base **main do repositório da turma** e a origem **pagina/SEU_USUARIO do seu fork**. Preencha a descrição e confira **Files changed**.

Peça a um colega que comente uma sugestão. Para enviar um ajuste na mesma PR, edite sua página e execute:

```bash
git add pages/SEU_USUARIO.html
git diff --staged
git commit -m "Ajusta página após revisão"
git push
```

O instrutor faz o merge. Depois, acesse o endereço do site fornecido por ele e clique no seu usuário na galeria.
