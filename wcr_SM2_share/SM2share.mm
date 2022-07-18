
<map>
  <node ID="root" TEXT="SM2纲要">
    <node TEXT="椭圆曲线原理" ID="cf2929619bf0ba43252ceb50325637f0" STYLE="bubble" POSITION="right">
      <node TEXT="椭圆曲线上加法群" ID="e232474b4aa03eef9ea81cdbc12870a7" STYLE="fork">
        <node TEXT="椭圆曲线性质" ID="041bbdf6f9818667876f2310361da40e" STYLE="fork">
          <node TEXT="整数点个数有限" ID="4da53fa54328978360cb05eb049cb357" STYLE="fork"/>
        </node>
        <node TEXT="曲线上的运算定义" ID="c5b79110b139f5310742cadd5f5ea462" STYLE="fork">
          <node TEXT="引入无穷原点定义单位元" ID="803b46489718549284b9aaf1ce7f0207" STYLE="fork"/>
          <node TEXT="三根定义二元运算，封闭性" ID="c1afd78367d31ff29c52415c630f223d" STYLE="fork"/>
          <node TEXT="有理点的特殊封闭性" ID="1760b93461d04a6b2d2ba179b15c4237" STYLE="fork"/>
          <node TEXT="结合律证明（图解）" ID="205836db0dccd5608b22f3a6577dd657" STYLE="fork"/>
          <node TEXT="通过可交换定义加法群" ID="fab5e7c2bf635005ad04ba729f0cd8a2" STYLE="fork"/>
        </node>
        <node TEXT="F（2m）下的运算" ID="56b240d8a9902576f6e260c867b2c9cd" STYLE="fork">
          <node TEXT="加法：异或" ID="1712371a5237e8bd687d6c7181ed32bd" STYLE="fork"/>
          <node TEXT="乘法：多项式乘法" ID="bb71f6daa0c888530a36098035944bc9" STYLE="fork"/>
        </node>
        <node TEXT="不同基的影响" ID="74a53e1bf7fafeab70a4938a9589e1dd" STYLE="fork">
          <node TEXT="多项式基：符合直觉认识，但乘法运算过繁，且求模麻烦" ID="4cedf22edd89739651e72d2ab3857ea2" STYLE="fork"/>
          <node TEXT="正规基：乘方优化为循环位移，密码算法中有奇效" ID="86b6a59507e77239499d2e3700e92f21" STYLE="fork"/>
        </node>
      </node>
      <node TEXT="信息编码问题" ID="5dd037210a6b2925148489e9d2d42038" STYLE="fork">
        <node TEXT="其他（以字节串为例）转曲线上的点过程" ID="286bf847a83d9ebb6e0b52445250cfd6" STYLE="fork">
          <node TEXT="字串=PC||X(||Y),其中len(PC)=1,len(X)=len(Y)" ID="856deba2b9cc065df86b2f22add90442" STYLE="fork"/>
          <node TEXT="压缩：PC=02或03（这时没有Y）" ID="c33d1c73d711e530fc52c05d837831ee" STYLE="fork"/>
          <node TEXT="未压缩：PC=04" ID="282dd2b963c5bd96e3b36787196b8647" STYLE="fork"/>
          <node TEXT="混合：PC=06或07" ID="59243c98e5f0a4f4fc45923ae66ee398" STYLE="fork"/>
        </node>
        <node TEXT="压缩细节" ID="ade9fd2518fa0e8bbd02afcccd5cdf62" STYLE="fork">
          <node TEXT="对于Fq，取y_p的最低位比特为压缩表示" ID="697b7330c819af49724055e33519cf64" STYLE="fork"/>
          <node TEXT="对于F2m，取y_p/x_p的最低比特表示" ID="ce9b48a930b7607d3c14c48287f0392e" STYLE="fork"/>
        </node>
        <node TEXT="一个疑点" ID="9a24676c5872126c5e6c232a738c4830" STYLE="fork">
          <node TEXT="并不是所有x的在曲线上，所以如直接硬编码特定信息会失败" ID="d9b9664f1d07223ea2a3a7ca91616cf9" STYLE="fork"/>
          <node TEXT="解决方案1：" ID="9d040aae34b8604eabaf7f19edeed091" STYLE="fork">
            <node TEXT="不直接用作加密，只用来生成参数" ID="8fc6d0a261c3ef075ca2e9cf72016664" STYLE="fork"/>
          </node>
          <node TEXT="解决方案2：" ID="427e6272039bc187a7f99947c250d695" STYLE="fork">
            <node TEXT="利用阶的Hasse定律，在信息后加定长随机后缀再编码" ID="31718681c840cbd5b00c247a7983b3a9" STYLE="fork"/>
          </node>
        </node>
      </node>
      <node TEXT="ECDLP攻击" ID="a91462104c54bcb1358745bfe6ba8bc5" STYLE="fork">
        <node TEXT="常规攻击（小质数）" ID="f64d8a52c7f2793b61bc7d205109d86e" STYLE="fork">
          <node TEXT="pohlig-hellman" ID="9b118336202c9974f92e7d6f5de419ee" STYLE="fork">
            <node TEXT="条件：阶光滑" ID="ca25389b5bd56d186e7ca0eb78584aa5" STYLE="fork"/>
            <node TEXT="原理：crt+小指数爆破" ID="bd1e3008698428c6d514d78cbd38b502" STYLE="fork"/>
          </node>
          <node TEXT="BSGS" ID="f51dcf8d894e61273ef500c7e3a36a69" STYLE="fork">
            <node TEXT="条件：时空复杂度O(sqrt(p))" ID="6118936dfcd327336e1d580d999ce47b" STYLE="fork"/>
            <node TEXT="原理：时间换空间" ID="fa27cce5d8a604910d198c6a15bd2abb" STYLE="fork"/>
          </node>
          <node TEXT="Pollard" ID="21663d5dd2fb49c85664b167a688861c" STYLE="fork">
            <node TEXT="条件：时间复杂度O(n^{1/4})" ID="012e21c75747f618f0e4af94a0421d92" STYLE="fork"/>
            <node TEXT="本质仍是分解质因数" ID="8d8d2d9216eda050aaa4bf2481df10d9" STYLE="fork"/>
          </node>
        </node>
        <node TEXT="弱曲线问题" ID="36f4b7c9083e987c8ef21bfa0f8c3e77" STYLE="fork">
          <node TEXT="异常曲线" ID="e3026e49c0e74ea81d6aa421e8070ad5" STYLE="fork">
            <node TEXT="特征 ：# E(Fp)=p" ID="6f5c559d1d2ca6988bbb4b757899ca7c" STYLE="fork"/>
            <node TEXT="攻击方式：Smart attack " ID="afb6a0be9849cce06643d6e9ed7f1d97" STYLE="fork"/>
          </node>
          <node TEXT="超奇异曲线" ID="6d772ae1de3a36a360404b7647812bf0" STYLE="fork">
            <node TEXT="特征：对于n阶基点G，若p^t=1 mod n,t&lt;MOV阈" ID="e1ae7aaa85fb7247cfdafed6a199b6b7" STYLE="fork"/>
            <node TEXT="攻击方式：MOV attack" ID="c057915f107fd7551d4319146e29d7e1" STYLE="fork"/>
          </node>
          <node TEXT="GHS" ID="fb9af46c7c97d3e9461edf17798cc608" STYLE="fork">
            <node TEXT="特征：F2m的m为8的倍数" ID="97b6370504168e50a4d5bfab23c4f87d" STYLE="fork"/>
          </node>
        </node>
        <node TEXT="侧信道" ID="49ed422ad6a93ea74e47716594e445a0" STYLE="fork">
          <node TEXT="时序攻击" ID="c85e0e858a2394cfeac7b78e817ac03a" STYLE="fork">
            <node TEXT="长度分析" ID="84864a3e467f900bc1e14369a4983076" STYLE="fork"/>
            <node TEXT="蒙哥马利算法" ID="f99cc5a78448dab3340cc95656d4913e" STYLE="fork"/>
          </node>
          <node TEXT="能量分析" ID="b4a6f9065674f595f1496614c82cb9f4" STYLE="fork">
            <node TEXT="运算资源整体一致" ID="77a8a9c33c9b8759a19073744615d222" STYLE="fork"/>
            <node TEXT="分支间调用功能不能有明显区别" ID="4fdaa2126af99bc398b0b25b5334950d" STYLE="fork"/>
            <node TEXT="例子：快速幂的优化" ID="2b1983e52cc15e51c632345f39c88f24" STYLE="fork"/>
          </node>
        </node>
      </node>
      <node TEXT="参数与判断流程" ID="64a496bd1ec9d3b292c9b4967271a81d" STYLE="fork">
        <node TEXT="Fp" ID="f79e4608450123dceef59217a56c53dc" STYLE="fork">
          <node TEXT="参数" ID="1a422fb46434b27f7527d3e116603db2" STYLE="fork">
            <node TEXT="域的规模 q=p ,p为大于 3的素数 ;" ID="b4729008d45366fadf7502aadcb94fa9" STYLE="fork"/>
            <node TEXT="(选项 )一个长度至少为 192的比特串 SEED" ID="4c466adfcc9a30b42818e5663e6bad83" STYLE="fork"/>
            <node TEXT="Fp中的两个元素a和 b,它们定义椭圆曲线 E的方程 y^2=x^3+ax+b;" ID="5cdd4e0de661b48dc7e1b92c9f036e9e" STYLE="fork"/>
            <node TEXT="基点 G=(Gx,Gy)∈ E(Fp),G≠ O;" ID="7c3d352b5940bc78f4d6042234126554" STYLE="fork"/>
            <node TEXT="基点 G的阶n要求 :n&gt;2^191,n&gt;4p^{1/2};" ID="ea86dd63fab33972c297412999ef9bf1" STYLE="fork"/>
            <node TEXT="(选项 )余因子h=#E(Fp)/n" ID="316d6bc5a8704e455368e3d4b7c171b1" STYLE="fork"/>
          </node>
          <node TEXT="验证" ID="35f29078b6046a3e356e14cd855ea0f0" STYLE="fork">
            <node TEXT="验证 4a^3+27b^2!=0 mod p" ID="3851a008d6f26c9c17beb765c1cdb5a4" STYLE="fork"/>
            <node TEXT="(选项)验证hash(SEED)*b^2=a^3 mod p" ID="ece07ea1eb73e0084d8d4b897a713e66" STYLE="fork"/>
            <node TEXT="验证 G in E and n*G=O" ID="f550cedec8e4b83d67ee91e2927c7ba7" STYLE="fork"/>
            <node TEXT="验证 n&gt;2^191,n&gt;4p^{1/2}" ID="856fc443dd95dc0993ef3e499ccdfc85" STYLE="fork"/>
            <node TEXT="(选项)验证floor((p^{1/2}+1)^2/n)==h" ID="2dfe34dd0a8fdcd7962e96c7eabeda9b" STYLE="fork"/>
            <node TEXT="验证抗MOV 和抗异常" ID="8976df40e17d87e4c8bc5bef380a5bcb" STYLE="fork"/>
          </node>
        </node>
        <node TEXT="F2m" ID="d5f2a0e2b2e8c649ed0613728074bfad" STYLE="fork">
          <node TEXT="参数" ID="c1784baa9f624cd916868f770ba0df09" STYLE="fork">
            <node TEXT="域的信息：" ID="8e0fb93c6875eacb68b36d26497cbc39" STYLE="fork">
              <node TEXT="q=2^m " ID="79a149c86ee6e3f0d97b9e7509b88e70" STYLE="fork"/>
              <node TEXT="元素表示法（TPB,PPB,GNB）" ID="f86486d2aee0cc7f824459a5bb4a910f" STYLE="fork"/>
              <node TEXT="约束多项式（TPB,PPB）" ID="ed3b22478e333281f95eef48c89a8fd4" STYLE="fork"/>
            </node>
            <node TEXT="(选项 )一个长度至少为 192的比特串 SEED" ID="b9158a7e58255ec49d635f57473cc8ca" STYLE="fork"/>
            <node TEXT="F2m中的两个元素a和b,它们定义椭圆曲线 E的方程 :y^2+xy=x^3+ax^2+b ;" ID="6989dd44d1029300ea7e4055771ea791" STYLE="fork"/>
            <node TEXT="基点 G=(Gx,Gy)∈ E(F2m ),G≠ O;" ID="29b553ec91276af92255d8a36c31d7a7" STYLE="fork"/>
            <node TEXT="基点 G的阶n(要求 :n &gt;2^191且n&gt;2^{2+m/2});" ID="1ad22b58b27fee0ac7ec9e9ec1ae20fe" STYLE="fork"/>
            <node TEXT="(选项 )余因子h=#E(Fp)/n" ID="9259414cb48c835ee768a34f5e0f7076" STYLE="fork"/>
          </node>
          <node TEXT="验证" ID="212b80d807a31d3683d5e6f0ba4b3f26" STYLE="fork">
            <node TEXT="验证域信息，q=2^m," ID="f5e02eba1e51c5cde8e588ce53d8d688" STYLE="fork">
              <node TEXT="若所用的是 TPB,则验证约化多项式是 F2上的不可约三项式 " ID="d11b48e12f03444a906423500defbbac" STYLE="fork"/>
              <node TEXT="若所用的是 PPB,则验证不存在 m次不可约三项式 ,且约化多项式是 F2上的不可约五项式 " ID="86ad209b41aeffaa82e561d25de49272" STYLE="fork"/>
              <node TEXT="若所用的是 GNB,则验证 m不能被 8整除 " ID="d55cd003216fe5076a1f0374c7757828" STYLE="fork"/>
            </node>
            <node TEXT="(选项)验证hash(SEED)截断为b " ID="8dcc04e23dd225e940fefa0deff031a4" STYLE="fork"/>
            <node TEXT="验证 G in E and n*G=O" ID="cc533347f0040cec34f5e3562ee7b40b" STYLE="fork"/>
            <node TEXT="验证 n&gt;2^191,n&gt;2^{2+m/2}" ID="e15b5d2b8f53236d337f6bfaec19a23a" STYLE="fork"/>
            <node TEXT="(选项)验证floor((2^{m/2}+1)^2/n)==h" ID="35e8b4c4dd015f6853b28b52df2a7b44" STYLE="fork"/>
            <node TEXT="验证抗MOV和抗GHS" ID="dacb1e9c955a693b793abc75162df5b9" STYLE="fork"/>
          </node>
        </node>
      </node>
      <node TEXT="复杂度估计" ID="02f00d41dfa783bfcb80ff1554699d23" STYLE="fork">
        <node TEXT="基本运算复杂度分析" ID="15d4a2537360d881cc613d0fc32f91a4" STYLE="fork"/>
        <node TEXT="影响因素分析" ID="fe628cc5f8248724e78b4b7e2a8bb729" STYLE="fork">
          <node TEXT="坐标系类型" ID="02dc2ce104e6919993b26615b50b4be4" STYLE="fork"/>
          <node TEXT="域" ID="ad72b2f14faac701eca717106737795d" STYLE="fork"/>
          <node TEXT="基" ID="4d1e74892853e87bf1d56dc0b284eef1" STYLE="fork"/>
        </node>
      </node>
      <node TEXT="一些辅助算法实现" ID="4c17fb723666d26adfef4eebb939aeac" STYLE="fork">
        <node TEXT="求元素的阶的算法" ID="c272b07e87d4062c1b0a27e6ca18f7aa" STYLE="fork">
          <node TEXT="SEA算法" ID="95baf05787045ac15b15376f12895c8b" STYLE="fork"/>
          <node TEXT="Satoh算法" ID="98f60ae190381548e94dbdd34a90310d" STYLE="fork"/>
        </node>
        <node TEXT="在扩域K=F2m上求F2内m阶不可约多项式f的根" ID="802fc3204e7680442f34f8ba497a49df" STYLE="fork">
          <node TEXT="输入：f,K" ID="d78ff76fdab66ff1c31a108e178d4069" STYLE="fork"/>
          <node TEXT="输出：一个合法根" ID="ab3d3553de2780bffa51ae831a2f05f1" STYLE="fork"/>
          <node TEXT="核心思想：通过随机元素迭代分解因式" ID="dcfc41b143d4ea69f42f0e5d148ef307" STYLE="fork"/>
          <node TEXT="伪代码：" ID="6e3db7d562813eb912f7b0bd6b886768" STYLE="fork"/>
        </node>
        <node TEXT="基变换算法" ID="1da0c1899202e21a7aeaabcfa097bf89" STYLE="fork">
          <node TEXT="输入：两个基B1,B2" ID="ed62a9ca480fe3d4e6586c464599219b" STYLE="fork"/>
          <node TEXT="输出：使得V1=V2*Eta的基变换矩阵Eta" ID="ead7a1e2c1c226a52f7c651755cbcdac" STYLE="fork"/>
          <node TEXT="流程：" ID="ae083ac2c3616ef13cddced8ba1c73dd" STYLE="fork">
            <node TEXT="找到B2的约化多项式f" ID="97d1bc68e2b41489f2034a4a031eb1c0" STYLE="fork"/>
            <node TEXT="求出f在B1下的一组基" ID="95f40366cc91c522c9e506d32b38f14c" STYLE="fork"/>
            <node TEXT="将其作为行向量组成基变换矩阵" ID="3547214b23a76e1fd65d4644d430b32f" STYLE="fork"/>
          </node>
        </node>
        <node TEXT="类快速幂算法" ID="fdbd166be93139c7d049de6585fb4bbf" STYLE="fork">
          <node TEXT="核心思想：通过结合律将(2*n+x)P=2*(nP)+xP将时间降到O(log)级，即比特长度级" ID="51ffc84866af78b961208afd3e311bad" STYLE="fork"/>
          <node TEXT="隐患：侧信道泄露" ID="eb1b98294a300892d6bdf4473b74fb2a" STYLE="fork"/>
        </node>
        <node TEXT="卢卡斯序列" ID="e786049fff14a39b6f895e120e4d9761" STYLE="fork">
          <node TEXT="定义：(X,Y)的lucas序列{U},伴随序列{V}，有U0=0,U1=1，V0=2,V1=X，B_k=XB_{k-1}-YB_{k-2}" ID="bd9c063c45ed4c522d7a5cd35d21be11" STYLE="fork"/>
          <node TEXT="优化算法（对给定的XY与k求U_k,V_k）：" ID="1b91b144328160b6477127ccf527a055" STYLE="fork">
            <node TEXT="取Delta=X^2-4Y" ID="951fee700cc6ecb2d5453a66d866ca97" STYLE="fork"/>
            <node TEXT="取k的比特串（K_{l-1}……K_0}，取i (l-1)-&gt;0:" ID="f35ad24d77a924b00d45443e52d62954" STYLE="fork">
              <node TEXT="取U,V=U*V，(V^2+Delta*U^2)/2" ID="dd710eddb6f367f100ee9c3b9ce1b6b5" STYLE="fork"/>
              <node TEXT="若K_i==1，则U,V=(X*U+V)/2，(X*V+Delta*U)/2" ID="b4e096c619da5e613b65d00f3ea90d9e" STYLE="fork"/>
            </node>
            <node TEXT="返回U,V" ID="b01f938b4dae44dc181891afe407060c" STYLE="fork"/>
          </node>
        </node>
        <node TEXT="模平方根计算" ID="e87d5b0ebf955a3b26f7c786c5e49111" STYLE="fork">
          <node TEXT="输入：模素数p，待开根数g" ID="43179f47e1e0fe2648dead04df45cd5a" STYLE="fork"/>
          <node TEXT="输出：一个根y或“无根”" ID="bc4a06ad85ca92ffdd391163ed2fbd0d" STYLE="fork"/>
          <node TEXT="细节：" ID="9c0804e7a8e7c6b6de1253194a948487" STYLE="fork">
            <node TEXT="p=3 mod 4时" ID="d502255a8a98d1542d9f7c6599663a2f" STYLE="fork">
              <node TEXT="取y=g^((p+1)//4) mod p" ID="e33076f88b81f89451ca2c5c4700fecf" STYLE="fork"/>
              <node TEXT="若y^2==g mod p，返回y，否则“无根”" ID="07ae1c07cc11d1da15d85cc3184d77f4" STYLE="fork"/>
            </node>
            <node TEXT="p=5 mod 8时" ID="ac1b8d11ced828f3715339e1dc7fbff1" STYLE="fork">
              <node TEXT="取z=g^((p-1)//4) mod p" ID="905cbf1c364265b9bf872b008ab78a68" STYLE="fork"/>
              <node TEXT="判断z：" ID="a82b4640f965c13c1261e56e5a196680" STYLE="fork">
                <node TEXT="若z==1 mod p,y=g^((p+3)//8) mod p;" ID="23535db25ac9e2e4d27af1ef1ef58b19" STYLE="fork"/>
                <node TEXT="若z==-1 mod p，y=2g*(4g)^((p+3)//8) mod p;" ID="9aea64a87aa243ecc6f69a37e870bdc4" STYLE="fork"/>
                <node TEXT="否则“wrong”" ID="580c0c5594b8c0c67f23682ddf96780c" STYLE="fork"/>
              </node>
              <node TEXT="若y^2==g mod p，返回y，否则“无根”" ID="2c5a0352a52d5c5e6d4de54fcfb0ba75" STYLE="fork"/>
            </node>
            <node TEXT="p=1 mod 8时" ID="8da92afb121dfe7c3fb9c79d8ade7015" STYLE="fork">
              <node TEXT="取X,Y=randint(0,p),g" ID="190c8dbb02f9e22e32b29c4afcab182e" STYLE="fork"/>
              <node TEXT="计算（X,Y）lucas序列的第(p+1)//2项" ID="9d21a8b8a183c99afc25f67b130b0e0a" STYLE="fork"/>
              <node TEXT="若V^2==4Y mod p,则y=V/2 mod p,返回y；" ID="68f575ac0659b75329760ead5e0ba327" STYLE="fork"/>
              <node TEXT="若U mod p !=\pm 1,则返回&quot;无根&quot;" ID="720cfba3f158ba40a1668b94cd798c11" STYLE="fork"/>
              <node TEXT="否则重新选择X,Y参数并循环 " ID="a92e274ec154a5bca7f84bf02a0eea7f" STYLE="fork"/>
            </node>
          </node>
        </node>
      </node>
    </node>
    <node TEXT="环境公开信息及标准" ID="e1a998f3e7743f13f33ac6649f0bf8de" STYLE="bubble" POSITION="right">
      <node TEXT="公开信息：" ID="54c526f346b7d10306c9c701124d5422" STYLE="fork">
        <node TEXT="双方身份标识IDA，IDB" ID="907597cf1e0efc80f5792e6a8f22a72e" STYLE="fork"/>
        <node TEXT="曲线信息" ID="200778b056d02ed7db3cde625716727f" STYLE="fork">
          <node TEXT="曲线参数Fq,a,b" ID="adeeacbb838884618941af8e45f5f67f" STYLE="fork"/>
          <node TEXT="基点G" ID="421662a253ee8b45a37eee8491c3378e" STYLE="fork"/>
        </node>
        <node TEXT="A使用私钥pa生产的公钥A=pa*G" ID="204e041dadaa45e1c6fdbf7a721a6441" STYLE="fork"/>
        <node TEXT="B使用私钥pb生成的公钥B=pb*G" ID="3ee60bc60be52cf670c8fc0f4e969712" STYLE="fork"/>
        <node TEXT="标准使用的256位输出hash函数H256" ID="edbd09bd422748b1f80b849028f2c3a2" STYLE="fork"/>
        <node TEXT="用户使用的hash函数H" ID="cbe71c9de3a5e0501d1851eb98e1ba1f" STYLE="fork"/>
      </node>
      <node TEXT="用户信息杂凑函数标准" ID="d2adc5b3f9e532d5d0ff85754ad46f58" STYLE="fork">
        <node TEXT="输入：" ID="606829ea1e857089c73b88d3390ca540" STYLE="fork">
          <node TEXT="身份信息IDA,A;" ID="bbc5520d5e49f53631caf4c35b94629d" STYLE="fork"/>
          <node TEXT="曲线信息a,b,G;" ID="2f820e8d844c775af288ca786e6e4e48" STYLE="fork"/>
        </node>
        <node TEXT="输出：A的杂凑值ZA" ID="7b60b1a41f078efca7082a955e4437bf" STYLE="fork"/>
        <node TEXT="过程：" ID="308aec804acdc3a6ed4bdfa06562acb3" STYLE="fork">
          <node TEXT="取IDA的比特长度eA转换为两个字节的比特串EA" ID="cf09a82f6cb82a3b6e892850eb6fb03f" STYLE="fork"/>
          <node TEXT="将整数a,b化为对应比特串Ba,Bb" ID="e784f4128baf960f34acef5c9347762c" STYLE="fork"/>
          <node TEXT="将点A与G坐标取出并转化比特串xA,yA,xG,yG" ID="f3fa05f9ada430694dc055c1403d31b1" STYLE="fork"/>
          <node TEXT="返回ZA=H256(EA||IDA||Ba||Bb||xG||yG||xA||yA)" ID="85350125081d5241bc810dd2c1e099a0" STYLE="fork"/>
        </node>
      </node>
      <node TEXT="密钥派生函数KDF" ID="5ffff4c848f45076daa203fc6020f26f" STYLE="fork">
        <node TEXT="参数：哈希函数Hv，v为输出长度" ID="6c9734e8a56e93bc52d79b5598d15d05" STYLE="fork"/>
        <node TEXT="输入：比特串Z，需要密钥的比特长度k" ID="ed22ee32046b70581acc11a58bc84a84" STYLE="fork"/>
        <node TEXT="输出：k长比特流K" ID="37827503edf89310c91f9c1b653e3d61" STYLE="fork"/>
        <node TEXT="过程：" ID="a0b8b8416c6d3b8ef0f70a1f6f32fd6f" STYLE="fork">
          <node TEXT="初始化计数器ct=0x00000001（32比特四字节）;" ID="79cc6e43e22be6b0863f6f7301724f73" STYLE="fork"/>
          <node TEXT="对于i 1-&gt;ceil(k/v):计算Hv_i(Z||ct),ct++;" ID="682632c012e1ea80143763a7f90f3baa" STYLE="fork"/>
          <node TEXT="将Hv_i按顺序从左往右拼合起来，取前k比特输出；" ID="636ef917c0af8b186bd4612ecb464148" STYLE="fork"/>
        </node>
      </node>
    </node>
    <node TEXT="签名" ID="bddac32b0d2ec79cb56ee4ba39143388" STYLE="bubble" POSITION="right">
      <node TEXT="生成签名" ID="752d772accdcbbf1cd43c27df2b14bf6" STYLE="fork">
        <node TEXT="参数" ID="00cac0ebac77c38a31da88705d94f523" STYLE="fork">
          <node TEXT="曲线E" ID="b5a87466b67e107f0295aee09fcdccd0" STYLE="fork"/>
          <node TEXT="基点G" ID="16c3eb696cb7fd81f42310efbf2bac69" STYLE="fork"/>
          <node TEXT="基点阶n" ID="bcfb0d63e0ff9c17dedb3ea362b108bf" STYLE="fork"/>
          <node TEXT="随机数k（不可重用）" ID="a5097a127bb8bbabcdcdba947436b57d" STYLE="fork"/>
          <node TEXT="哈希函数H" ID="5e3ceaee44accf33c2121f9d89b3d844" STYLE="fork"/>
        </node>
        <node TEXT="输入" ID="2fd3f675db9678d5b31c861e51896491" STYLE="fork">
          <node TEXT="身份信息ZA，私钥pa" ID="c13fadbfcf54b766771cce53d4dab698" STYLE="fork"/>
          <node TEXT="信息M" ID="701033ec704248217af74db403df586a" STYLE="fork"/>
        </node>
        <node TEXT="输出" ID="319d4bd6e0a355ecb1213c625dbf0fad" STYLE="fork">
          <node TEXT="签名字串对(r,s)" ID="abc3ff38ddc216dad67bd98088174763" STYLE="fork"/>
        </node>
        <node TEXT="流程" ID="bb75ef830c1dcc849a2d0bb563a342e6" STYLE="fork">
          <node TEXT="取e=H(ZA||M)" ID="39572170f17364144224b2051a989530" STYLE="fork"/>
          <node TEXT="生成随机数k，0&lt;k&lt;n" ID="0b8b28b257294c7092e8dc623115fcdd" STYLE="fork"/>
          <node TEXT="计算K=kG，取r=xK+e mod n" ID="acd896aaa06705dd1e29bcc8bb6c1fc8" STYLE="fork"/>
          <node TEXT="计算s=(k-r*pa)/(1+pa) mod n" ID="125ea52c560c38e875708c17f2f2f4f1" STYLE="fork"/>
          <node TEXT="验证r!=-k mod n,且r,s均不为0,则转换为字串返回；否则重新生成" ID="55a1c2ec64f98d8545d62d4ed0e06541" STYLE="fork"/>
        </node>
      </node>
      <node TEXT="验证签名" ID="95ffed61d6c8b88e2bfbfc7ac5e63f7f" STYLE="fork">
        <node TEXT="参数" ID="012f185ec07383f70022df1d9ff0ccb7" STYLE="fork">
          <node TEXT="曲线E" ID="a0fa219f4c3056d9aa53164eaa23ded4" STYLE="fork"/>
          <node TEXT="基点G" ID="f0b00ff01221d009a1ad6a3f00eaa762" STYLE="fork"/>
          <node TEXT="基点阶n" ID="cb2cddc0083eba323f03d60a610eeafb" STYLE="fork"/>
          <node TEXT="哈希函数H" ID="bc07320a14989ff7bdc8fa9581182b76" STYLE="fork"/>
        </node>
        <node TEXT="输入" ID="eb1e525da781faea373aaeb8aa802138" STYLE="fork">
          <node TEXT="身份信息ZA，公钥A" ID="7f463b857870592052299dac71febda8" STYLE="fork"/>
          <node TEXT="信息M" ID="7e6f89b1161c7ba34881da0702dd3785" STYLE="fork"/>
          <node TEXT="签名对(r,s)" ID="f9dae9c1c8c3115b9f3a1ac677390e64" STYLE="fork"/>
        </node>
        <node TEXT="输出" ID="27f0cee8471cc730d70f8ecf4e416240" STYLE="fork">
          <node TEXT="“通过”或“不通过”" ID="1339d7d502d9f3ec680c67daeea79a8c" STYLE="fork"/>
        </node>
        <node TEXT="流程" ID="7697e40d5c7f4251692cd2e0ac95513f" STYLE="fork">
          <node TEXT="计算e=H(ZA||M)" ID="7b7ad17ced895a72c2cf6eca55199593" STYLE="fork"/>
          <node TEXT="计算t=r+s mod n，若t==0返回“不通过”" ID="c7c121e18f2f20a802b08c2750aaaae3" STYLE="fork"/>
          <node TEXT="计算T=sG+tA" ID="1ee577053e8020bc0f911002239ff2a0" STYLE="fork"/>
          <node TEXT="验证r==Tx+e mod n，若成立则返回通过，否则不通过" ID="9f607c46fa7f24b3eda3def0ff85a00f" STYLE="fork"/>
        </node>
      </node>
      <node TEXT="攻击" ID="e4d8969eea82402792d078db3dc7423f" STYLE="fork">
        <node TEXT="k重用（还原私钥）" ID="ef8747848806acba2aa03f068b66f501" STYLE="fork">
          <node TEXT="原理：解方程组s_i=(k-r_i*pa)/(1+pa)得pa=(s_2-s_1)/(s_1+r_1-s_2-r_2)" ID="c535e9e8c5cc90793706606325e2e5ff" STYLE="fork"/>
          <node TEXT="防护：保证随机数生成器不可重复" ID="10d49122af2b272e7a68131c977f9220" STYLE="fork"/>
        </node>
        <node TEXT="e重组（伪造签名绕过）" ID="68bfab4e4ee3dfaa3d5315baeffa84b7" STYLE="fork">
          <node TEXT="原理：构造一组合法的(e,(r,s))绕过" ID="bda805f398e5c37b5b31c6c51ecdc6d8" STYLE="fork"/>
          <node TEXT="细节：" ID="1ab40c4e25974e01ce704b668863009d" STYLE="fork">
            <node TEXT="取随机数m,n计算K=mG+kA" ID="2c00acbc8cae668f4b388996d49a145a" STYLE="fork"/>
            <node TEXT="取e=xK-n+m,r=n-m,s=m" ID="632c59e72eb6a0830df44df4bcb2d510" STYLE="fork"/>
          </node>
          <node TEXT="防护：使用安全的hash，防止构造可能；不使用只针对(e,(r,s))的签名" ID="6020374e1b5df3835d42ebcc712dd21b" STYLE="fork"/>
        </node>
      </node>
    </node>
    <node TEXT="公钥加密" ID="13c7508581210d9aae43b6b3ef4a3ab5" STYLE="bubble" POSITION="left">
      <node TEXT="加密" ID="2271047dd1289f04f87308f6d81328c8" STYLE="fork">
        <node TEXT="参数" ID="adbffe782351e0a2a71e8404010fe286" STYLE="fork">
          <node TEXT="曲线E" ID="f73f43bc0f24d2a391764ba272465dbf" STYLE="fork"/>
          <node TEXT="基点G" ID="75f40aab277f35470850d9a448aa14a6" STYLE="fork"/>
          <node TEXT="基点阶n" ID="0d84955776ffa6065b05eec428ed8b8d" STYLE="fork"/>
          <node TEXT="随机数k（不可重用）" ID="84d352d0fbab4fb08c98fb78d7db62ca" STYLE="fork"/>
          <node TEXT="哈希函数H" ID="b42c3291d2016cad29a2230f09ea036f" STYLE="fork"/>
          <node TEXT="密钥流长度klen" ID="818082e622bedf979a0cb49a42f1aeac" STYLE="fork"/>
        </node>
        <node TEXT="输入" ID="55ea0db7f1f6226f2f96282b16a990aa" STYLE="fork">
          <node TEXT="信息比特串M" ID="957f5bd0902d54edfee7febed291a1e3" STYLE="fork"/>
        </node>
        <node TEXT="密钥" ID="c86daf384229f0e601f60531aa0bbdc8" STYLE="fork">
          <node TEXT="公钥B" ID="2215ce5cc87ea3aca420d5b9e22293e7" STYLE="fork"/>
        </node>
        <node TEXT="输出" ID="32a2b7345b50d398f9c4ec6a59cfe2b3" STYLE="fork">
          <node TEXT="密文C" ID="95700b57bd7bfb8107caf8dbb3de33f8" STYLE="fork"/>
        </node>
        <node TEXT="流程" ID="605a204aaeec32eda815a80796332d12" STYLE="fork">
          <node TEXT="生成随机数k，计算C1=k*G，并C1转换为比特串" ID="8cd64e5af692155039ed76bcb545babd" STYLE="fork"/>
          <node TEXT="计算S=h*B，验证非无穷远点" ID="ac4a52d5c2d5557a2cbe5adbe0546684" STYLE="fork"/>
          <node TEXT="计算k*G，并取其坐标xkG，ykG为比特串x1,y1" ID="bf2b83f11b9bcea6d8853e9ab1c64fe3" STYLE="fork"/>
          <node TEXT="t=KDF(x1||y1,klen)" ID="5ade04d1111edf27327333a82ef0d878" STYLE="fork"/>
          <node TEXT="计算C2=M^^t" ID="6879465e3dfc9722fc50080e78a173de" STYLE="fork"/>
          <node TEXT="计算C3=H(x1||M||y1)" ID="574b25195a454256bf9e1673c88c9d7e" STYLE="fork"/>
          <node TEXT="输出密文C=C1||C3||C2" ID="40079c8088342222079674b43e1e3691" STYLE="fork"/>
        </node>
      </node>
      <node TEXT="解密" ID="20fa58123405ed469b35ae10d7c6ace6" STYLE="fork">
        <node TEXT="参数" ID="435cd12cba425817810f6aabe457b82d" STYLE="fork">
          <node TEXT="曲线E" ID="549187d87b87f802ad350660f456eddd" STYLE="fork"/>
          <node TEXT="基点G" ID="292fdb3c0a863762e612d9204e23f264" STYLE="fork"/>
          <node TEXT="基点阶n" ID="596a74dde8cbe122a3847bce2c6ed931" STYLE="fork"/>
          <node TEXT="哈希函数H" ID="5bd83facda23c3c0d2df59626c4b7e24" STYLE="fork"/>
          <node TEXT="(选)密钥流长度klen" ID="440e331a849f310316a85916eb516824" STYLE="fork"/>
        </node>
        <node TEXT="输入" ID="19685f3a0ee9228d280a453555d6ae6f" STYLE="fork">
          <node TEXT="密文C" ID="a1fcf24a7002d84f590bb74a62cab916" STYLE="fork"/>
        </node>
        <node TEXT="密钥" ID="060acd814be4dc87ed1202ffa2a7afba" STYLE="fork">
          <node TEXT="私钥pb" ID="8706d32c6e9a901bc6d1c5e6b70498af" STYLE="fork"/>
        </node>
        <node TEXT="输出" ID="eb91cb31dbf616916ee21d5907378575" STYLE="fork">
          <node TEXT="信息比特串M" ID="62e4cd0b2632c9cde5666aec119404ba" STYLE="fork"/>
        </node>
        <node TEXT="流程" ID="07601ee5e7afde02ac9bf99321b0cd61" STYLE="fork">
          <node TEXT="划分C=C1||C3||C2" ID="858f5e1e1920abbe6f9d502bc080b37b" STYLE="fork"/>
          <node TEXT="取出C1转化为点，验证是否在曲线上" ID="e0ee0a5516bba538d8569ee9ea7959d5" STYLE="fork"/>
          <node TEXT="计算S=h*C1，验证非无穷远点" ID="040ff29f6872947964bbbea630ffeb77" STYLE="fork"/>
          <node TEXT="计算pb*C1，取其坐标xp,yp" ID="1e95401700a413dbe63ff69d89c1e231" STYLE="fork"/>
          <node TEXT="取C2长度为klen，计算t=KDF(xp||yp,klen)" ID="dc95656a82bd0e17131da3c1606486d0" STYLE="fork"/>
          <node TEXT="计算M=C^^t" ID="4884027d3d3a730042d71f800e3365a1" STYLE="fork"/>
          <node TEXT="验证C3==H(xp||M||yp)，通过则返回M" ID="fbed19f88d5f345fc117cec52979a9eb" STYLE="fork"/>
        </node>
      </node>
    </node>
    <node TEXT="密钥交换" ID="fd0169dc883e25ff40e6ecea8f521610" STYLE="bubble" POSITION="left">
      <node TEXT="参数：" ID="59f4d1bbb57b59c9d8bdae2ecb0bfd42" STYLE="fork">
        <node TEXT="曲线E" ID="f9981f5e8c89226ae34e28984f5f75bd" STYLE="fork"/>
        <node TEXT="基点G" ID="48e6131dab8c13b00ddfaeca7eaa2032" STYLE="fork"/>
        <node TEXT="基点阶n" ID="c4b0810e4ac4b0a84513f6a936abf846" STYLE="fork"/>
        <node TEXT="余因子h" ID="d275b4a241a3db49aaca0c47b839ec31" STYLE="fork"/>
        <node TEXT="w=ceil((log_2 n))/2-1" ID="916ee32bc8b7ad6204e9f879ce4e350b" STYLE="fork"/>
        <node TEXT="klen为比特长度" ID="10c74a21b88dc41251fd2125ad9e6a62" STYLE="fork"/>
        <node TEXT="哈希函数H" ID="ef0db1c694b047dd999f57a18a238f35" STYLE="fork"/>
      </node>
      <node TEXT="流程" ID="cf1545252f3d6fdcbd532f1e7f569a24" STYLE="fork">
        <node TEXT="A发起协商" ID="68bd0040984db88123c746e50c066217" STYLE="fork">
          <node TEXT="生成随机数rA" ID="9db20d9a30f5ff55d2943c0d9cc796ed" STYLE="fork"/>
          <node TEXT="计算RA=rA*G并发送给B" ID="706c361d7d967f6da0625d2fcd26995b" STYLE="fork"/>
        </node>
        <node TEXT="B回应协商" ID="934461812a8e283d5e322e1c7acbf83f" STYLE="fork">
          <node TEXT="生成随机数rB" ID="958d615a5f9e09c433e6b6722fa3a878" STYLE="fork"/>
          <node TEXT="计算RB=rB*G" ID="df0f7d1c3c2add9b60b0e0a6143406f9" STYLE="fork"/>
          <node TEXT="取xbar2=xRB&amp;(2^w-1)+2^w" ID="6576ccfae73c76541e973f4720216af7" STYLE="fork"/>
          <node TEXT="计算tB=pb+xbar2*rB mod n" ID="a77c8ed68d4311c708475ff2c8e1f1f3" STYLE="fork"/>
          <node TEXT="验证RA合法，取xbar1=xRA&amp;(2^w-1)+2^w" ID="8b83eabd39f3dec762e66f1165f00910" STYLE="fork"/>
          <node TEXT="计算V=h*tB(A+xbar1*RA),验证非无穷远点" ID="7acf9f9a9a7d7ff9f20d51039793305a" STYLE="fork"/>
          <node TEXT="计算KB=KDF(xV||yV||ZA||ZB,klen)" ID="f24d0ce70f81ae23f4bf6fea5c4c1050" STYLE="fork"/>
          <node TEXT="(可选)计算SB=H(0x02||yV||H(xV||ZA||ZB||xA||yA||xB||yB))" ID="6295db33f01dade5b36bd4f58589525d" STYLE="fork"/>
          <node TEXT="发送RB（和SB）给A" ID="5ba1e60247b99f988c1e3c421b0bfaa1" STYLE="fork"/>
        </node>
        <node TEXT="A验证协商" ID="488dbc97f9ae39f4a8bed54dd73941c6" STYLE="fork">
          <node TEXT="计算xbar1=xRA&amp;(2^w-1)+2^w" ID="7935864087717cde9c4fd2d7de5d573f" STYLE="fork"/>
          <node TEXT="计算tA=pa+xbar2*rA mod n" ID="9da51c3414acbc6ae3e89f896400a484" STYLE="fork"/>
          <node TEXT="验证RB合法，取xbar2=xRB&amp;(2^w-1)+2^w" ID="0ea11c8d0cace0733e92130aafd3e5e5" STYLE="fork"/>
          <node TEXT="计算U=h*tA(B+xbar2*RB),验证非无穷远点" ID="610e9aeec0d7baa075c3d47993b61f3b" STYLE="fork"/>
          <node TEXT="计算KA=KDF(xU||yU||ZA||ZB,klen)" ID="2d5262e62110e9b24386ad3e1502736c" STYLE="fork"/>
          <node TEXT="(可选)计算SA=H(0x02||yU||H(xU||ZA||ZB||xA||yA||xB||yB))，验证SA==SB，通过则协商成功" ID="8f25a6721e16d61d8c57e434871c67e6" STYLE="fork"/>
          <node TEXT="(可选)S1=H(0x03||yU||H(xU||ZA||ZB||xA||yA||xB||yB)) 发送给A" ID="5bc6b514b9ee6d14169e45baa80320e2" STYLE="fork"/>
        </node>
        <node TEXT="（可选）B确认协商结束" ID="5d8c2438ad0428dfe59d551089624ae2" STYLE="fork">
          <node TEXT="B 计算 S2=H(0x03||yV||H(xV||ZA||ZB||xA||yA||xB||yB))，验证S1==S2，通过则协商成功" ID="549485744f01d7692746f83d6dbb93fa" STYLE="fork"/>
        </node>
      </node>
    </node>
  </node>
</map>