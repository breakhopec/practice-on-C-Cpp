/*
** 对大写数据加密（伪）
** 包括生成 key，加密数据，解密数据
** 我知道可以用统计学推测出未加密数据（（
** 还有变量不能是字符串常量（本垃圾就因为这个折腾了一上午）
*/

int
prepare_key(char *key){

	char *p=key;

	while(*p!='\0'){

		if(!isupper(*p)) return 1;
		p++;
	}

	*(key+26)='\0';
	for(char *cp=key+strlen(key),ch='A';ch<='Z';ch++){

		if(strchr(key,ch)==NULL) *cp++=ch;
	}
	
	return 0;
}

int
encrypt(char *data,char const *key){
	
	for(;*data!='\0';data++){
		
		if(isupper(*data))
			*data=*(key+(*data-'A'));
	}
	
	return 0;
}

int
decrypt(char *data,char const *key){
	
	for(;*data!='\0';data++){
		
		if(isupper(*data))
			*data='A'+(strchr(key,*data)-key);
	}
	
	return 0;
}
