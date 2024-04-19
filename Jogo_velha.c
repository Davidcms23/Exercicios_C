#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>

//FUNÇÃO PARA MOSTRAR A TABELA
void tab(char tabela[3][3]){
    printf("_|1||2||3|\n");
    for(int i = 0; i < 3; i++){
        printf("%d", i + 1);
        for(int j = 0; j < 3; j++){
            printf("|%c|", tabela[i][j]);
        }
        printf("\n");
    }
}

//FUNÇÃO DE VERIFICAÇÃO DE VITÓRIA
int V(char tabela[3][3]){
    //horizontal e vertical
    for(int i = 0; i < 3; i++){
        if((tabela[i][0] == 'X' || tabela[i][0] == 'O') && tabela[i][0] == tabela[i][1] && tabela[i][0] == tabela[i][2]){
            return 1;
        }
        if((tabela[0][i] == 'X' || tabela[0][i] == 'O') && tabela[0][i] == tabela[1][i] && tabela[0][i] == tabela[2][i]){
            return 1;
        }
    }
    //diagonais
    if((tabela[0][0] == 'X' || tabela[0][0] == 'O') && tabela[0][0] == tabela[1][1] && tabela[0][0] == tabela[2][2]){
        return 1;
    }
    if((tabela[0][2] == 'X' || tabela[0][2] == 'O') && tabela[0][2] == tabela[1][1] && tabela[0][2] == tabela[2][0]){
        return 1;
    }
    return 0;
}

//FUNÇÃO DE JOGADA DO PC
void pc(char tabela[3][3]){
    int linha, coluna;
    do{
        linha = rand()%3;
        coluna = rand()%3;
    }while(tabela[linha][coluna] != ' ');

    tabela[linha][coluna] = 'O';
}

//JOGO
int main(){
    char tabela[3][3] = {{' ', ' ', ' '},
                         {' ', ' ', ' '},
                         {' ', ' ', ' '}};

    //MENU
    int menu = 0;
    printf("\nJOGO DA VELHA\n");
    printf("\nMENU:\n");
    printf("1 ou 2 jogadores: ");
    scanf("%d", &menu);

    int linhaX, colunaX, linhaO, colunaO;
    tab(tabela);

    //JOGO PARA 2 JOGADORES
    if(menu == 2){
        int jogadas = 0;
        while(1){
            //1 jogador joga
            printf("\nJogador 1\nEscolha a linha: ");
            scanf("%d", &linhaX);
            printf("Escolha a coluna: ");
            scanf("%d", &colunaX);
            if(tabela[linhaX - 1][colunaX - 1] == ' '){
                tabela[linhaX - 1][colunaX - 1] = 'X';
                tab(tabela);
                if(V(tabela)){
                    printf("Jogador 1 ganhou!\n");
                    break;
                }
            jogadas += 1;
            if(jogadas == 9){
                printf("EMPATE!!\n");
                break;
            } 
                //2 jogador joga
                printf("\nJogador 2\nEscolha a linha: ");
                scanf("%d", &linhaO);
                printf("Escolha a coluna: ");
                scanf("%d", &colunaO);
                if(tabela[linhaO - 1][colunaO - 1] == ' '){
                    tabela[linhaO - 1][colunaO - 1] = 'O';
                    tab(tabela);
                    if(V(tabela)){
                        printf("Jogador 2 ganhou!\n");
                        break;
                    }
                } 
                else{
                    printf("\nJogada invalida, tente novamente.\n");
                }
            } 
            else{
                printf("\nJogada invalida, tente novamente.\n");
            }
            jogadas += 1; 
            
        }
    } 

    // JOGO PARA 1 JOGADOR
    else{
        int jogadas = 0;
        while(1){
            //Jogador joga
            printf("\nJogador\nEscolha a linha: ");
            scanf("%d", &linhaX);
            printf("Escolha a coluna: ");
            scanf("%d", &colunaX);
            if(tabela[linhaX - 1][colunaX - 1] == ' '){
                tabela[linhaX - 1][colunaX - 1] = 'X';
                tab(tabela);
                if(V(tabela)){
                    printf("Jogador ganhou!\n");
                    break;
                }
            jogadas += 1;
            if(jogadas == 9){
                printf("EMPATE!!\n");
                break;
            }     
                //PC joga
                pc(tabela);
                tab(tabela);
                if (V(tabela)) {
                    printf("Computador ganhou!\n");
                    break;
                }
            } 
            else{
                tab(tabela);
                printf("\nJogada invalida, tente novamente.\n");
            }
            jogadas += 1;
        }
    }

    return 0;
}



