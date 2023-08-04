#include <iostream>
#include <map>

int main() {
    std::multimap<int, std::string> multimap;
    // 插入元素
    multimap.insert(std::make_pair(1, "apple"));
    multimap.insert(std::make_pair(2, "banana"));
    multimap.insert(std::make_pair(1, "orange"));

    // 遍历元素
    for (auto it = multimap.begin(); it != multimap.end(); ++it) {
        std::cout << it->first << ": " << it->second << std::endl;
    }

    // 查找元素
    auto range = multimap.equal_range(1);
    for (auto it = range.first; it != range.second; ++it) {
        std::cout << it->first << ": " << it->second << std::endl;
    }

    return 0;
}

