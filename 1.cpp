#include<bits/stdc++.h>
using namespace std;
class panchayat;
class subdivision;
class block;
std::vector<panchayat> vec;
std::vector<subdivision> vecs;
std::vector<block> vecb;
class subdivision
{
string name;
long long int popl_sub,no_of_blocks,avg_in_sub;
public:
	void entersub()
	{

		cin.clear();
		cin.ignore(std::numeric_limits<std::streamsize>::max(),'\n');
		cout<<"\nENTER THE NAME OF THE SUBDIVISION:\n";
		getline(cin,name);
		cout<<"\nENTER POPULLATION OF THE SUB DIVISION:\n";
		cin>>popl_sub;
		cout<<"\nENTER THE NO. OF BLOCKS IN THE SUB DIVISION: \n";
		cin>>no_of_blocks;
		cout<<"\nENTER THE AVERAGE INCOME OF THE SUBDISION\n";
		cin>>avg_in_sub;
	}
	void show_sub()
	{
		cout<<name<<" "<<popl_sub<<" "<<no_of_blocks<<" "<<avg_in_sub<<endl;
	}
void writeToObjects(vector<string> &vecs)
	{
		int j=1;
		for(int i=0;i<vecs.size();i++,j++)
		{
           if(j==1)
           	name=vecs[i];
           else if(j==2)
           	popl_sub=atoi(vecs[i].c_str());
           else if(j==3)
           	no_of_blocks=atoi(vecs[i].c_str());
           else
           avg_in_sub=atoi(vecs[i].c_str());
		}
	}
	friend void deletedatas();
	friend void editdatas();
	friend void searcheds();
	friend void writeDatas();
}obs;
void writeDatas()
{
	ofstream outx;
	outx.open("subdivision.csv");
	for (std::vector<subdivision>::iterator it = vecs.begin() ; it != vecs.end(); ++it)
	         	outx<<(*it).name<<","<<(*it).popl_sub<<","<<(*it).no_of_blocks<<","<<(*it).avg_in_sub<<"\n";	

}
void searcheds()
{
	cout<<"\nENTER THE subdivision TO BE SEARCHED:\n";
	string s;
	cin>>s;
		int c=0;
        for (std::vector<subdivision>::iterator it = vecs.begin() ; it != vecs.end(); ++it)
	    {
	    	
      if((*it).name==s)
      {
      	cout<<(*it).name<<","<<(*it).popl_sub<<","<<(*it).no_of_blocks<<","<<(*it).avg_in_sub<<"\n";
      	c=1;    
      }  
}
 if(c==1)
      	cout<<"\nsearch successful\n";
      else
      	cout<<"\nsearch unsuccessful\n";
      	}
