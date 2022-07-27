#include <stdio.h>
unsigned char S[256] = {             // S盒
	0x63,0x7C,0x77,0x7B,0xF2,0x6B,0x6F,0xC5,0x30,0x01,0x67,0x2B,0xFE,0xD7,0xAB,0x76,
	0xCA,0x82,0xC9,0x7D,0xFA,0x59,0x47,0xF0,0xAD,0xD4,0xA2,0xAF,0x9C,0xA4,0x72,0xC0,    
	0xB7,0xFD,0x93,0x26,0x36,0x3F,0xF7,0xCC,0x34,0xA5,0xE5,0xF1,0x71,0xD8,0x31,0x15,    
	0x04,0xC7,0x23,0xC3,0x18,0x96,0x05,0x9A,0x07,0x12,0x80,0xE2,0xEB,0x27,0xB2,0x75,    
	0x09,0x83,0x2C,0x1A,0x1B,0x6E,0x5A,0xA0,0x52,0x3B,0xD6,0xB3,0x29,0xE3,0x2F,0x84,    
	0x53,0xD1,0x00,0xED,0x20,0xFC,0xB1,0x5B,0x6A,0xCB,0xBE,0x39,0x4A,0x4C,0x58,0xCF,    
	0xD0,0xEF,0xAA,0xFB,0x43,0x4D,0x33,0x85,0x45,0xF9,0x02,0x7F,0x50,0x3C,0x9F,0xA8,    
	0x51,0xA3,0x40,0x8F,0x92,0x9D,0x38,0xF5,0xBC,0xB6,0xDA,0x21,0x10,0xFF,0xF3,0xD2,    
	0xCD,0x0C,0x13,0xEC,0x5F,0x97,0x44,0x17,0xC4,0xA7,0x7E,0x3D,0x64,0x5D,0x19,0x73,    
	0x60,0x81,0x4F,0xDC,0x22,0x2A,0x90,0x88,0x46,0xEE,0xB8,0x14,0xDE,0x5E,0x0B,0xDB,    
	0xE0,0x32,0x3A,0x0A,0x49,0x06,0x24,0x5C,0xC2,0xD3,0xAC,0x62,0x91,0x95,0xE4,0x79,    
	0xE7,0xC8,0x37,0x6D,0x8D,0xD5,0x4E,0xA9,0x6C,0x56,0xF4,0xEA,0x65,0x7A,0xAE,0x08,    
	0xBA,0x78,0x25,0x2E,0x1C,0xA6,0xB4,0xC6,0xE8,0xDD,0x74,0x1F,0x4B,0xBD,0x8B,0x8A,    
	0x70,0x3E,0xB5,0x66,0x48,0x03,0xF6,0x0E,0x61,0x35,0x57,0xB9,0x86,0xC1,0x1D,0x9E,    
	0xE1,0xF8,0x98,0x11,0x69,0xD9,0x8E,0x94,0x9B,0x1E,0x87,0xE9,0xCE,0x55,0x28,0xDF,   
	0x8C,0xA1,0x89,0x0D,0xBF,0xE6,0x42,0x68,0x41,0x99,0x2D,0x0F,0xB0,0x54,0xBB,0x16
	};
