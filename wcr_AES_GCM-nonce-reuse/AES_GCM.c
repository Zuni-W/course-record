#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
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


    unsigned char key[16]={0x9c,0x98,0xc0,0x4d,0xf9,0x38,0x7d,0xed,0x82,0x81,0x75,0xa9,0x2b,0xa6,0x52,0xd8};
//    unsigned char key[16]={0x66,0xe9,0x4b,0xd4,0xef,0x8a,0x2c,0x3b,0x88,0x4c,0xfa,0x59,0xca,0x34,0x2b,0x2e};
    unsigned char in[16]={0x40,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0};
    unsigned char out[16]={0};
void inc32(unsigned char *a)
{
    a[15]+=1;
    for(int i=15;i>=13;i--)
    {
        if (a[i]==0)
        a[i-1]+=1;
        else
            break;
    }
    return;
}
void GCTR(unsigned char key[16],int byteslen,unsigned char nonce[16],
        unsigned char* plaintext,unsigned char* ciphertext)
{
    unsigned char p[byteslen];
    for(int i=0;i<byteslen;i++)
    {
        p[i]=plaintext[i];
    }
    unsigned char round_key[11][16];
    keygen(key,round_key );
    for(int i=0;i<byteslen;i+=16)
    {
        AES_enc(round_key,nonce,ciphertext+i);
        *(unsigned int*)nonce+=1;//inc32(nonce);
        for(int j=i;j<byteslen;j++)
        {
            ciphertext[j]^=p[j];
        }
    }

}
void GCTR_SIV(unsigned char key[16],int byteslen,unsigned char nonce[16],
        unsigned char* plaintext,unsigned char* ciphertext)
{
    unsigned char round_key[11][16];
    keygen(key,round_key );
    unsigned char bitskey[16]={0};
    printf("nonce:");
    for(int i=0;i<16;i++)
    {
        printf("%02x ",nonce[i]);
    }
    printf("\n");
    for(int i=0;i<byteslen;i+=16)
    {
        AES_enc(round_key,nonce,bitskey);
        *(unsigned int*)nonce+=1;//inc32(nonce);
        printf("keybits: ");
        for(int j=0;i+j<byteslen&&j<16;j++)
        {
            ciphertext[i+j]=bitskey[j]^plaintext[i+j];
            printf("%02x ",bitskey[j]);
        }
        printf("\n");
    }

}
unsigned char cons[16]={1,0,0,0,0,0,0,0,0,0,0,0,0,0,0x4,0x92};
void Gmul(unsigned char *a,unsigned char* b,unsigned char* c)
{
    __uint128_t  m1,m2,ans=0;
    unsigned char *pm1=&m1,*pm2=&m2;
    for(int i=0;i<16;i++)
    {
        pm1[i]=a[15-i];
        pm2[i]=b[15-i];
    }
    while(m2)
    {
        if(pm2[15]&0x80)
        {
            ans^=m1;
        }

        if(m1&0x1)
        {
            m1>>=1;
            pm1[15]^=0xe1;
            //pm1[0]^=1;
        }
        else 
            m1>>=1;
        m2<<=1;    
    }
    unsigned char *pa=&ans;
    for(int i=0;i<16;i++)
    {
        c[i]=pa[15-i];
    }

}
void Pmul(unsigned char *a,unsigned char* b,unsigned char* c)
{
    __uint128_t  m1,m2,ans=0;
    unsigned char *pm1=&m1,*pm2=&m2;
    for(int i=0;i<16;i++)
    {
        pm1[i]=a[i];
        pm2[i]=b[i];
    }
    while(m2)
    {
        if(m2&0x1)
        {
            ans^=m1;
        }

        if(pm1[15]&0x80)
        {
            m1<<=1;
            pm1[15]^=0xc2;
            pm1[0]^=1;
        }
        else 
            m1<<=1;
        m2>>=1;    
    }
    unsigned char *pa=&ans;
    for(int i=0;i<16;i++)
    {
        c[i]=pa[i];
    }

}
void dot(unsigned char *a,unsigned char* b,unsigned char* c)
{
    unsigned char cons[16]={1,0,0,0,0,0,0,0,0,0,0,0,0,0,0x4,0x92};
    Pmul(a,b,c);
    Pmul(c,cons,c);
}
unsigned char ans[16]={0x38,0x4C,0x3C,0xED,
                       0xE5,0xCB,0xC5,0x56,
                       0x0F,0x00,0x2F,0x94,
                       0xA8,0xE4,0x20,0x5A};
