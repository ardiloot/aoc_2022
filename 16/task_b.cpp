#include <iostream>
#include <fstream>
#include <regex>
#include <sstream>
#include <vector>
#include <map>

typedef std::array<std::array<std::array<std::array<int16_t, 65536>, 27>, 61>, 61> CacheArray;

struct Valve {
    std::string name;
    int id = 0; 
    int mask = 0;
    int rate = 0;
    std::vector<std::string> str_links;
    std::vector<int> links;

};


std::vector<Valve> valves;
std::map<std::string, int> valve_id_map;
int num_openable_valves = 0;
int max_flow = 0;
CacheArray* dp;

void read_input() {
    std::ifstream in("input.txt");
    std::regex regex_line("Valve (.*) has flow rate=(.*); tunnels? leads? to valves? (.*)");

    for (std::string line; std::getline(in, line);) {
        std::smatch match; 
        std::regex_match(line, match, regex_line);

        Valve valve;
        valve.id = valves.size();
        valve.mask = 1 << num_openable_valves;
        valve.name = match[1];
        valve.rate = std::stoi(match[2]);
        std::istringstream ss(match[3]);
        for (std::string to; ss >> to;)
            valve.str_links.push_back(to.substr(0, 2));
        valve_id_map[valve.name] = valve.id;
        if (valve.rate)
            num_openable_valves++;
        valves.push_back(std::move(valve));
        max_flow += valve.rate;
    }

    for (Valve& v : valves) {
        for (auto& name : v.str_links) {
            v.links.push_back(valve_id_map.at(name));
        }
    }
}

int solve(int id1, int id2, int minutes, int opened) {
    if (minutes <= 0)
        return 0;

    if ((*dp)[id1][id2][minutes][opened] > 0)
        return (*dp)[id1][id2][minutes][opened];

    int res = 0;
    const Valve& v1 = valves[id1];
    const Valve& v2 = valves[id2];
    const bool can_open1 = v1.rate > 0 && (v1.mask & opened) == 0;
    const bool can_open2 = v2.rate > 0 && (v2.mask & opened) == 0;

    // 1. opens valve, 2. moves
    if (can_open1) {
        for (int to2 : v2.links) {
            res = std::max(res, solve(id1, to2, minutes - 1, opened | v1.mask));
        }
    }

    // 2. opens valve, 1. moves
    if (can_open2) {
        for (int to1 : v1.links) {
            res = std::max(res, solve(to1, id2, minutes - 1, opened | v2.mask));
        }
    }

    // Both open valves
    if (can_open1 && can_open2 && id1 != id2) {
        res = std::max(res, solve(id1, id2, minutes - 1, opened | v1.mask | v2.mask));
    }

    // Both move
    for (int to1 : v1.links) {
        for (int to2 : v2.links) {
            res = std::max(res, solve(to1, to2, minutes - 1, opened));
        }
    }

    // Flow for open valves
    for (const auto& v : valves) {
        if (v.rate > 0 && (v.mask & opened) != 0) {
            res += v.rate;
        }
    }

    (*dp)[id1][id2][minutes][opened] = res;
    return res;
}

int main() {
    dp = new CacheArray();

    read_input();
    const int home = valve_id_map["AA"];
    const int res = solve(home, home, 26, 0);
    std::cout << res << std::endl;

    return 0;
}