void deletedatas()
{
	string del;
	cout<<"\nENTER THE NAME OF THE subdivision TO BE DELETED\n";
	cin>>del;
	int c=0;
	 for (std::vector<subdivision>::iterator it = vecs.begin() ; it != vecs.end(); ++it)
	    {
      if((*it).name==del)
      {
      	vecs.erase(vecs.begin() + c);
      }
      c++;
      
  }
  writeDatas();
}
void show_ds()
{

	for (std::vector<subdivision>::iterator it = vecs.begin() ; it != vecs.end(); ++it)
	{
		
		cout<<"\n\n";
      (*it).show_sub();
	}
}
class block
{
string name;
long long int popl_block,no_of_panchayat,avg_in_block;
public:

friend void deletedatab();
friend void editdatab();
friend void searchedb();
friend void writeDatab();
void enterblock()
{

		cin.clear();
		cin.ignore(std::numeric_limits<std::streamsize>::max(),'\n');
		cout<<"\nENTER THE NAME OF THE block:\n";
		getline(cin,name);
		cout<<"\nENTER POPULLATION OF THE block:\n";
		cin>>popl_block;
		cin.clear();
		cin.ignore(std::numeric_limits<std::streamsize>::max(),'\n');
		cout<<"\nENTER THE no. of panchayat IN block: \n";
		cin>>no_of_panchayat;
		cin.clear();
		cin.ignore(std::numeric_limits<std::streamsize>::max(),'\n');
		cout<<"\nENTER THE AVERAGE INCOME OF THE block\n";
		cin>>avg_in_block;
}
void showblock()
{
cout<<name<<" "<<popl_block<<" "<<no_of_panchayat<<" "<<avg_in_block<<endl;
}
	
void writeToObjectb(vector<string> &vecs)
{
	int j=1;
	for(int i=0;i<vecs.size();i++,j++)
	{
        if(j==1)
          name=vecs[i];
        else if(j==2)
          popl_block=atoi(vecs[i].c_str());
        else if(j==3)
          no_of_panchayat=atoi(vecs[i].c_str());
        else
         avg_in_block=atoi(vecs[i].c_str());
	}
}


}obb;
void writeDatab()
{
	ofstream outf;
	outf.open("block.csv");
	for (std::vector<block>::iterator it = vecb.begin() ; it != vecb.end(); ++it)
	         	outf<<(*it).name<<","<<(*it).popl_block<<","<<(*it).no_of_panchayat<<","<<(*it).avg_in_block<<"\n";	

}
void searchedb()
{
	cout<<"\nENTER THE block TO BE SEARCHED:\n";
	string s;
	cin>>s;
		int c=0;
        for (std::vector<block>::iterator it = vecb.begin() ; it != vecb.end(); ++it)
	    {
      if((*it).name==s)
      {
      	cout<<(*it).name<<","<<(*it).popl_block<<","<<(*it).no_of_panchayat<<","<<(*it).avg_in_block<<"\n";	
      	c=1;    
      }  
}
 if(c==1)
      	cout<<"\nsearch successful\n";
      else
      	cout<<"\nsearch unsuccessful\n";
      	}
void deletedatab()
{
	string del;
	cout<<"\nENTER THE NAME OF THE subdivision TO BE DELETED\n";
	cin>>del;
	int c=0;
	 for (std::vector<block>::iterator it = vecb.begin() ; it != vecb.end(); ++it)
	    {
      if((*it).name==del)
      {
      	vecb.erase(vecb.begin() + c);
      }
      c++;
      
  }
  writeDatab();
}
void show_db()
{

	for (std::vector<block>::iterator it = vecb.begin() ; it != vecb.end(); ++it)
	{
		cout<<"\n\n";
      (*it).showblock();
	}
}
class panchayat
{

	long int popl,avg_income;
	string pname,inso,aq,sub,block;
public:
	void enter()
	{
		cin.clear();
		cin.ignore(std::numeric_limits<std::streamsize>::max(),'\n');
		cout<<"\nENTER THE NAME OF THE PANCHAYAT:\n";
		getline(cin,pname);
		cout<<"\nENTER THE SUBDISION UNDER WHICH THIS PANCHAYAT COMES\n";
		getline(cin,sub);
		cout<<"\nENTER THE BLOCK UNDER WHICH THIS PANCHAYAT COMES\n";
		getline(cin,block);
		cout<<"\nENTER POPULLATION:\n";
		cin>>popl;
		cin.clear();
		cin.ignore(std::numeric_limits<std::streamsize>::max(),'\n');
		cout<<"\nENTER THE INCOME SOURCE: \n";
		getline(cin,inso);
		cout<<"\nENTER THE AVERAGE QUALIFICATION\n";
		getline(cin,aq);
		cout<<"\nENTER THE AVERAGE INCOME OF THE PANCHAYAT\n";
		cin>>avg_income;
	}
	void show()
	{
      cout<<pname<<" "<<sub<<" "<<block<<" "<<popl<<" "<<inso<<" "<<aq<<" "<<avg_income<<endl;
	}
	void writeToObject(vector<string> &vec)
	{
		int j=1;
		for(int i=0;i<vec.size();i++,j++)
		{
           if(j==1)
           	pname=vec[i];
           else if(j==2)
           	sub=vec[i];
           else if(j==3)
           	block=vec[i];
           else if(j==4)
           popl=atoi(vec[i].c_str());
           else if(j==5)
           	inso=vec[i];
           else if(j==6)
           	aq=vec[i];
           else
           	avg_income=atoi(vec[i].c_str());
		}
	}
    friend void deletedata();
	friend void editdata();
	friend void searched();
	friend void writeData();
	
}obj;
void searched()
{
		cout<<"\nENTER THE PANCHAYAT TO BE SEARCHED:\n";
	string s;
	cin>>s;
		int c=0;
        for (std::vector<panchayat>::iterator it = vec.begin() ; it != vec.end(); ++it)
	    {
      if((*it).pname==s)
      {
      	cout<<(*it).pname<<"\t,\t"<<(*it).sub<<"\t,\t"<<(*it).block<<"\t,\t"<<(*it).popl<<"\t,\t"<<(*it).inso<<"\t,\t"<<(*it).aq<<"\t,\t"<<(*it).avg_income<<"\n";	
      	c=1;    
      }  
  }
      	   if(c==1)
      	cout<<"\nsearch successful\n";
      else
      	cout<<"\nsearch unsuccessful\n";
}

