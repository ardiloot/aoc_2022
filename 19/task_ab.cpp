#include <iostream>
#include <fstream>
#include <regex>
#include <array>
#include <unordered_map>

std::regex regex_line {
    "Blueprint (.*): Each ore robot costs (.*) ore. "
    "Each clay robot costs (.*) ore. "
    "Each obsidian robot costs (.*) ore and (.*) clay. "
    "Each geode robot costs (.*) ore and (.*) obsidian."
};
std::array<std::array<int, 3>, 5> robot_cost;
std::array<int, 5> robots = {1, 0, 0, 0, 0};
std::array<int, 3> resources = {0, 0, 0};
std::array<std::unordered_map<int, std::unordered_map<int, int>>, 33> cache;
int best_res = 0;

int parse(const std::string& line) {
    best_res = 0;
    for (int i = 0; i < cache.size(); i++)
        cache[i].clear();

    std::smatch m;
    std::regex_match(line, m, regex_line);
    int blueprint_id = std::stoi(m[1]);
    robot_cost[0] = {std::stoi(m[2]), 0, 0};
    robot_cost[1] = {std::stoi(m[3]), 0, 0};
    robot_cost[2] = {std::stoi(m[4]), std::stoi(m[5]), 0};
    robot_cost[3] = {std::stoi(m[6]), 0, std::stoi(m[7])};
    robot_cost[4] = {0, 0, 0}; // Fake robot costing nothing
    return blueprint_id;
}

bool can_build(int robot_to_build) {
    for (int j = 0; j < 3; j++) {
        if (resources[j] < robot_cost[robot_to_build][j])
            return false;
    }
    return true;
}

int solve(int upstream, int minutes) {
    if (minutes == 1)
        return robots[3];

    const int max_res = upstream + minutes * robots[3] + (minutes - 1) * minutes / 2;
    if (max_res <= best_res)
        return 0;

    const int key_robots = robots[0] + 512 * robots[1] + 512 * 512 * robots[2] + 512 * 512 * 512 * robots[3];
    const int key_resources = resources[0] + 1024 * resources[1] + 1024 * 1024 * resources[2];
    if (cache[minutes].count(key_robots) > 0 && cache[minutes].at(key_robots).count(key_resources) > 0) {
        return cache[minutes].at(key_robots).at(key_resources);
    }

    const int res_this = robots[3]; 
    int max_downstream = 0;
    for (int robot_to_build = 0; robot_to_build < 5; robot_to_build++) {
        if (!can_build(robot_to_build))
            continue;

        for (int j = 0; j < 3; j++)
            resources[j] += robots[j] - robot_cost[robot_to_build][j];
        ++robots[robot_to_build];

        max_downstream = std::max(max_downstream, solve(upstream + res_this, minutes - 1));
        
        --robots[robot_to_build];
        for (int j = 0; j < 3; j++)
            resources[j] += robot_cost[robot_to_build][j] - robots[j];
    }

    const int res = res_this + max_downstream;
    best_res = std::max(best_res, max_downstream + res_this);
    cache[minutes][key_robots].insert({key_resources, res});
    return res;
}

int main() {
    // Part 1
    {
        std::ifstream in("input.txt");
        int res = 0;
        for (std::string line; std::getline(in, line);) {
            const int blueprint_id = parse(line);
            const int r = solve(0, 24);
            res += r * blueprint_id;
        }
        std::cout << "Part 1: " << res << std::endl;
    }

    // Part 2
    {
        std::ifstream in("input.txt");
        int res = 1;
        for (std::string line; std::getline(in, line);) {
            const int blueprint_id = parse(line);
            const int r = solve(0, 32);
            res *= r;
            if (blueprint_id >= 3)
                break;
        }
        std::cout << "Part 2: " << res << std::endl;
    }
    return 0;
}