unsigned char IS[256] =  {                // S盒的逆
	0x52,0x09,0x6a,0xd5,0x30,0x36,0xa5,0x38,0xbf,0x40,0xa3,0x9e,0x81,0xf3,0xd7,0xfb,
	0x7c,0xe3,0x39,0x82,0x9b,0x2f,0xff,0x87,0x34,0x8e,0x43,0x44,0xc4,0xde,0xe9,0xcb,
	0x54,0x7b,0x94,0x32,0xa6,0xc2,0x23,0x3d,0xee,0x4c,0x95,0x0b,0x42,0xfa,0xc3,0x4e,
	0x08,0x2e,0xa1,0x66,0x28,0xd9,0x24,0xb2,0x76,0x5b,0xa2,0x49,0x6d,0x8b,0xd1,0x25,
	0x72,0xf8,0xf6,0x64,0x86,0x68,0x98,0x16,0xd4,0xa4,0x5c,0xcc,0x5d,0x65,0xb6,0x92,
	0x6c,0x70,0x48,0x50,0xfd,0xed,0xb9,0xda,0x5e,0x15,0x46,0x57,0xa7,0x8d,0x9d,0x84,
	0x90,0xd8,0xab,0x00,0x8c,0xbc,0xd3,0x0a,0xf7,0xe4,0x58,0x05,0xb8,0xb3,0x45,0x06,
	0xd0,0x2c,0x1e,0x8f,0xca,0x3f,0x0f,0x02,0xc1,0xaf,0xbd,0x03,0x01,0x13,0x8a,0x6b,
	0x3a,0x91,0x11,0x41,0x4f,0x67,0xdc,0xea,0x97,0xf2,0xcf,0xce,0xf0,0xb4,0xe6,0x73,
	0x96,0xac,0x74,0x22,0xe7,0xad,0x35,0x85,0xe2,0xf9,0x37,0xe8,0x1c,0x75,0xdf,0x6e,
	0x47,0xf1,0x1a,0x71,0x1d,0x29,0xc5,0x89,0x6f,0xb7,0x62,0x0e,0xaa,0x18,0xbe,0x1b,
	0xfc,0x56,0x3e,0x4b,0xc6,0xd2,0x79,0x20,0x9a,0xdb,0xc0,0xfe,0x78,0xcd,0x5a,0xf4,
	0x1f,0xdd,0xa8,0x33,0x88,0x07,0xc7,0x31,0xb1,0x12,0x10,0x59,0x27,0x80,0xec,0x5f,
	0x60,0x51,0x7f,0xa9,0x19,0xb5,0x4a,0x0d,0x2d,0xe5,0x7a,0x9f,0x93,0xc9,0x9c,0xef,
	0xa0,0xe0,0x3b,0x4d,0xae,0x2a,0xf5,0xb0,0xc8,0xeb,0xbb,0x3c,0x83,0x53,0x99,0x61,
	0x17,0x2b,0x04,0x7e,0xba,0x77,0xd6,0x26,0xe1,0x69,0x14,0x63,0x55,0x21,0x0c,0x7d
	};

void ShiftRows( unsigned char *b )     {  
	unsigned char t ;
	t = b[ 5] ;	b[ 5] = b[ 9] ;	b[ 9] = b[13] ;	b[13] = b[ 1] ;b[1]=t;
	t=b[2];b[ 2] = b[10] ;	b[10]=t;
    t=b[6];b[ 6] = b[14] ;	b[14] = t;
	t=b[3];b[ 3] = b[15] ;	b[15] = b[11] ;	b[11] = b[ 7] ;b[ 7] = t; 
} 
void InvShiftRows( unsigned char *b )     {      
	unsigned char t ;
	t = b[ 1] ;	b[ 1] = b[ 13] ;	b[ 13] = b[9] ;	b[9] = b[ 5] ;b[5]=t;
	t=b[2];b[ 2] = b[10] ;	b[10]=t;
    t=b[6];b[ 6] = b[14] ;	b[14] = t;
	t=b[7];b[ 7] = b[11] ;	b[11] = b[15] ;	b[15] = b[ 3] ;b[ 3] = t; 
} 

#define D(x) ( ((x)<<(1))^((((x)&0x80)?0xff:0)&0x1b))
#define MulE(x) ((D(D(D(x))))^(D(D(x)))^(D(x)))
#define MulB(x) ((D(D(D(x))))^(D(x))^(x))
#define MulD(x) ((D(D(D(x))))^(D(D(x)))^(x))
#define Mul9(x) ((D(D(D(x))))^(x))


unsigned char  round_key[11][16];