unsigned char H1[16]={  0x00,0xBA,0x5F,0x76,
                       0xF3,0xD8,0x98,0x2B,
                       0x19,0x99,0x20,0xE3,
                       0x22,0x1E,0xD0,0x5F,    
                       }                 ; 
unsigned char text1[448/8]={               
    0x3B,0xEA,0x33,0x21 ,                     
    0xBD,0xA9,0xEB,0xF0 ,                     
    0x2D,0x54,0x59,0xBC ,                     
    0xE4,0x29,0x5E,0x3A ,                     
    0xAE,0xF1,0xD4,0xE4 ,                     
    0xF5,0xF8,0x42,0x0A ,                     
    0x9E,0x22,0xF9,0x34 ,                     
    0x5E,0x0E,0x8F,0xD2 ,                     
    0xFE,0xAD,0xCD,0xA5 ,
    0x6F,0xFB,0x35,0x62 ,
    0xD5,0xB7,0xAC,0x58 ,
    0xDA,0x55,0x0D,0x52 ,
    0x43,0xBF,0xD6,0xD4 ,
    0x3E,0x00,0x27,0x05 ,
    };
    unsigned char H[16]={
    0x25,0x62,0x93,0x47,0x58,0x92,0x42,0x76,0x1d,0x31,0xf8,0x26,0xba,0x4b,0x75,0x7b
};
unsigned char text[32]={
    0x4f,0x4f,0x95,0x66,0x8c,0x83,0xdf,0xb6,0x40,0x17,0x62,0xbb,0x2d,0x01,0xa2,0x62,0xd1,0xa2,0x4d,0xdd,0x27,0x21,0xd0,0x06,0xbb,0xe4,0x5f,0x20,0xd3,0xc9,0xf3,0x62};


