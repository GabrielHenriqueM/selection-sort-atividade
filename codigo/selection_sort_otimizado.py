def selection_sort_otimizado(lista):
    n = len(lista)
    iteracoes = 0

    print("\nSELECTION SORT OTIMIZADO")
    print("Antes da ordenação:", lista)

    for i in range(n):
        min_index = i
        trocou = False

        for j in range(i + 1, n):
            iteracoes += 1
            if lista[j] < lista[min_index]:
                min_index = j
                trocou = True

        if min_index != i:
            valor_antigo = lista[i]
            valor_novo = lista[min_index]
            lista[i], lista[min_index] = lista[min_index], lista[i]
            print(f"Iteração {i + 1}: {lista} (trocou {valor_antigo} com {valor_novo})")
        else:
            print(f"Iteração {i + 1}: {lista} (sem troca)")

        if not trocou:
            break

    print("Depois da ordenação:", lista)
    print(f"Total de iterações (comparações): {iteracoes}\n")
    return lista, iteracoes

if __name__ == "__main__":
    vetor = [93, 12, 78, 41, 5, 66, 20]
    selection_sort_otimizado(vetor)
