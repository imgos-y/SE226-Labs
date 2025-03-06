#include <iostream>
#include <new>

using namespace std;


class Element {
public:
    int data;
     Element *next;

    Element (int d, Element *n)
    {
        data = d;
        next = n;
    }
};
class Queue{
private:
    Element* back;
    Element* front;

public:
    Queue(){
    back = nullptr;
    front = nullptr;

    }

    bool isEmpty() {
     return front == nullptr;
    }

    void enqueue(int input) {

            if(isEmpty()){

            front=new Element(input, nullptr);
            back=front;
            }

            else {
            back->next=new Element(input, nullptr);
            back=back->next;
            }
    }


    void dequeue(){
    if(!isEmpty()){
        Element *temp = front;
        if (front == back){
            front = nullptr;
            back = nullptr;
        } else {
            front = front->next;
        }
        delete temp;
    }
 }


     void print() {
        Element *p;
        for(p=front; p!=nullptr; p=p->next) {
            cout<<p->data<<" ";
        }
        cout << endl;
    }

    int size() {
        Element* p;
        int counter = 0;
        for(p=front; p!=nullptr; p=p->next) {
        counter++;
        }

        return counter;
    }

   int top() {
    if (isEmpty()) {
        cerr << "Queue is empty!" << endl;

        return -1;
    }
    return front->data;
}

};

int main()
{
    Queue *q = new Queue();

    cout<< "this is my list: "<<endl;
    cout<< "Size of the list "<< endl;
    cout<< "Top of the Values"<< endl;

    cout<< "Last list: "<<endl;
    cout<<endl;
    cout<< "--------------------------" << endl;


    // cout<<q->top();      kuyruk boş olursa top methodunda hata mesajı veriyo -1 çıktı alınıyo

    cout<<endl;

    q->enqueue(11);
    q->enqueue(12);
    q->enqueue(13);
    q->enqueue(14);
    q->enqueue(15);
    q->enqueue(16);

    q->dequeue();

    q->print();

    cout<<q->size();

    cout<<endl;

    cout<<endl;

    q->dequeue();

    q->print();

    return 0;
}