unsigned char rev(unsigned char a)
{
    a=((a&0x55)<<1)|((a&0xaa)>>1);
    a=((a&0x33)<<2)|((a&0xcc)>>2);
    a=((a&0x0f)<<4)|((a&0xf0)>>4);
    return a;
}
void GHASH1(unsigned char *text,int len,unsigned char H[16],unsigned char ans[16])
{
    //bd9b3997046731fb96251b91f9c99d7a
    unsigned char H1[16];
    for(int i=0;i<16;i++)
    {
        H1[i]=(H[i]);ans[i]=0;
    }
 
    for(int i=0;i<len;i+=16)
    {
        for(int j=0;j+i<len&&j<16;j++)
        {
            ans[j]^=(text[j+i]);
        }
        Gmul(ans,H1,ans);
    }
}
void GHASH(unsigned char *text,int len,unsigned char H[16],unsigned char ans[16])
{
    //bd9b3997046731fb96251b91f9c99d7a
    unsigned char H1[16];
    for(int i=0;i<16;i++)
    {
        H1[i]=(H[15-i]);ans[i]=0;
    }
    unsigned char in[16]={0x2,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0};
    Pmul(H1,in,H1); 
    for(int i=0;i<len;i+=16)
    {
        for(int j=0;j+i<len&&j<16;j++)
        {
            ans[15-j]^=(text[j+i]);
        }
        dot(ans,H1,ans);
    }
    for(int i=0;i<8;i++)
    {
        unsigned char tmp=(ans[i]);
        ans[i]=(ans[15-i]);
        ans[15-i]=tmp;
    }
}
void POLYVAL(unsigned char *text,int len,unsigned char H[16],unsigned char ans[16])
{
    for(int i=0;i<16;i++)ans[i]=0;
    for(int i=0;i<len;i+=16)
    {
        for(int j=0;j+i<len&&j<16;j++)
        {
            ans[j]^=text[j+i];
        }
        dot(ans,H,ans);
    }
}
void AES_GCM(unsigned char *key,
             unsigned char *AAD,int AADlen,
             unsigned char* plaintext,int textlen,
             unsigned char *tag,int taglen,
             unsigned char *nonce,int noncelen,unsigned char* ciphertext)
{
    unsigned char round_key[11][16];
    keygen(key,round_key);
    unsigned char J0[16]={0};
    unsigned char H[16]={0};
    if(noncelen==12)
    {
        J0[0]=0;
        for(int i=0;i<noncelen;i++)
        J0[i+4]=nonce[i];
        
    }
    else
    {
        exit(0);
       GHASH1(nonce,noncelen,H,J0);
    }
    AES_enc(round_key,H,H);
    *(unsigned int*)J0 +=1;
    unsigned char* c=(unsigned char*) calloc(
            (AADlen)+(AADlen%16)+
            (textlen)+(textlen%16)+16,sizeof(char));

    int cs=AADlen+(((16-AADlen)%16)+16)%16;
    int ls=cs+(textlen)+(((16-textlen)%16)+16)%16;
    *(unsigned long long*)(c+ls)=AADlen*8;
    *(unsigned long long*)(c+ls+8)=textlen*8;
    for(int i=0;i<AADlen;i++)
    {
        c[i]=AAD[i];
    }
    GCTR(key,textlen,J0,plaintext,c+cs);
    GHASH1(c,ls+16,H,tag);
    for(int i=0;i<4;i++)
    {
        J0[i]=0;
    }
    GCTR(key,16,J0,tag,tag);
    for(int i=0;i<textlen;i++)
    {
        ciphertext[i]=c[i+cs];
    }
    free(c);
    return;
}

void AES_GCM_SIV(unsigned char *key,
             unsigned char *AAD,int AADlen,
             unsigned char* plaintext,int textlen,
             unsigned char *tag,int taglen,
             unsigned char *nonce,int noncelen,unsigned char* ciphertext)
{
    unsigned char round_key[11][16];
    keygen(key,round_key);
    unsigned char J0[16]={0};
    unsigned char H[24]={0};
    unsigned char MEK[24]={0};
    if(noncelen==12)
    {
        J0[0]=0;
        for(int i=0;i<noncelen;i++)
        J0[i+4]=nonce[i];
        
    }
    else
    {
        exit(0);
       GHASH1(nonce,noncelen,H,J0);
    }
    AES_enc(round_key,J0,H);
    *(unsigned int*)J0 +=1;
    AES_enc(round_key,J0,H+8);
    unsigned char* c=(unsigned char*) calloc(
            (AADlen)+(AADlen%16)+
            (textlen)+(textlen%16)+16,sizeof(char));
    *(unsigned int*)J0 +=1;

    AES_enc(round_key,J0,MEK);
    *(unsigned int*)J0 +=1;
    AES_enc(round_key,J0,MEK+8);

    int cs=AADlen+(((16-AADlen)%16)+16)%16;
    int ls=cs+(textlen)+(((16-textlen)%16)+16)%16;
    *(unsigned long long*)(c+ls)=AADlen*8;
    *(unsigned long long*)(c+ls+8)=textlen*8;
    for(int i=0;i<AADlen;i++)
    {
        c[i]=AAD[i];
    }
    for(int i=0;i<textlen;i++)
    {
        c[cs+i]=plaintext[i];
    }
    POLYVAL(c,ls+16,H,tag);
    for(int i=0;i<12;i++)
    {
        tag[i]^=nonce[i];
    }
    tag[15]&=0x7f;
    keygen(MEK,round_key);
    AES_enc(round_key,tag,tag);
    for(int i=0;i<16;i++)
    {
        J0[i]=tag[i];
    }
    J0[15]|=0x80;
    GCTR_SIV(MEK,textlen,J0,plaintext,c+cs);
    for(int i=0;i<textlen;i++)
    {
        ciphertext[i]=c[i+cs];
    }
    free(c);
    return;
}
unsigned char GCM_nonce[16]={
0x75,0x2a,0xba,0xd3,0xe0,0xaf,0xb5,0xf4,0x34,0xdc,0x43,0x10,
};
unsigned char GCM_key[16]={
0xee,0x8e,0x1e,0xd9,0xff,0x25,0x40,0xae,0x8f,0x2b,0xa9,0xf5,0x0b,0xc2,0xf2,0x7c,
};
unsigned char GCM_AAD[16]="example";
unsigned char GCM_plaintext[16]={
"Hello world"
};
unsigned char GCM_ciphertext[32]={
0
};
unsigned char GCM_tag[16]={

};