void writeData()
{
	ofstream outf;
	outf.open("PANCHAYAT.csv");
	for (std::vector<panchayat>::iterator it = vec.begin() ; it != vec.end(); ++it)
	         	outf<<(*it).pname<<","<<(*it).sub<<","<<(*it).block<<","<<(*it).popl<<","<<(*it).inso<<","<<(*it).aq<<","<<(*it).avg_income<<"\n";	

}
void deletedata()
{
	string del;
	cout<<"\nENTER THE NAME OF THE PANCHAYAT TO BE DELETED\n";
	cin>>del;
	int c=0;
	 for (std::vector<panchayat>::iterator it = vec.begin() ; it != vec.end(); ++it)
	    {
      if((*it).pname==del)
      {
      	vec.erase(vec.begin() + c);
      }
      c++;
      
  }
  writeData();
}
template<typename Out>
void split(const std::string &s, char delim, Out result) {
    std::stringstream ss(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        *(result++) = item;
    }
}

void split(const std::string &s, std::vector<std::string> &elems,char delim) {
    split(s, delim, std::back_inserter(elems));
}

  void readf()
  {

	ifstream x("PANCHAYAT.csv");
	char z[100];
	while(x.getline(z,100))
	{
		string s;
		for(int i=0;z[i]!='\0';i++)
			s.push_back(z[i]);
		std::vector<string> v;
		split(s,v,',');
		obj.writeToObject(v);
		vec.push_back(obj);
	}
  }
  void readfs()
  {

	ifstream x("subdivision.csv");
	char z[100];
	while(x.getline(z,100))
	{
		string s;
		for(int i=0;z[i]!='\0';i++)
			s.push_back(z[i]);
		std::vector<string> v;
		split(s,v,',');
		obs.writeToObjects(v);
		vecs.push_back(obs);
	}
  }
void show()
{

	for (std::vector<panchayat>::iterator it = vec.begin() ; it != vec.end(); ++it)
	{
		cout<<"\n\n";
      (*it).show();
	}

	//x.close();
	//cout<<"ENTER THE PANCHAYAT TO BE SEARCHED:\n";
	//string s;
	//cin>>s;
	//searched(s);
}
class users
{
	public:
	virtual void showd(){}
	virtual void search(){}
	virtual void entered(){ }
	virtual void deleted(){ }
	virtual void showds(){}
	virtual void searchs(){}
	virtual void entereds(){ }
	virtual void deleteds(){ }
	virtual void showdb(){}
	virtual void searchb(){}
	virtual void enteredb(){ }
	virtual void deletedb(){ }
};
class admin:public users
{
public:
	void entered()
	{
		obj.enter();
	}
	void showd()
	{
		show();
	}
	void search()
	{
		searched();
	}
	void deleted()
	{
		deletedata();
	}
	void entereds()
	{
		obs.entersub();
	}
	void showds()
	{
		show_ds();
	}
	void searchs()
	{
		searcheds();
	}
	void deleteds()
	{
		deletedatas();
	}
	void enteredb()
	{
		obb.enterblock();
	}
	void showdb()
	{
		show_db();
	}
	void searchb()
	{
		searchedb();
	}
	void deletedb()
	{
		deletedatab();
	}
};

