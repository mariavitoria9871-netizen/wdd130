# Direitos Autorais 2020, Brigham Young University-Idaho. Todos os direitos reservados.

"""Implementação de interpretação de fórmulas químicas.

Os testes esperam:
- exportar `interpretar_formula(formula, dic_tabela_periodica)`
- exportar `FormulaError`
- suportar parênteses e multiplicadores após parênteses (ex.: (C2(NaCl)4H2)2C4Na)
- lançar FormulaError para fórmulas inválidas.
"""

from __future__ import annotations

from dataclasses import dataclass


class FormulaError(Exception):
    """Erro de parse/validação de fórmula química."""


@dataclass
class _Token:
    type: str
    value: str | None = None


def _tokenize(formula: str) -> list[_Token]:
    if formula is None:
        raise FormulaError("Fórmula inválida")
    if len(formula) == 0:
        raise FormulaError("Fórmula inválida")

    tokens: list[_Token] = []
    i = 0
    while i < len(formula):
        ch = formula[i]

        if ch == "(":
            tokens.append(_Token("LPAREN", ch))
            i += 1
            continue
        if ch == ")":
            tokens.append(_Token("RPAREN", ch))
            i += 1
            continue

        # Element symbol: Uppercase + optional lowercase
        if "A" <= ch <= "Z":
            sym = ch
            i += 1
            if i < len(formula) and "a" <= formula[i] <= "z":
                sym += formula[i]
                i += 1
            tokens.append(_Token("SYMBOL", sym))
            continue

        # Quantity must follow a SYMBOL or a ')'
        if "0" <= ch <= "9":
            j = i
            while j < len(formula) and "0" <= formula[j] <= "9":
                j += 1
            tokens.append(_Token("NUMBER", formula[i:j]))
            i = j
            continue

        # Any other char is invalid (inclui '-' e etc.)
        raise FormulaError("Fórmula inválida")

    return tokens


def _parse_int(token: _Token) -> int:
    try:
        n = int(token.value)  # type: ignore[arg-type]
    except Exception:
        raise FormulaError("Fórmula inválida")
    if n <= 0:
        raise FormulaError("Fórmula inválida")
    return n


def _merge_counts(target: dict[str, int], source: dict[str, int], factor: int = 1) -> None:
    for sym, cnt in source.items():
        target[sym] = target.get(sym, 0) + cnt * factor


def _parse_group(tokens: list[_Token], dic_tabela_periodica: dict[str, list], idx: int) -> tuple[dict[str, int], int]:
    counts: dict[str, int] = {}

    while idx < len(tokens):
        tok = tokens[idx]

        if tok.type == "RPAREN":
            # end of this group
            return counts, idx

        if tok.type == "LPAREN":
            # group
            subcounts, new_idx = _parse_group(tokens, dic_tabela_periodica, idx + 1)
            if new_idx >= len(tokens) or tokens[new_idx].type != "RPAREN":
                raise FormulaError("Fórmula inválida")
            idx = new_idx + 1  # consume ')'

            # optional quantity
            factor = 1
            if idx < len(tokens) and tokens[idx].type == "NUMBER":
                factor = _parse_int(tokens[idx])
                idx += 1

            _merge_counts(counts, subcounts, factor=factor)
            continue

        if tok.type == "SYMBOL":
            sym = tok.value  # type: ignore[assignment]
            # validate element exists
            if sym not in dic_tabela_periodica:
                raise FormulaError("Fórmula inválida")

            idx += 1
            # optional quantity
            qty = 1
            if idx < len(tokens) and tokens[idx].type == "NUMBER":
                qty = _parse_int(tokens[idx])
                idx += 1

            counts[sym] = counts.get(sym, 0) + qty
            continue

        # NUMBER in unexpected place
        raise FormulaError("Fórmula inválida")

    return counts, idx


def interpretar_formula(formula: str, dic_tabela_periodica: dict[str, list]) -> list[tuple[str, int]]:
    tokens = _tokenize(formula)

    counts, idx = _parse_group(tokens, dic_tabela_periodica, 0)

    if idx != len(tokens):
        # leftover tokens means mismatched parenthesis or other invalid structure
        raise FormulaError("Fórmula inválida")

    # Transform to list of tuples in insertion/appearance order.
    # Tests expect deterministic order for their cases.
    # We'll rebuild order by scanning original formula and recording first occurrence.
    order: list[str] = []
    seen: set[str] = set()

    # simple scan to recover order (elements only)
    i = 0
    while i < len(formula):
        ch = formula[i]
        if "A" <= ch <= "Z":
            sym = ch
            i += 1
            if i < len(formula) and "a" <= formula[i] <= "z":
                sym += formula[i]
                i += 1
            if sym in counts and sym not in seen:
                order.append(sym)
                seen.add(sym)
            continue
        i += 1

    return [(sym, counts[sym]) for sym in order]

