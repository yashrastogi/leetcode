#define vi vector<int>

class ProductOfNumbers {
private:
    vi data;
    void init() { data = vi(1, 1); }
public:
    ProductOfNumbers() { init(); }
    
    void add(int num) {
        if(num == 0) {
            init();
        } else {
            data.push_back(data.back() * num);
        }
    }
    
    int getProduct(int k) {
        if(data.size() > k) {
            return data.back() / data[data.size() - k - 1];
        } else {
            return 0;
        }
    }
};

/*
    auto p = ProductOfNumbers();
    p.add(1);
    p.getProduct();
    
 */