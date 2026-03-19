#include <iostream>
#include <random>
#include <vector>
#include <string>
#include <unordered_map>
#include <cstdlib>
#include <conio.h>

// Piece Placer Function -- Algorithm Used for NPC AI to place pieces appropriately within bounds.

std::vector<std::string> piecePlacer(std::vector<int> rng_set, std::string init_pos, int slots, std::vector<std::string> battle_board, std::vector<std::string> occ_sp) {

	std::vector<std::string> p_pos = { init_pos };

	int post_pos_rng = rng_set[0];
	int sign_rng = rng_set[1];
	
	if (post_pos_rng == 0) {
		std::string l_grid_sel = init_pos.substr(0, 1);

		int i = 0;

		for (std::string space : battle_board) {

			if (battle_board[i] == init_pos) {
				break;

			}

			else { i += 1; }
		}

		while (slots > 0) {

			if (init_pos.substr(1, 2) == "1" || init_pos.substr(1, 2) == "2" || init_pos.substr(1, 2) == "3" || init_pos.substr(1, 2) == "4") {
				
				std::string placement = battle_board[i + (1 * slots)];
				p_pos.push_back(placement);

				slots -= 1;
			}

			else if (init_pos.substr(1, 2) == "7" || init_pos.substr(1, 2) == "8" || init_pos.substr(1, 2) == "9" || init_pos.substr(1, 2) == "10") {

				std::string placement = battle_board[i - (1 * slots)];
				p_pos.push_back(placement);

				slots -= 1;

			}
			else { 
				sign_rng;

				if (sign_rng == 0) {

					std::string placement = battle_board[i + (1 * slots)];
					p_pos.push_back(placement);
					

					slots -= 1;
				}

				else if (sign_rng == 1) {

					std::string placement = battle_board[i - (1 * slots)];
					p_pos.push_back(placement);
					

					slots -= 1;

				}
			}
		}


	}

	else if (post_pos_rng == 1) {
		std::string n_grid_sel = init_pos.substr(1, 2);

		int i = 0;

		for (std::string space : battle_board) {

			if (battle_board[i] == init_pos) {
				break;
			}

			else { i += 1; }
		}

		while (slots > 0) {

			if (init_pos.substr(0, 1) == "A" || init_pos.substr(0, 1) == "B" || init_pos.substr(0, 1) == "C" || init_pos.substr(0, 1) == "D") {

				std::string placement = battle_board[i + (10 * slots)];
				p_pos.push_back(placement);
				

				slots -= 1;

			}

			else if (init_pos.substr(0, 1) == "G" || init_pos.substr(0, 1) == "H" || init_pos.substr(0, 1) == "I" || init_pos.substr(0, 1) == "J") {

				std::string placement = battle_board[i - (10 * slots)];
				p_pos.push_back(placement);
				

				slots -= 1;

			}

			else {

				sign_rng;

				if (sign_rng == 0) {

					std::string placement = battle_board[i + (10 * slots)];
					p_pos.push_back(placement);
					

					slots -= 1;
				}

				else if (sign_rng == 1) {

					std::string placement = battle_board[i - (10 * slots)];
					p_pos.push_back(placement);

					slots -= 1;

				}
			}
		}
	}

	return p_pos;
}







void static writeScreen(std::vector<std::string> disp_board) {

	system("cls");

	std::cout << "\n";
	std::cout << std::string(52, '*') << "\n Kills: " << std::string(31, ' ') << "Hits: " << "\n Losses: " << std::string(30, ' ') << "Misses: " << std::endl;
	std::cout << std::string(52, '*') << std::endl;

	int j = 0;
	for (int i = 0; i < disp_board.size(); i++) {

		if (disp_board[i] == "^^") {
			std::cout << " [" << "\033[33m" << disp_board[i] << "\033[0m" << "]";
		}

		else if (disp_board[i] == "< ") {
			std::cout << " [" << "\033[33m" << disp_board[i] << "\033[0m" << "]";
		}

		else if (disp_board[i] == "! ") {
			std::cout << " [" << "\033[31m" << disp_board[i] << "\033[0m" << "]";
		}

		else if (disp_board[i] == "@ ") {
			std::cout << " [" << "\033[34m" << disp_board[i] << "\033[0m" << "]";
		}

		else if (disp_board[i] == "##") {
			std::cout << " [" << "\033[33m" << disp_board[i] << "\033[0m" << "]";
		}
		else {
			std::cout << " [" << disp_board[i] << "]";
		}

		if (i == j + 9) {
			std::cout << "\n" << std::endl;
			j += 10;
		}
	}
}
 