void keygen(unsigned char key[16],unsigned char round_key[11][16]){

    unsigned char rcon[10] = {0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36};
    for(int i=0;i<16;i++)
    {
        round_key[0][i]=key[i];
    }
    for(int i=1;i<11;i++)
	{
	    round_key[i][0]=round_key[i-1][0]^S[round_key[i-1][13]]^rcon[i-1];
		round_key[i][1]=round_key[i-1][1]^S[round_key[i-1][14]];
		round_key[i][2]=round_key[i-1][2]^S[round_key[i-1][15]];
		round_key[i][3]=round_key[i-1][3]^S[round_key[i-1][12]];
        for(int j=4;j<16;j++)
	    {
            round_key[i][j]=round_key[i-1][j]^round_key[i][j-4];
        }   
    }
}
/*
void InvMixColumns(unsigned char *a)   
{
	unsigned char b[16];
	b[0] = MulE(tmp[0]) ^ MulB(tmp[1]) ^ MulD(tmp[2]) ^ Mul9(tmp[3]);
	b[1] = MulE(tmp[1]) ^ MulB(tmp[2]) ^ MulD(tmp[3]) ^ Mul9(tmp[0]);
	b[2] = MulE(tmp[2]) ^ MulB(tmp[3]) ^ MulD(tmp[0]) ^ Mul9(tmp[1]);
	b[3] = MulE(tmp[3]) ^ MulB(tmp[0]) ^ MulD(tmp[1]) ^ Mul9(tmp[2]);
	b[4] = MulE(tmp[4]) ^ MulB(tmp[5]) ^ MulD(tmp[6]) ^ Mul9(tmp[7]);
	b[5] = MulE(tmp[5]) ^ MulB(tmp[6]) ^ MulD(tmp[7]) ^ Mul9(tmp[4]);
	b[6] = MulE(tmp[6]) ^ MulB(tmp[7]) ^ MulD(tmp[4]) ^ Mul9(tmp[5]);
	b[7] = MulE(tmp[7]) ^ MulB(tmp[4]) ^ MulD(tmp[5]) ^ Mul9(tmp[6]);
	b[8] = MulE(tmp[8]) ^ MulB(tmp[9]) ^ MulD(tmp[10]) ^ Mul9(tmp[11]);
	b[9] = MulE(tmp[9]) ^ MulB(tmp[10]) ^ MulD(tmp[11]) ^ Mul9(tmp[8]);
	b[10] = MulE(tmp[10]) ^ MulB(tmp[11]) ^ MulD(tmp[8]) ^ Mul9(tmp[9]);
	b[11] = MulE(tmp[11]) ^ MulB(tmp[8]) ^ MulD(tmp[9]) ^ Mul9(tmp[10]);
	b[12] = MulE(tmp[12]) ^ MulB(tmp[13]) ^ MulD(tmp[14]) ^ Mul9(tmp[15]);
	b[13] = MulE(tmp[13]) ^ MulB(tmp[14]) ^ MulD(tmp[15]) ^ Mul9(tmp[12]);
	b[14] = MulE(tmp[14]) ^ MulB(tmp[15]) ^ MulD(tmp[12]) ^ Mul9(tmp[13]);
	b[15] = MulE(tmp[15]) ^ MulB(tmp[12]) ^ MulD(tmp[13]) ^ Mul9(tmp[14]);
	for (int i = 0; i < 16; i++)
		a[i] = b[i];
}
*/
void AES_enc(unsigned char round_key[11][16],
             unsigned char plaintext[16],
             unsigned char ciphertext[16]){

    unsigned char tmp[16];
    for(int i=0;i<16;i++)
    {
        tmp[i]=round_key[0][i]^plaintext[i];
    }

    for(int round=1;round<10;round++)
    {
        for(int j=0;j<16;j++)
        {
            tmp[j]=S[tmp[j]];
        }
        ShiftRows(tmp);
    	unsigned char b[16] ;
    	b[ 0] = D(tmp[0]) ^ D(tmp[1])^tmp[1] ^ tmp[2] ^ tmp[3];
    	b[ 1] = D(tmp[1]) ^ D(tmp[2])^tmp[2] ^ tmp[3] ^ tmp[0];
    	b[ 2] = D(tmp[2]) ^ D(tmp[3])^tmp[3] ^ tmp[0] ^ tmp[1];
    	b[ 3] = D(tmp[3]) ^ D(tmp[0])^tmp[0] ^ tmp[1] ^ tmp[2];
    	b[ 4] = D(tmp[4]) ^ D(tmp[5])^tmp[5] ^ tmp[6] ^ tmp[7];
    	b[ 5] = D(tmp[5]) ^ D(tmp[6])^tmp[6] ^ tmp[7] ^ tmp[4];
    	b[ 6] = D(tmp[6]) ^ D(tmp[7])^tmp[7] ^ tmp[4] ^ tmp[5];
    	b[ 7] = D(tmp[7]) ^ D(tmp[4])^tmp[4] ^ tmp[5] ^ tmp[6];
    	b[ 8] = D(tmp[8]) ^ D(tmp[9])^tmp[9] ^ tmp[10] ^ tmp[11];
    	b[ 9] = D(tmp[9]) ^ D(tmp[10])^tmp[10] ^ tmp[11] ^ tmp[8];
    	b[10] = D(tmp[10]) ^ D(tmp[11])^tmp[11] ^ tmp[8] ^ tmp[9];
    	b[11] = D(tmp[11]) ^ D(tmp[8])^tmp[8] ^ tmp[9] ^ tmp[10];
    	b[12] = D(tmp[12]) ^ D(tmp[13])^tmp[13] ^ tmp[14] ^ tmp[15];
    	b[13] = D(tmp[13]) ^ D(tmp[14])^tmp[14] ^ tmp[15] ^ tmp[12];
    	b[14] = D(tmp[14]) ^ D(tmp[15])^tmp[15] ^ tmp[12] ^ tmp[13];
    	b[15] = D(tmp[15]) ^ D(tmp[12])^tmp[12] ^ tmp[13] ^ tmp[14];
        for(int i=0;i<16;i++) tmp[i]=b[i];
        for(int i=0;i<16;i++)
        {
            tmp[i]=round_key[round][i]^tmp[i];
        } 
    
    }

        for(int j=0;j<16;j++)
        {
            tmp[j]=S[tmp[j]];
        }
        ShiftRows(tmp);
        for(int i=0;i<16;i++)
        {
            ciphertext[i]=round_key[10][i]^tmp[i];
        }

}

