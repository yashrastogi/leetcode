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
    FileSystem() {
        cout << __func__ << " entered!" << '\n';
        root = new FileNode("root");
        // auto testNode1 = new FileNode("testnodea");
        // auto testNode2 = new FileNode("testnodeb", false);
        // testNode2->content = "testContent";
        // testNode1->children.push_back(testNode2);
        // root->children.push_back(testNode1);
        cout << __func__ << " finished!" << '\n';
    }

    vector<string> ls(string path) {
        cout << __func__ << " entered!" << '\n';

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

        cout << __func__ << " finished!" << '\n';
        sort(ret.begin(), ret.end());
        return ret;
    }

    void mkdir(string path) {
        cout << __func__ << " entered!" << '\n';

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

        cout << __func__ << " finished!" << '\n';
    }

    string readContentFromFile(string filePath) {
        cout << __func__ << " entered!" << '\n';

        auto curr = root;
        int depth = 0;
        auto pathSplit = stringSplit(filePath, '/');
        while (depth < pathSplit.size()) {
            cout << curr->name << ": ";
            for (auto child : curr->children) {
                cout << child->name << ' ';
                cout << "trying to find: " << pathSplit[depth] << " ";
                if (child->name == pathSplit[depth]) {
                    curr = child;
                    depth += 1;
                }
            }
            cout << " endCurrName: " << curr->name << '\n';
        }
        cout << __func__ << " finished!" << '\n';
        return curr->content;
    }

    void addContentToFile(string filePath, string content) {
        cout << __func__ << " entered!" << '\n';

        auto curr = root;
        int depth = 0;
        auto pathSplit = stringSplit(filePath, '/');
        // maxDepth - 2 as get parent dir add child file
        cout << filePath << ' ' << content << '\n';
        while (depth + 1 < pathSplit.size())
            for (auto child : curr->children)
                if (child->name == pathSplit[depth]) {
                    curr = child;
                    depth += 1;
                }

        cout << "curr->name: " << curr->name
             << " pathSplit[d]: " << pathSplit[depth] << '\n';

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
        cout << __func__ << " finished!" << '\n';
    }

    vector<string> stringSplit(string s, char delim = ' ') {
        cout << __func__ << " entered!" << '\n';
        if (s == "/") return vector<string>();
        vector<string> ret;
        int start, end;
        for (end = s.find(delim), start = 0; end != -1;
             start = end + 1, end = s.find(delim, start))
            ret.push_back(s.substr(start, end - start));
        ret.push_back(s.substr(start, end - start));
        if (ret.size() > 0) ret.erase(ret.begin());

        cout << __func__ << " finished!" << '\n';
        return ret;
    }
};