int main()
{	
	bool batship = true;
	while (batship) {

		std::string a_list[10] = { "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"};
		std::string n_list[10] = { "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"};

		std::vector<std::string> battle_board;
		std::vector<std::string> shot_board;
		std::vector<std::string> ref_board;

		for (const std::string let : a_list) {
			for (const std::string num : n_list) {

				std::string g_space = let + num;

				battle_board.push_back(g_space);
				shot_board.push_back(g_space);
				ref_board.push_back(g_space);
			}
		}

		static std::random_device rd;
		static std::mt19937 gen(rd());
		std::uniform_int_distribution<int> dist(1, battle_board.size());
		std::uniform_int_distribution<int> dist2(0, 1);

		
		std::vector<std::string> occ_sp;
		std::unordered_map<std::string, std::vector<std::string>> grid_pos;

		int m_sel;

		std::cout << std::string(36, '=') << std::endl;
		std::cout << " Welcome to BattleShip!" << std::string(12, ' ') << "|" << "\n C++ Edition!" << std::string(22, ' ') << "|" << "\n Version: 0.10 (March 18th 2025) " << std::string(2, ' ') << "|" << "\n" << std::string(36, '=') << "\n" << std::endl;
		std::cout << " 1.) Play Game\n" << " 2.) Options\n" << " 3.) Close BattleShip\n" << "\nPlease Make a Selection: ";
		std::cin >> m_sel;

		if (m_sel == 1) {

			bool game_mode = true;
			while (game_mode) {

				std::string b_pieces[5] = { "Carrier", "Battleship", "Cruiser", "Sub", "Destroyer" };

				for (std::string piece : b_pieces) {

					if (piece == "Carrier") {

						int slots = 4;
						int init_pos_sel = dist(gen);
						std::string init_pos = battle_board[init_pos_sel - 1];
						
						int post_pos_rng = dist2(gen);
						int sign_rng = dist2(gen);
					    std::vector<int> rng_set = {post_pos_rng, sign_rng};

						std::vector<std::string> piece_pos = piecePlacer(rng_set, init_pos, slots, battle_board, occ_sp);

						grid_pos[piece] = piece_pos;
						
					}


					else if (piece == "Battleship") {

						int slots = 3;

						int init_pos_sel = dist(gen);
						std::string init_pos = battle_board[init_pos_sel - 1];

						for (std::string space : occ_sp) {

							while (init_pos == space) {

								init_pos_sel = dist(gen);
								init_pos = battle_board[init_pos_sel - 1];
							}
						}

						int post_pos_rng = dist2(gen);
						int sign_rng = dist2(gen);
						std::vector<int> rng_set = { post_pos_rng, sign_rng };

						std::vector<std::string> piece_pos = piecePlacer(rng_set, init_pos, slots, battle_board, occ_sp);

						int ind_num = occ_sp.size();
						bool reset = false;

						while (ind_num > 0) {

							reset = false;
							for (std::string p_pos : piece_pos) {
								for (std::string t_pos : occ_sp) {

									if (p_pos == t_pos) {

										int post_pos_rng = dist2(gen);
										int sign_rng = dist2(gen);
										std::vector<int> rng_set = { post_pos_rng, sign_rng };

										piece_pos = piecePlacer(rng_set, init_pos, slots, battle_board, occ_sp);
										ind_num = occ_sp.size();

										reset = true;
										break;
									}

									else { ind_num -= 1; }
								}

								if (reset == true) {
						
									reset = false;
									break;
								}
								else {}
							}
						}

						grid_pos[piece] = piece_pos;

					}


					else if (piece == "Cruiser") {

						int slots = 2;

						int init_pos_sel = dist(gen);
						std::string init_pos = battle_board[init_pos_sel - 1];

						for (std::string space : occ_sp) {

							while (init_pos == space) {

								init_pos_sel = dist(gen);
								init_pos = battle_board[init_pos_sel - 1];
							}
						}

						int post_pos_rng = dist2(gen);
						int sign_rng = dist2(gen);
						std::vector<int> rng_set = { post_pos_rng, sign_rng };

						std::vector<std::string> piece_pos = piecePlacer(rng_set, init_pos, slots, battle_board, occ_sp);

						int ind_num = occ_sp.size();
						bool reset = false;

						while (ind_num > 0) {
			
							reset = false;

							for (std::string p_pos : piece_pos) {

								for (std::string t_pos : occ_sp) {

									if (p_pos == t_pos) {

										int post_pos_rng = dist2(gen);
										int sign_rng = dist2(gen);
										std::vector<int> rng_set = { post_pos_rng, sign_rng };

										piece_pos = piecePlacer(rng_set, init_pos, slots, battle_board, occ_sp);
										reset = true;

										break;

									}

									else { ind_num -= 1; }
								}

								if (reset == true) {
									ind_num = occ_sp.size();

									reset = false;
								
									break;
								}
								else {}
							}
						}

						grid_pos[piece] = piece_pos;
					}


					else if (piece == "Sub") {
						int slots = 2;

						int init_pos_sel = dist(gen);
						std::string init_pos = battle_board[init_pos_sel - 1];

						for (std::string space : occ_sp) {

							while (init_pos == space) {

								init_pos_sel = dist(gen);
								init_pos = battle_board[init_pos_sel - 1];
							}
						}

						int post_pos_rng = dist2(gen);
						int sign_rng = dist2(gen);
						std::vector<int> rng_set = { post_pos_rng, sign_rng };

						std::vector<std::string> piece_pos = piecePlacer(rng_set, init_pos, slots, battle_board, occ_sp);

						int ind_num = occ_sp.size();
						bool reset = false;

						while (ind_num > 0) {
							
							reset = false;
							for (std::string p_pos : piece_pos) {

								for (std::string t_pos : occ_sp) {

									if (p_pos == t_pos) {

										int post_pos_rng = dist2(gen);
										int sign_rng = dist2(gen);
										std::vector<int> rng_set = { post_pos_rng, sign_rng };

										piece_pos = piecePlacer(rng_set, init_pos, slots, battle_board, occ_sp);
										ind_num = occ_sp.size();
										reset = true;
										
										break;

									}

									else { ind_num -= 1; }
								}

								if (reset == true) {
									
									reset = false;
									break;
								}
								else {}
							}
						}

						grid_pos[piece] = piece_pos;
					}


					else if (piece == "Destroyer") {

						int slots = 1;
						int init_pos_sel = dist(gen);
						std::string init_pos = battle_board[init_pos_sel - 1];

						for (std::string space : occ_sp) {

							while (init_pos == space) {

								init_pos_sel = dist(gen);
								init_pos = battle_board[init_pos_sel - 1];
							}
						}

						int post_pos_rng = dist2(gen);
						int sign_rng = dist2(gen);
						std::vector<int> rng_set = { post_pos_rng, sign_rng };

						std::vector<std::string> piece_pos = piecePlacer(rng_set, init_pos, slots, battle_board, occ_sp);

						int ind_num = occ_sp.size();
						bool reset = false;

						while (ind_num > 0) {
							
							reset = false;
							for (std::string p_pos : piece_pos) {

								for (std::string t_pos : occ_sp) {

									if (p_pos == t_pos) {

										int post_pos_rng = dist2(gen);
										int sign_rng = dist2(gen);
										std::vector<int> rng_set = { post_pos_rng, sign_rng };

										piece_pos = piecePlacer(rng_set, init_pos, slots, battle_board, occ_sp);
										ind_num = occ_sp.size();
										reset = true;
										
										break;

									}
									else { ind_num -= 1; }
								}

								if (reset == true) {
									
									reset = false;
									break;
								}
								else {}
							}
						}

						grid_pos[piece] = piece_pos;
					}
				}


				bool p_place = true;
				int slots = 0;

				std::vector<std::string> disp_board = battle_board;
				writeScreen(disp_board);

				std::vector<std::string> p_pos;
				std::unordered_map<std::string, std::vector<std::string>> grid_pos_p;
				
				while (p_place) {

					int x = 0;
					
					int next = 0;
					int rot = 0;
					
					std::vector<std::string> prev_sp;
					std::string next_sp;
				
					for (std::string piece : b_pieces) {
					
						if (piece == "Carrier") {
							slots = 5;
						}

						else if (piece == "Battleship") {
							slots = 4;
						}

						else if (piece == "Cruiser") {
							slots = 3;
						}

						else if (piece == "Sub") {
							slots = 3;
						}

						else if (piece == "Destroyer") {
							slots = 2;
						}

						bool placement = true;
						while (placement) {

							int i = 0;
							for (i; i < slots; i++) {

								if (rot == 0) {

									prev_sp.push_back(battle_board[x + (i * 10)]);
									battle_board[x + (i * 10)] = "^^";

								}

								else {

									prev_sp.push_back(battle_board[x + i]);
									battle_board[x + i] = "< ";
								}

							}

							disp_board = battle_board;
							writeScreen(disp_board);
							
							i = 0;
							for (i; i < slots; i++) {

								std::string prev = prev_sp[i];
							
								if (rot == 0) {

									battle_board[x + (i * 10)] = prev;

								}

								else { battle_board[x + i] = prev; }
							}
							


							if (_kbhit) {

								char key = _getch();

								if (key == 27) {
									return 0;
								}

								else if (key == 13) {

									if (rot == 0) {

										for (i = 0; i < slots; i++) {

											p_pos.push_back(battle_board[x + (i * 10)]);
											battle_board[x + (i * 10)] = "^^";
											
										}

										grid_pos_p[piece] = p_pos;
										p_pos.clear();

										placement = false;

									}

									else {

										for (i = 0; i < slots; i++) {

											p_pos.push_back(battle_board[x + i]);
											battle_board[x + i] = "< ";
										}

										grid_pos_p[piece] = p_pos;
										p_pos.clear();

										placement = false;

									}

									
								}

								else {
									switch (key) {

									case 'w': if (x > 0) x -= 10; break;
									case 's': if (x < 99) x += 10; break;
									case 'a': if (x > 0) x--; break;
									case 'd': if (x < 99) x++; break;
									case 'r': if (rot == 1) rot = 0; else if (rot == 0) rot = 1; break;
									
					
									case 'q': return 0;

									}
								}
									
								prev_sp.clear();

								i = 0;
								for (i; i < slots; i++) {

									if (rot == 0) {
										next_sp = battle_board[x + (i * 10)];
										prev_sp.push_back(next_sp);


									}

									else {

										next_sp = battle_board[x + i];
										prev_sp.push_back(next_sp);

									}
								}
								

							}
							

						
						}


						if (grid_pos_p.size() == 5) {

							p_place = false;
							break;
						}

					}

					

				}


				// Continue Game Logic Code from Here.....

				std::cout << "Flipping a coin to determine who starts..." << "\n\nCall it:" << "\n1.) Heads" << "\n2.) Tails" << "\nMake a choice: " << std::endl;

				bool game_loop = true;
				bool p_turn;

				{
					int c_toss;
					int p_call;
					c_toss = dist2(gen);

					std::cin >> p_call;
					p_call -= 1;

					if (p_call == c_toss) {

						std::cout << "Player gets first shot..." << std::endl;
						p_turn = true;

					}

					else {

						std::cout << "CPU gets first shot..." << std::endl;
						p_turn = false;

					}
				}

				std::vector<std::string> shot_list;
				std::vector<std::string> prev_sp;
				std::string next_sp;
			
				while (game_loop) {
					
					int x = 0;

					if (p_turn) {

						disp_board = shot_board;

						bool p_shot = true;
						bool shot_mode = true;
						

						std::cout << "Player's Shooting....\n" << std::endl;
						
						while (shot_mode) {

							while (p_shot) {

								bool hit = false;

								prev_sp.push_back(shot_board[x]);

								shot_board[x] = "##";


								disp_board = shot_board;
								writeScreen(disp_board);

								std::string prev = prev_sp[0];

								shot_board[x] = prev;

								if (_kbhit) {

									char key = _getch();

									if (key == 27) {
										return 0;
									}


									else if (key == 13) {

										std::string shot = shot_board[x];

										for (auto& pairs : grid_pos) {

											for (int i = 0; i < pairs.second.size(); i++) {

												if (shot == pairs.second[i]) {

													std::cout << "HIT!" << std::endl;

													pairs.second[i] = "! ";
													shot_board[x] = "! ";
													prev = shot_board[0];
													hit = true;
													x = 0;

													break;

												}

												else {


												}

											}

											if (hit) {
												break;
											}

											else {
												shot_board[x] = "@ ";
												prev = shot_board[0];

											}
										}

										if (hit == false) {

											x = 0; // LEAVE THIS IN!!! --- NOT REDUNDANT
										}

										p_shot = false;
										shot_mode = false;
										p_turn = false;


									}

									else {

										switch (key) {

										case 'w': if (x > 0) x -= 10; break;
										case 's': if (x < 99) x += 10; break;
										case 'a': if (x > 0) x--; break;
										case 'd': if (x < 99) x++; break;
										case 'q': return 0;

										}
									}

									prev_sp.clear();
									next_sp = shot_board[x];
									prev_sp.push_back(next_sp);

								}
							}
						}
					}

					else {

						std::cout << "\nCPU's shooting..." << std::endl;

						bool cpu_hit = false;
						bool shot_check;
						int cpu_shot_sel = dist(gen);
						std::string cpu_shot = ref_board[cpu_shot_sel - 1];

						disp_board = battle_board;
						writeScreen(disp_board);

						for (int i = 0; i < shot_list.size(); i++) {

							while (cpu_shot == shot_list[i]) {

								std::cout << "Debug --- Repeat Move Detected" << std::endl;
								cpu_shot_sel = dist(gen);
								cpu_shot = ref_board[cpu_shot_sel - 1];
								i = 0;

								break;
							}
						}

						for (auto& pair : grid_pos_p) {

							for (int i = 0; i < pair.second.size(); i++) {

								std::cout << "Debug --- Checking Space: " << pair.second[i] << std::endl;
								std::cout << "Debug --- NPC Chosen Shot: " << cpu_shot << std::endl;

								if (cpu_shot == pair.second[i]) {

									std::cout << "\nDebug --- CPU Shot: " << cpu_shot << std::endl;
									std::cout << "Debug --- CPU Scored a Hit! " << cpu_shot << std::endl;

									battle_board[cpu_shot_sel - 1] = "! ";
									shot_list.push_back(cpu_shot);

									cpu_hit = true;
									break;
								}
							}

							if (cpu_hit) {
								break;
							}
						}
						
						if (cpu_hit == false) {


							std::cout << "Debug --- CPU Missed!" << std::endl;

							battle_board[cpu_shot_sel - 1] = "@ ";
							shot_list.push_back(cpu_shot);

						
						}

						bool s_sunk = false;

						for (auto& pair : grid_pos) {
							
							std::cout << "\nDebug --- Selected Piece: " << pair.first << std::endl;

							for (int i = 0; i < pair.second.size(); i++) {

								std::cout << "Debug --- Piece Space: " << pair.second[i] << std::endl;

								std::cout << "Debug --- i + 1 value: " << i + 1 << std::endl;
								std::cout << "Debug --- Vector Size: " << pair.second.size() << std::endl;

								if (i + 1 == pair.second.size()) {

									break;
								}

								else {

									std::cout << "Debug --- [i] value: " << pair.second[i] << "\nDebug --- [i] + 1 value: " << pair.second[i + 1] << std::endl;

									if (pair.second[i] == "! " && pair.second[i] == pair.second[i + 1]) {

										s_sunk = true;
									}

									else { s_sunk = false; }

								}

								if (s_sunk == true) {

									std::cout << "Debug --- Breaking the vector loop" << std::endl;
									pair.second.clear();
									grid_pos[pair.first] = { "SUNK" };

									std::cout << "Debug --- Checking SUNK Update --- Piece: " << pair.first << "\nPiece Status: " << pair.second[0] << std::endl;
									break;
								}
							}
						}

						std::cout << "Debug --- Did a ship sink?: " << s_sunk << std::endl;

						std::cout << "Now Switching back to Player Shot..." << std::endl;

						int dulling;
						std::cin >> dulling;

						p_turn = true;
						
					}

				}



			}
		}

		else if (m_sel == 2) {
			std::cout << "Implementing Options Menu Here...";
		}

		else if (m_sel == 3) {
			break;
		}
	}

}