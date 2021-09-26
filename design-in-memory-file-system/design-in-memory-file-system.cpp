struct FileNode {
    bool isDir;
    string name;
    string content;
    vector<FileNode *> children;

    FileNode(string name, bool isDir = true) {
        this->isDir = isDir;
        this->name = name;
        this->content = "";
    }
};

class FileSystem {
   private:
    FileNode *root;

   public:
    FileSystem() { root = new FileNode("root"); }

    vector<string> ls(string path) {
        auto curr = root;
        auto pathSplit = stringSplit(path, '/');
        vector<string> ret;
        int depth = 0;
        while (depth < pathSplit.size())
            for (auto child : curr->children)
                if (child->name == pathSplit[depth]) {
                    curr = child;
                    depth += 1;
                }
        if (curr->isDir)
            for (auto child : curr->children) ret.push_back(child->name);
        else
            ret.push_back(curr->name);
        sort(ret.begin(), ret.end());
        return ret;
    }

    void mkdir(string path) {
        auto curr = root;
        auto pathSplit = stringSplit(path, '/');
        int depth = 0;
        while (depth < pathSplit.size()) {
            bool found = false;
            for (auto child : curr->children) {
                if (child->name == pathSplit[depth]) {
                    found = true;
                    curr = child;
                    depth += 1;
                }
            }
            if (!found) {
                auto tempNode = new FileNode(pathSplit[depth]);
                curr->children.push_back(tempNode);
                curr = tempNode;
                depth += 1;
            }
        }
    }

    string readContentFromFile(string filePath) {
        auto curr = root;
        int depth = 0;
        auto pathSplit = stringSplit(filePath, '/');
        while (depth < pathSplit.size()) {
            for (auto child : curr->children) {
                if (child->name == pathSplit[depth]) {
                    curr = child;
                    depth += 1;
                }
            }
        }
        return curr->content;
    }

    void addContentToFile(string filePath, string content) {
        auto curr = root;
        int depth = 0;
        auto pathSplit = stringSplit(filePath, '/');
        // maxDepth - 2 as get parent dir add child file
        while (depth + 1 < pathSplit.size())
            for (auto child : curr->children)
                if (child->name == pathSplit[depth]) {
                    curr = child;
                    depth += 1;
                }
        FileNode *fileIfFound = nullptr;
        for (auto child : curr->children)
            if (child->name == pathSplit[depth]) fileIfFound = child;

        if (fileIfFound) {
            fileIfFound->content += content;
        } else {
            auto tempNode = new FileNode(pathSplit.back(), false);
            tempNode->content = content;
            curr->children.push_back(tempNode);
        }
    }

    vector<string> stringSplit(string s, char delim = ' ') {
        if (s == "/") return vector<string>();
        vector<string> ret;
        int start, end;
        for (end = s.find(delim), start = 0; end != -1;
             start = end + 1, end = s.find(delim, start))
            ret.push_back(s.substr(start, end - start));
        ret.push_back(s.substr(start, end - start));
        if (ret.size() > 0) ret.erase(ret.begin());
        return ret;
    }
};