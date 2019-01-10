#include <fstream>
#include <iostream>
#include <thread>
#include <vector>

namespace Fibo {

  // calcule le Nieme terme de la suite de "Fibonacci modulo 42"
  // precondition : N >= 0
  int FibonacciMod42(int N) {
    int f_curr = 0;
    int f_prec = 1;
    for (int i=1; i<=N; i++) {
      int tmp = f_curr;
      f_curr = (f_curr + f_prec) % 42;
      f_prec = tmp;
    }
    return f_curr;
  }

  //////////////////////////////////////////////////////////////////////

  // fonction pour repartir les calculs
  void calculerTout(std::vector<int> &data) {
    // effectue tous les calculs
    for (unsigned i=0; i<data.size(); i++) {
      data[i] = FibonacciMod42(i);
    }
  };

  std::vector<int> fiboSequentiel(int nbData) {
    // cree le tableau de donnees a calculer
    std::vector<int> data(nbData); 
    // calcule les donnees sequentiellement
    calculerTout(data);
    return data;
  }

  //////////////////////////////////////////////////////////////////////
  
  // fonction pour repartir les calculs
  void calculerBloc(std::vector<int> &data, unsigned i0, unsigned i1) {
    // effectue tous les calculs
    for (unsigned i=i0; i<i1; i++) {
      data[i] = FibonacciMod42(i);
    }
  };

  std::vector<int> fiboBlocs(int nbData) {
    // cree le tableau de donnees a calculer
    std::vector<int> data(nbData); 
    // calculer sur deux threads, par bloc
    
    std::thread t1(calculerBloc, std::ref(data), 0, nbData/2);
    std::thread t2(calculerBloc, std::ref(data), nbData/2, nbData);
    
    t1.join();
    t2.join();

    return data;
  }

  //////////////////////////////////////////////////////////////////////
 
  void calculerCyclique2(std::vector<int> &data, int begin, int step) {
    
    for (int i = begin; i < data.size(); i += step) {
      data[i] = FibonacciMod42(i);
    }
  };
  
  std::vector<int> fiboCyclique2(int nbData) {
    // cree le tableau de donnees a calculer
    std::vector<int> data(nbData); 
    // calculer sur deux threads, cycliquement
    // exécute le noyau de calcul en parallèle sur 2 threads
    
    std::thread t1(calculerCyclique2, std::ref(data), 0, 2);
    std::thread t2(calculerCyclique2, std::ref(data), 1, 2);
    
    t1.join();
    t2.join();
    
    return data;
  }

  //////////////////////////////////////////////////////////////////////

  std::vector<int> fiboCycliqueN(int nbData, int nbProc) {
    // cree le tableau de donnees a calculer
    std::vector<int> data(nbData); 
    // calculer sur N threads, cycliquement
    std::vector<std::thread> threads(nbProc);
    
    std::thread myThreads[nbProc];

    for (int i = 0; i < nbProc; i++) {
        myThreads[i] = std::thread(calculerCyclique2, std::ref(data), i, nbProc);
    }
    
    for (int i = 0; i < nbProc; i++) {
        myThreads[i].join();
    }
    
    return data;
  }

  //////////////////////////////////////////////////////////////////////

  void fiboCycliqueNFake(int nbData, int nbProc) {
    // calculer sur N threads, cycliquement, en ignorant le résultat
    // cree le tableau de donnees a calculer
    std::vector<int> data(nbData); 
    // calculer sur N threads, cycliquement
    std::vector<std::thread> threads(nbProc);
    
    std::thread myThreads[nbProc];

    for (int i = 0; i < nbProc; i++) {
        myThreads[i] = std::thread(calculerCyclique2, std::ref(data), i, nbProc);
    }
    
    for (int i = 0; i < nbProc; i++) {
        myThreads[i].join();
    }
  }

}  // namespace Fibo

