#pragma once

class Index {
    public:
    Index();
    void Build(); 
    void Match(const TargetInfo& target_info); 
private:
  AttrTree* index_tree_ = nullptr;
};