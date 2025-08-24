#!/usr/bin/env python3
"""
Gerador de senhas com:
- comprimento configurável
- inclusão de: minúsculas, maiúsculas, dígitos, símbolos
- garantia de unicidade (nunca repete uma senha já gerada)

A unicidade é verificada contra um banco local (arquivo JSON) de hashes SHA-256
das senhas já emitidas. Se você apagar o arquivo, perde o histórico.
"""

from dataclasses import dataclass
from typing import Set
import secrets
import string
import json
import hashlib
from pathlib import Path

HIST_PATH = Path("password_history.json")  # onde persistimos os hashes

@dataclass
class PasswordConfig:
    length: int = 16
    use_lower: bool = True
    use_upper: bool = True
    use_digits: bool = True
    use_symbols: bool = True
    # símbolos “seguros” para muitas aplicações (evita espaços e aspas)
    symbols: str = "!@#$%^&*()-_=+[]{};:,.?/"

def load_history() -> Set[str]:
    if HIST_PATH.exists():
        try:
            data = json.loads(HIST_PATH.read_text(encoding="utf-8"))
            if isinstance(data, list):
                return set(data)
        except Exception:
            pass
    return set()

def save_history(history: Set[str]) -> None:
    HIST_PATH.write_text(json.dumps(sorted(history)), encoding="utf-8")

def build_pool(cfg: PasswordConfig) -> str:
    pool = ""
    if cfg.use_lower:   pool += string.ascii_lowercase
    if cfg.use_upper:   pool += string.ascii_uppercase
    if cfg.use_digits:  pool += string.digits
    if cfg.use_symbols: pool += cfg.symbols
    if not pool:
        raise ValueError("Selecione ao menos um conjunto de caracteres.")
    return pool

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def max_unique(length: int, pool_size: int) -> int:
    # número máximo teórico de senhas distintas = pool_size ** length
    # (cuidado: pode ficar enorme; aqui só usamos para checagem/erro)
    return pool_size ** length

def generate_unique_password(cfg: PasswordConfig, history: Set[str]) -> str:
    pool = build_pool(cfg)

    # Checagem: se já usamos todo o espaço possível, não há como manter unicidade
    # (evita loop infinito).
    if len(history) >= max_unique(cfg.length, len(pool)):
        raise RuntimeError(
            "Impossível gerar senha única: espaço de busca esgotado "
            f"(pool={len(pool)} chars, comprimento={cfg.length})."
        )

    # Para garantir que cada senha contenha ao menos um char de cada classe ativada,
    # construímos um esqueleto com um char de cada classe selecionada e completamos
    # aleatoriamente com o pool completo; depois embaralhamos.
    parts = []
    if cfg.use_lower:   parts.append(secrets.choice(string.ascii_lowercase))
    if cfg.use_upper:   parts.append(secrets.choice(string.ascii_uppercase))
    if cfg.use_digits:  parts.append(secrets.choice(string.digits))
    if cfg.use_symbols: parts.append(secrets.choice(cfg.symbols))

    if len(parts) > cfg.length:
        raise ValueError(
            f"Comprimento mínimo para as categorias escolhidas é {len(parts)}."
        )
