//main_simd.c

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "sm4_simd_sbox_new.h"
int main() {
    // 01 23 45 67 89 ab cd ef fe dc ba 98 76 54 32 10
    unsigned char key[16 * 8] = {0x01, 0x23, 0x45, 0x67, 0x89, 0xab,
                                 0xcd, 0xef, 0xfe, 0xdc, 0xba, 0x98,
                                 0x76, 0x54, 0x32, 0x10};
    // 01 23 45 67 89 ab cd ef fe dc ba 98 76 54 32 10
    // 00 00 ... 00
    unsigned int in[16 * 8] = {0x01234567, 0x89abcdef,
                                0xfedcba98, 0x76543210};
    SM4_Key sm4_key;
    int success = SM4_KeyInit(key, &sm4_key);
    if (success) {
        clock_t t1,t2;
        int p;
        scanf("%d",&p);
        t1=clock();
        for(int i=0;i<p;i++)
        SM4_Encrypt_x8(in, in, sm4_key);
        t2=clock();
        printf(" %f s,%f Mb/s,%f spt\n",(double)(t2-t1)/CLOCKS_PER_SEC,(128.0*p*8)/((1<<20)*(double)(t2-t1)/CLOCKS_PER_SEC),((double)(t2-t1)/(p*CLOCKS_PER_SEC)));

        // 68 1e df 34 d2 06 96 5e 86 b3 e9 4f 53 6e 42 46
        // 26 77 f4 6b 09 c1 22 cc 97 55 33 10 5b d4 a2 2a
        // 26 ...
        printf("C:\n");
        for (int j = 0; j < 8; j++) {
            printf("\t");
            for (int i = 0; i < 4; i++) {
                printf("%08x ", in[i + 4 * j]);
            }
            printf("\n");
        }

        printf("P:\n");
        SM4_Decrypt_x8(in, in, sm4_key);
        // 01 23 45 67 89 ab cd ef fe dc ba 98 76 54 32 10
        // 00 00 ... 00
        for (int j = 0; j < 8; j++) {
            printf("\t");
            for (int i = 0; i < 4; i++) {
                printf("%08x ", in[i + 4 * j]);
            }
            printf("\n");
        }
        
        SM4_KeyDelete(sm4_key);
    }
    system("pause");
    return 0;
}
