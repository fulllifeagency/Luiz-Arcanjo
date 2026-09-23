# Luiz Arcanjo

Site oficial de Luiz Arcanjo, com biografia, discografia, Academy, loja, devocionais, igreja, agenda e contato.

## Estrutura

- Site estático em HTML, CSS e JavaScript.
- Páginas internas geradas por `generate_pages.py`.
- Formulário processado por uma Cloudflare Pages Function em `functions/api/contact.js`.
- Envio de mensagens por Resend.

## Desenvolvimento local

Execute um servidor estático na raiz do projeto. Para atualizar as páginas geradas:

```bash
python3 generate_pages.py
```

## Variáveis de ambiente

Use `.dev.vars.example` como referência. Em produção, configure no Cloudflare Pages:

- `RESEND_API_KEY`
- `RESEND_FROM`
- `CONTACT_TO`