void AES_dec(unsigned char round_key[11][16],
             unsigned char ciphertext[16],
             unsigned char plaintext[16]){

    unsigned char tmp[16];
    for(int i=0;i<16;i++)
    {
        tmp[i]=round_key[10][i]^ciphertext[i];
    }
    InvShiftRows(tmp);
    for(int j=0;j<16;j++)
    {
        tmp[j]=IS[tmp[j]];
    }
    for(int round=9;round>0;round--)
    {
        
        for(int i=0;i<16;i++)
        {
            tmp[i]=round_key[round][i]^tmp[i];
        } 
    	unsigned char b[16];
    	b[0] = MulE(tmp[0]) ^ MulB(tmp[1]) ^ MulD(tmp[2]) ^ Mul9(tmp[3]);
    	b[1] = MulE(tmp[1]) ^ MulB(tmp[2]) ^ MulD(tmp[3]) ^ Mul9(tmp[0]);
    	b[2] = MulE(tmp[2]) ^ MulB(tmp[3]) ^ MulD(tmp[0]) ^ Mul9(tmp[1]);
    	b[3] = MulE(tmp[3]) ^ MulB(tmp[0]) ^ MulD(tmp[1]) ^ Mul9(tmp[2]);
    	b[4] = MulE(tmp[4]) ^ MulB(tmp[5]) ^ MulD(tmp[6]) ^ Mul9(tmp[7]);
    	b[5] = MulE(tmp[5]) ^ MulB(tmp[6]) ^ MulD(tmp[7]) ^ Mul9(tmp[4]);
    	b[6] = MulE(tmp[6]) ^ MulB(tmp[7]) ^ MulD(tmp[4]) ^ Mul9(tmp[5]);
    	b[7] = MulE(tmp[7]) ^ MulB(tmp[4]) ^ MulD(tmp[5]) ^ Mul9(tmp[6]);
    	b[8] = MulE(tmp[8]) ^ MulB(tmp[9]) ^ MulD(tmp[10]) ^ Mul9(tmp[11]);
    	b[9] = MulE(tmp[9]) ^ MulB(tmp[10]) ^ MulD(tmp[11]) ^ Mul9(tmp[8]);
    	b[10] = MulE(tmp[10]) ^ MulB(tmp[11]) ^ MulD(tmp[8]) ^ Mul9(tmp[9]);
    	b[11] = MulE(tmp[11]) ^ MulB(tmp[8]) ^ MulD(tmp[9]) ^ Mul9(tmp[10]);
    	b[12] = MulE(tmp[12]) ^ MulB(tmp[13]) ^ MulD(tmp[14]) ^ Mul9(tmp[15]);
    	b[13] = MulE(tmp[13]) ^ MulB(tmp[14]) ^ MulD(tmp[15]) ^ Mul9(tmp[12]);
    	b[14] = MulE(tmp[14]) ^ MulB(tmp[15]) ^ MulD(tmp[12]) ^ Mul9(tmp[13]);
    	b[15] = MulE(tmp[15]) ^ MulB(tmp[12]) ^ MulD(tmp[13]) ^ Mul9(tmp[14]);
    	for (int i = 0; i < 16; i++)
    		tmp[i] = b[i];
        InvShiftRows(tmp);
        for(int j=0;j<16;j++)
        {
            tmp[j]=IS[tmp[j]];
        }

        

    }
        for(int i=0;i<16;i++)
        {
            plaintext[i]=round_key[0][i]^tmp[i];
        }

}

    unsigned char key[16]={1,0};
    unsigned char in[16]={1,2,3,4,0};
    unsigned char out[16]={0};
