import time
from selection_sort_simples import selection_sort
from selection_sort_otimizado import selection_sort_otimizado

def testar_algoritmo(nome, func, lista):
    inicio = time.time()
    _, iteracoes = func(lista.copy())
    fim = time.time()
    tempo = fim - inicio
    print(f"{nome:<10} -> Tempo: {tempo:.6f}s | Comparações: {iteracoes}")
    return tempo, iteracoes

if __name__ == "__main__":
    print("\nCOMPARAÇÃO ENTRE SELECTION SORT SIMPLES E OTIMIZADO (COM LISTAS ORDENADAS)\n")

    tamanhos = [5, 10, 20]
    for tamanho in tamanhos:
        print(f"Teste com vetor ordenado de {tamanho} elementos:")
        vetor_ordenado = list(range(tamanho)) 

        testar_algoritmo("Simples", selection_sort, vetor_ordenado)
        testar_algoritmo("Otimizado", selection_sort_otimizado, vetor_ordenado)
        print()
