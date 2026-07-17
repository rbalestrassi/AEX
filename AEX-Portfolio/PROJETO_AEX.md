# AEX Air Automotive — Portfólio de Compressores
## Contexto do Projeto

Portfólio online dos compressores da marca **AEX (Air Automotive)**, distribuída exclusivamente pela **Arkalt** no Brasil. Marca com posicionamento premium, identidade visual escura/minimalista/tecnológica.

---

## Arquivo principal
`aex-portfolio.html` — arquivo único HTML/CSS/JS, sem dependências externas além de Google Fonts. Tudo embutido (logo, imagem hero, dados dos produtos).

---

## O que já foi feito

### Layout e identidade
- Header fixo com logo real da AEX embutida em base64 (PNG, fundo escuro, logo branca)
- Hero com título impactante, imagem de compressor técnica (sketch style) com animação de entrada + flutuação contínua, `mix-blend-mode: screen` para remover fundo preto
- Paleta: `#1a1a1a` fundo, `#f5f4f4` branco, `#888` cinza, tipografia Barlow Condensed + Barlow
- Grid de produtos com filtros por linha (Leve, Pesada, Agrícola, Rodoviária) e busca por código/nome/veículo
- Footer com tagline da marca

### Produtos
- **59 compressores reais** cadastrados com código e nome corretos (AEX-6502 a AEX-6598)
- Dados estruturados por produto: código, nome, linha, modelo do compressor, tensão, gás refrigerante, saída, polia, fixação/conexão, tipo de óleo, conectores, código OEM, peso líquido/bruto, dimensões, alinhamento, veículos compatíveis, observações
- Campo `images[]` — array de até 6 fotos por produto
- Campo `image` — primeira foto (compatibilidade e card)

### Modal de detalhe
- Layout duas colunas: galeria (esquerda) + identificação (direita)
- **Galeria com setas ‹ › nas laterais** para navegar entre fotos
- Miniaturas clicáveis embaixo com contador "1 / N"
- Navegação por teclado: ← → para trocar foto, ESC para fechar
- Proporção 1080×692px (`object-fit: contain`)
- Seção "Especificações Técnicas" recolhível
- Seção "Informações e Recomendações de Uso" recolhível — texto padrão AEX para todos os produtos, editável individualmente no admin

### Texto padrão de recomendações (aplicado a todos os produtos)
**Prevenção da Peça:**
- Certifique-se de que o modelo e a voltagem estão corretos antes da instalação.
- Para garantir maior vida útil do compressor, utilize lubrificação e componentes compatíveis.
- Antes da instalação, mantenha o compressor armazenado em local apropriado, longe de influências climáticas extremas.

**Diagnóstico de Falhas:**
- Verifique se há irregularidades ou rupturas na polia e no cubo.
- Verifique a integridade física e elétrica da bobina.
- Verifique se a carcaça apresenta parafusos soltos ou mal fixados.
- Verifique o tipo adequado e a quantidade de óleo para o funcionamento.
- Verifique se há vazamento no sistema.
- Certifique-se de abastecer o compressor com óleo novo a cada troca.

**Observações:**
- Para garantir o bom funcionamento do sistema, após a reposição do compressor providencie também a reposição do Condensador e Filtro Acumulador/Secador.
- Ao substituir qualquer peça do ar-condicionado, é necessária a limpeza completa do sistema e reposição do gás refrigerante e do óleo.

### Painel Admin
- Acesso por senha (padrão: `aex2024`, alterável nas configurações)
- Tabs: Adicionar produto / Gerenciar produtos / Configurações
- Campos completos por produto (todos os dados técnicos + até 6 fotos)
- Preview das fotos antes de salvar
- Remover fotos individualmente
- **Upload em lote** (tab Gerenciar): associação automática por nome de arquivo

### Upload em lote — convenção de nomes de arquivo
```
6502.jpg       → foto 1 do AEX-6502
6502_2.jpg     → foto 2
6502_3.jpg     → foto 3
6502_4.jpg     → foto 4
6502_5.jpg     → foto 5
6502_6.jpg     → foto 6
```
Aceita qualquer separador: `6502-2.jpg`, `AEX-6502_2.jpg`, `6502 2.jpg`

**PENDENTE:** a função `bulkUpload` atual só associa 1 foto por produto. Precisa ser atualizada para agrupar múltiplas fotos do mesmo produto (pelo sufixo _2, _3, etc.) e popular o array `images[]` corretamente.

### Armazenamento
- Dados salvos em `localStorage` do navegador
- Chaves: `aex_products` (array JSON), `aex_pwd` (senha admin)
- Export/import via JSON para backup
- **Importante:** ao abrir o arquivo pela primeira vez num navegador novo, carrega os 59 produtos padrão do `buildDefaults()`. Se o localStorage já tiver dados de uma versão anterior, manter os dados existentes.

---

## Próximos passos pendentes

1. **Corrigir upload em lote** para aceitar múltiplas fotos por produto (sufixo `_2`, `_3`...)
2. **Passo 4 (planejado):** busca por veículo — usuário digita modelo/ano e encontra o compressor correto. Requer tabela de compatibilidade (o cliente tem os dados).
3. **Hospedagem:** publicar em Netlify, Vercel ou GitHub Pages (arquivo único, sem backend necessário)

---

## Lista dos 59 compressores (código → nome → linha)

