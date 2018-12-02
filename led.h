#ifndef LED_H
#define LED_H
#include <string>
#include <iostream>
using namespace std;

class Image {
	unsigned char* im;
	public:
		Image(unsigned char* _val) : im(_val) {}
		unsigned char* getChar() const{
					 return im;
		}
		static Image CROSS();
		static Image SQUARE();
		static Image CIRCLE();
		static Image TRIANGLE();
		static Image FULL();
		static Image BLANK();
};
class Led_Writer{
  public:
    Led_Writer();
    ~Led_Writer();
    void write(const Image& left, const Image& right);
    void write(int valL=LOW,int valR=LOW);
  private:  
    unsigned char* getChar(int val);
    void writeHelp(unsigned char*, unsigned char*);
};
#endif
