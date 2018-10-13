#include<bits/stdc++.h>
using namespace std;
class BST{
private:
struct Node{
	int data;
	Node*left;
	Node*right;
};Node*root;
public:
	BST(){
		root=NULL;
	}
bool isempty();
void insert(int);
void remove(int);
void inorder(Node*);
void preorder(Node*);
void postorder(Node*);
void print_inorder();
void print_preorder();
void print_postorder();

};
bool BST::isempty(){
	return (root==NULL);
}
void BST::insert(int data){
		Node*temp=new Node;
		Node*parent;
		temp->data=data;
		temp->left=NULL;
		temp->right=NULL;
		if(isempty())
		root=temp;
		else
		{
			Node*current=new Node;
			while(current){
				parent=current;
				if(temp->data>current->data)
				current=current->right;
				else
				current=current->left;
			}
			if(temp->data>parent->data)
			parent->right=temp;
			else
			parent->left=temp;
		}

}
void BST::remove(int data){
	bool found=false;
	if(isempty())
	{
		cout<<"This tree is empty"<<endl;
		return;
	}
	Node*current;
	Node*parent;
	current=root;
	while(current!=NULL)
	{
		if(current->data==data){
			found=true;
			break;
		}
		else{
			parent=current;
			if(data>current->data)
			current=current->right;
			else
			current=current->left;
		}}
		if(!found)
		{cout<<"Data does not exist in tree"<<endl;	return;
	}
	if(current->right==NULL&&current->left!=NULL||current->right!=NULL&&current->left==NULL){
		
	if(current->right!=NULL&&current->left==NULL){
	
		if(parent->left=current)
		{
			parent->left=current->right;
			delete current;
		}
		else
		{
			parent->right=current->right;
			delete current;
		}
	}else
	{
			if(parent->left=current)
		{
			parent->left=current->left;
			delete current;
		}
			else
		{
			parent->right=current->left;
			delete current;
		}
	}
	}
	if(current->right==NULL&&current->left==NULL){
		
		if(parent->right==current)parent->right==NULL;
		else
		parent->left=NULL;
		
		delete current;
		return;
	}
	
	if(current->left!=NULL&&current->right!=NULL)
	{
			Node*cod=new Node;
		cod=current->right;
		
		if(cod->left==NULL&&cod->right==NULL){
			current=cod;
			delete cod;
			current->right=NULL;
		}
		else{
			if((current->right)->left!=NULL){
				Node*lcurr;
				Node*lcurrp;
				lcurrp=current->right;
				lcurr=(current->right)->left;
				while(current->left!=NULL){
					lcurrp=lcurr;
					lcurr=lcurr->left;
				}
				
				current->data=lcurr->data;
				delete lcurr;
				lcurrp->left=NULL;
			}else
			{
				Node*temp;
				temp=current->right;
				current->data=temp->data;
				current->right=temp->right;
				delete temp;
			}
			
		}
		return;
	}
			
}
void BST::inorder(Node* p){

	if(p!=NULL){
		
		inorder(p->left);
		cout<<p->data<<" "<<endl;
		inorder(p->right);
		
	}
}
void BST::preorder(Node*p){
	
	if(p!=NULL){
		cout<<p->data<<" "<<endl;
		inorder(p->left);
		
		inorder(p->right);
		
	}
}
void BST::postorder(Node*p){
		
	if(p!=NULL){
	
		inorder(p->left);
		inorder(p->right);
			cout<<p->data<<" "<<endl;
	}
}
void BST::print_inorder(){
	inorder(root);
}
void BST::print_preorder(){
	preorder(root);
}
void BST::print_postorder(){
	postorder(root);
}
int main(){
	int data;
	BST tree;
	int choice;
	cout<<"1.insert"<<endl;
	cout<<"2.delete"<<endl;
	cout<<"3.inorder"<<endl;
	cout<<"4.post-order"<<endl;
	cout<<"5.pre-order"<<endl;
	while(1){
		cout<<"enter choice"<<endl;
		cin>>choice;
		switch(choice){
			case 1:
				cout<<"what to insert";
				cin>>data;
				tree.insert(data);
				break;
				case 2:
					cout<<"what to delete";
					cin>>data;
					tree.remove(data);
				break;
				case 3:
					tree.print_inorder();
					break;
					case 4:
						tree.print_postorder();
						break;
						case 5:
							tree.print_preorder();
							break;
					
		}
		
	}
}
