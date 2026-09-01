def executar_ia_adivinhacao():
    print("=" * 55)
    print("      MINI-IA: ÁRVORE DE DECISÃO INTERATIVA      ")
    print("=" * 55)
    print("Pense em um destes animais:")
    print("LEÃO, TUBARÃO, ÁGUIA, CACHORRO, GATO, ELEFANTE,")
    print("MACACO, PINGUIM, COBRA ou CAVALO.")
    print("Responda apenas com 's' (sim) ou 'n' (não).\n")

    # BASE DE CONHECIMENTO (Estrutura da Árvore de Decisão)
    arvore_conhecimento = {
        "pergunta": "O animal vive na água?",
        "sim": {
            "pergunta": "O animal é um peixe?",
            "sim": {
                "palpite": "Tubarão"
            },
            "nao": {
                "pergunta": "O animal é conhecido por nadar e viver em regiões muito frias?",
                "sim": {
                    "palpite": "Pinguim"
                },
                "nao": {
                    "palpite": "Tubarão"
                }
            }
        },
        "nao": {
            "pergunta": "O animal consegue voar?",
            "sim": {
                "palpite": "Águia"
            },
            "nao": {
                "pergunta": "O animal é considerado um pet doméstico?",
                "sim": {
                    "pergunta": "O animal costuma miar?",
                    "sim": {
                        "palpite": "Gato"
                    },
                    "nao": {
                        "palpite": "Cachorro"
                    }
                },
                "nao": {
                    "pergunta": "O animal é muito grande e possui uma tromba?",
                    "sim": {
                        "palpite": "Elefante"
                    },
                    "nao": {
                        "pergunta": "O animal costuma viver em árvores?",
                        "sim": {
                            "palpite": "Macaco"
                        },
                        "nao": {
                            "pergunta": "O animal possui escamas e rasteja?",
                            "sim": {
                                "palpite": "Cobra"
                            },
                            "nao": {
                                "pergunta": "O animal é usado para montaria?",
                                "sim": {
                                    "palpite": "Cavalo"
                                },
                                "nao": {
                                    "palpite": "Leão"
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    # MOTOR DE INFERÊNCIA (Navegação na Árvore)
    no_atual = arvore_conhecimento

    while "pergunta" in no_atual:
        resposta = input(f"{no_atual['pergunta']} (s/n): ").lower().strip()

        if resposta == 's':
            no_atual = no_atual["sim"]
        elif resposta == 'n':
            no_atual = no_atual["nao"]
        else:
            print("Entrada inválida! Digite apenas 's' para sim ou 'n' para não.\n")

    # CONCLUSÃO DA IA (Nó Folha)
    print("\n" + "=" * 55)
    print(f"Palpite da IA: Você pensou no(a) {no_atual['palpite']}!")
    print("=" * 55)


if __name__ == "__main__":
    executar_ia_adivinhacao()