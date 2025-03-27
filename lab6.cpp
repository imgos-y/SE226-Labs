/*#include <iostream>
using namespace std;

int recursiveSum(int n) {
    if (n == 0)
        return 0;
    return n + recursiveSum(n - 1);
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    int result = recursiveSum(n);
    cout << "Sum from 1 to " << n << " is: " << result << endl;
    return 0;
}*\
 // question5
#include <iostream>
using namespace std;


int recursiveSum(int n) {
    if (n == 0)
        return 0;
    return n + recursiveSum(n - 1);
}


int recursiveSum() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    return recursiveSum(n);  
}

int main() {
    int result = recursiveSum();  
    cout << "Sum is: " << result << endl;
    return 0;
}