void inc32(unsigned char a)
{
    return;
}
void GCTR(unsigned char key[16],int byteslen,unsigned char nonce[16],
        unsigned char* plaintext,unsigned char* ciphertext)
{
    keygen(key,round_key);
    for(int i=0;i<byteslen;i+=16)
    {
        AES_enc(round_key,nonce,ciphertext+i);
        inc32(nonce);
        for(int j=i;j<byteslen;j++)
        {
            ciphertext[j]^=plaintext[j];
        }
    }

}
void mul(unsigned char *a,unsigned char* b);
void GHASH(unsigned char *text,int len,unsigned char* H,unsigned char ans[16])
{
    for(int i=0;i<16;i++)ans[i]=0;
    for(int i=0;i<len;i+=16)
    {
        for(int j=0;j+i<len&&j<16;j++)
        {
            ans[j]^=text[j+i];
        }
        mul(ans,H);
    }
}

void AES_GCM(unsigned char *AAD,int AADlen,
             unsigned char* plaintext,int textlen,
             unsigned char *tag,int taglen,
             unsigned char nonce,int noncelen)
{
    if(noncelen==12)
    {
        //J0=nonce;
    }
    else
    {
      //  J0=GHASH(nonce);
    }
}
int main(int argc, char *argv[])
{
    

    keygen(key,round_key);
    AES_enc(round_key,in,out);
    for(int i=0;i<16;i++)
    {
        printf("%02x ",out[i]);
    }
    printf("\n");
    AES_dec(round_key,out,out);
    for(int i=0;i<16;i++)
    {
        printf("%02x ",out[i]);
    }
    return 0;
}