| Código | Nome | Linha |
|--------|------|-------|
| AEX-6502 | 7H15 Orelha 8PK 12V (S/P/Cima) | Leve |
| AEX-6503 | 7H15 Orelha Polia 8PK 24V (S/P/Cima) | Pesada |
| AEX-6504 | 7H15 Orelha Polia 2A 24V (S/P/Cima) | Pesada |
| AEX-6505 | Chevrolet Prisma 2013> (Onix/Sonic) | Leve |
| AEX-6506 | 7H15 10PK 24V Scania (S/P/Cima) | Pesada |
| AEX-6507 | 10SRE11C Toyota Nova Hilux 2.8 2016> | Leve |
| AEX-6508 | 10SRE18C John Deere 8PK 12V | Agrícola |
| AEX-6509 | CVC GM Corsa Classic/Celta 02>08 | Leve |
| AEX-6510 | Mod Visteon HS15 Ford Fiesta/EcoSport | Leve |
| AEX-6511 | Mod CVC VW Gol G5/G6/Voyage/Fox | Leve |
| AEX-6512 | F250/F350/F4000 Motor Cummins 8PK | Pesada |
| AEX-6513 | Mod Sanden SD7V16 Renault Logan/Sandero | Leve |
| AEX-6514 | 10S15 Toyota Hilux/SW4/SRV 7PK 12V | Leve |
| AEX-6515 | Mod Calsonic S10 2.8 2012> Diesel | Leve |
| AEX-6516 | Calsonic Fiat Palio/Uno/Strada | Leve |
| AEX-6517 | M.B 7SBU16C Axor 9PK 24V | Pesada |
| AEX-6518 | Mitsubishi L200 Triton 2017> | Leve |
| AEX-6519 | Iveco Stralis/Eurostar 4PK 24V | Pesada |
| AEX-6520 | 10S17C MAQ Komatsu D61/D475/PC350 | Agrícola |
| AEX-6521 | Ford FS10/FX15/F-250/F4000/F350 | Leve |
| AEX-6522 | Fiat Mobi 1.0/Palio Way 13> | Leve |
| AEX-6523 | Ford Ranger Diesel 2016>2019 | Leve |
| AEX-6524 | Mod Sanden M.B Sprinter 415/416/515 | Pesada |
| AEX-6525 | VW Gol Mod 10P08 6PK 12V | Leve |
| AEX-6526 | VW Gol Mod 10P08 6PK 12V (var.) | Leve |
| AEX-6527 | 6SES14C Toyota Corolla 13>19 1.8/2.0 | Leve |
| AEX-6528 | Mod CVC VW Gol/Parati/Saveiro 1.8 | Leve |
| AEX-6529 | VW Golf 13>/Polo 18>/Audi A3/Q3 | Leve |
| AEX-6530 | 7H15 Case 821/W20E 8PK 24V F/Case | Agrícola |
| AEX-6531 | Mod Denso Ford Ka/Fiesta 1.0/1.6 | Leve |
| AEX-6532 | Mod Sanden VW Saveiro 2014>/Fox 2.0 | Leve |
| AEX-6533 | Herrison Escavadeira Hyundai/XCMG | Agrícola |
| AEX-6534 | Mod Mahle Fiat Pulse/Fastback 1.0 | Leve |
| AEX-6535 | Nissan Sentra Polia 7PK 12V 2014> | Leve |
| AEX-6536 | Fiat Toro/Renegade/Compass/Rampage | Leve |
| AEX-6537 | Fiat Etorq 1.8 Tritec/Palio/Doblo | Leve |
| AEX-6538 | GM Onix Plus/Tracker 1.0/1.2 3CC | Leve |
| AEX-6539 | Mod Doowon DV14N Hyundai Creta 1.0 | Leve |
| AEX-6540 | Mod Doowon Hyundai DV10 HB20 1.0 21 | Leve |
| AEX-6541 | Mod Doowon Hyundai DV10 HB20 1.0 21 (var.) | Leve |
| AEX-6542 | Mod Doowon DVE16N Hyundai Creta 2.0 | Leve |
| AEX-6543 | Mod CVC GM S10/Blazer/Troller | Leve |
| AEX-6544 | 10P15 Passante (Sem Kit) | Leve |
| AEX-6545 | 10P15 Orelha Universal (S/Kit) | Leve |
| AEX-6546 | 7H15 Case/New Holland (F/Case) | Agrícola |
| AEX-6547 | 7H15 Cater/Case 8PK 24V P/Funda | Agrícola |
| AEX-6548 | 7H15 Cater/Case 8PK 24V P/Funda (var.) | Agrícola |
| AEX-6549 | 6020 Trator Farmall/New Holland/Case | Agrícola |
| AEX-6550 | Caminhão Volvo Polia 180mm 24V | Pesada |
| AEX-6551 | 7H15 Caminhão DAF XF105 410/460 7P | Pesada |
| AEX-6552 | 7H15 4358 DAF XF FTS 480 2021> 8PK | Pesada |
| AEX-6553 | 7H15 4358 DAF XF FTS 480 2021> 8PK (var.) | Pesada |
| AEX-6554 | Máquina Volvo 8 Orelha Polia 2A 24V | Pesada |
| AEX-6555 | 10PA15C M.B Atron/Axor/Actros 15> | Pesada |
| AEX-6556 | 10PA15C 11PK 24V M.B Atego/Atron | Pesada |
| AEX-6557 | Mod Mahle CVC VW Gol G7 2016>/Up | Leve |
| AEX-6558 | Caminhão Novo Volvo Polia 180mm 24V | Pesada |
| AEX-6588 | Orig GM Trailblazer 31UX 2020> | Leve |
| AEX-6598 | Orig Novo Trailblazer 2022> | Leve |

---

## Instrução para continuar

Ao iniciar no Claude Code, diga:

> "Tenho um projeto de portfólio HTML para a marca AEX. Leia o arquivo PROJETO_AEX.md para entender o contexto e o arquivo aex-portfolio.html para ver o código atual. Preciso corrigir a função bulkUpload para aceitar múltiplas fotos por produto usando sufixo _2, _3 no nome do arquivo."

