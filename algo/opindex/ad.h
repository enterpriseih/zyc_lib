#pragma once
#include <string>
#include <vector>

#include "algo/opindex/attr.h"

class Ad {
 private:
  uint64_t ad_group_id;
  std::vector<Attr>
      predicates_;  // 广告是断言的集合，因为可以离散化，所以断言中的操作符只有=
  std::string ToString() {
    std::string result = "ad_group_id: ";
    result += std::to_string(ad_group_id);
    result += "\n";
    for (auto& one_attr : predicates_) {
      result += "attr_type: ";
      result += one_attr.attr_type;
      result += "\n";
      result += "attr_value: ";
      result += one_attr.attr_value;
    }
  }
};