class people:public users
{
       void showd()
	{
		obj.show();
	}
	void search()
	{
		searched();
	}
	void showds()
	{
		obs.show_sub();
	}
	void searchs()
	{
		searcheds();
	}
	void showdb()
	{
		obb.showblock();
	}
	void searchb()
	{
		searchedb();
	}
};

int main()
{
	   int x;
	   readf();
	   readfs();
	    int i=1;
	  while(i)
	  {
	   cout<<"   \n    DATABASE FOR A SOCIO ECONOMIC SURVEY OF BHUBANESWAR DISTRICT OF ODHISHA\n\n";
       cout<<" ENTER CHOICE TO LOGIN:\n\n";
       cout<<"1. ADMIN\n\n2. NORMAL PUBLIC\n\n";
      cout<<"-->";
       cin>>x;
       if(x==1)
       {
       	int y;
	  users  *ptr= new admin;
	  cout<<" \nENTER YoUR CHOICE:\n\n";
       cout<<"\n1. ENTER A NEW PANCHAYAT\n\n2. SHOW DETAILS OF ALL PANCHAYATS\n\n3. TO SEARCH A PANCHAYAT IN FILE\n\n4. TO DELDTE A PANCHAYAT\n\n5. ENTER A NEW subdivision\n\n2. SHOW DETAILS OF ALL subdivision\n\n3. TO SEARCH A subdivision IN FILE\n\n4. TO DELDTE A subdivision\n";
       cout<<"\n9. ENTER A NEW block\n\n10. SHOW DETAILS OF ALL blocks\n\n11. TO SEARCH A block IN FILE\n\n12. TO DELDTE A block\n";
       cout<<"\n-->";
       cin>>y;
       switch(y)
       {
       case 1:
       {
	   		ptr->entered();
	   		vec.push_back(obj);
	   		break;
	   }
      case 2:
      	{
      		int n;
      		ptr->showd();
      		break;
      	}
      	case 3:
      	{
      			ptr->search();
      			break;
      	}
      	case 4:
      	{
      		ptr->deleted();
      		break;
      	}
      	case 5:
       {
	   		ptr->entereds();
	   		vecs.push_back(obs);
	   		break;
	   }
      case 6:
      	{
      		int n;
      		ptr->showds();
      		break;
      	}
      	case 7:
      	{
      			ptr->searchs();
      			break;
      	}
      	case 8:
      	{
      		ptr->deleteds();
      		break;
      	}
      	  case 9:
       {
	   		ptr->enteredb();
	   		vecb.push_back(obb);
	   		break;
	   }
      case 10:
      	{
      		int n;
      		ptr->showdb();
      		break;
      	}
      	case 11:
      	{
      			ptr->searchb();
      			break;
      	}
      	case 12:
      	{
      		ptr->deletedb();
      		break;
      	}
      	default:
      	cout<<"wrong choice\n";
      }

     }
   if(x==2)
    {
   cout<<"\n1. SHOW DETAILS OF ALL PANCHAYATS\n\n2. TO SEARCH A PANCHAYAT IN FILE\n3. SHOW DETAILS OF ALL subdivision\n\n4. TO SEARCH A subdivision IN FILE";
        int n;
        cin>>n;
      	users  *ptr= new people;
      	switch(n)
      	{
      	case 1:{
      	ptr->showd();
          break;
         }
      	case 2:{
      	    ptr->search();
      	    break;
      	}
      	case 3:{
      	ptr->showds();
           break;
       }
      	case 4:{
      	    ptr->searchs();
      	    break;
      	}
      	case 5:{
      	ptr->showdb();
          break;
         }
      	case 6:{
      	    ptr->searchb();
      	    break;
      	}
          default:
          cout<<"wrong choice";
        }
    }
    cout<<"PRESS 1 TO CONTINUE & PRESS 0 TO EXIT\n";
    cin>>i;
     }
     writeData();
     writeDatab();
     writeDatas();
}