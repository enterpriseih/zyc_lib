#pragma once
#include "algo/opindex/attr_tree.h"
struct Node {
  Node* next_ = nullptr;
  Attr* attr = nullptr;
};
class AttrTree {};