unsigned char GCM_key1[16]={
};
int main(int argc, char *argv[])
{
    

    AES_GCM(GCM_key,GCM_AAD,7,GCM_ciphertext,32,GCM_tag,16,GCM_nonce,12,GCM_key1);

    printf("all zero:\n");
    for(int i=0;i<32;i++)
    {
        printf("%02x ",GCM_key1[i]);
       
    }
    printf("\n");
    printf("\n");
    for(int i=0;i<16;i++)
    {
        printf("%02x ",GCM_tag[i]);
    }
    printf("\n");
    printf("being attacked:\n");
 

    AES_GCM(GCM_key,GCM_AAD,7,GCM_plaintext,11,GCM_tag,16,GCM_nonce,12,GCM_ciphertext);

    for(int i=0;i<11;i++)
    {
        printf("%02x ",GCM_ciphertext[i]);
    }
    printf("\n");
    printf("\n");
    for(int i=0;i<16;i++)
    {
        printf("%02x ",GCM_tag[i]);
    }
    printf("\n");
    printf("\n");

    printf("the secret is\n");
    for(int i=0;i<11;i++)
    {
        printf("%02x ",GCM_key1[i]^GCM_ciphertext[i]);
    }
    printf("\n");
    for(int i=0;i<11;i++)
    {
        printf("%c",GCM_key1[i]^GCM_ciphertext[i]);
    }
//    GHASH1(text,32,H,ans);
//
//    for(int i=0;i<16;i++)
//    {
//        printf("%02x ",ans[i]);
//    }
//    printf("\n");
//    printf("\n");
//    GHASH(text,32,H,ans);
//
//    for(int i=0;i<16;i++)
//    {
//        printf("%02x ",ans[i]);
//    }
//    printf("\n");
//    printf("\n");
//    POLYVAL(text,32,H,ans);
//
//    for(int i=0;i<16;i++)
//    {
//        printf("%02x ",ans[i]);
//    }
//    printf("\n");
//    printf("\n");
//    Gmul(key,in,out);
//    for(int i=0;i<16;i++)
//    {
//        printf("%02x ",out[i]);
//    }
//    printf("\n");
//    printf("\n");
//    Gmul(in,key,out);
//    for(int i=0;i<16;i++)
//    {
//        printf("%02x ",out[i]);
//    }
//    printf("\n");
//    printf("\n");
//    dot(key,in,out);
//    for(int i=0;i<16;i++)
//    {
//        printf("%02x ",out[i]);
//    }
//    printf("\n");
//    printf("\n");
//    dot(in,key,out);
//    for(int i=0;i<16;i++)
//    {
//        printf("%02x ",out[i]);
//    }
//    printf("\n");
//    keygen(key,round_key);
//    AES_enc(round_key,in,out);
//    for(int i=0;i<16;i++)
//    {
//        printf("%02x ",out[i]);
//    }
//    printf("\n");
//    AES_dec(round_key,out,out);
//    for(int i=0;i<16;i++)
//    {
//        printf("%02x ",out[i]);
//    }
    return 0;
}
