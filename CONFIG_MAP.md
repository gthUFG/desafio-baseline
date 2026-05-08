# CONFIG_MAP.md

## Mapa de Configuração do Projeto

Este documento descreve os Itens de Configuração (ICs) do projeto e a política de versionamento adotada.

---

# 1. Política de Versionamento

O projeto utiliza Versionamento Semântico (SemVer):

MAJOR.MINOR.PATCH


## Regras

- MAJOR:
  Alterações incompatíveis com versões anteriores.

- MINOR:
  Novas funcionalidades compatíveis com versões anteriores.

- PATCH:
  Correções de bugs e melhorias pequenas sem quebra de compatibilidade.

---

# 2. Itens de Configuração (ICs)

## IC-001 — Código Fonte

Descrição:
Arquivos principais do sistema escritos em Python.

Local: /desafio-baseline

Principal: codigozinho.py

Versionamento:
SemVer

Responsável:
Equipe de Desenvolvimento

---

## IC-002 — Arquivos de Configuração

Descrição:
Arquivos `.env`, `config.env` e configurações gerais do sistema.

Local: /desafio-baseline

Versionamento:
SemVer

Responsável:
Equipe DevOps

---

## IC-003 — Dependências Python

Descrição:
Bibliotecas utilizadas pelo projeto.

Arquivo:
`requirements.txt`

Versionamento:
Versões fixadas por biblioteca.
