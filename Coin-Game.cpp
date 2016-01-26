#include <iostream>
using namespace std;
int chips = 0, taken = 0, cpu = 0, chip = 0, constant = 2;
bool player = 0;

void take_token(int p){
	do{//player idiot check
		cout << "\nPlayer " << p + 1 << ": take 1 or 2 chips" << endl;
		cin >> taken;
		if ((taken == 1) || (taken == 2)){//actual game runs the cycles for how many chips have been taken accepts only user input
			chips -= taken;
			cout << "Chips Remaining:" << chips << endl;
			break;
		}
		else{
			cout << "You may only 1 or 2 chips" << endl;
		}
	} while (true);
}

void drawchips(int chips){//displays the chips that are left
	for (int b = 1; b <= chips; b++){
		cout << "@ ";
	}
}

void multiplayer(){//function for 2 players
	do{
		drawchips(chips);
		take_token(player);
		player = !player;

	} while (chips > 0);//end game loop
	cout << "Player " << !player + 1 << " wins" << endl;
}

void AITURN(){//AI function for singleplayer
	do{
		taken = chips % 3;
		if ((taken == 1) || (taken == 2)){
			chips -= taken;
			break;
		}
		else {
			taken = 2;
			chips -= taken;
			break;
		}
	} while (true);
	cout << "\nComputer takes " << taken << " chips:" << endl;
	cout << "Chips remaining:" << chips << endl;
}
void singleplayer(){//Singleplayer gamemode
	do{
		drawchips(chips);
		take_token(0);
		if (chips <= 0){
			break;
		}
		drawchips(chips);
		AITURN();
	} while (chips > 0);
	cout << "WINNER" << endl;//Displays winner
}
int main(){
	chips = 10;
	do {
		cout << "The idea behind this game is that each player may only take 1 or 2 chips at \nduring a turn and the objective is to take the last chip. There are ten chips \non the table." << endl;//Game Instructions \n attached to other words to make instructions easier to read 
		cout << "How many player<1 or 2>?" << endl;
		cin >> cpu;
		// Dictates how the game will be played either Singleplayer or Multiplayer
		if (cpu == 2){
			multiplayer();
			break;
		}
		if (cpu == 1){
			singleplayer();
			break;
		}
		else {
			cout << "You may only have 1 or 2 players!!!!!!!" << endl;
		}
	} while (true);
	cin >> taken;
}
